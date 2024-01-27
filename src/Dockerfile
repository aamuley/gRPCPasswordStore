# standard python image
FROM python:3.8-buster

WORKDIR /src

# Copy and install requirements
COPY requirements.txt requirements.txt  
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y openssl
RUN pip install -r requirements.txt
RUN pip install grpcio-tools
RUN pip install grpclib
# RUN pip install cryptography

# Copy app code
COPY . .
ENV PYTHONPATH /src

# Generate gRPC code
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. client.proto

# # expose server port
EXPOSE 50051 

# Start server 
# CMD [ "python3", "server/server.py" ]
ENTRYPOINT [ "python3", "server/server.py" ]
