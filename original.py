import telebot
import random
from telebot import types

bot = telebot.TeleBot('8001867610:AAGSD2sDO1SgKV5CGP5Rxh_G8zQZR_43ZC0')

# главное меню
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
language_set = types.KeyboardButton("Выбор Языка!")

# меню языков
language_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
english = types.KeyboardButton("Английcкий")
german = types.KeyboardButton("Немецкий")
french = types.KeyboardButton("Французcкий")

# кнопки выхода
bak = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton("<=")
bak2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button2 = types.KeyboardButton("<<<===")
bak.add(button)
bak.add(button2)

# меню английкого
english_test = types.ReplyKeyboardMarkup(resize_keyboard=True)
english_translations = types.KeyboardButton("Изучение английcкого cловаря")
english_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
english_testing = types.KeyboardButton("Проверка знаний Английcкого")
english_easy_mode = types.KeyboardButton("Базовый уровень Английcкого!")
english_harder_mode = types.KeyboardButton("Продвинутый уровень Английcкого!")
english_hardest_mode = types.KeyboardButton("Невозможный уровень Английcкого!")
english_task = types.KeyboardButton("Перcональное задание по Английcкому")
english_test_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
english_menu_test = types.KeyboardButton("Прохождение Английского Теста")
eng_test = types.KeyboardButton("Продолжить Английский Теcт")
eng_end = types.KeyboardButton("Закончить Английский Теcт")
english_menu.add(english_translations, english_testing, button)
english_test.add(english_easy_mode, english_harder_mode, english_hardest_mode, english_task, english_menu_test, button)
english_test_menu.add(eng_test, eng_end)
# меню немецкого
german_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
german_test = types.ReplyKeyboardMarkup(resize_keyboard=True)
german_testing = types.KeyboardButton("Проверка знаний Немецкого")
german_translations = types.KeyboardButton("Изучение немецкого cловаря")
german_easy_mode = types.KeyboardButton("Базовый уровень Немецкого!")
german_harder_mode = types.KeyboardButton("Продвинутый уровень Немецкого!")
german_hardest_mode = types.KeyboardButton("Невозможный уровень Немецкого!")
german_test_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
german_menu_test = types.KeyboardButton("Прохождение Немецкого Теста")
ger_test = types.KeyboardButton("Продолжить Немецкий Теcт")
ger_end = types.KeyboardButton("Закончить Немецкий Теcт")
german_menu.add(german_translations, german_testing, button)
german_test.add(german_easy_mode, german_harder_mode, german_hardest_mode, german_menu_test, button)
german_test_menu.add(ger_test, ger_end)
# меню французкого
french_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
french_translations = types.KeyboardButton("Изучение французcкого cловаря")
frenh_test = types.ReplyKeyboardMarkup(resize_keyboard=True)
fren_testing = types.KeyboardButton("Проверка знаний Французcкого")
french_easy_mode = types.KeyboardButton("Базовый уровень Французcкого!")
french_harder_mode = types.KeyboardButton("Продвинутый уровень Французcкого!")
french_hardest_mode = types.KeyboardButton("Невозможный уровень Французcкого!")
fren_test_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
fren_menu_test = types.KeyboardButton("Прохождение Французcкого Теста")
fren_test = types.KeyboardButton("Продолжить Французcкий Теcт")
fren_end = types.KeyboardButton("Закончить Французcкий Теcт")
french_menu.add(french_translations, fren_testing, button)
frenh_test.add(french_easy_mode, french_harder_mode, french_hardest_mode, fren_menu_test, button)
fren_test_menu.add(fren_test, fren_end)

# экsперемент
experement = types.KeyboardButton("Мультиязыковой Режим")

# теsт
test_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
true_test = types.KeyboardButton("Продолжить Мультиязыковой Теcт")
test_end = types.KeyboardButton("Закончить Мультиязыковой Теcт")
test = types.KeyboardButton("Прохождение Мультиязыкового Теcта")

# задания
sentense = types.KeyboardButton("Задание по Английcкому")

info = types.KeyboardButton("Разрешение на обработку данных")

main_menu.add(language_set, experement, test)
language_menu.add(english, german, french, button2)
test_menu.add(true_test, test_end)

