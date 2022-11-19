n = int(input('Write a number'))
if n%15 == 0:
      print('üjbej')
elif  n%3 == 0 and n%5 != 0:
      print('3')
elif n%5 == 0 and n%3 != 0:
      print('5')
else: 
      quit

