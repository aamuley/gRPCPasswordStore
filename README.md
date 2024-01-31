# gRPC Password Store
(If the formatting is messed up, please see the notion page here: https://gorgeous-serpent-2d2.notion.site/gRPC-Password-Store-a970dd65eb034b4d80800b5ad1a2910f)

## Client Side

I created a client python script to call the server created that has a CLI interface, uses the pyCryptography library to encrypt the passwords, and connects to the local docker container with the server. 

### Usage:

The code is stored in src/client.py. To invoke the store and get functions, I provided a CLI Interface to allow the user to add and query for the secrets/passwords

- **Store a secret:**

```jsx
python3 client.py store <secret>
```

- **Query for a secret**

```jsx
python3 client.py get <uuid>
```

### Motivations

1. **pyCryptography vs OpenSSL**
    
    It would have been great to use the OpenSSL library to perform the symmetric encryption but importing the methods in docker was a major roadblock that I hit. Despite adding the libraries in my docker installation, it was difficult to access them and the compilation process was ridiculously long because of all the extraneous packages. 
    
    So I decided it would be better to use a simpler package and one that could be easily dockerized and the pyCryptography methods are what I ended up using
    
    The type of encryption I used was Fernet Symmetric Encryption (see [https://cryptography.io/en/latest/fernet/](https://cryptography.io/en/latest/fernet/)) 
    
    Fernet is a type of CBC Mode Encryption Scheme that also uses elements such as a timestamp, hmac to authenticate, and has a clear library in python. 
    
    ![Untitled](gRPC%20Password%20Store%20a970dd65eb034b4d80800b5ad1a2910f/Untitled.png)
    
2. **Fixed vs generated keys**
    
    Since I wanted to run the same file multiple times and maintain a single key that I could use to decrypt them, I hardcoded a derived key into the client code. This isnt a great security practice but we need a method to store a single encryption key per client or a mapping to determine which encryption keys were for which secrets
    
    I looked into creating an interface for this application where I could store all the website→uuid mappings in localstorage and then store a client encryption key as a cookie for example. Then I could securely keep track of the client keys to encrypt/decrypt and also ensure all network passwords are encrypted. If the database does not find the key, it should return garbage that an attacker can attempt to decrypt to not share any info about uuids that are present in the database. 
    
    ```python
    #from src/client.py
    ...
    channel = grpc.insecure_channel('0.0.0.0:50051') 
    stub = client_pb2_grpc.SecretStoreStub(channel)
    key = b'yGVu2nkya5rb5iif3qP_uK6Vfd4g2Yn6mYtwPHzjyjA='
    p = Fernet(key)
    ...
    ```
    

## Server-side

### Usage

To start the server run the shell script provided 

`./src/build_and_run.sh`

This runs docker-compose down (remove any previous containers), docker-compose build, docker-compose up -d (run and maintain containers) but you can run each command individually if needed too. 

### Motivations and Details

1. **Protobuf Definitions**
    
    `src/client.proto`
    
    - 2 basic rpcs-  C and R
        - *Create Rpc = StoreSecret*
            - Takes in a StoreRequest with the uuid and the user encrypted secret
            - Returns a StoreResponse with the uuid for matching and a success boolean
        - *Read Rpc = RetrieveSecret*
            - Takes in a StoreRequest with the uuid
            - Returns a StoreResponse with the encrypted password and a success boolean
2. **Parallel Request Processing**
    
    To leverage gRPC server-side parallel request processing, i defined a set of workers in src/server/server.py. I initially set the number of workers to be 10, but this value can be changed to allow the server to be scaled if there are more requests coming in at the same time. 
    
    ```python
    # from src/server/server.py
    ...
    def serve():
      server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
      add_SecretStoreServicer_to_server(
            SecretStoreServicer(), server)
    ... 
    ```
    
3. **Local Network**
    
    To create a separate subnet that the server and mongodb containers to communicate over, I created a “secrets” network with a bridge driver. I used the bridge driver instead of a host driver because this allows containers with the same docker host to communicate and I could package them together but still connect over the network
    
    ```python
    # from docker-compose.yml
    networks:
        secrets:
            driver: bridge
    ```
    

## Database

The motivation for this stack generally was to use a vetted but also applicable stack for development. Having documentation and other developers who have answered questions about integrating these definitely simplified this. 

**MongoDB**

I chose MongoDB for my database for this project because I wanted a highly available replicated database to ensure uptime and data consistency. 

**Containerization**

I created a separate container for my database so that the application can be scalable, perhaps providing a shared database and multiple collections for a joint application. Separating each of the components allows there to be more joint usage.