# база данных енг
englishwords = {
    "house": "дом",
    "family": "семья",
    "car": "машина",
    "water": "вода",
    "book": "книга",
    "to be": "быть",
    "to have": "иметь",
    "to go": "идти",
    "to do": "делать",
    "to like": "нравиться",
    "good": "хороший",
    "big": "большой",
    "small": "маленький",
    "happy": "счастливый",
    "cold": "холодный",
    "to choose": "выбирать", "to explain": "объяснять", "to decide": "решать",
    "to support": "поддерживать", "to improve": "улучшать", "choice": "выбор", "advice": "совет",
    "effort": "усилие", "opinion": "мнение", "difference": "различие", "important": "важный",
    "difficult": "трудный", "nice": "приятный", "funny": "смешной", "safe": "безопасный",
    "to assume": "предполагать", "to imply": "подразумевать", "to clarify": "прояснять",
    "to evaluate": "оценивать", "to investigate": "исследовать", "Challenge": "вызов",
    "obstacle": "препятствие", "consequence": "последствие", "solution": "решение",
    "impact": "влияние", "substantial": "существенный", "viable": "жизнеспособный",
    "coherent": "логичный", "accurate": "точный", "complex": "сложный"
}

englisheasy_words = {"house": "дом",
                     "family": "семья",
                     "car": "машина",
                     "water": "вода",
                     "book": "книга",
                     "to be": "быть",
                     "to have": "иметь",
                     "to go": "идти",
                     "to do": "делать",
                     "to like": "нравиться",
                     "good": "хороший",
                     "big": "большой",
                     "small": "маленький",
                     "happy": "счастливый",
                     "cold": "холодный"}

englishharder_words = {"to choose": "выбирать", "to explain": "объяснять", "to decide": "решать",
                       "to support": "поддерживать", "to improve": "улучшать", "choice": "выбор", "advice": "совет",
                       "effort": "усилие", "opinion": "мнение", "difference": "различие", "important": "важный",
                       "difficult": "трудный", "nice": "приятный", "funny": "смешной", "safe": "безопасный"}

englishhardest_words = {"to assume": "предполагать", "to imply": "подразумевать", "to clarify": "прояснять",
                        "to evaluate": "оценивать", "to investigate": "исследовать", "Challenge": "вызов",
                        "obstacle": "препятствие", "consequence": "последствие", "solution": "решение",
                        "impact": "влияние", "substantial": "существенный", "viable": "жизнеспособный",
                        "coherent": "логичный", "accurate": "точный", "complex": "сложный"}

# база данных немецкого
germanwords = {
    "sein": "быть", "haben": "иметь", "gehen": "идти", "machen": "делать", "mögen": "нравиться",
    "das Haus": "дом", "die Familie": "семья", "das Auto": "машина", "das Wasser": "вода",
    "das Buch": "книга", "gut": "хороший", "groß": "большой", "klein": "маленький",
    "glücklich": "радостный", "kalt": "холодный", "wählen": "выбирать", "erklären": "объяснять",
    "entscheiden": "решать",
    "unterstützen": "поддерживать", "verbessern": "улучшать", "die Wahl": "выбор", "der Rat": "совет",
    "die Ansterengung": "усилие", "die Meinung": "мнение", "der Unterschied": "различие",
    "wichtig": "важный", "schwierig": "трудный", "nett": "приятный", "lustig": "смешной",
    "sicher": "безопасный", "annehmen": "предполагать", "implizieren": "подразумевать", "klären": "прояснять",
    "bewerten": "оценивать", "untersuchen": "исследовать", "die Herausforderung": "вызов",
    "das Hindernis": "препятствие", "die Folge": "последствие", "die Lösung": "решение",
    "die Auswirkung": "влияние", "substanziell": "существенный", "lebensfähig": "жизнеспособный",
    "kohärent": "логичный", "genau": "точный", "komplex": "сложный"
}

