# pcost.py
#
# Exercise 1.27
import os
import sys
script_dir = os.path.dirname(__file__)

def portfolio_cost(filename):
    f = open(script_dir +'/'+filename, 'rt')
    heads = next(f)

    total_cost = 0.0

    for line in f:
        name, shares, price = line.rstrip().split(',')
        shares
        try:
            total_cost = total_cost + int(shares) * float(price)
        except ValueError:
            continue

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)