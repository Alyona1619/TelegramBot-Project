import telebot
from telebot import types
from notion_database.page import Page
from notion_database.properties import Properties
from notion_database.database import Database

token = 'secret_1RiuGReKtVd1FSDEqtOPLgf2FSHvJGvXmAOBwKCh710'
db_id = 'a6fc9f7f128d4b33a37916eda8f78269'

D = Database(integrations_token=token)
D.retrieve_database(db_id, get_properties=True)
properties_list = D.properties_list

name = ''
memories = ''
evaluation = ''
sleep=False
eat=False
read=False
drink=False
care=False
step=False

bot = telebot.TeleBot('6211233672:AAGLlrz8Wt3BzUag1GYb930PFe7-vVnVtP0')
user_data = {}
menu1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = types.KeyboardButton("Homemade facial massage")
menu1.row(btn1)
btn2 = types.KeyboardButton("Healthy eating")
menu1.row(btn2)
btn3 = types.KeyboardButton("Healthy sleep")
menu1.row(btn3)
btn4 = types.KeyboardButton("Diary of healthy habits")
menu1.row(btn4)
back = types.KeyboardButton("Go back to the main menu")
menu1.row(back)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Say hello")
    btn2 = types.KeyboardButton("What can you do?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Hi! I am your personal bot that will help you maintain your natural beauty.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def func(message):
    if message.text == "Say hello":
        bot.send_message(message.from_user.id, "Hi! Ask me what I can do.")
    if message.text == "What can you do?":
        bot.send_message(message.chat.id, text="Choose a topic that interests you", reply_markup=menu1)

    elif message.text == "Go back to the main menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Say hello")
        button2 = types.KeyboardButton("What can you do?")
        markup.add(button1, button2)
        bot.send_message(message.from_user.id, text="You are back in the main menu", reply_markup=markup)


    elif message.text == "Homemade facial massage":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Preparation for the procedure", callback_data="prepare")
        markup.row(button1)
        button2 = types.InlineKeyboardButton(text="The benefits of facial massage", callback_data="useful")
        markup.row(button2)
        button3 = types.InlineKeyboardButton(text="Types of massage", callback_data="various_mas")
        markup.row(button3)
        button4 = types.InlineKeyboardButton(text="Facial Massagers", callback_data="equipment")
        markup.row(button4)
        back = types.InlineKeyboardButton(text="", callback_data="back")
        markup.row(back)
        bot.send_message(message.from_user.id,
                         "What would you like to know about massage?".format(message.from_user),
                         reply_markup=markup)

    elif message.text == "Healthy eating":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Vitamins and trace elements", callback_data="vitamins")
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
    elif message.text == "Healthy sleep":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Сколько нужно спать?", callback_data="how_much")
        markup.row(button1)
        button2 = types.InlineKeyboardButton(text="Влияние сна", callback_data="influence")
        markup.row(button2)
        button3 = types.InlineKeyboardButton(text="Восстановление после бессонницы", callback_data="bad_sleep")
        markup.row(button3)
        button4 = types.InlineKeyboardButton(text="Что съесть, чтобы лучше спать?", callback_data="healthy_food")
        markup.row(button4)
        back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        markup.row(back)
        bot.send_message(message.from_user.id,
                         "Что ты хочешь знать про сон?".format(message.from_user),
                         reply_markup=markup)


    elif message.text == "Diary of healthy habits":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ask = types.KeyboardButton("Answer the questions")
        markup.add(ask)
        bot.send_message(message.from_user.id,
                         "<b>How many harmful habits do you have?\nAnd how many beneficial ones?</b>\n\n" \
                         "Each of us can become better, healthier, more positive, and more successful!" \
                         "We have our whole life for that, 365 days a year, 7 days a week, 24 hours a day, and 60 minutes per hour.\n" \
                         "Add new beneficial habits to your life!\n\n" \
                         "The bot will ask you some questions every day, thereby reminding you to do something useful, "\
                         "and record your answers in a table!", reply_markup=markup, parse_mode='HTML')

    elif message.text == "Answer the questions":
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "What is your name?", reply_markup=a)
        bot.register_next_step_handler(message, get_name)

    elif message.text != "Say hello":
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал.../start")

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
   
    P = Page(integrations_token=token)
    P.create_page(database_id=db_id, properties=PROPERTY)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "prepare":
        bot.send_message(call.message.chat.id,
                         "&#129524;<b>PREPARATION FOR THE PROCEDURE</b>&#129524;\n\n" \
                         "Do not neglect the preparation. Otherwise, instead of firm skin, you may end up with pimples, blackheads, and various inflammations.\n\n" \
                         "Before starting the procedure, you need to choose a massage product. If you have dry skin, coconut oil will be suitable; for oily skin, " \
                         "it is better to use grape seed oil or a lightweight gel-cream. The texture of the product should not be too thick, but if it absorbs quickly, " \
                         "you won't be able to perform a full massage. You will have to constantly apply the cream. Make sure the product does not clog pores.\n\n" \
                         "<u><b>The preparatory procedures include several stages:</b></u>\n\n" \
                         "&#9989;<b>Thorough cleansing.</b> First, remove makeup with a special product: milk or micellar water. Then, make sure to wash your face with" \
                         "a foam or gel cleanser, pat your face dry with a towel, but do not rub it.\n" \
                         "&#9989;<b>Warming up.</b> The skin will respond better to the massage with creams or oils if you warm it up before " \
                         "the procedure. There is no need to steam your face; simply apply a warm towel and wait for 5 minutes.\n" \
                         "&#9989;<b>Moisturizing.</b> Massage is performed only after applying the cream. If you pull on dry skin, wrinkles and " \
                         "various damages may appear. Apply a lightweight cream or oil in a small amount along the massage lines." \
                         ,parse_mode='HTML')
    elif call.data == "useful":
        bot.send_message(call.message.chat.id,
                         "&#128171;<b>THE BENEFITS OF FACIAL MASSAGE</b>&#128171;\n\n" \
                         "The exceptional aspect of self-facial massage is that it can restore the physiological processes that have been disrupted and led to facial aging.\n\n" \
                         "<b><u>What exactly happened?</u></b>\n\n" \
                         "&#49;&#65039;&#8419; Blood flow slowed down, making it difficult to deliver nutrients to the skin cells, and local metabolism was inhibited\n" \
                         "&#50;&#65039;&#8419; Structural changes occurred in the skin: collagen, elastin, and lipids were produced in smaller quantities; " \
                         "existing collagen fibers were damaged; due to a decrease in the ability of hyaluronic acid molecules to retain moisture, "
                         "the dermis became less hydrated, and so on. All the essential characteristics of youthful skin declined: firmness, elasticity, " \
                         "strength, smoothness, and turgor.\n" \
                         "&#51;&#65039;&#8419; Let's dig deeper: the muscles. What happened to them? On the face and neck, they became tense due to overexertion, meaning they literally " \
                         "became shorter, lost elasticity, and became unable to stretch to their natural length. What did these contracted muscles do to the skin, " \
                         "which was already aging on its own? They pulled it into folds (wrinkles) and caused sagging(bulldog cheeks, vague jawline, drooping eyelids).\n" \
                         "&#52;&#65039;&#8419; Additionally, lymphatic circulation has become impaired, resulting in stagnant toxins and metabolic waste accumulating on the face like dirty mud. " \
                         "This leads to swelling, puffiness, loose skin, under-eye bags, increased wrinkles, and a downward shift of tissues.\n\n" \
                         "<b>Now let's think about what to do for rejuvenation. Logic suggests the main task is to reverse theseprocesses. In other words, we must:</b> \n\n" \
                         "&#9989; help accelerate blood circulation, improve cell nutrition\n" \
                         "&#9989; restore lymphatic flow, alleviate stagnation and edema\n" \
                         "&#9989; relax spasmodic muscles, elongate them to their natural size, and restore their elasticity\n" \
                         "&#9989; strengthen the skin by stimulating the synthesis of collagen, elastin fibers, and hyaluronic acid making it firm, elastic, strong, and well-hydrated\n\n" \
                         "Achieve all of this can only be done through self-massage. There are auxiliary methods (cosmetics, nutrition, hydration, overall physical activity, etc.), " \
                         "but self-massage is the foundation.\n\n" \
                         "<u><b>The results of a skillful anti-aging massage</b>:</u>\n\n" \
                         "&#128900;Wrinkles, folds, creases, and nasolabial lines are smoothed\n" \
                         "&#128900;The skin becomes firm and taut\n" \
                         "&#128900;Edema, under-eye bags, and &quot;bulldog cheeks&quot; are reduced\n" \
                         "&#128900;The jawline is lifted, and the &quot;youthful angle&quot; is well-defined without a double chin\n" \
                         "&#128900;The gaze appears more open and refreshed\n" \
                         "&#128900;The corners of the lips are lifted\n" \
                         "&#128900;The nose appears more refined\n" \
                         "&#128900;The complexion appears healthy and vibrant",
                         parse_mode='HTML')
    elif call.data == "various_mas":
        bot.send_message(call.message.chat.id,
                         "&#127800;<b>TYPES OF HOME FACIAL MASSAGE AND TECHNIQUES</b>&#127800;\n\n" \
                         "<b><u>Classic Massage</u></b>\n\n" \
                         "How to perform a facial massage? The most important thing is to master the technique. To do this, it is necessary to have a good " \
                         "understanding of the massage lines and control the pressure of your fingers.\nThe technique of performing a classic facial massage " \
                         "revolves around four main movements:\n&#9643;Rubbing\n&#9643;Stroking\n&#9643;Kneading\n&#9643;Vibration\n\n" \
                         "All movements are performed in a specific sequence and do not involve strong pressure. Let's list the main stages of a classic facial massage.\n\n" \
                         "&#9725;Usually, the massage starts from the chin (direction - from the lower point in the middle towards the earlobe).\n" \
                         "&#9725;Then, the area around the mouth is worked on.\n" \
                         "&#9725;The next stage is the cheeks.\n" \
                         "&#9725;Then, the outer corners of the eyes are massaged.\n" \
                         "&#9725;The T-zone is massaged in the direction from the nose towards the temples.\n" \
                         "&#9725;The massage session concludes with a massage of the forehead.\n\n" \
                         "The main movements in classical facial massage are stroking. Less time is dedicated to vibrations, " \
                         "kneading, and tapping. Usually, the entire procedure takes no more than 30 minutes.\n" \
                         "To feel the effects of a classical facial massage, sometimes just one session is enough. " \
                         "The skin immediately becomes firmer and more toned. The complexion changes, and a radiant glow appears. " \
                         "To maintain the achieved results, it is recommended to undergo a course of 8-10 sessions, once per week." \

                         

                         ,
                         parse_mode='HTML')
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