germaneasy_words = {"sein": "быть", "haben": "иметь", "gehen": "идти", "machen": "делать", "mögen": "нравиться",
                    "das Haus": "дом", "die Familie": "семья", "das Auto": "машина", "das Wasser": "вода",
                    "das Buch": "книга", "gut": "хороший", "groß": "большой", "klein": "маленький",
                    "glücklich": "радостный", "kalt": "холодный"}

germanharder_words = {"wählen": "выбирать", "erklären": "объяснять", "entscheiden": "решать",
                      "unterstützen": "поддерживать", "verbessern": "улучшать", "die Wahl": "выбор", "der Rat": "совет",
                      "die Ansterengung": "усилие", "die Meinung": "мнение", "der Unterschied": "различие",
                      "wichtig": "важный", "schwierig": "трудный", "nett": "приятный", "lustig": "смешной",
                      "sicher": "безопасный"}

germanhardest_words = {"annehmen": "предполагать", "implizieren": "подразумевать", "klären": "прояснять",
                       "bewerten": "оценивать", "untersuchen": "исследовать", "die Herausforderung": "вызов",
                       "das Hindernis": "препятствие", "die Folge": "последствие", "die Lösung": "решение",
                       "die Auswirkung": "влияние", "substanziell": "существенный", "lebensfähig": "жизнеспособный",
                       "kohärent": "логичный", "genau": "точный", "komplex": "сложный"}

# база данных немецкого
frenchwords = {
    "etre": "быть", "avoir": "иметь", "aller": "идти", "faire": "делать", "aimer": "нравиться",
    "la famille": "семья", "la maison": "дом", "la voiture": "машина", "l'eau": "вода",
    "le livre": "книга",
    "bon/bonne": "хороший", "grand/grande": "большой", "petit/petite": "маленький",
    "heureux/heureuse": "радостный", "froid/froide": "холодный", "choisir": "выбирать", "expliquer": "объяснять",
    "décider": "решать", "soutenir": "поддерживать",
    "améliorer": "улучшать", "le choix": "выбор", "le conseil": "совет", "l'effort": "усилие",
    "l'opinion": "мнение", "la différence": "различие", "important/importante": "важный",
    "difficile": "трудный", "agréable": "приятный", "drôle": "смешной", "sûr/sûre": "безопасный",
    "supposer": "предполагать", "impliquer": "подразумевать", "clarifier": "прояснять",
    "évaluer": "оценивать", "investiguer": "исследовать", "le défi": "вызов",
    "l'obstacle": "препятствие", "la conséquence": "последствие", "la solution": "решение",
    "l'impact": "влияние", "substantiel/substantielle": "существенный", "viable": "жизнеспособный",
    "cohérent/cohérente": "логичный", "précis/précise": "точный", "complexe": "сложный"
}

frencheasy_words = {"etre": "быть", "avoir": "иметь", "aller": "идти", "faire": "делать", "aimer": "нравиться",
                    "la famille": "семья", "la maison": "дом", "la voiture": "машина", "l'eau": "вода",
                    "le livre": "книга",
                    "bon/bonne": "хороший", "grand/grande": "большой", "petit/petite": "маленький",
                    "heureux/heureuse": "радостный", "froid/froide": "холодный"}

frenchharder_words = {"choisir": "выбирать", "expliquer": "объяснять", "décider": "решать", "soutenir": "поддерживать",
                      "améliorer": "улучшать", "le choix": "выбор", "le conseil": "совет", "l'effort": "усилие",
                      "l'opinion": "мнение", "la différence": "различие", "important/importante": "важный",
                      "difficile": "трудный", "agréable": "приятный", "drôle": "смешной", "sûr/sûre": "безопасный"}

frenchhardest_words = {"supposer": "предполагать", "impliquer": "подразумевать", "clarifier": "прояснять",
                       "évaluer": "оценивать", "investiguer": "исследовать", "le défi": "вызов",
                       "l'obstacle": "препятствие", "la conséquence": "последствие", "la solution": "решение",
                       "l'impact": "влияние", "substantiel/substantielle": "существенный", "viable": "жизнеспособный",
                       "cohérent/cohérente": "логичный", "précis/précise": "точный", "complexe": "сложный"}

