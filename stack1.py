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


def parChecker(string):
    if len(string) == 0:
        print("There's no string!!!")
        return False
    s = Stack()
    mark = False
    index =0
    while index < len(string):
        symbol = string[index]
        if symbol in "{([":
            mark = True
            s.push(symbol)


        elif symbol == ")" and s.peek() == "(":
            s.pop()
        elif symbol == ")" and s.peek() != "(":
            break
        elif symbol == "}" and s.peek() == "{":
            s.pop()
        elif symbol == "}" and s.peek() != "{":
            break

        elif symbol == "]" and s.peek() == "[":
            s.pop()
        elif symbol == "]" and s.peek() != "[":
            break

        index = index + 1

    if mark and s.isEmpty():
        return True
    else:
        return False


string1 = input("Enter a string to check: ")

if parChecker(string1):
    print("Symmetric!!!")
else:
    print("Unsymmetric!!!")