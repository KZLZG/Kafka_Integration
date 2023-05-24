import grpc
from grpc_API_pb2_grpc import BackendServiceStub
from grpc_API_pb2 import GetPostsByChannelRequest


channel = grpc.insecure_channel("localhost:50051")
client = BackendServiceStub(channel)

request = GetPostsByChannelRequest(channel_id=1)
info = client.GetPostsByChannel(request)

print(info)