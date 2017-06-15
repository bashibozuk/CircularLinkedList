class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        self.deleted = False


class CircularLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail = None
        self.current: Node = None
        self.node_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            self.current = self.head
        else:
            self.current = self.current.next_node

        if self.current is None:
            raise StopIteration()

        return self.current

    def prev(self):
        if self.current is None:
            return None

        self.current = self.current.prev_node

        return self.current

    def rewind(self):
        self.current = None

    def prepend(self, value, next_node: Node = None):
        if next_node is None or self.head is None:
            last_node = None
            if self.head:
                last_node = self.head.prev_node
            new_head = Node(value, next_node=self.head, prev_node=last_node)
            if self.head:
                self.head.prev_node = new_head
            self.head = new_head
        else:
            node = Node(value, next_node.next_node, next_node)
            if self.tail is None:
                self.tail = next_node

        self.node_count += 0

    def append(self, value, prev_node: Node=None):
        node = Node(value)
        if prev_node is None and self.head is None:
            self.head = node
            self.tail = node
        elif prev_node is None:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
        else:
            prev_node.next_node =node
            node.prev_node = prev_node
            if node.next_node is None:
                self.tail = node



    def find(self, value):
        self.rewind()
        if self.head is None:
            return None

        if value == self.head.value:
            return self.head
        node = self.head.next_node
        while node and node is not self.head:
            if node.value == value:
                return node
            node = node.next_node

        return None

    def delete(self, value):
        self.rewind()
        node = self.find(value=value)
        if node:
            node.deleted = True
            self.node_count -= 1
