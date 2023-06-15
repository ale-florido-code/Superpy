# Superpy

## Welcome to Superpy

Hello colleague, welcome to Superpy!
In this program we can do many amazing things.
We can register the buying and selling of products.
Everything will be saved automatically in csv.

We can view the stock, what we have bought and sold. 

It's also possible to watch reports and graphs.
If you like json files, we can make json files either!
Let's start and enjoy Superpy :) !

## Help

Every command begins with: **py main.py**
After this we can add words and the program will get to work for us!
If you need help from te program, just enter:

```cmd
py main.py -h
```

The program will display the **help** screen.

## Buy a box

If you want to buy something it's necessary to use all fields.
Let's show an example:

```cmd
python main.py buy --product_name Apple --buy_date -3 --buy_price 55 --expiration_date 2023-03-23
```

Of course we start with **main.py**. After this we use the word **buy**. Now the program knows we want to buy something.

After this we enter the name of the product, for example **--product_name Banana**. Because we only buy per box, it is not necessary to enter a price per piece or how many pieces.

Then we need to fill in the buy date. If we only enter **--buy_date**, the program will automatically take the date now. The timezone will be Paris, even if our administrative colleagues in the US use the system. If you want a date in the future or past, it works like this:

a positive number is in the future, a negative number is in the past.
    1. --buy_date -3
    2. --buy_date 2

In the first example the date will be 3 days ago. In the second example the date will be the day after tomorrow.

Now we need to fill in the buy price per box ass follow:

```cmd
-- buy_price 55
```

Finally, we enter the expiration date. The format needs to be YYYY-MM-DD.
for example: **--expiration_date 2023-03-23

If we entered all the fields, we could press enter. Again, it's necessary to fill in al the fields, otherwise you will get an error.

## Sell a box

If we have sold a hole box, or a part of the box and the expiration date has been exceeded we need to register this as sales!
First we check the stock for the id of the box.

It's very important to register if we sold a box.
It will be removed from stock. Now all our colleagues can see that it is no longer in stock. It's also important for management to be able to see up-to-date information about turnover and profit margin.

Let's sell a box!
First check the stock:

```cmd
py main.py report --stock
```

Here we see al the boxes we have in stock. You can find the id here (and many other info).

Now we are ready to sell. See the next example: 

```cmd
py main.py sell --id 1874510404688 --sell_date -5 --sell_price 102
```

First we use the word sell. Superpy will now know we want to sell something. Than fill in the id you found in the stock. The sell date works the same as buy date. (-1 yesterday, 1 tomorrow, empty: date now).

Finally we enter the sale price. Know we can press enter and we sold a box! Be aware we need to enter all the fields again, otherwise you will get an error.

## Report

With the **report** commando we can:

- view the current **stock**, commando:
**py main.py report --stock**

- view what we have **sold**, commando:
**py main.py report --sold**

- view what we have **bought**, commando:
**py main.py report --bought**

- calculate **margin profit**, commando:
**py main.py report --profit**

- calculate **revenue**, commando:
**py main.py report --revenue**

- show revenue last 10 days graph, commando:
**py main.py report --graph_revenue**

- show margin profit last 10 days graph, commando:
**py main.py report --graph_margin**

- show all products whose expiration date is today or earlier.
**py main.py report --expiration_date**

## Json

We can make a json file from one of the csv files. It will be saved automatically in the json_files folder.

- Make json from **bought.csv**, command: **py main.py json --make_bought**
- Make json from **sold.csv**, commando: **py main.py json --make_sold**
- Make json from **stock.csv**, commando: **py main.py json --make_stock**

## Thanks for using Superpy

Thanks for using Superpy, and remember, if you need help while you are using Superpy:
py main.py -h!

## Only for IT department

This message is only for the IT department.
Please install plotext:

```cmd
pip install plotext
```

Pandas is also necessary.