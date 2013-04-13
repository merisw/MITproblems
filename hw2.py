balance = 320000
annualInterestRate = .2

monthlyInterestRate = annualInterestRate/12.0
low = balance/12
high = (balance*((1 + monthlyInterestRate)**12))/12.0
remainingBalance = balance

while abs(remainingBalance) > .1:
    remainingBalance = balance
    minPayment = round(((low + high)/2), 2)
    for month in range(1, 13):
        unpaid = remainingBalance - minPayment
        remainingBalance = unpaid + (monthlyInterestRate*unpaid)
    if remainingBalance > 0:
        low = minPayment
    else:
        high = minPayment
    
print 'Lowest Payment: ' + str(minPayment)
