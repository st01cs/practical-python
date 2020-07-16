# pcost.py
#
# Exercise 1.27
import os
script_dir = os.path.dirname(__file__)
f = open(script_dir +'/Data/portfolio.csv', 'rt')
heads = next(f)

total_cost = 0.0

for line in f:
    name, shares, price = line.rstrip().split(',')
    total_cost = total_cost + int(shares) * float(price)

print(total_cost)