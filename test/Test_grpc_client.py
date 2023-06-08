import grpc
from protobufs.grpc_API_pb2_grpc import BackendServiceStub, BackendServiceStub, BrokerServiceStub
from protobufs.grpc_API_pb2 import GetSubChannelsRequest, GetPostsByChannelRequest, ErrorInDelieveryRequest, PostNewSubRequest, PostNewPostRequest
from google.protobuf.json_format import MessageToDict

'''
channel = grpc.insecure_channel("localhost:50052")
client = BrokerServiceStub(channel)
request = PostNewPostRequest(post_id = 1,
                            channel_id = 2,
                            channel_name = '3',
                            text = '4',
                            status = '5',
                            date_sent = '6')
info = client.PostNewPost(request)


request = GetPostsByChannelRequest(channel_id=1)
info = client.GetPostsByChannel(request)

request = GetSubChannelsRequest(sub_id=1)
info = MessageToDict(client.GetSubChannels(request))

request = ErrorInDelieveryRequest(post_id=1)
info = client.ErrorInDelievery(request)

request = PostNewSubRequest(sub_id=1, channel_id=1)
info = client.PostNewSub(request)
'''
channel = grpc.insecure_channel("localhost:50051")
client = BackendServiceStub(channel)

request = ErrorInDelieveryRequest(post_id=23)
info = client.ErrorInDelievery(request)
print(info)
