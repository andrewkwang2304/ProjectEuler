def isPalindromic(num):
   
   # will feed num into an array, so you can compare the digits!
   
   arr = []
   while num != 0:
      num, d = divmod(num, 10)
      arr.append(int(d))
   arr.reverse()

   # Now we can start comparing the digits in the array to see if it's a palindrome

   a = 0
   b = len(arr) - 1
   iterations = len(arr)//2

   while iterations != 0:
      if(arr[a] == arr[b]):
         a += 1
         b -= 1
         iterations -= 1
      else:
         return False
   return True

   '''
   # splice test. It's more concise, so I'll try to fool around with it. The one below isn't working.

   a = (len(arr)//2) - 1
   if(arr[a:] == arr[:-a:-1]):
      return True
   else:
      return False
   '''


largest = 0

for i in range(100, 1000):
   for j in range(100, 1000):
      result = i*j
      if isPalindromic(result) and result > largest:
         largest = result
         print(str(i) + " and " + str(j) + " produce " + str(largest))
