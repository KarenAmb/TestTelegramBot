from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings

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
    dp.add_handler(MessageHandler(Filters.text, talking_with_user))
    updater.start_polling()
    updater.idle()


# функция обработки комманды /start!
def user_welcomming(bot, update):
    my_text = "Здарова {}! Я только начал жить, не суди строго =)".format(update.message.chat.first_name)
    logging.info('Пользоавтель {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(my_text)


# Функция общения с пользователем
def talking_with_user(bot, update):
    user_text = update.message.text
    logging.info('Пользователь @{} ({}) ввел: {} '.format(update.message.chat.username,
                                                          update.message.chat.first_name,
                                                          user_text))  # Логируем все что пишет юзер
    update.message.reply_text(user_text + '. Окей, и что?')


# функция для обработки ошибок
def error(bot, update, error):
    # тут он пишет в чем суть ошибки
    # logging.warning('Update "%s" caused error "%s"', update, error)
    pass  # пропускаем все ошибки


if __name__ == "__main__":
    logging.info('Bot has been started')  # Сообщение о старте успешном бота в логе
    main()
