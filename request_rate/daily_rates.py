import requests
import pandas as pd
from common.utils import convert_unix_to_normal


def get_usd_kgs_1d():
    buy_data = requests.get("https://valuta.kg/api/rates/history.json?currency=usd").json()["data"]["buy"]
    buy_data = pd.DataFrame(data=buy_data, columns=["date", "buy_value"])
    buy_data["date"] = buy_data["date"].apply(convert_unix_to_normal)

    avg_value = buy_data.sort_values("date").tail(1)["buy_value"].values[0]

    return avg_value