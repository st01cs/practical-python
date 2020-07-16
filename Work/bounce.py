# bounce.py
#
# Exercise 1.5
height = 100
for i in range(1,11):
    next_height = height * 0.6
    print("%d\t%.4f" % (i, round(next_height, ndigits=4)))
    height = next_height
