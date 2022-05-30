from datetime import datetime, timedelta


def date_in_future(integer):
    date = datetime.now()
    if isinstance(integer, int):
        date = date + timedelta(days=integer)
    return date.strftime("%d-%m-%Y %H:%M:%S")
