import math
num = int(input("Enter a number: "))

try:
    print(math.sqrt(num))
except:
    print("Bad value for square root\nUsing absolute value instead")
    print("%.3f"%math.sqrt(abs(num)))

