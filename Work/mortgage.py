# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_month = 0

extra_payment_start_month = 1
extra_payment_end_month = 12
extra_payment = 1000


while principal > 0:
    payment_month = payment_month + 1
    principal = principal * (1+rate/12)
    total_payment_month = payment
    
    if((payment_month >= extra_payment_start_month) & (payment_month <= extra_payment_end_month)):
        total_payment_month = total_payment_month + extra_payment
    
    if(principal > total_payment_month):
        principal = principal - total_payment_month
    else:
        total_payment_month = principal
        principal = 0
    total_paid = total_paid + total_payment_month
    
    print('%d\t%.2f\t%.2f' % (payment_month, total_paid, principal))

print('\n')
print('Total paid %.2f over %d months' % (total_paid, payment_month))