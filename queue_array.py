# Queue ADT - circular array implementation

class Queue:
    """Implements an efficient first-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity, init_items=None):
        """Creates a queue with a capacity and initializes with init_items"""
        self.capacity= capacity         # capacity of queue
        self.items = [None]*capacity    # array for queue
        self.num_items = 0              # number of items in queue
        self.front = 0                  # front index of queue (items removed from front)
        self.rear = 0                   # rear index of queue (items enter at rear)
        if init_items is not None:      # if init_items is not None, initialize queue
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items
                self.rear = self.num_items % self.capacity # % capacity addresses length=capacity

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.capacity == other.capacity
            and self.get_items() == other.get_items()
            )

    def __repr__(self):
        return ("Queue({!r}, {!r})".format(self.capacity, self.get_items()))

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self):
        if self.num_items == 0:
            return []
        if self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]

    def is_empty(self):
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        """Returns true if the queue is full and false otherwise
        Must be O(1)"""
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        """enqueues item, raises IndexError if Queue is full
        Must be O(1)"""
        if self.num_items == self.capacity:
            raise IndexError
        else:
            self.items[self.rear % self.capacity] = item
            self.num_items += 1
            self.rear += 1

    def dequeue(self):
        """dequeues item, raises IndexError is Queue is empty
        Must be O(1)"""
        if self.num_items == 0:
            raise IndexError
        else:
            value = self.items[self.front % self.capacity]
            self.front += 1
            self.num_items -= 1
            return value

    def size(self):
        """Returns the number of items in the queue
        Must be O(1)"""
        return self.num_items

if __name__ == "__main__":
    q1 = Queue(10)
    print(q1)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print(q1)
    q2 = Queue(10)
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q1==q2)
    print(q2.dequeue())
    print(q2)
    print(q1 == q2)
    print(q2.dequeue())
    print(q2.dequeue())
    q2.enqueue(4)
    q2.enqueue(5)
    q2.enqueue(6)
    q2.enqueue(7)
    q2.enqueue(8)
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q2.items)
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.dequeue())
    print(q2.items,q2.front,q2.rear,q2.get_items())
    print(q2)
    print(q2==q1)
