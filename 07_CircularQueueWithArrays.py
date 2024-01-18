class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [-1] * capacity
        self.head = self.tail = 0

    def is_empty(self) -> bool:
        return self.tail == self.head

    def is_full(self) -> bool:
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, data: int) -> bool:
        if self.is_full():
            return False
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            return -1
        
        elem = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        return elem

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.head]

# create a new circular queue with capacity 5
cq = CircularQueue(5)

# enqueue some elements
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)

# print the front and rear of the queue
print("front:", cq.front())

# dequeue some elements
print("dequeued:", cq.dequeue())
print("dequeued:", cq.dequeue())

# print the front and rear of the queue
print("front:", cq.front())

# enqueue some more elements
cq.enqueue(5)
cq.enqueue(6)
cq.enqueue(7)

# print the front and rear of the queue
print("front:", cq.front())

# dequeue all elements
print("dequeued:", cq.dequeue())
print("dequeued:", cq.dequeue())
print("dequeued:", cq.dequeue())
print("dequeued:", cq.dequeue())

# print the front and rear of the queue
print("front:", cq.front())
