# This program prints the sum of even fibonaccis under 4,000,000.

sum = 0
a, b = 1, 2
while b < 4000000:
   if b % 2 == 0:
      sum = sum + b
   #print(b, end=' ')
   a, b = b, a+b

print(sum)
