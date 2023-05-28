import grpc
from grpc_API_pb2_grpc import BackendServiceStub, BackendServiceStub
from grpc_API_pb2 import GetSubChannelsRequest, GetPostsByChannelRequest, ErrorInDelieveryRequest, PostNewSubRequest
from google.protobuf.json_format import MessageToDict


channel = grpc.insecure_channel("localhost:50051")
client = BackendServiceStub(channel)

'''
request = GetPostsByChannelRequest(channel_id=1)
info = client.GetPostsByChannel(request)

request = GetSubChannelsRequest(sub_id=1)
info = MessageToDict(client.GetSubChannels(request))

request = ErrorInDelieveryRequest(post_id=1)
info = client.ErrorInDelievery(request)

request = PostNewSubRequest(sub_id=1, channel_id=1)
info = client.PostNewSub(request)
'''
request = ErrorInDelieveryRequest(post_id=1)
info = client.ErrorInDelievery(request)

print(info.status)
