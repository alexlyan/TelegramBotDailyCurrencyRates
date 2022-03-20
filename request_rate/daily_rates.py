"""Methods for project."""

import pandas as pd
import requests

from common.utils import convert_unix_to_normal


def get_usd_kgs_1d() -> str:
    """Return value of 1usd to kgs.

    :return: rate value for 1 usd to kgs
    """
    buy_data = requests.get(
        "https://valuta.kg/api/rates/history.json?currency=usd"
    ).json()["data"]["buy"]
    buy_data = pd.DataFrame(data=buy_data, columns=["date", "buy_value"])
    buy_data["date"] = buy_data["date"].apply(convert_unix_to_normal)

    avg_value = buy_data.sort_values("date").tail(1)["buy_value"].values[0]

    return avg_value


def get_usd_kgs_last_15mins() -> str:
    """Return value of 1usd to kgs last 15 mins.

    :return: rate value for 1 usd to kgs
    """
    buy_data = requests.get(
        "https://valuta.kg/api/rates.json?currency=usd"
    ).json()
    if not buy_data["error"]:
        buy_data = buy_data["data"]["buy"]
        buy_data = pd.DataFrame(data=buy_data, columns=["date", "buy_value"])
        buy_data["date"] = buy_data["date"].apply(convert_unix_to_normal)

        avg_value = buy_data.sort_values("date").tail(2)["buy_value"].mean()

        return avg_value

    else:
        return "Values are not valid this time, use avg 1d method"
