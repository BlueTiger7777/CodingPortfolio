import decimal

# Set the precision to calculate pi
decimal.getcontext().prec = 100

# Calculate pi to the specified precision
pi = decimal.Decimal(0)
for k in range(0, 100):
    pi += (decimal.Decimal(-1)**k)/(decimal.Decimal(2*k+1))
pi *= 4

# Print the result
print(pi)

import math

n = int(input('Enter the number of digits of pi to be calculated: '))

pi = str(round(math.pi, n))

print('The value of pi is:', pi)
