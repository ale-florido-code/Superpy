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
    with open(pa.full_path_text, 'r') as f:
        old_date = ...
    daysback = old_date + timedelta(dagen)
    daysbackcIso = daysback.strftime("%Y-%m-%d")

    write_date_text(daysbackIso)
    return daysbackcIso


# This is not necessary because of Pytz. To practice, I liked to make a .txt anyway.
def write_date_text():
    with open(pa.full_path_text, 'w') as f:
        f.write(date_now)

def change_date(new_date):
    # new_date = datetime.datetime.now().strftime("%Y-%m-%d" "%H:%M:%S")

    with open("date_now.txt", "w") as file:
         file.write(new_date)
