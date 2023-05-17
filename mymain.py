import telebot
from notion_database.page import Page
from notion_database.properties import Properties
from notion_database.database import Database
from keyboards import *
from consts import *
from messages import *

bot = telebot.TeleBot(BOTTOKEN)

D = Database(integrations_token=N_TOKEN)
D.retrieve_database(DB_ID, get_properties=True)
properties_list = D.properties_list


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Привет! Я BeautyTouch Bot!\nЯ твой помощник по уходу за собой, массажу и ведению "
                     "здорового образа жизни. Выбери язык, на котором я буду с тобой общаться:\n\n"
                     "Hi! I'm a BeautyTouch Bot!\nI am your assistant for self-care, massage and healthy lifestyle. "
                     "Choose the language in which I will communicate with you:", reply_markup=keyboard)


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
                                          'Советы по питанию', 'Советы по сну', 'Types of Massage',
                                          'Types of Massagers',
                                          'Nutrition Tips',
                                          'Sleep Tips', ])
def choose_subtopic(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language:
        topic = message.text
        if language == 'Русский':
            bot.send_message(chat_id, "Выберите подтему:", reply_markup=get_subtopics_keyboard(chat_id, topic))
        elif language == 'English':
            bot.send_message(chat_id, "Choose a subtopic:", reply_markup=get_subtopics_keyboard(chat_id, topic))


@bot.message_handler(func=lambda message: message.text in all_topics)
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


@bot.message_handler(func=lambda message: message.text in ['Дневник полезных привычек', 'Diary of healthy habits'])
def diary(message):
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language == 'Русский':
        bot.send_message(chat_id, "<b> Сколько у вас вредных привычек? А сколько полезных?</b>\n\n"
                                  "Каждый из нас может стать лучше, здоровее, позитивнее и успешнее!"
                                  "У нас есть для этого вся наша жизнь, 365 дней в году, 7 дней в неделю, 24 часа в сутки и 60 минут в час"
                                  "Добавьте в свою жизнь новые полезные привычки!"
                                  "Бот будет задавать вам несколько вопросов каждый день, тем самым напоминая вам о необходимости сделать что-то полезное"
                                  "и запишет ваши ответы в таблицу!", parse_mode='HTML', reply_markup=get_diary_keyboard(chat_id))
    elif language == 'English':
        bot.send_message(chat_id,
                         "<b>How many harmful habits do you have?\nAnd how many beneficial ones?</b>\n\n"
                         "Each of us can become better, healthier, more positive, and more successful!"
                         "We have our whole life for that, 365 days a year, 7 days a week, 24 hours a day, and 60 minutes per hour.\n"
                         "Add new beneficial habits to your life!\n\n"
                         "The bot will ask you some questions every day, thereby reminding you to do something useful, "
                         "and record your answers in a table!", parse_mode='HTML', reply_markup=get_diary_keyboard(chat_id))


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


name = ''
memories = ''
evaluation = ''
sleep = False
eat = False
read = False
drink = False
care = False
step = False


@bot.message_handler(func=lambda message: message.text in ['Answer the questions', 'Ответить на вопросы'])
def start_ask_questions(message):
    chat_id = message.chat.id
    a = types.ReplyKeyboardRemove()
    bot.send_message(chat_id, "What is your name?", reply_markup=a)
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'What do you remember most today?')
    bot.register_next_step_handler(message, get_memories)


def get_memories(message):
    global memories
    memories = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    excellent = types.KeyboardButton("\U0001F603 excellent")
    normal = types.KeyboardButton("\U0001F642 normal")
    bad = types.KeyboardButton("\U0001F61E bad")
    markup.add(excellent, normal, bad)
    bot.send_message(message.from_user.id, 'Give an assessment of today', reply_markup=markup)
    bot.register_next_step_handler(message, get_evaluation)


def get_evaluation(message):
    global evaluation
    evaluation = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("\U0001F603 Yes")
    no = types.KeyboardButton("\U0001F61E No")
    markup.add(yes, no)
    bot.send_message(message.from_user.id, 'Have you drunk 1.5 liters of water?', reply_markup=markup)
    bot.register_next_step_handler(message, get_drinking)


def get_drinking(message):
    global drink
    if message.text == 'Yes':
        drink = True
    else:
        drink = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("\U0001F603 Yes")
    no = types.KeyboardButton("\U0001F61E No")
    markup.add(yes, no)
    bot.send_message(message.from_user.id, 'Have you slept more than 8 hours?', reply_markup=markup)
    bot.register_next_step_handler(message, get_sleeping)


def get_sleeping(message):
    global sleep
    if message.text == 'Yes':
        sleep = True
    else:
        sleep = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("\U0001F603 Yes")
    no = types.KeyboardButton("\U0001F61E No")
    markup.add(yes, no)
    bot.send_message(message.from_user.id, 'Have you walked at least 10,000 steps?', reply_markup=markup)
    bot.register_next_step_handler(message, get_walking)


def get_walking(message):
    global step
    if message.text == 'Yes':
        step = True
    else:
        step = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("\U0001F603 Yes")
    no = types.KeyboardButton("\U0001F61E No")
    markup.add(yes, no)
    bot.send_message(message.from_user.id, 'Have you eaten healthy food?', reply_markup=markup)
    bot.register_next_step_handler(message, get_eating)


def get_eating(message):
    global eat
    if message.text == 'Yes':
        eat = True
    else:
        eat = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("\U0001F603 Yes")
    no = types.KeyboardButton("\U0001F61E No")
    markup.add(yes, no)
    bot.send_message(message.from_user.id, 'Have you read at least 20 pages of the book?', reply_markup=markup)
    bot.register_next_step_handler(message, get_reading)


def get_reading(message):
    global read
    if message.text == 'Yes':
        read = True
    else:
        read = True

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton("\U0001F603 Yes")
    no = types.KeyboardButton("\U0001F61E No")
    markup.add(yes, no)
    bot.send_message(message.from_user.id, 'Have you performed skin care procedures?', reply_markup=markup)
    bot.register_next_step_handler(message, get_caring)


def get_caring(message):

    global care
    if message.text == 'Yes':
        care = True
    else:
        care = True

    fill_table(name, memories, sleep, eat, read, drink, care, step)
    chat_id = message.chat.id
    language = user_language.get(chat_id)
    if language == 'Русский':
        bot.send_message(chat_id, "Спасибо! Ответы записаны! Возвращаю в главное меню", reply_markup=get_topics_keyboard(chat_id))
    elif language == 'English':
        bot.send_message(chat_id, "Thanks! The answers are recorded! I return to the main menu", reply_markup=get_topics_keyboard(chat_id))


def fill_table(name, memories, sleep, eat, read, drink, care, step):
    PROPERTY = Properties()
    PROPERTY.set_title("Name", f"{name}")
    PROPERTY.set_select("Evaluation of the day", evaluation)
    PROPERTY.set_rich_text("What do you remember most today?", f"{memories}")
    PROPERTY.set_checkbox("Sleep more than 8 hours", sleep)
    PROPERTY.set_checkbox("Eat healthy food", eat)
    PROPERTY.set_checkbox("Read at least 20 pages of the book", read)
    PROPERTY.set_checkbox("Drink 1.5 liters of water", drink)
    PROPERTY.set_checkbox("Facial skin care", care)
    PROPERTY.set_checkbox("Go 10,000 steps", step)

    P = Page(integrations_token=N_TOKEN)
    P.create_page(database_id=DB_ID, properties=PROPERTY)


bot.polling(none_stop=True, interval=0)
