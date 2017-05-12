class stack:
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

s = stack()

s.push('!!!')
s.push('world')
s.push('hello')

print(s.peek())

while not s.isEmpty():
    print(s.pop())
