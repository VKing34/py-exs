list = [1,2,3,4]
A = [list]*3
print(A)
list[2] = 0
print(A)

list = [1024, 3, True, 6.5]
print(list)
list.append(False)
print(list)

list.insert(2,3.5)
print(list)

list.insert(0,34)
print(list)

print(list.pop())
print(list)

print(list.pop(2))
print(list)

list.sort()
print(list)

list.reverse()
print(list)

print(list.count(6.5))

print(list.index(3.5))

list.remove(6.5)
print(list)

del list[0]
print(list)