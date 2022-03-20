# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from request_rate.daily_rates import get_usd_kgs_1d


def get_cur_1d(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Avg. Currency for today: {get_usd_kgs_1d()}')

updater = Updater('5250151891:AAHVazpIZVQoROOeJwqk_WGyPYHd8DN-Gms')

updater.dispatcher.add_handler(CommandHandler('cur1d', get_cur_1d))

updater.start_polling()
updater.idle()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