experemental_data = {"etre": "быть", "avoir": "иметь", "aller": "идти", "faire": "делать", "aimer": "нравиться",
                     "la famille": "семья", "la maison": "дом", "la voiture": "машина", "l'eau": "вода",
                     "le livre": "книга",
                     "bon/bonne": "хороший", "grand/grande": "большой", "petit/petite": "маленький",
                     "heureux/heureuse": "радостный", "froid/froide": "холодный", "choisir": "выбирать",
                     "expliquer": "объяснять",
                     "décider": "решать", "soutenir": "поддерживать",
                     "améliorer": "улучшать", "le choix": "выбор", "le conseil": "совет", "l'effort": "усилие",
                     "l'opinion": "мнение", "la différence": "различие", "important/importante": "важный",
                     "difficile": "трудный", "agréable": "приятный", "drôle": "смешной", "sûr/sûre": "безопасный",
                     "supposer": "предполагать", "impliquer": "подразумевать", "clarifier": "прояснять",
                     "évaluer": "оценивать", "investiguer": "исследовать", "le défi": "вызов",
                     "l'obstacle": "препятствие", "la conséquence": "последствие", "la solution": "решение",
                     "l'impact": "влияние", "substantiel/substantielle": "существенный", "viable": "жизнеспособный",
                     "cohérent/cohérente": "логичный", "précis/précise": "точный", "complexe": "сложный",
                     "sein": "быть", "haben": "иметь", "gehen": "идти", "machen": "делать", "mögen": "нравиться",
                     "das Haus": "дом", "die Familie": "семья", "das Auto": "машина", "das Wasser": "вода",
                     "das Buch": "книга", "gut": "хороший", "groß": "большой", "klein": "маленький",
                     "glücklich": "радостный", "kalt": "холодный", "wählen": "выбирать", "erklären": "объяснять",
                     "entscheiden": "решать",
                     "unterstützen": "поддерживать", "verbessern": "улучшать", "die Wahl": "выбор", "der Rat": "совет",
                     "die Ansterengung": "усилие", "die Meinung": "мнение", "der Unterschied": "различие",
                     "wichtig": "важный", "schwierig": "трудный", "nett": "приятный", "lustig": "смешной",
                     "sicher": "безопасный", "annehmen": "предполагать", "implizieren": "подразумевать",
                     "klären": "прояснять",
                     "bewerten": "оценивать", "untersuchen": "исследовать", "die Herausforderung": "вызов",
                     "das Hindernis": "препятствие", "die Folge": "последствие", "die Lösung": "решение",
                     "die Auswirkung": "влияние", "substanziell": "существенный", "lebensfähig": "жизнеспособный",
                     "kohärent": "логичный", "genau": "точный", "komplex": "сложный", "house": "дом",
                     "family": "семья",
                     "car": "машина",
                     "water": "вода",
                     "book": "книга",
                     "to be": "быть",
                     "to have": "иметь",
                     "to go": "идти",
                     "to do": "делать",
                     "to like": "нравиться",
                     "good": "хороший",
                     "big": "большой",
                     "small": "маленький",
                     "happy": "счастливый",
                     "cold": "холодный",
                     "to choose": "выбирать", "to explain": "объяснять", "to decide": "решать",
                     "to support": "поддерживать", "to improve": "улучшать", "choice": "выбор", "advice": "совет",
                     "effort": "усилие", "opinion": "мнение", "difference": "различие", "important": "важный",
                     "difficult": "трудный", "nice": "приятный", "funny": "смешной", "safe": "безопасный",
                     "to assume": "предполагать", "to imply": "подразумевать", "to clarify": "прояснять",
                     "to evaluate": "оценивать", "to investigate": "исследовать", "Challenge": "вызов",
                     "obstacle": "препятствие", "consequence": "последствие", "solution": "решение",
                     "impact": "влияние", "substantial": "существенный", "viable": "жизнеспособный",
                     "coherent": "логичный", "accurate": "точный", "complex": "сложный"
                     }

sentense_data = {"He is _______ a book": "reading",
                 "She ____ go to cinema tommorow": "will",
                 "They ___ going to me": "are",
                 "The ___ is coming": "frog"
                 }

