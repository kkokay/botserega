# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
updater = Updater(token='759000195:AAG37yASLFCzk_MS2rGHtux9UpxquGirwwQ') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, я Серега предсказатель, я помогу тебе сделать выбор, спроси меня о чем-нибудь')

def textMessage(bot, update):
    response = update.message.text
    if "?" in response:
        bot.send_message(chat_id=update.message.chat_id, text=random.choice(answers))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="К сожалению я так деграднул, что могу только рандомно отвечать на твои вопросы")

answers = [
#Положительные:

"Бесспорно)0)",
"Конечно да)",
"Никаких сомнений!",
"Определённо да!",
"Можешь быть уверен в этом",

#Нерешительно положительные

"Мне кажется — «да»",
"Вероятнее всего",
#"Хорошие перспективы",
"Знаки говорят — «да»",
"Да",

#Нейтральные

"Пока не ясно, попробуй снова ;)",
"Спроси позже :p",
"Лучше не рассказывать))",
"Сейчас нельзя предсказать((",
"Сконцентрируйся и спроси опять",

#Отрицательные

"Даже не думай!",
"Мой ответ — «нет»",
"По моим данным — «нет»",
#"Перспективы не очень хорошие",
"Весьма сомнительно))"
]

#print(random.choice(answers))


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
