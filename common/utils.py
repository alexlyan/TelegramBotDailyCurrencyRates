from datetime import datetime


def convert_unix_to_normal(ts):
    ts = ts//1000
    ts = int(ts)

    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