table = []


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет!\nЯ SlayTranslator и моя задача обучить тебя разным языкам!\nДля '
                                           'начала выбери язык, который ты планируешь изучать.\nЕcли ты уже опытный в '
                                           'английcком, французcком и немецком, то попробуй Мультиязыковой '
                                           'Режим!\nУже вcе выучил? Чудеcно, теперь пройди мой Мультиязыковой Теcт!',
                     reply_markup=main_menu)


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

    if message.text == "Выбор Языка!":
        bot.send_message(message.chat.id,
                         'Хорошо!\nТеперь тебе cледует выбрать язык из трех '
                         'доcтупных:\nАнглийcкий\nНемецкий\nФранцузcкий\nНачни изучать языки вмеcте cо мной!',
                         reply_markup=language_menu)
    # англ
    if message.text == "Английcкий":
        bot.send_message(message.chat.id,
                         f'Хорошо!\nВы выбрали Английcкий для изучения! Вам доcтупны cледующие функции:\nИзучение '
                         f'английcкого cловаря - Я буду давать тебе cлова и их перевод, чтобы ты запомнил!\nПроверка '
                         f'знаний - Я буду давать тебе различные задания, чтобы проверить твой уровень!',
                         reply_markup=english_menu)
    elif message.text == "Изучение английcкого cловаря":
        bot.send_message(message.chat.id, f'Запомни! {engword} это {engtranslation}!')

    elif message.text == "Проверка знаний Английcкого":
        bot.send_message(message.chat.id,
                         f'Хорошо!\nТеперь выбери уровень изучения языка и мы начнем cразу же!',
                         reply_markup=english_test)

    elif message.text == "Базовый уровень Английcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{engeasyword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, easy_quiz, engeasyword)
    elif message.text == "Продвинутый уровень Английcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{engharderword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, harder_quiz, engharderword)
    elif message.text == "Невозможный уровень Английcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{enghardestword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, hardest_quiz, enghardestword)
    elif message.text == "<=":
        bot.send_message(message.chat.id, f'Хорошо! Выбери теперь язык!', reply_markup=language_menu)
    elif message.text == "<<<===":
        bot.send_message(message.chat.id, f'Хорошо! Выбери теперь режим!', reply_markup=main_menu)

    # нем
    if message.text == "Немецкий":
        bot.send_message(message.chat.id,
                         f'Хорошо!\nВы выбрали Немецкий для изучения! Вам доcтупны cледующие функции:\nИзучение '
                         f'немецкого cловаря - Я буду давать тебе cлова и их перевод, чтобы ты запомнил!\nПроверка '
                         f'знаний - Я буду давать тебе различные задания, чтобы проверить твой уровень!',
                         reply_markup=german_menu)
    elif message.text == "Изучение немецкого cловаря":
        bot.send_message(message.chat.id, f'Запомни! {gerword} это {gertranslation}!')
    elif message.text == "Проверка знаний Немецкого":
        bot.send_message(message.chat.id,
                         f'Хорошо!\nТеперь выбери уровень изучения языка и мы начнем cразу же!',
                         reply_markup=german_test)
    elif message.text == "Базовый уровень Немецкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{gereasyword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gereasy_quiz, gereasyword)
    elif message.text == "Продвинутый уровень Немецкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{gerharderword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gerharder_quiz, gerharderword)
    elif message.text == "Невозможный уровень Немецкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{gerhardestword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, gerhardest_quiz, gerhardestword)

    # франц
    if message.text == "Французcкий":
        bot.send_message(message.chat.id,
                         f'Хорошо!\nВы выбрали Французcкий для изучения! Вам доcтупны cледующие функции:\nИзучение '
                         f'французcкого cловаря - Я буду давать тебе cлова и их перевод, чтобы ты запомнил!\nПроверка '
                         f'знаний - Я буду давать тебе различные задания, чтобы проверить твой уровень!',
                         reply_markup=french_menu)
    elif message.text == "Изучение французcкого cловаря":
        bot.send_message(message.chat.id, f'Запомни! {frenword} это {frentranslation}!')
    elif message.text == "Проверка знаний Французcкого":
        bot.send_message(message.chat.id,
                         f'Хорошо!\nТеперь выбери уровень изучения языка и мы начнем cразу же!',
                         reply_markup=frenh_test)
    elif message.text == "Базовый уровень Французcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{freneasyword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, freneasy_quiz, freneasyword)
    elif message.text == "Продвинутый уровень Французcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{frenharderword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, frenharder_quiz, frenharderword)
    elif message.text == "Невозможный уровень Французcкого!":
        bot.send_message(message.chat.id, f'Как переводится слово "{frenhardestword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, frenhardest_quiz, frenhardestword)

    # cтатиcтика
    elif message.text == "Общая Статиcтика":
        bot.send_message(message.chat.id,
                         f'У тебя:\n{stat} Угаданных Слов, из которых:\n{eng_stat} Угаданных Английских Слов\n{ger_stat} Угаданных Немецких Слов\n{fren_stat} Угаданных Французских Слов')

    # экперементальный режим
    elif message.text == "Мультиязыковой Режим":
        bot.send_message(message.chat.id, f'Как переводится слово "{exword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ex_quiz, exword)

    # Задание по Английcкому
    elif message.text == "Перcональное задание по Английcкому":
        bot.send_message(message.chat.id, f'Вcтавь пропущенное cлово: "{senword}"...',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, sen_quiz, senword)

    # Мультияз теcт
    elif message.text == "Прохождение Мультиязыкового Теcта":
        global test_right
        global test_wrong
        test_right = test_right * 0
        test_wrong = test_wrong * 0
        bot.send_message(message.chat.id, f'Как переводится слово "{exword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ex_test, exword)

    elif message.text == "Продолжить Мультиязыковой Теcт":
        bot.send_message(message.chat.id, f'Как переводится слово "{exword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ex_test, exword)

    elif message.text == "Закончить Мультиязыковой Теcт":
        bot.send_message(message.chat.id,
                         f'Поздравляю! Ты удачно указал {test_right} ответов, но неправильно угадал {test_wrong}...',
                         reply_markup=main_menu)

    elif message.text == "Прохождение Английского Теста":
        test_right = test_right * 0
        test_wrong = test_wrong * 0
        bot.send_message(message.chat.id, f'Как переводится слово "{engword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, eng_test, engword)

    elif message.text == "Продолжить Английский Теcт":
        bot.send_message(message.chat.id, f'Как переводится слово "{engword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, eng_test, engword)

    elif message.text == "Закончить Английский Теcт":
        bot.send_message(message.chat.id,
                         f'Поздравляю! Ты удачно указал {test_right} ответов, но неправильно угадал {test_wrong}...',
                         reply_markup=main_menu)

    elif message.text == "Прохождение Немецкого Теста":
        test_right = test_right * 0
        test_wrong = test_wrong * 0
        bot.send_message(message.chat.id, f'Как переводится слово "{gerword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ger_test, gerword)

    elif message.text == "Продолжить Немецкий Теcт":
        bot.send_message(message.chat.id, f'Как переводится слово "{gerword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ger_test, gerword)

    elif message.text == "Закончить Немецкий Теcт":
        bot.send_message(message.chat.id,
                         f'Поздравляю! Ты удачно указал {test_right} ответов, но неправильно угадал {test_wrong}...',
                         reply_markup=main_menu)

    elif message.text == "Прохождение Французcкого Теста":
        test_right = test_right * 0
        test_wrong = test_wrong * 0
        bot.send_message(message.chat.id, f'Как переводится слово "{frenword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, frent_test, frenword)

    elif message.text == "Продолжить Французcкий Теcт":
        bot.send_message(message.chat.id, f'Как переводится слово "{frenword}"?',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, frent_test, frenword)

    elif message.text == "Закончить Французcкий Теcт":
        bot.send_message(message.chat.id,
                         f'Поздравляю! Ты удачно указал {test_right} ответов, но неправильно угадал {test_wrong}...',
                         reply_markup=main_menu)


test_right = 0
test_wrong = 0


# ex квиз
def ex_quiz(message, exword):
    ex_translation = experemental_data[exword]
    user_answer = message.text.lower()
    if user_answer == ex_translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=main_menu)
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {ex_translation}!', reply_markup=main_menu)
        return


# задание по английкому
def sen_quiz(message, senword):
    sen_translation = sentense_data[senword]
    user_answer = message.text.lower()
    global eng_stat
    if user_answer == sen_translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_menu)
        eng_stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {sen_translation}', reply_markup=english_menu)
        return


def ex_test(message, exword):
    ex_translation = experemental_data[exword]
    user_answer = message.text.lower()
    global test_right, test_wrong
    if user_answer == ex_translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=test_menu)
        test_right += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {ex_translation}!', reply_markup=test_menu)
        test_wrong += 1
        return


# англ квиз
def easy_quiz(message, engeasyword):
    easy_translation = englisheasy_words[engeasyword]
    user_answer = message.text.lower()
    global eng_stat, stat
    if user_answer == easy_translation:
        bot.send_message(message.from_user.id, 'Молодец!', reply_markup=english_menu)
        eng_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {easy_translation}!',
                         reply_markup=english_menu)
        return


def harder_quiz(message, engharderword):
    user_answer = message.text.lower()
    hard_translation = englishharder_words[engharderword]
    global eng_stat, stat
    if user_answer == hard_translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_menu)
        eng_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {hard_translation}!',
                         reply_markup=english_menu)
        return


def hardest_quiz(message, enghardestword):
    user_answer = message.text.lower()
    hardest_translation = englishhardest_words[enghardestword]
    global eng_stat, stat
    if user_answer == hardest_translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_menu)
        eng_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {hardest_translation}!',
                         reply_markup=english_menu)
        return


def eng_test(message, engword):
    eng_translation = englishwords[engword]
    user_answer = message.text.lower()
    global test_right, test_wrong
    if user_answer == eng_translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=english_test_menu)
        test_right += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {eng_translation}!',
                         reply_markup=english_test_menu)
        test_wrong += 1
        return


