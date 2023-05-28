import telebot;
from telebot import types;
import Producer
#import Consumer

blogs ={}
data = {}

TOKEN = '6041479103:AAE0IdzKKoIKASwtP0zXSDVE_bDz8V23NhE'
bot = telebot.TeleBot(TOKEN)

def show_posts(user_id, posts):
    for key, post  in posts.items():
            question = 'Блог: ' + str(post["channel"]) + '\nСоздано: '+ str(post["date_sent"]) + '\nТекст: '+ str(post["text"]) + '\nНомер поста: '+str(post["post_id"]);
            bot.send_message(user_id, text=question)

            
def draw_blogs(user_id, blogs):    
    for key, blog  in blogs.items():
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            key_sub = types.InlineKeyboardButton(text='Подписаться', callback_data=blog["channel_id"]);  #кнопка Подписаться
            keyboard.add(key_sub); #добавляем кнопку в клавиатуру
            question = 'Блоггер: ' + str(blog["author"]) + '\nАудитория: '+ str(blog["sub_count"]) + '\nПишет про: '+str(blog["topic"]);
            bot.send_message(user_id, text=question, reply_markup=keyboard)




print("bot started")
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    print("start")
    bot.send_message(message.chat.id, 'Я на связи. Для помощи - напиши /help')


@bot.message_handler(content_types=["text"])
def handle_text(message):
# Функция, обрабатывающая команду /help
    if message.text == "/help":
         print("bot help")
         bot.send_message(message.chat.id,
                                        'Если хочешь посмотреть список блогеров и подписаться - напиши команду /blogs\
                                        \nЕсли хочешь посмотреть список блогеров и подписаться - напиши команду /start')
# Функция, обрабатывающая команду /blogs 
    if message.text == "/blogs":
        print("bot blogs")
        user_id = message.from_user.id
        draw_blogs(user_id, blogs)
    if message.text == "/posts":
        show_posts(message.from_user.id, data)
 

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data: #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Подписались на ' + call.data);


# Опрос API ТГ
bot.polling(none_stop=True, interval=0.5)
