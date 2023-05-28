from time import sleep
from json import dumps
from kafka import KafkaProducer
import grpc

from grpc_API_pb2_grpc import BrokerService, BrokerServiceServicer, add_BackendServiceServicer_to_server
from concurrent import futures
from grpc_API_pb2 import GetPostsByChannelResponse


data =  {
    1: {
        "post_id": 1,
        "id_channel": 1,
        "text":"1",
        "photo": "aboba",
        "status":"sent",
        "date_sent": "15.05",
    },
    2: {
        "post_id": 2,
        "id_channel": 2,
        "text":"2",
        "photo": "notaboba",
        "status":"sent",
        "date_sent": "16.05",
    },
    3: {
        "post_id": 3,
        "id_channel": 3,
        "text":"3",
        "photo": "somephoto",
        "status":"sent",
        "date_sent": "16.06",
    },
    }




def poll(message):
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'], 
        value_serializer=lambda x: dumps(x).encode("utf-8"),
        )
    print("polling")

        #for key, item in data.items():
        #print("producer sends")
    producer.send(
                "test",
                value=message,
    )
    print(message)    
    print("end")



class BrokerService(BrokerServiceServicer):
    def PostNewPost(self, request, context):
        status=0
        try:
            poll(request)
            print("polled")
        except Exception as e:
            print('Cannot pull ', e)
            status = 1
        return GetPostsByChannelResponse(status = status)






def serve():
    print("running server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BackendServiceServicer_to_server(BrokerService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()




poll('test2')