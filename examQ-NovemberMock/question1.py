# numberIn = int(input('Enter a positive number: '))
# numberOut = 0
# count = 0

# while numberIn > 0:
#   count = count + 1
#   partValue = numberIn % 2
#   numberIn = numberIn // 2

#   for i in range(1,count):
#     partValue = partValue * 10
  
#   numberOut = numberOut + partValue

# print('The result is: ', numberOut)

# The purpose is to half the number

NumberIn = int(input('Enter a positive whole number: '))
NumberOut = 0
Count = 0
while NumberIn > 0:
  Count += 1
  PartValue = NumberIn % 2
  NumberIn = NumberIn // 2
  for i in range(1, Count):
    PartValue = PartValue * 10
  NumberOut = NumberOut + PartValue
print('The result is: ', NumberOut)
