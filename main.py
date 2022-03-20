# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from datetime import datetime
import pandas as pd
import os


def convert_unix_to_normal(ts):
    ts = ts//1000
    ts = int(ts)

    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def get_usd_kgs_1d():
    buy_data = requests.get("https://valuta.kg/api/rates/history.json?currency=usd").json()["data"]["buy"]
    buy_data = pd.DataFrame(data=buy_data, columns=["date", "buy_value"])
    buy_data["date"] = buy_data["date"].apply(convert_unix_to_normal)

    avg_value = buy_data.sort_values("date").tail(1)["buy_value"].values[0]

    return avg_value


def get_cur_1d(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Avg. Currency for today: {get_usd_kgs_1d()}')

updater = Updater('5250151891:AAHVazpIZVQoROOeJwqk_WGyPYHd8DN-Gms')

updater.dispatcher.add_handler(CommandHandler('cur1d', get_cur_1d))

updater.start_polling()
updater.idle()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
