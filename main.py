"""
A bot powered stock sim. currently one stock two bots. can make db for diff bots/stocks
problems- stock price can be negative

TODO
Try to consolidate functions and variables (is previous_day_price really necessary or can i use last of price_plt array?)
Add a bot that randomly selects buy/sell disrespecting of price
Make it so that multiple bots of one type can use same function
Make bots trade simultaneously or randomly selected (randint then if/elif) (multithreading)
Start doing making price vars decimal type (built in, import)
COMMENT STUFF. seriously
"""

# imports
import random
import matplotlib.pyplot as plt

# prices in cents/pennies
start_price = 10
amount_of_stocks = 100
current_price = 9
previous_day_price = start_price
stocks_bought_on_previous_day = 0
stocks_sold_on_previous_day = 0

# plotting array
prices_plt = []
careful_bot_bal_plt = []
risky_bot_bal_plt = []

price_clear = open("price_history.txt", "w")
price_clear.write("")
price_clear.close()
price_file = open("price_history.txt", "a")

bot_bal = 100
bot_stocks_owned = 0


# careful bot
def bot_buy_stock():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global bot_bal
    global bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    # needs to be int for operations
    for stock in range(int(previous_day_price) - int(current_price)):
        # to ensure no negative vals
        if amount_of_stocks > 0 and bot_bal > int(current_price):
            amount_of_stocks -= 1
            bot_stocks_owned += 1
            bot_bal = bot_bal - int(current_price)
            stocks_bought_on_previous_day += 1


def bot_sell_stock():
    # global var imports
    global amount_of_stocks
    global current_price
    global previous_day_price
    global bot_bal
    global bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    for stock in range(bot_stocks_owned):
        if bot_stocks_owned > 0:
            amount_of_stocks += 1
            bot_stocks_owned -= 1
            bot_bal = bot_bal + int(current_price)
            stocks_sold_on_previous_day += 1


def bot_user():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global bot_bal
    global bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    if bot_bal < current_price and bot_stocks_owned > 0:
        bot_sell_stock()

    elif current_price < previous_day_price:
        bot_buy_stock()

    elif current_price > previous_day_price:
        for stock in range(int(previous_day_price) - int(current_price)):
            bot_sell_stock()

    elif current_price == previous_day_price:
        bot_sell_stock()


# risky bot
risky_bot_bal = 100
risky_bot_stocks_owned = 0


def risky_bot_buy_stock():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global risky_bot_bal
    global risky_bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    for stock in range(int(risky_bot_bal / int(current_price))):
        if amount_of_stocks > 0 and risky_bot_bal > int(current_price):
            amount_of_stocks -= 1
            risky_bot_stocks_owned += 1
            risky_bot_bal = risky_bot_bal - int(current_price)
            stocks_bought_on_previous_day += 1


def risky_bot_sell_stock():
    # global var imports
    global amount_of_stocks
    global current_price
    global previous_day_price
    global risky_bot_bal
    global risky_bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    for stock in range(risky_bot_stocks_owned):
        if risky_bot_stocks_owned > 0:
            amount_of_stocks += 1
            risky_bot_stocks_owned -= 1
            risky_bot_bal = risky_bot_bal + int(current_price)
            stocks_sold_on_previous_day += 1


def risky_bot_user():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global risky_bot_bal
    global risky_bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day

    if risky_bot_bal < current_price and risky_bot_stocks_owned > 0:
        risky_bot_sell_stock()

    elif current_price < previous_day_price:
        risky_bot_buy_stock()

    elif current_price > previous_day_price:
        risky_bot_sell_stock()

    elif current_price == previous_day_price:
        risky_bot_sell_stock()


def next_day():
    global current_price
    global previous_day_price
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day

    # this needs to be set before because current_price changes in market randomisation
    previous_day_price = current_price

    # randomises market slightly
    for item in range(stocks_sold_on_previous_day):
        current_price -= random.uniform(0.01, 0.05)
    for item in range(stocks_bought_on_previous_day):
        current_price += random.uniform(0.01, 0.05)

    # reset vars
    stocks_sold_on_previous_day = 0
    stocks_bought_on_previous_day = 0


for i in range(10000):
    # print statements mostly for checking, price_history as well.
    print("bot balance " + str(bot_bal))
    print("bot stocks owned " + str(bot_stocks_owned))
    print("total amount of stocks left to buy " + str(amount_of_stocks))
    print("current price " + str(current_price))
    print("previous day price " + str(previous_day_price))

    print("risky bot balance " + str(risky_bot_bal))
    print("risky bot stocks owned " + str(risky_bot_stocks_owned))
    print("total amount of stocks left to buy " + str(amount_of_stocks))
    print("current price " + str(current_price))
    print("previous day price " + str(previous_day_price))
    # function calls
    bot_user()
    risky_bot_user()

    print("end of day " + str(i))
    print(" ")
    # writes price to file
    price_file.write(str(current_price) + "\n")

    # adds necessary vals to plotting arrays
    prices_plt.append(current_price)
    careful_bot_bal_plt.append(bot_bal/100)
    risky_bot_bal_plt.append(risky_bot_bal/1000)

    next_day()

# plotting price history
print(prices_plt)
print(careful_bot_bal_plt)
print(risky_bot_bal_plt)

plt.plot(prices_plt)
plt.plot(careful_bot_bal_plt)
plt.plot(risky_bot_bal_plt)

plt.show()
