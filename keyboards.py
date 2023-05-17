from consts import *
from telebot import types

keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
keyboard.add(types.KeyboardButton('Русский'), types.KeyboardButton('English'))

def get_topics_keyboard(chat_id):
    language = user_language[chat_id]
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'Русский':
        topics = ['Виды массажа', 'Виды массажеров', 'Ошибки, совершаемые во время массажа', 'Противопоказания',
                  'Советы по питанию', 'Советы по сну', 'Дневник полезных привычек']
    elif language == 'English':
        topics = ['Types of Massage', 'Types of Massagers', 'Mistakes', 'Contraindications', 'Nutrition Tips',
                  'Sleep Tips', 'Diary of healthy habits']
    for topic in topics:
        keyboard.add(types.KeyboardButton(topic))
    return keyboard


def get_subtopics_keyboard(chat_id, topic):
    language = user_language[chat_id]
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'Русский' and topic == 'Виды массажа':
        subtopics = all_topics[0:5]
    elif language == 'English' and topic == 'Types of Massage':
        subtopics = all_topics[22:27]

    elif language == 'Русский' and topic == 'Виды массажеров':
        subtopics = all_topics[5:10]
    elif language == 'English' and topic == 'Types of Massagers':
        subtopics = all_topics[29:34]

    elif language == 'Русский' and topic == 'Советы по питанию':
        subtopics = all_topics[12:17]
    elif language == 'English' and topic == 'Nutrition Tips':
        subtopics = all_topics[34:39]

    elif language == 'Русский' and topic == 'Советы по сну':
        subtopics = all_topics[18:22]
    elif language == 'English' and topic == 'Sleep Tips':
        subtopics = all_topics[39:44]

    for subtopic in subtopics:
        keyboard.add(types.KeyboardButton(subtopic))
    keyboard.add(types.KeyboardButton('Back' if language == 'English' else 'Назад'))
    return keyboard


def get_diary_keyboard(chat_id):
    language = user_language.get(chat_id)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    if language == 'English':
        keyboard.add(types.KeyboardButton('Answer the questions'))
        keyboard.add(types.KeyboardButton('Back'))
    else:
        keyboard.add(types.KeyboardButton('Ответить на вопросы'))
        keyboard.add(types.KeyboardButton('Назад'))
    return keyboard
