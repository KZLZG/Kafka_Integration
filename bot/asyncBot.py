import grpc
from protobufs.grpc_API_pb2_grpc import BackendServiceStub
import asyncio
import brokerService.Consumer as Consumer
from google.protobuf.json_format import MessageToDict
from protobufs.grpc_API_pb2 import GetSubChannelsRequest, GetPostsByChannelRequest, ErrorInDelieveryRequest, PostNewSubRequest
from TgClient import TgClient
import re


BOT_TOKEN = 'SOME TOKEN'
bot = TgClient(BOT_TOKEN)


channel = grpc.insecure_channel("localhost:50051")
client = BackendServiceStub(channel)

async def ShowBlogs(user_id):
    
    try:
            request = GetSubChannelsRequest(sub_id=1)
            info = MessageToDict(client.GetSubChannels(request))
            print(info['channels'])
            try:
                await draw_blogs(user_id, info['channels'])
            except:
                print('cannot draw_blogs')
    except:
            print('backend grpc down')
            await  bot.send_message(user_id, 'Sorry, our backend is down')

async def NewSub(user_id, some_num):
    try:
        request = PostNewSubRequest(sub_id=user_id, channel_id=some_num)
        info = client.PostNewSub(request)
            # Try из словаря взять такого айди, except такого нет
        await bot.send_message(user_id, "Вы подписались на "+str(some_num))
    except:
        print('backend grpc down')
        await draw_blogs(user_id, 'Sorry, our backend is down')


# обработка сообщений пользователя
async def handle_text(message):
    user_id = message.chat.id
    some_num = re.search(r'\d', message.text)

# обработка команды /start
    if message.text == "/start":
        print("start")
        await bot.send_message(user_id, 'Я на связи. Для помощи - напиши /help')

# обработка команды /help
    elif message.text == "/help":
        print("bot help")
        await bot.send_message(user_id,
                                        'Если хочешь посмотреть список блогеров и подписаться - напиши команду /blogs\
                                       \nЕсли хочешь посмотреть список блогеров и подписаться - напиши команду /start\
                                       \nДля подписки - напиши команду /sub и id канала')
# обработка команды /blogs 
    elif "/blogs" == message.text:
        print("bot blogs")
        await ShowBlogs(user_id)
        
# обработка команды /sub x
    elif "/sub" in message.text and bool(some_num): 
        print("bot sub")
        some_num = int(some_num.group(0))
        await NewSub(user_id, some_num)


# обработка всего остального
    elif message.text: 
        print("bot some text")
        await bot.send_message(user_id, "Такому я еще не обучен, попробуйте предложенные мной команды по /help")



# отправка пользователю списка всех блогеров            
async def draw_blogs(user_id, channels):    
    for channel  in channels:        
        question = 'ID: ' + str(channel["subId"]) + '\nБлоггер: ' + str(channel["channelName"]) + '\nАудитория: '+ str(channel["subCount"]) + '\nПишет про: '+str(channel["topic"]);
        #{'subId': 2, 'channelId': 2, 'channelName': '2', 'topic': '2', 'subCount': 1}
        #print(question)
        await bot.send_message(user_id, question)

async def ShowNewPost(new_post):
    question =  'Новый пост!\n' + 'ID: ' + str(new_post["postId"]) \
                    + '\nБлоггер: ' + str(new_post['channelId'])\
                    + '\n' + \
                    str(new_post["text"]) + '\nСоздано: ' + str(new_post["dateSent"]);
    #print(question)
    try:
        
        await bot.send_message(385210730, question) # sub_id
    except Exception as inner_e:
        print('Error sending new post to bot', inner_e)
        request = ErrorInDelieveryRequest(post_id=1)
        info = client.ErrorInDelievery(request)
        print('Sent error to backend', info)

# цикл опроса кафки и отправления новых постов пользователю
async def check_kafka():
    print('checking kafka')
    try:
        new_post = Consumer.listen() # обращение к Кафке
        print(new_post)
        if new_post:
            await ShowNewPost(new_post)
    except Exception as e:
        print('Error checking Kafka', e)



# главный цикл бота
async def run_echo():
    print("bot started")
    offset = 0
    while True:
        await check_kafka() # Запрос новых событий у Кафки
        try:
            res = await bot.get_updates_in_objects(offset=offset, timeout=5) #получение новых сообщений от Telegram
            for item in res.result: #Обработка новых сообщений
                    offset = item.update_id + 1
                    await handle_text(item.message) # вызов функции обработки текста сообщения пользователя
        except:
            print()

if __name__ == "__main__":
   asyncio.run(run_echo())


   '''
def show_posts(user_id, posts):
request = ErrorInDelieveryRequest(post_id=1)
info = client.ErrorInDelievery(request)
request = GetPostsByChannelRequest(channel_id=1)
info = client.GetPostsByChannel(request)
    for key, post  in posts.items():
            question = 'Блог: ' + str(post["channel"]) + '\nСоздано: '+ str(post["date_sent"]) + '\nТекст: '+ str(post["text"]) + '\nНомер поста: '+str(post["post_id"]);
            c.send_message(item.message.chat.id, text=question)
'''