class ArrayQueue:
    """
    FIFO(First-In, First-Out) 원칙을 따르는 큐 자료구조 클래스.
    Python의 기본 list를 사용하여 구현합니다.
    """

    def __init__(self):
        """새로운 빈 큐를 초기화합니다."""
        self.items = []

    def enqueue(self, item):
        """
        큐의 맨 뒤(rear)에 데이터를 추가합니다. (삽입)
        list.append()는 효율적인 연산입니다. (O(1))
        :param item: 큐에 추가할 데이터
        """
        self.items.append(item)

    def dequeue(self):
        """
        큐의 맨 앞(front)에서 데이터를 제거하고 반환합니다. (삭제)
        list.pop(0)는 매우 비효율적인 연산입니다. (O(n))
        :return: 큐의 맨 앞에 있던 데이터 또는 None
        """
        if self.is_empty():
            print("오류: 큐가 비어있습니다.")
            return None
        return self.items.pop(0)

    def peek(self):
        """
        큐의 맨 앞 데이터를 제거하지 않고 확인합니다.
        :return: 큐의 맨 앞에 있는 데이터 또는 None
        """
        if self.is_empty():
            print("오류: 큐가 비어있습니다.")
            return None
        return self.items[0]

    def is_empty(self):
        """
        큐가 비어있는지 여부를 확인합니다.
        :return: 큐가 비어있으면 True, 아니면 False
        """
        return len(self.items) == 0

    def size(self):
        """
        큐에 들어있는 데이터의 개수를 반환합니다.
        :return: 큐의 크기 (정수)
        """
        return len(self.items)


class BTNode:
    def __init__(self,elem, left=None, right=None):
        self.data = elem
        self.left= left
        self.right = right


def preorder(n):
    if n is not None:
        print(n.data, end='')
        preorder(n.left)
        preorder(n.right)
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end='')
def levelorder(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end='')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right)+1

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft +1
    else: return  hRight+1


d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f= BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A', b, c)

print('\n In-Order : ', end=''); inorder(root)
print('\n Pre-Order : ', end=''); preorder(root)
print('\n Post-Order : ', end=''); postorder(root)
print('\n Level-Order : ', end=''); levelorder(root)
print()

print("노드 개수 = %d개" % count_node(root))
print("트리 높이 = %d" % count_node(root))









