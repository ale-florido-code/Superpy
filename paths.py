import os

# ABSOLUTE PATH
absolute_path = os.path.dirname(__file__)
print(absolute_path)

# bought.csv
relative_path_bought = "csv_files/bought.csv"
full_path_bought = os.path.join(absolute_path, relative_path_bought)

# sold.csv
relative_path_text = "csv_files/sold.csv"
full_path_sold = os.path.join(absolute_path, relative_path_text)

# stock.csv
relative_path_text = "csv_files/stock.csv"
full_path_stock = os.path.join(absolute_path, relative_path_text)

# text.csv
relative_path_text = "csv_files/date_now.txt"
full_path_text = os.path.join(absolute_path, relative_path_text)

# bought.json
relative_path_bought = "json_files/bought.json"
full_path_bought_json = os.path.join(absolute_path, relative_path_bought)

# sold.json
relative_path_sold = "json_files/sold.json"
full_path_sold_json = os.path.join(absolute_path, relative_path_sold)

# stock.json
relative_path_stock = "json_files/stock.json"
full_path_stock_json = os.path.join(absolute_path, relative_path_stock)
