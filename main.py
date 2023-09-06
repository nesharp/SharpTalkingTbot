import users
import telebot
from telebot import types
import time

# production token
token = '6352429547:AAFwPOdadxX726y9VmLi5_FuS92pKoGtk90'
# test token
# token = '6483800445:AAER23eZoRpn2P-PVSdHJTBbQ3QO54oU1DA'
bot = telebot.TeleBot(token)
pairs = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    # creating keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('/search'))
    markup.add(types.KeyboardButton('/stop'))
    # checking if user is new
    if (str(message.from_user.id) not in users.getUsersId()):
        # sending message to new user
        bot.send_message(
            message.chat.id, 'Hello, im bot for anonymous chat.To start chacting click search', reply_markup=markup)
        users.addUser(message.from_user.id)

    else:
        # sending message to returned user
        bot.send_message(message.chat.id, 'Hello again!', reply_markup=markup)
@bot.message_handler(commands=['stop'])
def stop_message(message):
    users.deleteUser(message.from_user.id)
    # if (str(message.from_user.id) in pairs):
    #     bot.send_message(pairs[str(message.from_user.id)], 'Click search to start chatting')
    #     pairs.pop(str(pairs[str(message.from_user.id)]))
    # bot.send_message(message.chat.id, 'You are disconnected from chat')

@bot.message_handler(commands=['search'])
def search_message(message):
    
    try:
        if (str(message.from_user.id) not in users.getUsersId()):
            bot.send_message(message.chat.id, 'Click start to start chatting')
        else:
            if (str(message.from_user.id) in pairs):
                # delete pair from dict
                pairs.pop(str(pairs[str(message.from_user.id)]))
                # sending messages to users about termination
                bot.send_message(pairs[str(message.from_user.id)],
                                'Your interlocutor terminated the conversation')
                # sending message to user about searching
                bot.send_message(message.from_user.id, 'Searching...')
                # searching for new pair
                randomUserId = users.getRandomUserId(message.from_user.id)
                while (str(randomUserId) in pairs or randomUserId == "None"):
                    randomUserId = users.getRandomUserId(message.from_user.id)
                    time.sleep(1)
                # adding pairs to dict
                pairs[str(message.from_user.id)] = randomUserId
                pairs[str(randomUserId)] = message.from_user.id
                # sending messages to users about connection
                bot.send_message(message.from_user.id, 'Found!')
                bot.send_message(randomUserId, 'You are connected to pair!')
            else:
                bot.send_message(message.chat.id, 'Searching...')
                # getting random user id
                randomUserId = users.getRandomUserId(message.from_user.id)
                while (str(randomUserId) in pairs or randomUserId == "None"):
                    randomUserId = users.getRandomUserId(message.from_user.id)
                    time.sleep(1)
                # adding paira to dict
                pairs[str(message.from_user.id)] = randomUserId
                pairs[str(randomUserId)] = message.from_user.id
                # seding messages to users abou connection
                bot.send_message(message.from_user.id, 'Found!')
                bot.send_message(randomUserId, 'You are connected to pair!')
    except:
        users.deleteUser(pairs[str(message.from_user.id)])
        print(pairs)
        pairs.pop(str(message.from_user.id))
        bot.send_message(message.from_user.id, 'Click /search to start chatting')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        # checking if user is in pair
        if (str(message.from_user.id) in pairs):
            # sending message to pair
            bot.send_message(pairs[str(message.from_user.id)], message.text)
        else:
            # sending message to invalid pair
            bot.send_message(message.from_user.id, 'Error, click search to start chatting')
    except:
        # sending message to invalid pair
        users.deleteUser(pairs[str(message.from_user.id)])
        print(pairs)
        print(str(pairs[str(message.from_user.id)]))
        pairs.pop(str(pairs[str(message.from_user.id)]))
        bot.send_message(message.from_user.id, 'Click search to start chatting')

bot.polling(none_stop=True, interval=0)
