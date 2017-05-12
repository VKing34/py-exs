class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self,x):
        self.item.insert(0,x)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],5))
