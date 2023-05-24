import grpc
import grpc_API_pb2_grpc
from concurrent import futures
from grpc_API_pb2 import GetPostsByChannelResponse, PostNewPostRequest

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

response = GetPostsByChannelResponse()
response.posts.add(
                    post_id = data[1]["post_id"],
                    channel_id = data[1]["channel_id"],
                    channel_name = data[1]["channel"],
                    text = data[1]["text"],
                    photo = data[1]["photo"],
                    status = data[1]["status"],
                    date_sent = data[1]["date_sent"]
        )
#print(response)


class BackendService(grpc_API_pb2_grpc.BackendServiceServicer):
    def GetPostsByChannel(self, request, context):
        response = GetPostsByChannelResponse()
        response.posts.add(
                    post_id = data[1]["post_id"],
                    channel_id = data[1]["channel_id"],
                    channel_name = data[1]["channel"],
                    text = data[1]["text"],
                    photo = data[1]["photo"],
                    status = data[1]["status"],
                    date_sent = data[1]["date_sent"]
        )
        return GetPostsByChannelResponse(posts = response.posts)

    



def serve():
    print("running server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_API_pb2_grpc.add_BackendServiceServicer_to_server(BackendService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()