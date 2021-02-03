import matplotlib.pyplot as plt
import requests
from tkinter import *


def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


root = Tk()

# root.iconbitmap(r'')

# Tkinter is two-step process 1: Define the thing 2: Put the thing the screen

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': "Put your coinmarketcap API Key '
}

# Create a header

header_name = Label(root, text="NAME", bg="#00BFFF", font="Verdana 8 bold")
header_name.grid(row=0, column=0, sticky="nsew")

header_rank = Label(root, text="RANK", bg="#00BFFF", font="Verdana 8 bold")
header_rank.grid(row=0, column=1, sticky="nsew")

header_current_price = Label(root, text="CURRENT PRICE", bg="#00BFFF", font="Verdana 8 bold")
header_current_price.grid(row=0, column=2, sticky="nsew")

header_price_paid = Label(root, text="PRICE PAID", bg="#00BFFF", font="Verdana 8 bold")
header_price_paid.grid(row=0, column=3, sticky="nsew")

header_profit_loss_per = Label(root, text="PROFIT/LOSS PER", bg="#00BFFF", font="Verdana 8 bold")
header_profit_loss_per.grid(row=0, column=4, sticky="nsew")

header_1_hour_change = Label(root, text="1 HOUR CHANGE", bg="#00BFFF", font="Verdana 8 bold")
header_1_hour_change.grid(row=0, column=5, sticky="nsew")

header_24_hour_change = Label(root, text="24 HOUR CHANGE", bg="#00BFFF", font="Verdana 8 bold")
header_24_hour_change.grid(row=0, column=6, sticky="nsew")

header_7_day_change = Label(root, text="7 DAY CHANGE", bg="#00BFFF", font="Verdana 8 bold")
header_7_day_change.grid(row=0, column=7, sticky="nsew")

header_current_value = Label(root, text="CURRENT VALUE", bg="#00BFFF", font="Verdana 8 bold")
header_current_value.grid(row=0, column=8, sticky="nsew")

header_profit_loss_total = Label(root, text="PROFIT/LOSS TOTAL", bg="#00BFFF", font="Verdana 8 bold")
header_profit_loss_total.grid(row=0, column=9, sticky="nsew")


# END HEADER


