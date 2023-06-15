# Report Superpy

## 1. Most proud

I am most proud of the code below. See comments for explanation.
The lower part of the function is missing because the file should not be too large.

```python
def graph_margin_profit():
    list_profits = []                               # empty list
    df = pd.read_csv(pa.full_path_sold)             # creates dataframe sold.csv with pandas
    sellprice = df['sell_date'].values              # Takes values sell_date from dataframe
    unique_dates_list =
    pd.Series(sellprice).drop_duplicates().tolist() # Creates a list with unique dates
    for date in unique_dates_list:                  # For loop that use the list with unique dates. 
        list_profits.append(calculate_margin_profit(date)) # This is the part I'm the most proud of! It first takes the empty list list_profits. Than it appends the complicated function that needs a specific date to calculate the margin profit.  
    unique_dates_list.sort(reverse=True)            # Sort most recent date first.
    unique_dates_last_10_days = unique_dates_list[:10] # Takes the first 10 from the list. 
    # now the data is complete to make the Graph!
```

## 2. Pytz

I decided to use Pytz because it was recommended by Python official documentation itself, to work with a time zone. That's why I trusted this third party code.
Since Pytz does not return the desired format, it was necessary to use strftime() as well.
The same goes for time delta(). I used time_now to test if the timezone was really correct. I also tested some other timezones.. and it works great!

```python
my_date_now = datetime.datetime.now(pytz.timezone('Europe/Paris')) 
date_now = my_date_now.strftime("%Y-%m-%d")
time_now = my_date_now.strftime("%H:%M:%S")
yesterday_full = my_date_now - timedelta(days=1)
yesterday = yesterday_full.strftime("%Y-%m-%d")
```

## 3. Plotext

I decided to use Plotext instead of Matplotlib. Since IT changes so quickly, I thought it would be nice to find a library myself.
I saw several positive reviews about Plotext on Youtube and that made me curious. Since it is a third party I have checked the security on [this site](https://snyk.io/advisor/python/plotext).
