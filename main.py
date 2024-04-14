print ('Loan Calculator')
print()

loan = 1000
apr = 0.05
total_interest = 0

for year in range (10):
    loan += loan*apr
    print ('Year', year+1, 'is', round(loan,2))
    total_interest += loan*apr
print('You paid', round(total_interest, 2), 'in interest!')