"""
A bot powered stock sim. currently one stock one bot. can make db for diff bots/stocks
problems- numbers get too high for stocks available, prices loop because of only one bot.
"""

# prices in cents/pennies
start_price = 10
amount_of_stocks = 10
current_price = 900
previous_day_price = start_price
stocks_bought_on_previous_day = 0
stocks_sold_on_previous_day = 0
price_clear = open("price_history.txt", "w")
price_clear.write("")
price_clear.close()
price_file = open("price_history.txt", "a")

# provisionally bot can buy every stock
bot_bal = 100
bot_stocks_owned = 0


def bot_buy_stock():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global bot_bal
    global bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    for stock in range(previous_day_price - current_price):
        amount_of_stocks -= 1
        bot_stocks_owned += 1
        bot_bal = bot_bal - current_price
        stocks_bought_on_previous_day += 1


def bot_sell_stock():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global bot_bal
    global bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    for stock in range(10):
        amount_of_stocks += 1
        bot_stocks_owned -= 1
        bot_bal = bot_bal + current_price
        stocks_sold_on_previous_day += 1


def bot_user():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global bot_bal
    global bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    if current_price < previous_day_price:
        bot_buy_stock()

    elif current_price > previous_day_price:
        for stock in range(previous_day_price - current_price):
            bot_sell_stock()
    elif current_price == previous_day_price:
        for ss in range(10):
            amount_of_stocks += 1
            bot_stocks_owned -= 1
            bot_bal = bot_bal + current_price
            stocks_sold_on_previous_day += 1


def next_day():
    global current_price
    global previous_day_price
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day

    previous_day_price = current_price
    for item in range(stocks_sold_on_previous_day):
        current_price -= 1
    for item in range(stocks_bought_on_previous_day):
        current_price += 1
    stocks_sold_on_previous_day = 0
    stocks_bought_on_previous_day = 0


for i in range(12):
    print("bot balance " + str(bot_bal))
    print("bot stocks owned " + str(bot_stocks_owned))
    print("total amount of stocks left to buy " + str(amount_of_stocks))
    print("current price " + str(current_price))
    bot_user()
    print("end of day " + str(i))
    print(" ")
    price_file.write(str(current_price) + "\n")
    next_day()
