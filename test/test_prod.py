from time import sleep
from json import dumps
from kafka import KafkaProducer

my_producer = KafkaProducer(
    #bootstrap_servers=["broker:9092"],
    bootstrap_servers = ['localhost:9092'], 
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)


for n in range(20): 
    print("mailed ")
    my_data = {'num' : n} 
    my_producer.send('testnum', value = my_data) 
    sleep(1) 
