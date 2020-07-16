# pcost.py
#
# Exercise 1.27
import os
script_dir = os.path.dirname(__file__)

def portfolio_cost(filename):
    f = open(script_dir +'/'+filename, 'rt')
    heads = next(f)

    total_cost = 0.0

    for line in f:
        name, shares, price = line.rstrip().split(',')
        total_cost = total_cost + int(shares) * float(price)
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)