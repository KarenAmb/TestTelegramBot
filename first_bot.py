# запуск на сервере амазона в постоянку nohup python3 first_bot.py > /dev/null &
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Sticker, StickerSet
import logging
import settings
import ephem
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

# logger = logging.getLogger(__name__)

# Главная функция с заданием ключа, обработчиков комманд.
def main():
    updater = Updater(settings.TELEGRAM_API_KEY)  # ключ теперь в отдельном файле
    dp = updater.dispatcher
    # обрабатываем ошибки
    dp.add_error_handler(error)
    dp.add_handler(CommandHandler('start', user_welcomming))
    dp.add_handler(CommandHandler('planet', planet_status))
    dp.add_handler(CommandHandler('getsticker',get_sticker))
    dp.add_handler(MessageHandler(Filters.text, talking_with_user))
    updater.start_polling()
    updater.idle()


# функция обработки комманды /start!
def user_welcomming(bot, update):
    my_text = "Здарова {}! Я только начал жить! \n" \
              "Могу сказать в каком созвездии планета сегодня. Напиши /planet Mars например\n" \
              "Могу ответить стикером. Напиши /getsticker и смайлик 😕 например.\n" \
              "у меня есть стикеры на эти эмодзи:😕😂😊😏".format(update.message.chat.first_name)
    logging.info('Пользоавтель {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(my_text)


# Функция общения с пользователем
def talking_with_user(bot, update):
    user_text = update.message.text
    logging.info('Пользователь @{} ({}) ввел: {} '.format(update.message.chat.username,
                                                          update.message.chat.first_name,
                                                          user_text))  # Логируем все что пишет юзер
    update.message.reply_text('Ты написал: '+user_text + '... Но для меня это ничего не значит. \n Напиши /start')


# Функция ответа на /planet "Planet"  и выдачи созвездия планеты сегодня
def planet_status(bot, update):
    today_date = datetime.datetime.now().strftime('%Y/%m/%d')
    user_text = update.message.text
    logging.info('Пользователь @{} ({}) ввел: {} '.format(update.message.chat.username,
                                                          update.message.chat.first_name,
                                                          user_text))
    if 'Venus' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Venus(today_date))[1]))
    elif 'Mars' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Mars(today_date))[1]))
    elif 'Mercury' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Mercury(today_date))[1]))
    elif 'Earth' in user_text:
        update.message.reply_text("Ну ты в своем уме?)")
    elif 'Jupiter' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Jupiter(today_date))[1]))
    elif 'Saturn' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Saturn(today_date))[1]))
    elif 'Uranus' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Uranus(today_date))[1]))
    elif 'Neptune' in user_text:
        update.message.reply_text("Находится в созвездии {}".format(ephem.constellation(ephem.Neptune(today_date))[1]))
    else:
        update.message.reply_text("Планеты на английском надо. Введите например /planet Venus")

def get_sticker(bot, update):
    user_emoji = update.message.text
    print(user_emoji)
    logging.info('Пользователь @{} ({}) ввел: {} '.format(update.message.chat.username,
                                                          update.message.chat.first_name,
                                                          user_emoji))
    if "😕" in user_emoji:
        update.message.reply_sticker(Sticker(file_id='CAADAgADOAADX8p-CzLiVfbJsCagAg',width=100,height=100))
    elif "😂" in user_emoji:
        update.message.reply_sticker(Sticker(file_id='CAADAgADwgYAAvoLtghYZz5i3gqMNgI', width=100, height=100))
    elif "😊" in user_emoji:
        update.message.reply_sticker(Sticker(file_id='CAADAgAD2gYAAvoLtgggBeUJREiG7QI', width=100, height=100))
    elif "😏" in user_emoji:
        update.message.reply_sticker(Sticker(file_id='CAADAgADXgAD1jUSAAHMmC9kAAFQGeUC', width=100, height=100))
    else:
        update.message.reply_text("На такой Эмодзи стикера у меня нет, извини =(")

# функция для обработки ошибок
def error(bot, update, error):
    # тут он пишет в чем суть ошибки
    # logging.warning('Update "%s" caused error "%s"', update, error)
    pass  # пропускаем все ошибки


if __name__ == "__main__":
    logging.info('Bot has been started')  # Сообщение о старте успешном бота в логе
    main()
