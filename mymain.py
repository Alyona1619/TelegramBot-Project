import telebot
from messages import *

# Токен вашего бота, полученный от BotFather
BOTTOKEN = '5136913496:AAFVF_8Ua_bXVTGtC3N6XuMI8YbTZ_UOLCo'

# Создаем экземпляр бота
bot = telebot.TeleBot(BOTTOKEN)

# Клавиатура с выбором языка
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard.add(telebot.types.KeyboardButton('Русский'), telebot.types.KeyboardButton('English'))

# Словарь для хранения выбранного языка пользователей
user_language = {}


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Выбери язык / Hello! Choose a language.", reply_markup=keyboard)


def get_topics_keyboard(chat_id):
    language = user_language[chat_id]
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'Русский':
        topics = ['Виды массажа', 'Виды массажеров', 'Советы по питанию', 'Советы по сну', 'Популярные вопросы']
    elif language == 'English':
        topics = ['Types of Massage', 'Types of Massagers', 'Nutrition Tips', 'Sleep Tips', 'Frequently Asked Questions']
    for topic in topics:
        keyboard.add(telebot.types.KeyboardButton(topic))
    return keyboard


def get_subtopics_keyboard(chat_id, topic):
    language = user_language[chat_id]
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'Русский' and topic == 'Виды массажа':
        subtopics = ['Подготовка к процедуре', 'Классический массаж', 'Пластический массаж', 'Лимфодренажный массаж', 'Польза массажа']
    elif language == 'English' and topic == 'Types of Massage':
        subtopics = ['Preparation for the Procedure', 'Swedish Massage', 'Deep Tissue Massage', 'Lymphatic Drainage Massage', 'Benefits of Massage']
    for subtopic in subtopics:
        keyboard.add(telebot.types.KeyboardButton(subtopic))
    return keyboard


@bot.message_handler(func=lambda message: message.text in ['Виды массажа', 'Types of Massage'])
def choose_subtopic(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language:
        topic = message.text
        if language == 'Русский':
            bot.send_message(chat_id, "Выберите подтему:", reply_markup=get_subtopics_keyboard(chat_id, topic))
        elif language == 'English':
            bot.send_message(chat_id, "Choose a subtopic:", reply_markup=get_subtopics_keyboard(chat_id, topic))


@bot.message_handler(func=lambda message: message.text in ['Подготовка к процедуре', 'Preparation for the Procedure', 'Классический массаж', 'Swedish Massage', ...])
def show_subtopic_details(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    subtopic = message.text
    if language and subtopic:
        if language in messages and subtopic in messages[language]:
            data = messages[language][subtopic]
            text = data['text']
            image_url = data['image_url']
            bot.send_message(chat_id, text)
            bot.send_photo(chat_id, image_url)
        else:
            bot.send_message(chat_id, "Для выбранного языка и подтемы отсутствуют данные.")
    else:
        bot.send_message(chat_id, "Ошибка: отсутствует выбранный язык или подтема.")

@bot.message_handler(func=lambda message: message.text in ['Русский', 'English'])
def choose_language(message):
    chat_id = message.chat.id
    language = message.text
    user_language[chat_id] = language
    if language == 'Русский':
        bot.send_message(chat_id, "Ты выбрал язык: Русский")
        bot.send_message(chat_id, "Выбери интересующую тебя тему:", reply_markup=get_topics_keyboard(chat_id))
    elif language == 'English':
        bot.send_message(chat_id, "You chose the language: English")
        bot.send_message(chat_id, "Choose the topic you are interested in:", reply_markup=get_topics_keyboard(chat_id))

bot.polling()
