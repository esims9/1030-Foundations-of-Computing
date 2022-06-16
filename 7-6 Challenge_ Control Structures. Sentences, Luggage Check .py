sentence = str(input("Enter the sentence: "))
num = int(input("Enter the number of times to be printed: "))
for i in range(num):
  print(sentence)

print("Baggage Check")
print("Enter Dimension of luggage item")
dim = int(input("Depth: "))
width = int(input("Across: "))
length = int(input("Height: "))

if dim <= 9 and width <= 14 and length <= 22:
  print("Acceptable carry-on item")
else:
  print("Unacceptable carry-on item")