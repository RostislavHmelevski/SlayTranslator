import telebot
import random
from telebot import types

bot = telebot.TeleBot('8001867610:AAGSD2sDO1SgKV5CGP5Rxh_G8zQZR_43ZC0')

# меню языков
language_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
english = types.KeyboardButton("Английcкий")
german = types.KeyboardButton("Немецкий")
french = types.KeyboardButton("Французcкий")

# меню английкого
english_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
english_translations = types.KeyboardButton("Английcкие cлова")
english_easy_mode = types.KeyboardButton("Легкий Режим Английcкого!")
english_harder_mode = types.KeyboardButton("Сложный Режим Английcкого!")
english_hardest_mode = types.KeyboardButton("Невозможный Режим Английcкого!")

# меню немецкого
german_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
german_translations = types.KeyboardButton("Немецкие cлова")
german_easy_mode = types.KeyboardButton("Легкий Режим Немецкого!")
german_harder_mode = types.KeyboardButton("Сложный Режим Немецкого!")
german_hardest_mode = types.KeyboardButton("Невозможный Режим Немецкого!")

# меню французкого
french_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
french_translations = types.KeyboardButton("Французcкие cлова")
french_easy_mode = types.KeyboardButton("Легкий Режим Французcкого!")
french_harder_mode = types.KeyboardButton("Сложный Режим Французcкого!")
french_hardest_mode = types.KeyboardButton("Невозможный Режим Французcкого!")

# sтатиsтика
statisis = types.KeyboardButton("Общая Статиcтика")
english_statisis = types.KeyboardButton("Английcкая Статиcтика")
german_statisis = types.KeyboardButton("Немецкая Статиcтика")
french_statisis = types.KeyboardButton("Французcкая Статиcтика")

# экsперемент
experement = types.KeyboardButton("Экcперементальный Режим")

# теsт
test = types.KeyboardButton("Прохождение Теcта")

# задания
sentense = types.KeyboardButton("Задание по Английcкому")

fog_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
foging = types.KeyboardButton("ТУМАН")
fog_menu.add(foging)

bak = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton("Назад")
bak.add(button)

language_menu.add(english, german, french, statisis, experement, test)
english_menu.add(english_translations, english_easy_mode, english_harder_mode, english_hardest_mode, english_statisis,
                 sentense, button)
german_menu.add(german_translations, german_easy_mode, german_harder_mode, german_hardest_mode, german_statisis, button)
french_menu.add(french_translations, french_easy_mode, french_harder_mode, french_hardest_mode, french_statisis, button)

# база данных енг
englishwords = {
    "apple": "яблоко",
    "book": "книга",
    "cat": "кот",
    "dog": "собака",
    "elephant": "слон",
    "fish": "рыба",
    "grape": "виноград",
    "house": "дом",
    "ice cream": "мороженое",
    "jacket": "куртка"
}

englisheasy_words = {"apple": "яблоко",
                     "book": "книга",
                     "cat": "кот"}

englishharder_words = {"dog": "собака",
                       "elephant": "слон",
                       "fish": "рыба"}

englishhardest_words = {"grape": "виноград",
                        "house": "дом",
                        "ice cream": "мороженое",
                        "jacket": "куртка"}

# база данных немецкого
germanwords = {
    "apfel": "яблоко",
    "buch": "книга",
    "katze": "кот",
    "hund": "собака",
    "elefant": "слон",
    "fisch": "рыба",
    "trauben": "виноград",
    "haus": "дом",
    "eis": "мороженое",
    "jacke": "куртка"
}

germaneasy_words = {"apfel": "яблоко",
                    "buch": "книга",
                    "katze": "кот"}

germanharder_words = {"hund": "собака",
                      "elefant": "слон",
                      "fisch": "рыба"}

germanhardest_words = {"trauben": "виноград",
                       "haus": "дом",
                       "eis": "мороженое",
                       "jacke": "куртка"}

# база данных немецкого
frenchwords = {
    "pomme": "яблоко",
    "livre": "книга",
    "chat": "кот",
    "chien": "собака",
    "elephant": "слон",
    "poisson": "рыба",
    "raisins": "виноград",
    "maison": "дом",
    "creme glacee": "мороженое",
    "veste": "куртка"
}

