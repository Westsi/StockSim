"""
A bot powered stock sim. currently one stock two bots. can make db for diff bots/stocks
All bots right now are short term- buy low sell high between 5 or so days

TODO
Make it so that multiple bots of one type can use same function
Make bots trade simultaneously or randomly selected (randint then if/elif) (multithreading)
Start doing making price vars decimal type (built in, import)
"""

# imports
import random
import matplotlib.pyplot as plt

# prices in cents/pennies
start_price = 10
amount_of_stocks = 1000
current_price = 9
previous_day_price = start_price
stocks_bought_on_previous_day = 0
stocks_sold_on_previous_day = 0

# plotting array
prices_plt = []
careful_bot_bal_plt = []
risky_bot_bal_plt = []
random_bot_bal_plt = []
total_amount_in_economy = []

# clear file for price history then opens for append which is done in days sim at bottom for loop
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
    # needs to be int for operations]
    if current_price > 1:
        for stock in range(int(previous_day_price) - int(current_price)):
            # to ensure no negative vals
            if amount_of_stocks > 0 and bot_bal > int(current_price) and current_price != 0:
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
    # sells everything
    for stock in range(bot_stocks_owned):
        # check to ensure never negative
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
    # so that it can get some money back
    if bot_bal < current_price and bot_stocks_owned > 0:
        bot_sell_stock()
    # buy low
    elif current_price < previous_day_price:
        bot_buy_stock()
    # sell high
    elif current_price > previous_day_price:
        # for stock in range(int(previous_day_price) - int(current_price)):
        # i dont completely know what effect this for loop has but it adds some weird stuff into market and bot balance
        # uncomment the for loop and indent bot_sell_stock to see
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
    if current_price > 1:
        for stock in range(int(risky_bot_bal / int(current_price))):
            if amount_of_stocks > 0 and risky_bot_bal > int(current_price) and current_price != 0:
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
        # for stock in range(int(previous_day_price) - int(current_price)):
        risky_bot_sell_stock()

    elif current_price == previous_day_price:
        risky_bot_sell_stock()


random_bot_bal = 10000
random_bot_stocks_owned = 0


# random bot
def random_bot_buy_stock():
    global amount_of_stocks
    global current_price
    global previous_day_price
    global random_bot_bal
    global random_bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    # needs to be int for operations
    if current_price > 1:
        for stock in range(random.randint(0, 20)):
            # to ensure no negative vals
            if amount_of_stocks > 0 and random_bot_bal > int(current_price) and current_price != 0:
                amount_of_stocks -= 1
                random_bot_stocks_owned += 1
                random_bot_bal = random_bot_bal - int(current_price)
                stocks_bought_on_previous_day += 1
                # just to make sure bot doesn't go broke
            if random_bot_bal < 1000:
                random_bot_bal += 5000


def random_bot_sell_stock():
    # global var imports
    global amount_of_stocks
    global current_price
    global previous_day_price
    global random_bot_bal
    global random_bot_stocks_owned
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day
    # sells everything
    for stock in range(random.randint(0, random_bot_stocks_owned)):
        # check to ensure never negative
        if random_bot_stocks_owned > 0:
            amount_of_stocks += 1
            random_bot_stocks_owned -= 1
            random_bot_bal = random_bot_bal + int(current_price)
            stocks_sold_on_previous_day += 1


def random_bot_user():
    # to simulate 100 random users
    for no in range(100):
        rand_num = random.uniform(0, 1)
        if rand_num > 0.5:
            random_bot_buy_stock()
        elif rand_num <= 0.5:
            random_bot_sell_stock()


def next_day():
    global current_price
    global previous_day_price
    global stocks_bought_on_previous_day
    global stocks_sold_on_previous_day

    # this needs to be set before because current_price changes in market randomisation
    previous_day_price = current_price

    # randomises market slightly
    for item in range(stocks_sold_on_previous_day):
        # to stop economic crash
        if not current_price < 1:
            current_price -= random.uniform(0.01, 0.05)
    for item in range(stocks_bought_on_previous_day):
        current_price += random.uniform(0.01, 0.05)

    # reset vars
    stocks_sold_on_previous_day = 0
    stocks_bought_on_previous_day = 0


# range is number of days basically
for i in range(100):
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

    print("random bot balance " + str(random_bot_bal))
    print("random bot stocks owned " + str(random_bot_stocks_owned))
    print("total amount of stocks left to buy " + str(amount_of_stocks))
    print("current price " + str(current_price))
    print("previous day price " + str(previous_day_price))

    # function calls
    bot_user()
    risky_bot_user()
    random_bot_user()

    print("end of day " + str(i))
    print(" ")
    # writes price to file
    price_file.write(str(current_price) + "\n")

    # adds necessary vals to plotting arrays
    prices_plt.append(current_price)
    careful_bot_bal_plt.append(bot_bal / 1000)
    risky_bot_bal_plt.append(risky_bot_bal / 10000)
    random_bot_bal_plt.append(random_bot_bal / 100)

    next_day()

# plotting price history
print(prices_plt)
print(careful_bot_bal_plt)
print(risky_bot_bal_plt)
print(random_bot_bal_plt)

plt.xlabel("Days Passed")
plt.ylabel("Amount of Money (SOLUSCOIN)")
plt.title("Different Bots against Price")

plt.plot(prices_plt)
plt.plot(careful_bot_bal_plt)
plt.plot(risky_bot_bal_plt)
plt.plot(random_bot_bal_plt)

plt.legend(['prices', 'careful bot', 'risky bot', 'random bot'], loc='best')

plt.show()
