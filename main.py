"""main file."""

import logging

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from config.config import TELEGRAM_BOT_TOKEN

from request_rate.daily_rates import get_usd_kgs_1d, get_usd_kgs_last_15mins

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = TELEGRAM_BOT_TOKEN
updater = Updater(TOKEN)

def get_cur_1d(update: Update, context: CallbackContext) -> None:
    """Send telegram message with value.

    :param update:
    :param context:
    :return:
    """
    update.message.reply_text(f'Avg. Currency for today: {get_usd_kgs_1d()}')


def get_cur_15min(update: Update, context: CallbackContext) -> None:
    """Send telegram message with value.

    :param update:
    :param context:
    :return:
    """
    update.message.reply_text(f'Avg. Currency for last 15 mins: {get_usd_kgs_last_15mins()}')


updater.dispatcher.add_handler(CommandHandler('cur1d', get_cur_1d))
updater.dispatcher.add_handler(CommandHandler('cur15mins', get_cur_15min))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