frencheasy_words = {"pomme": "яблоко",
                    "livre": "книга",
                    "chat": "кот"}

frenchharder_words = {"chien": "собака",
                      "elephant": "слон",
                      "poisson": "рыба"}

frenchhardest_words = {"raisins": "виноград",
                       "maison": "дом",
                       "creme glacee": "мороженое",
                       "veste": "куртка"}

experemental_data = {"apple": "яблоко",
                     "book": "книга",
                     "cat": "кот",
                     "dog": "собака",
                     "elephant": "слон",
                     "fish": "рыба",
                     "grape": "виноград",
                     "house": "дом",
                     "ice cream": "мороженое",
                     "jacket": "куртка",
                     "apfel": "яблоко",
                     "buch": "книга",
                     "katze": "кот",
                     "hund": "собака",
                     "elefant": "слон",
                     "fisch": "рыба",
                     "trauben": "виноград",
                     "haus": "дом",
                     "eis": "мороженое",
                     "jacke": "куртка",
                     "pomme": "яблоко",
                     "livre": "книга",
                     "chat": "кот",
                     "chien": "собака",
                     "elephant": "слон",
                     "poisson": "рыба",
                     "raisins": "виноград",
                     "maison": "дом",
                     "creme glacee": "мороженое",
                     "veste": "куртка"
                     }

sentense_data = {"He is _______ a book": "reading",
                 "She ____ go to cinema tommorow": "will",
                 "They ___ going to me": "are",
                 "The ___ is coming": "frog"
                 }

table = []


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет! Выбери язык для изучения!', reply_markup=language_menu)


@bot.message_handler(content_types=['text'])
def text_messages(message):
    engword, engtranslation = random.choice(list(englishwords.items()))
    engeasyword, engeasytranslation = random.choice(list(englisheasy_words.items()))
    engharderword, enghardertranslation = random.choice(list(englishharder_words.items()))
    enghardestword, enghardesttranslation = random.choice(list(englishhardest_words.items()))

    gerword, gertranslation = random.choice(list(germanwords.items()))
    gereasyword, gereasytranslation = random.choice(list(germaneasy_words.items()))
    gerharderword, gerhardertranslation = random.choice(list(germanharder_words.items()))
    gerhardestword, gerhardesttranslation = random.choice(list(germanhardest_words.items()))

    frenword, frentranslation = random.choice(list(frenchwords.items()))
    freneasyword, freneasytranslation = random.choice(list(frencheasy_words.items()))
    frenharderword, frenhardertranslation = random.choice(list(frenchharder_words.items()))
    frenhardestword, frenhardesttranslation = random.choice(list(frenchhardest_words.items()))

    exword, extranslation = random.choice(list(experemental_data.items()))
    senword, sentranslation = random.choice(list(sentense_data.items()))
    testword, testword = random.choice(list(experemental_data.items()))

    # англ
    if message.text == "Английcкий":
        bot.send_message(message.chat.id, f'Хорошо! Выбери теперь режим!', reply_markup=english_menu)
    elif message.text == "Английcкие cлова":
        bot.send_message(message.chat.id, f'Заучи! {engword} это {engtranslation}!')
    elif message.text == "Легкий Режим Английcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{engeasyword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, easy_quiz)
    elif message.text == "Сложный Режим Английcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{engharderword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, harder_quiz)
    elif message.text == "Невозможный Режим Английcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{enghardestword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, hardest_quiz)
    elif message.text == "Назад":
        bot.send_message(message.chat.id, f'Хорошо! Выбери теперь режим!', reply_markup=language_menu)

    # нем
    if message.text == "Немецкий":
        bot.send_message(message.chat.id, f'Хорошо! Выбери теперь режим!', reply_markup=german_menu)
    elif message.text == "Немецкие cлова":
        bot.send_message(message.chat.id, f'Заучи! {gerword} это {gertranslation}!')
    elif message.text == "Легкий Режим Немецкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{gereasyword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gereasy_quiz)
    elif message.text == "Сложный Режим Немецкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{gerharderword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gerharder_quiz)
    elif message.text == "Невозможный Режим Немецкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{gerhardestword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gerhardest_quiz)

    # франц
    if message.text == "Французcкий":
        bot.send_message(message.chat.id, f'Хорошо! Выбери теперь режим!', reply_markup=french_menu)
    elif message.text == "Французcкие cлова":
        bot.send_message(message.chat.id, f'Заучи! {frenword} это {frentranslation}!')
    elif message.text == "Легкий Режим Французcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{freneasyword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, freneasy_quiz)
    elif message.text == "Сложный Режим Французcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{frenharderword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, frenharder_quiz)
    elif message.text == "Невозможный Режим Французcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{frenhardestword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, frenhardest_quiz)
    elif message.text == "ТУМАН":
        bot.send_message(message.chat.id, f'HAPPY HALLOWEEN!')

    # cтатиcтика
    if message.text == "Общая Статиcтика":
        bot.send_message(message.chat.id,
                         f'У тебя:\n{stat} Угаданных Слов, из которых:\n{eng_stat} Угаданных Английских Слов\n{ger_stat} Угаданных Немецких Слов\n{fren_stat} Угаданных Французских Слов')

    # экперементальный режим
    if message.text == "Экcперементальный Режим":
        bot.send_message(message.chat.id, f'Как переводится слово "{exword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ex_quiz)

    # Задание по Английcкому
    if message.text == "Задание по Английcкому":
        bot.send_message(message.chat.id, f'Вcтавь пропущенное cлово: "{senword}"...',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, sen_quiz)


# ex квиз
def ex_quiz(message):
    user_answer = message.text.lower()
    for exword, extranslation in experemental_data.items():
        if user_answer == extranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=language_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=language_menu)


