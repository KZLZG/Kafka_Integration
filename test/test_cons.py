# importing the required modules 
from json import loads 
from kafka import KafkaConsumer 

# generating the Kafka Consumer 
my_consumer = KafkaConsumer( 
    'BloggerPost', 
     bootstrap_servers = ['localhost : 9092'], 
     auto_offset_reset = 'earliest', 
     enable_auto_commit = True, 
     group_id = 'my-group', 
     value_deserializer = lambda x : loads(x.decode('utf-8')) 
     ) 


print("start")
for message in my_consumer: 
    message = message.value 
    print(message) 
