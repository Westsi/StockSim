import random

with open("top1kstocks.txt", "r") as f:
    stocks = f.readlines()

budget = 100000

totalspend = 0
while (budget > 0):
    rndstock = random.choice(stocks)
    stocks.remove(rndstock)
    tospend = random.randint(1000, 4000)
    if tospend > budget:
        tospend = budget
    budget -= tospend
    totalspend += tospend
    print(f"BUY {rndstock.strip()} ${tospend}")

print(totalspend)