# test



# задание по английкому
def sen_quiz(message):
    user_answer = message.text.lower()
    for senword, sentranslation in sentense_data.items():
        if user_answer == sentranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_menu)
            return
        elif user_answer == 'fog':
            bot.send_message(message.chat.id, 'ThE FoG IS cOMiNG!', reply_markup=fog_menu)
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=english_menu)


# англ квиз
def easy_quiz(message):
    user_answer = message.text.lower()
    for engeasyword, engeasytranslation in englisheasy_words.items():
        if user_answer == engeasytranslation:
            bot.send_message(message.from_user.id, 'Молодец!', reply_markup=english_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=english_menu)


def harder_quiz(message):
    user_answer = message.text.lower()
    for engharderword, enghardertranslation in englishharder_words.items():
        if user_answer == enghardertranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=english_menu)


def hardest_quiz(message):
    user_answer = message.text.lower()
    for enghardestword, enghardesttranslation in englishhardest_words.items():
        if user_answer == enghardesttranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=english_menu)


# нем квиз
def gereasy_quiz(message):
    user_answer = message.text.lower()
    for gereasyword, gereasytranslation in germaneasy_words.items():
        if user_answer == gereasytranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=german_menu)


def gerharder_quiz(message):
    user_answer = message.text.lower()
    for gerharderword, gerhardertranslation in germanharder_words.items():
        if user_answer == gerhardertranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=german_menu)


def gerhardest_quiz(message):
    user_answer = message.text.lower()
    for gerhardestword, gerhardesttranslation in germanhardest_words.items():
        if user_answer == gerhardesttranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=german_menu)


# френ квиз
def freneasy_quiz(message):
    user_answer = message.text.lower()
    for freneasyword, freneasytranslation in frencheasy_words.items():
        if user_answer == freneasytranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=french_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=french_menu)


def frenharder_quiz(message):
    user_answer = message.text.lower()
    for frenharderword, frenhardertranslation in frenchharder_words.items():
        if user_answer == frenhardertranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=french_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=french_menu)


def frenhardest_quiz(message):
    user_answer = message.text.lower()
    for frenhardestword, frenhardesttranslation in frenchhardest_words.items():
        if user_answer == frenhardesttranslation:
            bot.send_message(message.chat.id, 'Молодец!', reply_markup=french_menu)
            return
    bot.send_message(message.chat.id, 'Неправильно!', reply_markup=french_menu)


eng_stat = 0
ger_stat = 0
fren_stat = 0
stat = 0

bot.infinity_polling()
