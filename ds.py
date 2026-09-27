# custom data structures library
# implements core data structures from scratch

# ============================================================
# dynamic array implementation
# ============================================================

class ArrayList:
    """a resizable array backed by a python list."""

    def __init__(self):
        # the underlying storage
        self._data = []

    def append(self, value):
        # add element to the end - o(1) amortized
        self._data.append(value)

    def get(self, index):
        # get element at index - o(1)
        if index < 0 or index >= len(self._data):
            raise IndexError("index out of range")
        return self._data[index]

    def set(self, index, value):
        # update element at index - o(1)
        if index < 0 or index >= len(self._data):
            raise IndexError("index out of range")
        self._data[index] = value

    def remove(self, index):
        # remove element at index - o(n) because elements shift
        if index < 0 or index >= len(self._data):
            raise IndexError("index out of range")
        return self._data.pop(index)

    def length(self):
        # return number of elements - o(1)
        return len(self._data)

    def is_empty(self):
        # check if array is empty - o(1)
        return len(self._data) == 0

    def __str__(self):
        # string representation for printing
        return str(self._data)

    def __len__(self):
        # allows use of len() on the object
        return len(self._data)


# ============================================================
# singly linked list implementation
# ============================================================

class Node:
    """a single node in a linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """a singly linked list."""

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        # add element to the end - o(n)
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self._size += 1

    def prepend(self, value):
        # add element to the front - o(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def remove(self, value):
        # remove first occurrence of value - o(n)
        if not self.head:
            return False

        # handle case where head is the one to remove
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        # search through the list
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

    def contains(self, value):
        # check if value exists - o(n)
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        # convert to python list for easy printing
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def length(self):
        # return size of list - o(1)
        return self._size

    def __str__(self):
        return " -> ".join(str(v) for v in self.to_list())


# ============================================================
# stack implementation (lifo - last in first out)
# ============================================================

class Stack:
    """a stack data structure using a list."""

    def __init__(self):
        self._data = []

    def push(self, value):
        # add element to top - o(1)
        self._data.append(value)

    def pop(self):
        # remove and return top element - o(1)
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        # view top element without removing - o(1)
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        # check if stack is empty - o(1)
        return len(self._data) == 0

    def size(self):
        # return number of elements - o(1)
        return len(self._data)

    def __str__(self):
        return str(self._data)


# ============================================================
# queue implementation (fifo - first in first out)
# ============================================================

class Queue:
    """a queue data structure using two stacks for o(1) amortized operations."""

    def __init__(self):
        # in_stack holds new elements, out_stack holds ready-to-dequeue elements
        self._in_stack = []
        self._out_stack = []

    def enqueue(self, value):
        # add element to back of queue - o(1)
        self._in_stack.append(value)

    def dequeue(self):
        # remove and return front element - o(1) amortized
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        # if out_stack is empty, move everything from in_stack
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack.pop()

    def peek(self):
        # view front element without removing - o(1) amortized
        if self.is_empty():
            raise IndexError("peek from empty queue")

        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack[-1]

    def is_empty(self):
        # check if queue is empty - o(1)
        return len(self._in_stack) == 0 and len(self._out_stack) == 0

    def size(self):
        # return total number of elements - o(1)
        return len(self._in_stack) + len(self._out_stack)

    def __str__(self):
        # display in queue order
        all_items = list(reversed(self._in_stack)) + self._out_stack[::-1]
        return str(all_items)


# ============================================================
# hashmap implementation (key-value store)
# ============================================================

class HashMap:
    """a hashmap with separate chaining for collision handling."""

    def __init__(self, capacity=16):
        # start with a small number of buckets
        self._capacity = capacity
        # each bucket holds a list of (key, value) pairs
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _hash(self, key):
        # generate a hash index from the key
        # use python's built-in hash and mod by capacity
        return hash(key) % self._capacity

    def put(self, key, value):
        # add or update a key-value pair - o(1) average
        index = self._hash(key)
        bucket = self._buckets[index]

        # check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # update existing value
                bucket[i] = (key, value)
                return

        # otherwise add new pair
        bucket.append((key, value))
        self._size += 1

        # resize if load factor exceeds 0.75
        if self._size / self._capacity > 0.75:
            self._resize()

    def get(self, key):
        # retrieve value by key - o(1) average
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"key not found: {key}")

    def remove(self, key):
        # remove a key-value pair - o(1) average
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return

        raise KeyError(f"key not found: {key}")

    def contains(self, key):
        # check if key exists - o(1) average
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    def keys(self):
        # return all keys
        all_keys = []
        for bucket in self._buckets:
            for k, v in bucket:
                all_keys.append(k)
        return all_keys

    def values(self):
        # return all values
        all_values = []
        for bucket in self._buckets:
            for k, v in bucket:
                all_values.append(v)
        return all_values

    def _resize(self):
        # double the capacity and rehash all items
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        # reinsert all existing pairs
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)

    def size(self):
        return self._size

    def __str__(self):
        pairs = []
        for bucket in self._buckets:
            for k, v in bucket:
                pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"