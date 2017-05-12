class node:
    def __init__(self, newdata):
        self.data = newdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self,newnext):
        self.next = newnext


class Singlelist:
    def __init__(self):
        self.head= None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count = count + 1
            cur = cur.getnext()

        return count

    def search(self,item):
        cur = self.head
        while cur != None:
            if cur.getdata() == item:
                return True
            cur = cur.getnext()
        return False

    def remove(self,item):
        cur = self.head
        if cur.getdata() == item:
            self.head = cur.getnext()
            return True

        pre = None
        while cur.getdata() != item:
            pre = cur
            cur = cur.getnext()
            if cur.getdata() == item:
                pre.setnext(cur.getnext)
                return True

        return False


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self,newdata):
        cur = self.head
        pre = None
        while cur.getdata() > newdata:
            pre = cur
            cur = cur.getnext()

        temp = node(newdata)
        if pre == None:
            temp.setnext(self.head)
            self.head = temp
        else:
            pre.setnext(temp)
            temp.setnext(cur)
