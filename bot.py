import telebot
from telebot import types

bot = telebot.TeleBot('6211233672:AAGLlrz8Wt3BzUag1GYb930PFe7-vVnVtP0')
user_data = {}
menu1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = types.KeyboardButton("Домашний массаж")
menu1.row(btn1)
btn2 = types.KeyboardButton("Питание")
menu1.row(btn2)
btn3 = types.KeyboardButton("Сон")
menu1.row(btn3)
btn4 = types.KeyboardButton("Полезные привычки")
menu1.row(btn4)
back = types.KeyboardButton("Вернуться в главное меню")
menu1.row(back)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Что ты можешь?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет! Я твой персональный бот для красоты".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def func(message):
    if message.text == "👋 Поздороваться":
        bot.send_message(message.from_user.id, "Привет! Спроси меня, что я могу")
    if message.text == "Что ты можешь?":
        bot.send_message(message.chat.id, text="Выбери тему", reply_markup=menu1)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("Что ты можешь?")
        markup.add(button1, button2)
        bot.send_message(message.from_user.id, text="Вы вернулись в главное меню", reply_markup=markup)


    elif message.text == "Домашний массаж":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Подготовка к процедуре", callback_data="prepare")
        markup.row(button1)
        button2 = types.InlineKeyboardButton(text="Польза", callback_data="useful")
        markup.row(button2)
        button3 = types.InlineKeyboardButton(text="Виды массажа", callback_data="various_mas")
        markup.row(button3)
        button4 = types.InlineKeyboardButton(text="Массажеры для лица ", callback_data="equipment")
        markup.row(button4)
        back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        markup.row(back)
        bot.send_message(message.from_user.id,
                         "Что ты хочешь знать про массаж?".format(message.from_user),
                         reply_markup=markup)

    elif message.text == "Питание":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Витамины и микроэлементы", callback_data="vitamins")
        markup.row(button1)
        button2 = types.InlineKeyboardButton(text="Полезные продукты", callback_data="useful_products")
        markup.row(button2)
        button3 = types.InlineKeyboardButton(text="Питьевой режим", callback_data="water")
        markup.row(button3)
        button4 = types.InlineKeyboardButton(text="Правила питания для здоровой кожи", callback_data="rules")
        markup.row(button4)
        button5 = types.InlineKeyboardButton(text="Вредные продукты", callback_data="junk_food")
        markup.row(button5)
        back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        markup.row(back)
        bot.send_message(message.from_user.id,
                         "Что ты хочешь знать про питание?".format(message.from_user),
                         reply_markup=markup)
    elif message.text == "Сон":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Сколько нужно спать?", callback_data="how_much")
        markup.row(button1)
        button2 = types.InlineKeyboardButton(text="Влияние сна", callback_data="influence")
        markup.row(button2)
        button3 = types.InlineKeyboardButton(text="Восстановление после бессонници", callback_data="bad_sleep")
        markup.row(button3)
        button4 = types.InlineKeyboardButton(text="Что съесть, чтобы лучше спать?", callback_data="healthy_food")
        markup.row(button4)
        back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        markup.row(back)
        bot.send_message(message.from_user.id,
                         "Что ты хочешь знать про сон?".format(message.from_user),
                         reply_markup=markup)

    elif message.text == "Полезные привычки":
        bot.send_message(message.from_user.id, "(тут notion подключить)")

    elif message.text != "👋 Поздороваться":
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал.../start")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "prepare":
        bot.send_message(call.message.chat.id, 'Далее про массаж')
    elif call.data == "useful":
        bot.send_message(call.message.chat.id, 'Далее про полезность')
    elif call.data == "various_mas":
        bot.send_message(call.message.chat.id, 'Далее про виды массажа')
    elif call.data == "equipment":
        bot.send_message(call.message.chat.id, 'Далее про инструменты')
    elif call.data == "vitamins":
        bot.send_message(call.message.chat.id, 'Далее про витамины')
    elif call.data == "useful_products":
        bot.send_message(call.message.chat.id, 'Далее про полезные продукты')
    elif call.data == "water":
        bot.send_message(call.message.chat.id, 'Далее про воду')
    elif call.data == "rules":
        bot.send_message(call.message.chat.id, 'Далее про правила')
    elif call.data == "junk_food":
        bot.send_message(call.message.chat.id, 'Далее про нездоровую пищу')
    elif call.data == "how_much":
        bot.send_message(call.message.chat.id, 'Далее про сколько спать')
    elif call.data == "influence":
        bot.send_message(call.message.chat.id, 'Далее про влияние сна')
    elif call.data == "bad_sleep":
        bot.send_message(call.message.chat.id, 'Далее про бессоницу')
    elif call.data == "healthy_food":
        bot.send_message(call.message.chat.id, 'Далее про здоровую пищу')
    elif call.data == "back":
        bot.send_message(call.message.chat.id, 'Выбери тему', reply_markup=menu1)



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

# @bot.message_handler(commands=['start'])
# def start(message):
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    btn1 = types.KeyboardButton("👋 Поздороваться")
#    btn2 = types.KeyboardButton("❓ Задать вопрос")
#    markup.add(btn1, btn2)
#    bot.send_message(message.chat.id,
#                     text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
#                         message.from_user), reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def func(message):
#    if (message.text == "👋 Поздороваться"):
#        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
#    elif (message.text == "❓ Задать вопрос"):
#        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#        btn1 = types.KeyboardButton("Как меня зовут?")
#        btn2 = types.KeyboardButton("Что я могу?")
#        back = types.KeyboardButton("Вернуться в главное меню")
#        markup.add(btn1, btn2, back)
#        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

#    elif (message.text == "Как меня зовут?"):
#        bot.send_message(message.chat.id, "У меня нет имени..")

#    elif message.text == "Что я могу?":
#        bot.send_message(message.chat.id, text="Поздороваться с читателями")

#    elif (message.text == "Вернуться в главное меню"):
#        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#        button1 = types.KeyboardButton("👋 Поздороваться")
#        button2 = types.KeyboardButton("❓ Задать вопрос")
#        markup.add(button1, button2)
#        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#    else:
#        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


# bot.polling(none_stop=True)

bot.polling(none_stop=True, interval=0)
