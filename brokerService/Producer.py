from time import sleep
from json import dumps
from kafka import KafkaProducer
import grpc
import json
from google.protobuf.json_format import MessageToJson
from protobufs.grpc_API_pb2_grpc import BrokerService, BrokerServiceServicer, add_BrokerServiceServicer_to_server
from concurrent import futures
from protobufs.grpc_API_pb2 import PostNewPostResponse



def PolltoKafka(message):
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'], 
        value_serializer=lambda x: dumps(x).encode("utf-8"),
        )
    print("polling")
    producer.send(
                "test",
                value=json.loads(MessageToJson(message)),
    )
    print(message)    
    print("end")



class BrokerService(BrokerServiceServicer):
    def PostNewPost(self, request, context):
        print('newPost')
        status=0
        try:
            PolltoKafka(request)
            print("polled")
        except Exception as e:
            print('Cannot pull ', e)
            status = 1
        return PostNewPostResponse(status = status)






def serve():
    print("running server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BrokerServiceServicer_to_server(BrokerService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()




if __name__ == "__main__":
    serve()