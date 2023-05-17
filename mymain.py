import telebot
from messages import *

BOTTOKEN = '5136913496:AAFVF_8Ua_bXVTGtC3N6XuMI8YbTZ_UOLCo'

bot = telebot.TeleBot(BOTTOKEN)

# Клавиатура с выбором языка
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard.add(telebot.types.KeyboardButton('Русский'), telebot.types.KeyboardButton('English'))

# Словарь для хранения выбранного языка пользователей
user_language = {}

all_topics = ['Подготовка к процедуре', 'Классический массаж', 'Пластический массаж', 'Лимфодренажный массаж',
              'Польза массажа', 'Механические массажеры для лица', 'Вакуумные массажеры для лица', #4
              'Ультразвуковые массажеры для лица', 'Микротоковые массажеры для лица', #7
              'Многофункциональные массажеры для лица', 'Витамины и микроэлементы', 'Полезные продукты', 'Питьевой режим', #9
              'Правила питания для здоровой кожи', 'Вредные продукты', 'Сколько нужно спать и почему вредно недосыпать?', #13
              'Как сон влияет на гормоны и кожу?','Как восстановить кожу после бессонницы?', #16
              'Что съесть, чтобы крепко спать?', 'Правила "Доброй ночи"', #18
              'Preparation for the Procedure', 'Classic massage', 'Plastic massage', 'Lymphatic drainage massage',
              'The benefits of facial massage', 'Mechanical', 'Vacuum', 'Ultrasonic', 'Multifunctional',
              'Vitamins and Micronutrients', 'Healthy products', 'Unhealthy products', 'Drinking regime',
              'Dietary rules for healthy skin', 'How much sleep do you need?', 'How does sleep affect hormones and the skin?',
              'How can you restore the skin after insomnia?', 'What to eat to sleep well?', 'The rules of "Good night"'
              ]

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Привет! Я BeautyTouch Bot! Я твой помощник по уходу за собой, массажу и ведению "
                     "здорового образа жизни. Выбери язык, на котором я буду с тобой общаться:\n\n"
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
        subtopics = all_topics[0:5]
    elif language == 'English' and topic == 'Types of Massage':
        subtopics = all_topics[20:25]

    elif language == 'Русский' and topic == 'Виды массажеров':
        subtopics = all_topics[5:10]
    elif language == 'English' and topic == 'Types of Massagers':
        subtopics = all_topics[25:30]

    elif language == 'Русский' and topic == 'Советы по питанию':
        subtopics = all_topics[10:15]
    elif language == 'English' and topic == 'Nutrition Tips':
        subtopics = all_topics[30:35]

    elif language == 'Русский' and topic == 'Советы по сну':
        subtopics = all_topics[15:20]
    elif language == 'English' and topic == 'Sleep Tips':
        subtopics = all_topics[35:40]

    for subtopic in subtopics:
        keyboard.add(telebot.types.KeyboardButton(subtopic))
    keyboard.add(telebot.types.KeyboardButton('Back' if language == 'English' else 'Назад'))
    return keyboard


@bot.message_handler(
    func=lambda message: message.text in ['Ошибки, совершаемые во время массажа', 'Противопоказания', 'Mistakes',
                                          'Contraindications'])
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
            bot.send_photo(chat_id, photo=open(image_url, 'rb'))
        else:
            bot.send_message(chat_id, "Для выбранного языка и темы отсутствуют данные.")
    else:
        bot.send_message(chat_id, "Ошибка: отсутствует выбранный язык или тема.")


@bot.message_handler(
    func=lambda message: message.text in ['Виды массажа', 'Виды массажеров',
                                          'Советы по питанию', 'Советы по сну',
                                          'Популярные вопросы', 'Types of Massage', 'Types of Massagers', 'Nutrition Tips',
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
    func=lambda message: message.text in all_topics)
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
            bot.send_photo(chat_id, photo=open(image_url, 'rb'))
        else:
            bot.send_message(chat_id, "Для выбранного языка и подтемы отсутствуют данные.")
    else:
        bot.send_message(chat_id, "Ошибка: отсутствует выбранный язык или подтема.")


@bot.message_handler(func=lambda message: message.text in ['Back', 'Назад'])
def go_back(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language == 'Русский':
        bot.send_message(chat_id, "Выбери интересующую тебя тему:", reply_markup=get_topics_keyboard(chat_id))
    elif language == 'English':
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
