# This is the project of broker service with an async Telegram bot written on Python in monolith architecture
- ## I have the backend broker-service that works with kafka broker on one side and backend web-service on another and also there is an implemented Telegram bot to work with Telegram API.
- ## My service communicates with web-service by gRPC API, with kafka broker by TCP and with Telegram API by HTTP
So  there are these parts:
1. __bot__ - this is a folder with the async bot that has an async kafka consumer implemented and listens for any messages in kafka topic and for messages from Telegram user and it is also a gRPC client for web-service;
2. __brokerService__ - this is a folder that contains Kafka async Consumer that is imported in Telegram bot and used to listen for new messages in kafka topic; Also it contains a service that is basically a Kafka producer that is also a gRPC server for web-service so when the web-service needs to produce a new message into the kafka topic it will call producer's method;
3. __protobufs__ - contains files describing the gRPC API between my service and the web-service;
4. __test__ - test-files to test different parts of my project.
- ## STARTING THE PROJECT:
1. start a kafka container and the web-service(or test gRPC server)
2. py consumer.py
3. py producer.py
4. py asyncBot.py