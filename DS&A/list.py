from pyasn1_modules.rfc4490 import id_Gost28147_89_None_KeyWrap


class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
    def append(self, node):
        if  node is not None:
            node.link= self.link
            self.link = node
    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def isFull(self):
        return False
    def getNode(self, pos):
        if pos < 0: return None
        ptr = self.head
        for i in range(pos):
            if not ptr == None:
                ptr = ptr.link
        return ptr
    def getEntry(self,pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data
    def insert(self, pos,e):
        node = Node(e, None)
        before = self.getNode(pos-1)
        if before == None:
            node.link = self.head
            self.head = node
        else: before.append(node)
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else: return before.popNext()
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count +=1
        return count
    def dispaly(self, msg='LinkedList: '):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='')
            ptr = ptr.link
        print('None')

    def swap_list(self, head):
        if head is None  or head.link is  None:
            return
        head, head.link = head.link, head

        swap_list(head.link.link)
        return head

s = LinkedList()
s.dispaly('연결리스트(초기): ')
s.insert(0,1)
s.insert(0,2)
s.insert(0,3)
s.insert(0,4)

