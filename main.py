# Imports
import argparse
import sys
import dates as d
import main_functions as ma

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# Dates

def main():
    # prints
    print(d.time_now)
    d.write_date_text()

    parser = argparse.ArgumentParser(
        prog="Superpy",
        description="Purchasing and Sales registration and reports",
        epilog="Thanks for using %(prog)s! :)",
    )

    subparsers = parser.add_subparsers(dest='command')

    # subparser BUY
    buy = subparsers.add_parser(
        'buy', help="For more help options type: python main.py buy -h")
    buy.set_defaults(func=ma.append_bought)

    # subparser SELL
    sell = subparsers.add_parser(
        'sell', help='For more help options type: python main.py sell -h')
    sell.set_defaults(func=ma.sell)

    # subparser REPORT
    report = subparsers.add_parser(
        'report', help='For more help options type: python main.py report -h')
    report.set_defaults(func=ma.report)

    # subparser Json
    json = subparsers.add_parser(
        'json', help='For more help options type: python main.py json -h')
    json.set_defaults(func=ma.make_json)

    # add arguments BUY
    buy.add_argument(
        "--product_name",
        type=str,
        action="store",
        dest="product_name",
        help="Enter product name",
        required=True,
    )

    buy.add_argument(
        "--buy_date",
        const=d.date_now,
        default=d.choose_days_back,
        dest="buy_date",
        help="Enter '' = date now. -1 yesterday, -3 three days ago, 1 tomorrow etc.",
        nargs="?",
    )

    buy.add_argument(
        "--buy_price",
        type=int,
        action="store",
        dest="buy_price",
        help="Enter buy price",
        required=True,
    )

    buy.add_argument(
        "--expiration_date",
        type=d.datetime.date.fromisoformat,
        action="store",
        dest="expiration_date",
        help="Enter Expiration Date - format YYYY-MM-DD",
        required=True,
    )

    # add arguments SELL
    sell.add_argument(
        "--id",
        action="store",
        dest="id",
        help="Enter purchase id",
        required=True,
    )

    sell.add_argument(
        "--sell_price",
        type=int,
        action="store",
        dest="sell_price",
        help="Enter sell price",
        required=True,
    )

    sell.add_argument(
        "--sell_date",
        const=d.date_now,
        default=d.choose_days_back,
        dest="sell_date",
        help="Enter '' = date now. -1 yesterday, -3 three days ago, 1 tomorrow etc.",
        nargs="?",
    )

    # add arguments REPORT
    report.add_argument(
        "--revenue",
        type=d.datetime.date.fromisoformat,
        action="store",
        dest="revenue",
        help="Report revenue specific date - format date YYYY-MM-DD",
        required=False,
    )

    report.add_argument(
        "--profit",
        type=d.datetime.date.fromisoformat,
        action="store",
        dest="profit",
        help="Report margin profit specific date - format date YYYY-MM-DD",
        required=False,
    )

    report.add_argument(
        "--graph_margin",
        action="store_true",
        dest="graph_margin",
        help="Report graph margin profit last 10 days",
        required=False,
    )

    report.add_argument(
        "--graph_revenue",
        action="store_true",
        dest="graph_revenue",
        help="Report graph margin profit last 10 days",
        required=False,
    )

    report.add_argument(
        "--stock",
        action="store_true",
        dest="stock",
        help="Report view current stock",
        required=False,
    )

    report.add_argument(
        "--bought",
        action="store_true",
        dest="bought",
        help="Report view all bought products",
        required=False,
    )

    report.add_argument(
        "--sold",
        action="store_true",
        dest="sold",
        help="Report view all sold products",
        required=False,
    )

    report.add_argument(
        "--expiration_date",
        action="store_true",
        dest="expiration_date",
        help="Report view expiration dates from now or earlier",
        required=False,
    )

    # add arguments JSON
    json.add_argument(
        "--make_bought",
        action="store_true",
        dest="make_bought",
        help="Makes json file bought.json from bought.csv",
        required=False,
    )

    json.add_argument(
        "--make_sold",
        action="store_true",
        dest="make_sold",
        help="Makes json file sold.json from sold.csv",
        required=False,
    )

    json.add_argument(
        "--make_stock",
        action="store_true",
        dest="make_stock",
        help="Makes json file stock.json from stock.csv",
        required=False,
    )

    # This is for the subparsers. Otherwise it will be a mess in the help section!
    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
