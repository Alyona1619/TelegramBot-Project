import telebot
from telebot import types

bot = telebot.TeleBot('6211233672:AAGLlrz8Wt3BzUag1GYb930PFe7-vVnVtP0');
# name = '';
# surname = '';
# age = 0;
start = '';


@bot.message_handler(content_types=['text', 'document', 'audio'])
def start(message):
    global start;
    start = message.text;
    if not (start.startswith('/')):
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?\n /start")
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Вот что я могу: \nДомашний массаж /massage \nПитание /food \nСон /dream \nПолезные привычки /habits")
    if message.text == "/massage":
        bot.send_message(message.from_user.id,
                         "Подготовка к процедуре /prepare \nПольза /useful \nВиды массажа /types_massage \nМассажеры для лица /types_equipment")
    if message.text == "/food":
        bot.send_message(message.from_user.id,
                         "Витамины и микроэлементы /vitamins \nПолезные продукты /useful_products \nПитьевой режим /water \nПравила питания для здоровой кожи /rules \nВредные продукты /junk_food")
    if message.text == "/dream":
        bot.send_message(message.from_user.id,
                         "Сколько нужно спать /how_much \nВлияние сна /vliyan \nВосстановление после бессонници /bad_sleep \nЧто съесть? чтобы лучше спать? /healthy_food")
    if message.text == "/habits":
        bot.send_message(message.from_user.id, "(тут notion подключить)")


# def get_name(message):  # получаем фамилию
#    global name;
#    name = message.text;
#    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
#    bot.register_next_step_handler(message, get_surname);


# def get_surname(message):
#    global surname;
#    surname = message.text;
#    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
#    bot.register_next_step_handler(message, get_age);


# def get_age(message):
#    global age;
#    while age == 0:  # проверяем что возраст изменился
#        try:
#            age = int(message.text)  # проверяем, что возраст введен корректно
#        except Exception:
#            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
#    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')


# def get_age(message):
#    global age;
#    while age == 0:  # проверяем что возраст изменился
#        try:
#            age = int(message.text)  # проверяем, что возраст введен корректно
#        except Exception:
#            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
#    keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
#    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
#    keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
#    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
#    keyboard.add(key_no);
#    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?';
#    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
#         # код сохранения данных, или их обработки
#        bot.send_message(call.message.chat.id, 'Запомню : )');
#    if call.data == "no":
#        bot.send_message(call.message.chat.id, 'не запомню : (');
#         # переспрашиваем

# keyboard = types.InlineKeyboardMarkup();
# key_massage = types.InlineKeyboardButton(text='Домашний массаж', callback_data='massage');
# keyboard.add(key_massage);  # добавляем кнопку в клавиатуру
# key_food = types.InlineKeyboardButton(text='Питание', callback_data='food');
# keyboard.add(key_food);
# key_dream = types.InlineKeyboardButton(text='Сон', callback_data='dream');
# keyboard.add(key_dream);
# key_habits = types.InlineKeyboardButton(text='Полезные привычки', callback_data='habits');
# keyboard.add(key_habits);
# bot.send_message(message.from_user.id, text='Вот что я могу: \n', reply_markup=keyboard)
# else:
#   bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# if message.text == '/reg':
#   bot.send_message(message.from_user.id, "Как тебя зовут?");
#  bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
# else:
#   bot.send_message(message.from_user.id, 'Напиши /reg');
# else:
# bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#    if call.data == "massage":
#        bot.send_message(call.message.chat.id, 'Далее про массаж');
#    if call.data == "food":
#        bot.send_message(call.message.chat.id, 'Далее про питание');
#    if call.data == "dream":
#        bot.send_message(call.message.chat.id, 'Далее про сон');
#    if call.data == "dream":
#        bot.send_message(call.message.chat.id, 'тут notion подключить');

bot.polling(none_stop=True, interval=0)
