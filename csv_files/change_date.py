import datetime

def change_date():
    new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("date_now.txt", "w") as file:
        file.write(new_date)

change_date()
