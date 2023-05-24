from time import sleep
from json import dumps
from kafka import KafkaProducer
''''''
producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'], 
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)
''''''
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

def poll():
    print("start")
    for key, item in data.items():
            print("producer sends")
            producer.send(
                "BloggerPost",
                value=item,
            )
    print("end")

poll()