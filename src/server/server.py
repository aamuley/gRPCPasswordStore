import grpc
import pymongo
from concurrent import futures
import client_pb2
from client_pb2_grpc import add_SecretStoreServicer_to_server
import  client_pb2_grpc 
import client_grpc
from database import get_database

collection = None

class SecretStoreServicer(client_pb2_grpc.SecretStoreServicer):

  def StoreSecret(self, request, context):
    name = request.name  # uuid made from time on client side
    secret = request.secret # encrypted secret to store
    collection = get_database()['secrets'] #collection = secrets

    # format and add to mongodb
    sec = {"name": name, "secret": secret}
    collection.insert_one(sec)

    return client_pb2.StoreResponse(name=name, success=True)

  def RetrieveSecret(self, request, context):
    name = request.name # uuid made from time on client side
    collection = get_database()['secrets']

    # get from mongodb
    sec = collection.find_one({"name": name})

    # check if found
    if not sec:
      return client_pb2.RetrieveResponse(success=False)
    else:
      return client_pb2.RetrieveResponse(name=sec["secret"], success=True)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  add_SecretStoreServicer_to_server(
        SecretStoreServicer(), server)
  print("Created server")

  server.add_insecure_port('0.0.0.0:50051')
  print("Listening on port 50051")
  server.start()
  server.wait_for_termination()
  

if __name__ == '__main__':
  print("starting db...")
  # import db instance from database.py
  collection = get_database()['secrets']
  collection.auth
  print("Starting server...")
  serve()

# Here is a reference snippet of code from client/lib/client_grpc.py:
# class MyServiceClass(MyServiceClass_pb2_grpc.MyServiceClassServicer):
#     def __init__(self) -> None:
#         super().__init__()
#         self.client = pymongo.MongoClient(CONNSTRING) # Connection to Mongo database
#         self.client.server_info()
#     async def get_info(self, request, context):
#         response_info = MyScript(request.code).get_something()  # Call 
#         return MyServiceClasse_pb2.InfoResponse(info= response_info)
# async def serve():
#     server = grpc.aio.server()
#     start_pb2_grpc.add_MyServiceClass_to_server(
#         MyServiceClass(), server)
#     listen_addr = '[::]:50051'
#     server.add_insecure_port(listen_addr)
#     logging.info("Starting server on %s", listen_addr)
#     await server.start()
#     await server.wait_for_termination()