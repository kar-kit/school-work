
#! INLCUDE THIS
if __name__ == 'main':
  #! Requires a 13 digit array
  ISBN = [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in range(1,14):
  #! Replaces the 1st digit of the array
  ISBN[count] = int(input('Please enter next digit of the ISBN'))

calculatedDigit = 0
count = 1

#! Why is this
while count < 13:
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
