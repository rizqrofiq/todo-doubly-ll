from .node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next_node
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev_node

        return temp

    def set_value(self, index, data):
        temp = self.get(index)
        if temp:
            temp.data = data
            return True

        return False

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            temp.prev_node = None

        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
            temp.next_node = None

        self.length -= 1
        return temp

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        temp = pre.next_node
        pre.next_node = temp.next_node
        temp.next_node = None

        self.length -= 1
        return temp
