class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item)-1]

    def size(self):
        return len(self.item)



def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

def baseConvert(num,base):
    digits = "0123456789ABCDEFGHIJKLMNOP"
    s = Stack()

    while num > 0:
        s.push(num%base)
        num = int(num//base)

    string = ""
    while not s.isEmpty():
        string = string + str(digits[s.pop()])

    return string


print("---------------Dec to Binary----------------")
decNumber = int(input("Enter a decimal number: "))
print("The binary number: ", divideBy2(decNumber))

print("----------------base Converter--------------")
num = int(input("Enter a decimal number: "))
base = int(input("Enter the base of number: "))
print("The result: ",baseConvert(num,base))




