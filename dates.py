import datetime
from datetime import timedelta
import pytz                         # Geeft daadwerkelijke tijd tijdzone.
import paths as pa

# See report for explanation
my_date_now = datetime.datetime.now(pytz.timezone('Europe/Paris'))
date_now = my_date_now.strftime("%Y-%m-%d")
time_now = my_date_now.strftime("%H:%M:%S")
yesterday_full = my_date_now - timedelta(days=1)
yesterday = yesterday_full.strftime("%Y-%m-%d")


def choose_days_back(number_days):
    dagen = int(number_days)
    daysback = my_date_now + timedelta(dagen)
    daysbackcIso = daysback.strftime("%Y-%m-%d")
    return daysbackcIso


# This is not necessary because of Pytz. To practice, I liked to make a .txt anyway.
def write_date_text():
    with open(pa.full_path_text, 'w') as f:
        f.write(date_now)
