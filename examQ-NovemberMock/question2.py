ISBN = []

for i in range(1,13):
  count = int(input('Please enter next digit of the ISBN'))
  ISBN.append(count)

calculatedDigit = 0
count = 1

while count:
  calculatedDigit = calculatedDigit + ISBN
  count = count + 1
  calculatedDigit = calculatedDigit + ISBN*3
  count = count + 1

while calculatedDigit >= 10:
  calculatedDigit = calculatedDigit - 10

calculatedDigit = 10 - calculatedDigit

if calculatedDigit == 10:
  calculatedDigit = 0

if calculatedDigit == ISBN[13]:
  print('Valid ISBN')
else:
  print('Invalid ISBN')
