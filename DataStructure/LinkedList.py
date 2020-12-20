class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表节点范围")
        p: Node = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index: int):
        if index < 0 or index > self.size:
            raise Exception("超出链表节点范围")
        node = Node(data)
        if self.size == 0:
            # 空链表
            self.head = node
            self.last = node
        elif index == 0:
            # 插入头部
            node.next = self.head
            self.head = node
        elif self.size == index:
            # 插入尾部
            self.last.next = node
            self.last = node
        else:
            # 插入中间
            prev_node = self.get(index - 1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def update(self, data, index: int):
        if index < 0 or index > self.size:
            raise Exception("超出链表节点范围")
        p: Node = self.head
        for i in range(index):
            p = p.next
        p.data = data

    def remove(self, index: int):
        if index < 0 or index > self.size:
            raise Exception("超出链表节点范围")
        if index == 0:
            # 删除头节点
            removed_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            # 删除尾节点
            prev_node = self.get(index - 1)
            removed_node = prev_node.next
            prev_node.next = None
            self.last = prev_node
        else:
            # 删除中间节点
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            removed_node = prev_node.next
            prev_node.next = next_node
        self.size -= 1
        return removed_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(9, -1, -1):
        linked_list.insert(i, 0)
    linked_list.insert(10, 5)
    linked_list.update("A", 7)
    linked_list.remove(0)
    linked_list.remove(3)
    linked_list.output()

