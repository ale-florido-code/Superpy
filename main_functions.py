import pandas as pd
from csv import writer
import csv
import paths as pa
import dates as d
import plotext as plt
import json


# Appends line to bought.csv
def append_bought(args):
    ID = id(args)
    # I used the opposite because the default for argparse is date now.
    if args.buy_date != d.date_now:
        args.buy_date = d.choose_days_back(args.buy_date)
    with open(pa.full_path_bought, mode='a', newline='') as f_object:
        with open('csv_files/stock.csv', mode='a', newline='', encoding='utf-8') as f_object2:
            writer_object = writer(f_object)
            writer_object2 = writer(f_object2)
            writer_object.writerow(
                [ID, args.product_name, args.buy_date,
                 args.buy_price, args.expiration_date])
            writer_object2.writerow(
                [ID, args.product_name, args.buy_date, args.buy_price, args.expiration_date])


# Appends line to sold.csv
def sell(args):
    if args.sell_date != d.date_now:
        args.sell_date = d.choose_days_back(args.sell_date)
    df = pd.read_csv(pa.full_path_stock)
    args.id = int(args.id)
    if args.id in df['id'].values:
        idsales = id(args)  # creates sales id.
        df = df[df.id != args.id]
        # removes line with bought_id from stock!
        df.to_csv(pa.full_path_stock, index=False)
        with open(pa.full_path_sold, mode='a', newline='', encoding='utf-8') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(
                [idsales, args.id, args.sell_date, args.sell_price])
    else:
        print("Not in stock!")


# Main function REPORT
def report(args):
    # py main.py report --stock
    if args.stock:
        df = pd.read_csv(pa.full_path_stock)
        print(df)
    # py main.py report --bought
    if args.bought:
        df = pd.read_csv(pa.full_path_bought)
        print(df)
    # py main.py report --sold
    if args.sold:
        df = pd.read_csv(pa.full_path_sold)
        print(df)
    # py main.py report --profit 2023-03-11
    if args.profit:
        print(
            f'The margin of profit for {args.profit} is: {calculate_margin_profit(args.profit)} euros')
    # py main.py report --graph
    if args.revenue:
        print(
            f'The revenue for {args.revenue} is: {calculate_revenue(args.revenue)} euros')
    # py main.py report --graph_revenue
    if args.graph_revenue:
        graph_revenue()
    # py main.py report --graph_margin
    if args.graph_margin:
        graph_margin_profit()
    # py main.py report --expiration_date
    if args.expiration_date:
        print(expiration_date())


# py main.py report --expiration_date
def expiration_date():
    df = pd.read_csv(pa.full_path_stock)
    df = df[(df['expiration_date'] <= d.date_now)]
    return df


# py main.py report --revenue
def calculate_revenue(date):
    list_date = [str(date)]
    df = pd.read_csv(pa.full_path_sold)
    df = df[df.sell_date.isin(list_date)]
    sellprice = df['sell_price'].values
    total_revenue = 0
    for x in sellprice:
        total_revenue += x
    return total_revenue


# py main.py report --profit
def calculate_margin_profit(date):
    list_date = [str(date)]
    df = pd.read_csv(pa.full_path_sold)
    df = df[df.sell_date.isin(list_date)]
    sellprice = df['sell_price'].values
    bought_id = df['bought_id'].values
    df2 = pd.read_csv(pa.full_path_bought)
    df2 = df2[df2.id.isin(bought_id)]
    buy_price = df2['buy_price'].values
    total_sales = 0
    for x in sellprice:
        total_sales += x
    total_bought = 0
    for y in buy_price:
        total_bought += y
    margin_of_profit = (total_sales - total_bought) / total_sales * 100
    return margin_of_profit


# py main.py report --graph_revenue
def graph_revenue():
    list_profits = []
    df = pd.read_csv(pa.full_path_sold)
    sellprice = df['sell_date'].values
    unique_dates_list = pd.Series(sellprice).drop_duplicates().tolist()
    for date in unique_dates_list:
        list_profits.append(calculate_revenue(date))
    unique_dates_list.sort(reverse=True)
    unique_dates_last_10_days = unique_dates_list[:10]
    plt.bar(unique_dates_last_10_days, list_profits, color='green')
    plt.canvas_color('white')
    plt.title("Revenue last 10 days")
    plt.xlabel("x = date")
    plt.ylabel("y = % margin profit")
    plt.show()


#  py main.py report --graph_margin
def graph_margin_profit():
    list_profits = []
    df = pd.read_csv(pa.full_path_sold)
    sellprice = df['sell_date'].values
    unique_dates_list = pd.Series(sellprice).drop_duplicates().tolist()
    for date in unique_dates_list:
        list_profits.append(calculate_margin_profit(date))
    unique_dates_list.sort(reverse=True)
    unique_dates_last_10_days = unique_dates_list[:10]
    plt.bar(unique_dates_last_10_days, list_profits, color='green')
    plt.canvas_color('white')
    plt.title("Margin of profit last 10 days")
    plt.xlabel("x = date")
    plt.ylabel("y = % margin profit")
    plt.show()


# py main.py json --make_bought
def make_json_bought():
    csvFilePath = pa.full_path_bought
    jsonFilePath = pa.full_path_bought_json
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['id']
            data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# py main.py json --make_sold
def make_json_sold():
    csvFilePath = pa.full_path_sold
    jsonFilePath = pa.full_path_sold_json
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['id']
            data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# py main.py json --make_stock
def make_json_stock():
    csvFilePath = pa.full_path_stock
    jsonFilePath = pa.full_path_stock_json
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['id']
            data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Main function JSON
def make_json(args):
    if args.make_bought:
        print(make_json_bought())
    if args.make_sold:
        make_json_sold()
    if args.make_stock:
        make_json_stock()
