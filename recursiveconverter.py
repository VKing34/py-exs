def converter(n,base):
    digits = "0123456789ABCDEF"
    if n < base:
        return digits[n]
    else:
        return converter(n//base,base) + digits[n%base]


print("---------------Converter-----------------")
n = int(input("Enter a ingeter number: "))
base = int(input("Enter the base: "))
print("The result: ",converter(n,base))
print("-----------------------------------------")