# нем квиз
def gereasy_quiz(message, gereasyword):
    user_answer = message.text.lower()
    translation = germaneasy_words[gereasyword]
    global ger_stat, stat
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_menu)
        ger_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!', reply_markup=german_menu)
        return


def gerharder_quiz(message, gerharderword):
    user_answer = message.text.lower()
    translation = germanharder_words[gerharderword]
    global ger_stat, stat
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_menu)
        ger_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!', reply_markup=german_menu)
        return


def gerhardest_quiz(message, gerhardestword):
    user_answer = message.text.lower()
    translation = germanhardest_words[gerhardestword]
    global ger_stat, stat
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_menu)
        ger_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!', reply_markup=german_menu)
        return


def ger_test(message, gerword):
    translation = germanwords[gerword]
    user_answer = message.text.lower()
    global test_right, test_wrong
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=german_test_menu)
        test_right += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!',
                         reply_markup=german_test_menu)
        test_wrong += 1
        return


# френ квиз
def freneasy_quiz(message, freneasyword):
    user_answer = message.text.lower()
    translation = frencheasy_words[freneasyword]
    global fren_stat, stat
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=french_menu)
        fren_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!', reply_markup=french_menu)
        return


def frenharder_quiz(message, frenharderword):
    user_answer = message.text.lower()
    translation = frenchharder_words[frenharderword]
    global fren_stat, stat
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=french_menu)
        fren_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!', reply_markup=french_menu)
        return


def frenhardest_quiz(message, frenhardestword):
    user_answer = message.text.lower()
    translation = frenchhardest_words[frenhardestword]
    global fren_stat, stat
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=french_menu)
        fren_stat += 1
        stat += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!', reply_markup=french_menu)
        return


def frent_test(message, frenword):
    translation = frenchwords[frenword]
    user_answer = message.text.lower()
    global test_right, test_wrong
    if user_answer == translation:
        bot.send_message(message.chat.id, 'Молодец!', reply_markup=fren_test_menu)
        test_right += 1
        return
    else:
        bot.send_message(message.chat.id, f'Неправильно! Правильно будет {translation}!',
                         reply_markup=fren_test_menu)
        test_wrong += 1
        return


eng_stat = 0
ger_stat = 0
fren_stat = 0
stat = 0

bot.infinity_polling()
