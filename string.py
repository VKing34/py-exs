name = input("Enter your name: ")
print("Hello",name.upper(),"and your name has", len(name),"characters.")

age =  int(input("How old are you? "))

print("%s is %d years old" % (name,age))

item1 = input("What the fuck do you want? ")
price = 25.5
print("The %+10s costs %.2f cents"%(item1,price))

item2 = {"name":"banana","cost":24}
print("The %(name)-10s costs %(cost)5.1f cents"%item2)