from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from json import loads
import time


consumer = KafkaConsumer( 
    'test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    max_poll_records = 1,
    group_id='my-group')
 

def listen():
    #print('start')
    #start = time.time()
    #end = time.time()
    #print(end-start)
    consumer.poll()
    for topic_partition in consumer.assignment():
        committed_offset = consumer.committed(topic_partition)
    
# получаем последний доступный offset для всех партиций
    end_offsets = {}
    for tp in consumer.partitions_for_topic('test'):
        partition = TopicPartition('test', tp)
        end_offsets[partition] = consumer.end_offsets([partition])[partition]

# устанавливаем начальный offset на последний коммит
    for tp in consumer.assignment():
        if committed_offset is None:
            consumer.seek_to_end(tp)  # если нет коммитов, идём в конец
        else:
            consumer.seek(tp, committed_offset)

# запускаем чтение
    message = consumer.poll(timeout_ms= 1000)
    consumer.commit()
    # ваш код обработки сообщения здесь
    if message:
        #print(json.loads(messages[tp][0]._asdict()['value'].decode()))
        #print(dict(messages._asdict()))
        return loads(message[tp][0]._asdict()['value'].decode())
    else:
        return None

'''if __name__ == "__main__":
    print(listen())
'''



''' for tp, records in messages.items():
                print(type(records[0]))'''




'''bootstrap_servers = ['localhost : 9092'], 
     #consumer_timeout_ms=1000,
     auto_offset_reset = 'earliest', 
     enable_auto_commit = True, 
     group_id = 'my-group',
     #max_poll_records=1,
     value_deserializer = lambda x : loads(x.decode('utf-8')) '''
'''data = []
    tp = TopicPartition('test', 0)
    consumer.assign([tp])
    consumer.seek_to_end(tp)
    consumer.seek_to_beginning()'''
    #messages = consumer.poll(timeout_ms=3000)
    #print(messages)
    
'''
    for message in messages.values():
        # обрабатываем новые сообщения
            print(message.value.decode())
    #consumer.seek_to_beginning()
    consumer.committed()
    lastOffset = consumer.end_offsets([tp])[tp]
    print("start")
    for message in consumer:
        print('inloop')
        print(message)
        if message.offset == lastOffset - 1:
               break
        #data.append(message.value)
            #print(message.value)
            #if message.offset == lastOffset - 1:
            #   break
        try:
        except Exception as e:
            print("Kafka down")
            channel = grpc.insecure_channel("localhost:50051")
            client = BackendServiceStub(channel)
            request = ErrorInDelieveryRequest(post_id=1)
            info = client.GetPostsByChannel(request)
            print(e, "\n об этой ошибке сообщил бэкенду, статус:", info)
    return data'''
    
    
    
'''if not messages:  # если новых сообщений нет, то выходим из цикла
        break
    
#consumer.close()'''