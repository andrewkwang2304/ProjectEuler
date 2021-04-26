# This program will return the largest prime given a positive integer input.

def largest_prime(i, n):
   copy = n
   while i < n:
      if copy % i == 0:
         largest = i
         copy = copy/i
         if copy == 1:
            return largest
      else:
         i = i + 1

val = int(input("Input a positive integer: "))

print(largest_prime(2, val))
