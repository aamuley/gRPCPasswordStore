import grpc
import client_pb2
import client_pb2_grpc
import sys
import uuid    
from cryptography.fernet import Fernet

# Initialize gRPC channel
channel = grpc.insecure_channel('0.0.0.0:50051') 
stub = client_pb2_grpc.SecretStoreStub(channel)
key = b'yGVu2nkya5rb5iif3qP_uK6Vfd4g2Yn6mYtwPHzjyjA='
p = Fernet(key)

# Client functions 

def store_secret(value):
  key = str(uuid.uuid4())
  value = p.encrypt(bytes(value, 'utf-8'))
  request = client_pb2.StoreRequest(name=key, secret=value.decode('utf-8'))
  # print(value.decode('utf-8'))
  response = stub.StoreSecret(request)
  return response

def get_secret(key):
  request = client_pb2.RetrieveRequest(name=key)
  response = stub.RetrieveSecret(request)
  if not response.name:
    print("Error: Secret not found")
  else:
    value = response.name.encode('utf-8')
    response.name = p.decrypt(value).decode('utf-8')
    return response

# reference:

# store_response = store_secret('my_key', 'my_secret')
# print(store_response)

# secret = get_secret('my_key')
# print(secret)

# allow for cli interfacing including input error handling
if __name__ == '__main__':
  if sys.argv[1] == 'store':
    if not sys.argv[2]:
      print("Error: Please provide a value to store")
    else:
        value = sys.argv[2]
        print("Storing value: " + value)
        resp = store_secret(value)
        print(resp)

  elif sys.argv[1] == 'get':
    if not sys.argv[2]:
      print("Error: Please provide a value to retrieve")
    else:
        key = sys.argv[2]
        resp = get_secret(key)
        print(resp)

  else:
    print("Error: Unsupported command for the client, please call \" get \" or \" store \"")

# basic commands:
    # python3 client.py store <my_secret>
    # python3 client.py get <my_key>