def lookup():
    api = requests.get(url, params=parameters, headers=headers).json()
    data = api['data']

    # My portfolio
    my_portfolio = [
        {
            "sym": "BTC",
            "amount_owned": 0,
            "price_paid_per": 0,
        },
        {
            "sym": "NEXO",
            "amount_owned": 0,
            "price_paid_per": 0,
        },
        {
            "sym": "ZEBI",
            "amount_owned": 130000,
            "price_paid_per": 0.0060,
        },
        {
            "sym": "BASE",
            "amount_owned": 200,
            "price_paid_per": 1,
        },
        {
            "sym": "ORN",
            "amount_owned": 0,
            "price_paid_per": 0,
        },
        {
            "sym": "COTI",
            "amount_owned": 19220,
            "price_paid_per": 0.046,
        },
        {
            "sym": "CHR",
            "amount_owned": 25000,
            "price_paid_per": 0.030,
        },
        {
            "sym": "PLT",
            "amount_owned": 4119,
            "price_paid_per": 0.010,
        },
        {
            "sym": "ZEE",
            "amount_owned": 0,
            "price_paid_per": 0,
        },
        {
            "sym": "DOCK",
            "amount_owned": 31888,
            "price_paid_per": 0.020,
        },
        {
            "sym": "SUTER",
            "amount_owned": 125855,
            "price_paid_per": 0.0030,
        },
        {
            "sym": "ROYA",
            "amount_owned": 0,
            "price_paid_per": 0,
        },
        {
            "sym": "PLOT",
            "amount_owned": 9326,
            "price_paid_per": 0.045,
        }

    ]

    portfolio_profit_loss = 0

    row_count = 1  # row starts at 1 bc headers are in row 0

    total_current_value = 0
    pie = []
    pie_size = []

    for x in data:
        for coin in my_portfolio:
            if coin["sym"] == x['symbol']:
                # Do some math
                total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
                current_value = float(coin["amount_owned"]) * float(x['quote']['USD']['price'])
                profit_loss = current_value - total_paid
                portfolio_profit_loss += profit_loss
                profit_loss_per_coin = float(x['quote']['USD']['price']) - float(coin["price_paid_per"])

                total_current_value += current_value

                pie.append(x["name"])
                pie_size.append(coin["amount_owned"])

                # Get the quotes: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest
                # "symbol": "BTC", "name" : Bitcoin, "cmc_rank": 'gives you the rank of the coin',
                # ['quote']['USD']['price']: gives you the price in USD

                # print(x['name'])
                # print(" Current Price: ${0:.6f}".format(float(x['quote']['USD']['price'])))
                # print(" Profit/Loss: ${0:.2f}".format(profit_loss_per_coin))
                # print(" Rank: {0:.0f}".format(float(x["cmc_rank"])))
                # print(" Total Paid: ${0:.2f}".format(float(total_paid)))
                # print(" Current Value: ${0:.2f}".format(float(current_value)))
                # print(" Profit/Loss: ${0:.2f}".format(profit_loss))
                # print("----------------------------------")

                name = Label(root, text=x['name'], bg="#F0E68C")
                name.grid(row=row_count, column=0, sticky="nsew")

                rank = Label(root, text=x["cmc_rank"], bg="#E0FFFF")
                rank.grid(row=row_count, column=1, sticky="nsew")

                current_price = Label(root, text="${0:.6f}".format(float(x['quote']['USD']['price'])), bg="#F0E68C")
                current_price.grid(row=row_count, column=2, sticky="nsew")

                price_paid = Label(root, text="${0:.6f}".format(float(coin["price_paid_per"])), bg="#E0FFFF")
                price_paid.grid(row=row_count, column=3, sticky="nsew")

                profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin)), bg="#F0E68C",
                                        fg=red_green(float(profit_loss_per_coin)))

                profit_loss_per.grid(row=row_count, column=4, sticky="nsew")

                one_hr_change = Label(root, text="{0:.2f}%".format(float(x["quote"]["USD"]["percent_change_1h"])),
                                      bg="#E0FFFF", fg=red_green(float(x["quote"]["USD"]["percent_change_1h"])))
                one_hr_change.grid(row=row_count, column=5, sticky="nsew")

                twenty24_hour_change = Label(root,
                                             text="${0:.2f}%".format(float(x["quote"]["USD"]["percent_change_24h"])),
                                             bg="#F0E68C", fg=red_green(float(x["quote"]["USD"]["percent_change_24h"])))
                twenty24_hour_change.grid(row=row_count, column=6, sticky="nsew")

                seven_day_change = Label(root, text="{0:.2f}%".format(float(x["quote"]["USD"]["percent_change_7d"])),
                                         bg="#E0FFFF", fg=red_green(float(x["quote"]["USD"]["percent_change_7d"])))
                seven_day_change.grid(row=row_count, column=7, sticky="nsew")

                current_value = Label(root, text="${0:.2f}".format(float(current_value)), bg="#F0E68C")
                current_value.grid(row=row_count, column=8, sticky="nsew")

                profit_loss_total = Label(root, text="${0:.2f}".format(profit_loss), bg="#E0FFFF",
                                          fg=red_green(float(profit_loss)))
                profit_loss_total.grid(row=row_count, column=9, sticky="nsew")

                row_count += 1

    portfolio_profits = Label(root, text="P/L: ${0:.2f}".format(float(portfolio_profit_loss)), font="Verdana 8 bold",
                              fg=red_green(float(portfolio_profit_loss)))
    portfolio_profits.grid(row=row_count, column=0, sticky="w", padx=10, pady=10)

    root.title("Crypto Currency - Portfolio Value: ${0:.2f}".format(float(total_current_value)))
    # total_current_value_output = Label(root, text="Profit/Loss: ${0:.2f}".format(float(total_current_value)), font="Verdana 8 bold",
    #                                    fg=red_green(float(total_current_value)))
    # total_current_value.grid(row=row_count+1, column=1, sticky="w", padx=10, pady=10)
    data = ""

    # Update Button
    update_button = Button(root, text="Update Prices", command=lookup)
    update_button.grid(row=row_count, column=9, sticky="ws", padx=10, pady=10)

    def graph(pie, pie_sizes):

        labels = pie
        sizes = pie_size

        colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral", "silver", "red", ]
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout
        plt.show()

    graph_button = Button(root, text="PIE CHART", command=lambda: graph(pie, pie_size))
    graph_button.grid(row=row_count, column=8, sticky="es", pady=10)


lookup()
root.mainloop()
