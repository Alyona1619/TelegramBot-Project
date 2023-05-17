import telebot
from messages import *

BOTTOKEN = '5136913496:AAFVF_8Ua_bXVTGtC3N6XuMI8YbTZ_UOLCo'

bot = telebot.TeleBot(BOTTOKEN)

# Клавиатура с выбором языка
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard.add(telebot.types.KeyboardButton('Русский'), telebot.types.KeyboardButton('English'))

# Словарь для хранения выбранного языка пользователей
user_language = {}


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Привет! Я BeautyTouch Bot! Я твой помощник по уходу за собой, массажу и ведению "
                     "здорового образа жизни. Выбери язык, на котором я буду с тобой общаться: / "
                     "Hi! I'm a BeautyTouch Bot! I am your assistant for self-care, massage and healthy lifestyle. "
                     "Choose the language in which I will communicate with you:", reply_markup=keyboard)


def get_topics_keyboard(chat_id):
    language = user_language[chat_id]
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'Русский':
        topics = ['Виды массажа', 'Виды массажеров', 'Ошибки, совершаемые во время массажа', 'Противопоказания',
                  'Советы по питанию', 'Советы по сну', 'Популярные вопросы']
    elif language == 'English':
        topics = ['Types of Massage', 'Types of Massagers', 'Mistakes', 'Contraindications', 'Nutrition Tips',
                  'Sleep Tips', 'Frequently Asked Questions']
    for topic in topics:
        keyboard.add(telebot.types.KeyboardButton(topic))
    return keyboard


def get_subtopics_keyboard(chat_id, topic):
    language = user_language[chat_id]
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'Русский' and topic == 'Виды массажа':
        subtopics = ['Подготовка к процедуре', 'Классический массаж', 'Пластический массаж', 'Лимфодренажный массаж',
                     'Польза массажа']
    elif language == 'English' and topic == 'Types of Massage':
        subtopics = ['Preparation for the Procedure', 'Swedish Massage', 'Deep Tissue Massage',
                     'Lymphatic Drainage Massage', 'Benefits of Massage']

    elif language == 'Русский' and topic == 'Виды массажеров':
        subtopics = ['Механические массажеры для лица', 'Вакуумные массажеры для лица',
                     'Ультразвуковые массажеры для лица', 'Микротоковые массажеры для лица',
                     'Многофункциональные массажеры для лица']
    elif language == 'English' and topic == 'Types of Massagers':
        subtopics = ['', '', '',
                     '', '']

    elif language == 'Русский' and topic == 'Питание':
        subtopics = ['Витамины и микроэлементы', '',
                     '', '',
                     '']
    elif language == 'English' and topic == 'Nutrition':
        subtopics = ['', '', '',
                     '', '']

    for subtopic in subtopics:
        keyboard.add(telebot.types.KeyboardButton(subtopic))
    keyboard.add(telebot.types.KeyboardButton('Back' if language == 'English' else 'Назад'))
    return keyboard


@bot.message_handler(
    func=lambda message: message.text in ['Ошибки, совершаемые во время массажа', 'Противопоказания', 'Mistakes', 'Contraindications'])
def show_topic_details(message):
    chat_id = message.chat.id
    language = user_language[chat_id]
    topic = message.text
    if language and topic:
        if language in messages and topic in messages[language]:
            data = messages[language][topic]
            text = data['text']
            image_url = data['image_url']
            bot.send_message(chat_id, text, parse_mode='HTML')
            bot.send_photo(chat_id, image_url)
        else:
            bot.send_message(chat_id, "Для выбранного языка и темы отсутствуют данные.")
    else:
        bot.send_message(chat_id, "Ошибка: отсутствует выбранный язык или тема.")


@bot.message_handler(
    func=lambda message: message.text in ['Виды массажа', 'Виды массажеров', 'Ошибки', 'Противопоказания',
                                          'Советы по питанию', 'Советы по сну',
                                          'Популярные вопросы', 'Types of Massage', 'Types of Massagers', 'Mistakes',
                                          'Contraindications', 'Nutrition Tips',
                                          'Sleep Tips', 'Frequently Asked Questions'])
def choose_subtopic(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language:
        topic = message.text
        if language == 'Русский':
            bot.send_message(chat_id, "Выберите подтему:", reply_markup=get_subtopics_keyboard(chat_id, topic))
        elif language == 'English':
            bot.send_message(chat_id, "Choose a subtopic:", reply_markup=get_subtopics_keyboard(chat_id, topic))


@bot.message_handler(
    func=lambda message: message.text in ['Подготовка к процедуре', 'Классический массаж', 'Пластический массаж',
                                          'Лимфодренажный массаж', 'Польза массажа', 'Preparation for the Procedure',
                                          'Swedish Massage', 'Deep Tissue Massage', 'Lymphatic Drainage Massage',
                                          'Benefits of Massage'])
def show_subtopic_details(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    subtopic = message.text
    if language and subtopic:
        if language in messages and subtopic in messages[language]:
            data = messages[language][subtopic]
            text = data['text']
            image_url = data['image_url']
            bot.send_message(chat_id, text, parse_mode='HTML')
            bot.send_photo(chat_id, image_url)
        else:
            bot.send_message(chat_id, "Для выбранного языка и подтемы отсутствуют данные.")
    else:
        bot.send_message(chat_id, "Ошибка: отсутствует выбранный язык или подтема.")


@bot.message_handler(func=lambda message: message.text in ['Back', 'Назад'])
def go_back(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language:
        bot.send_message(chat_id, "Choose the topic you are interested in:", reply_markup=get_topics_keyboard(chat_id))


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


bot.polling(none_stop=True, interval=0)
