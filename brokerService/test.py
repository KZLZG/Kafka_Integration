import grpc
import protobufs.grpc_API_pb2_grpc as grpc_API_pb2_grpc
from concurrent import futures
import protobufs.grpc_API_pb2 as grpc_API_pb2

class BrokerService(grpc_API_pb2_grpc.BrokerServiceServicer):
    def PostNewPost(self, request, context):
        print(request)
        return grpc_API_pb2.PostNewPostResponse(status = 0)


def serve():
    print("running server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_API_pb2_grpc.add_BrokerServiceServicer_to_server(BrokerService(), server)
    server.add_insecure_port("[::]:50060")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()