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

s = Stack()
def converter(n, base):
    digits = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            s.push(digits[n])
        else:
            s.push(digits[n%base])

        n = n//base
    result = ""
    while not s.isEmpty():
        result = result + s.pop()
    return result

print("---------------Converter-----------------")
n = int(input("Enter a ingeter number: "))
base = int(input("Enter the base: "))
print("The result: ",converter(n,base))
print("-----------------------------------------")


