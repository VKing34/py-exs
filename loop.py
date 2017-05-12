count =1
while count <= 5:
    print(count)
    count += 1

while count <= 10 and not False:
    print(count)
    count += 1


for item in [1,3,5,6,2]:
    print(item)

list = [x*x for x in range(1,11) if x%2 != 0]
print(list)

