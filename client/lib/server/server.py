import grpc
from concurrent import futures
import client.lib.client_pb2 as client_pb2
import client.lib.client_grpc as client_grpc

class SecretStoreService(client_grpc.SecretStoreService):

  def StoreSecret(self, request, context):
    name = request.name 
    secret = request.secret

    # Implement storage logic

    # Return response
    return client_pb2.StoreResponse(name=name, success=True)

  def RetrieveSecret(self, request, context):
    # Get request data
    name = request.name

    # Implement retrieval logic

    # Return response
    return client_pb2.RetrieveResponse(name="secret", success=True)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  client_grpc.add_SecretStoreService_to_server(
        SecretStoreService(), server)

  server.add_insecure_port('[::]:50051')
  server.start()

if __name__ == '__main__':
  serve()