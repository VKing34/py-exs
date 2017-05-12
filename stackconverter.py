from pythonds.basic.stack import Stack

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


