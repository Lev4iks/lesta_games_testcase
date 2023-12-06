class CircularBufferList:
    """First realization"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, value):
        if len(self.buffer) < self.capacity:
            self.buffer.append(value)
        else:
            self.buffer = self.buffer[1:] + [value]

    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.pop(0)


class CircularBufferArray:
    """Second realization"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = self.tail = self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            self.dequeue()
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size = max(self.size - 1, 0)
        return value


class CircularBufferLinkedList:
    """Third realization"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            return None
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
