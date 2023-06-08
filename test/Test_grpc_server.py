import grpc
import protobufs.grpc_API_pb2_grpc as grpc_API_pb2_grpc
from concurrent import futures
import protobufs.grpc_API_pb2 as grpc_API_pb2

data =  {
    1: {
        "post_id": 1,
        "channel_id": 1,
        "channel": "1",
        "text":"1",
        "photo": "aboba",
        "status":"sent",
        "date_sent": "15.05",
    },
    2: {
        "post_id": 2,
        "channel_id":2,
        "channel": "2",
        "text":"2",
        "photo": "notaboba",
        "status":"sent",
        "date_sent": "16.05",
    },
    3: {
        "post_id": 3,
        "channel_id": 3,
        "channel": "3",
        "text":"3",
        "photo": "somephoto",
        "status":"sent",
        "date_sent": "16.06",
    },
}


class BackendService(grpc_API_pb2_grpc.BackendServiceServicer):
    def GetPostsByChannel(self, request, context):
        response = grpc_API_pb2.GetPostsByChannelResponse()
        response.posts.add(
                    post_id = data[1]["post_id"],
                    channel_id = data[1]["channel_id"],
                    channel_name = data[1]["channel"],
                    text = data[1]["text"],
                    photo = data[1]["photo"],
                    status = data[1]["status"],
                    date_sent = data[1]["date_sent"]
        )
        return grpc_API_pb2.GetPostsByChannelResponse(posts = response.posts)
    
    def GetSubChannels(self, request, context):
        response = grpc_API_pb2.GetSubChannelsResponse()
        for i in data:
            response.channels.add(
                    sub_id = data[request.sub_id]["post_id"],
                    channel_id = data[request.sub_id]["channel_id"],
                    channel_name = data[request.sub_id]["channel"],
                    topic = data[request.sub_id]["text"],
                    sub_count = data[request.sub_id]["post_id"])
        return grpc_API_pb2.GetSubChannelsResponse(channels = response.channels)
    
    def ErrorInDelievery(self, request, context):
        return grpc_API_pb2.ErrorInDelieveryResponse(status = request.post_id)
    
    def PostNewSub(self, request, context):
        print(request.sub_id, request.channel_id)
        return grpc_API_pb2.PostNewSubResponse(status = request.sub_id + request.channel_id)

    



def serve():
    print("running server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_API_pb2_grpc.add_BackendServiceServicer_to_server(BackendService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()