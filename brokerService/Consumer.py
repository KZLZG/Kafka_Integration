from kafka import KafkaConsumer
import grpc
from json import loads
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


consumer = KafkaConsumer( 
    'BloggerPost', 
     bootstrap_servers = ['localhost : 9092'], 
     auto_offset_reset = 'earliest', 
     enable_auto_commit = True, 
     group_id = 'my-group',
     value_deserializer = lambda x : loads(x.decode('utf-8')) 
     ) 

print("start")
for message in consumer:
   
    # send message
    try:
        for i in note_info.email:
            mail.send_email(
                project_title=note_info.project_title,
                section_title=note_info.section_title,
                notification_title=note_info.notification_title,
                description=note_info.description,
                email=i,
            )
        f = open("mail_logs.txt", "w")
        f.write("sent message with id" + str(message["notification_id"]))

    except Exception as e:
        print(e)