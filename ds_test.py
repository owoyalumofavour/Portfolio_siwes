# unit tests for the custom data structures library

import unittest
from ds import ArrayList, LinkedList, Stack, Queue, HashMap


class TestArrayList(unittest.TestCase):

    def test_append_and_get(self):
        arr = ArrayList()
        arr.append(10)
        arr.append(20)
        arr.append(30)

        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)
        self.assertEqual(arr.get(2), 30)

    def test_length(self):
        arr = ArrayList()
        self.assertEqual(arr.length(), 0)

        arr.append(1)
        arr.append(2)
        self.assertEqual(arr.length(), 2)

    def test_remove(self):
        arr = ArrayList()
        arr.append(1)
        arr.append(2)
        arr.append(3)

        arr.remove(1)
        self.assertEqual(arr.length(), 2)
        self.assertEqual(arr.get(1), 3)

    def test_out_of_range(self):
        arr = ArrayList()
        arr.append(1)

        with self.assertRaises(IndexError):
            arr.get(5)

    def test_is_empty(self):
        arr = ArrayList()
        self.assertTrue(arr.is_empty())
        arr.append(1)
        self.assertFalse(arr.is_empty())


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        lst.append(3)

        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.length(), 3)

    def test_prepend(self):
        lst = LinkedList()
        lst.append(2)
        lst.prepend(1)
        lst.prepend(0)

        self.assertEqual(lst.to_list(), [0, 1, 2])

    def test_remove(self):
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        lst.append(3)

        result = lst.remove(2)
        self.assertTrue(result)
        self.assertEqual(lst.to_list(), [1, 3])

    def test_remove_missing(self):
        lst = LinkedList()
        lst.append(1)

        result = lst.remove(99)
        self.assertFalse(result)

    def test_contains(self):
        lst = LinkedList()
        lst.append(1)
        lst.append(2)

        self.assertTrue(lst.contains(2))
        self.assertFalse(lst.contains(99))


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # lifo - last in first out
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_peek(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.size(), 2)

    def test_pop_empty(self):
        stack = Stack()

        with self.assertRaises(IndexError):
            stack.pop()

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # fifo - first in first out
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_peek(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.size(), 2)

    def test_dequeue_empty(self):
        queue = Queue()

        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)


class TestHashMap(unittest.TestCase):

    def test_put_and_get(self):
        hm = HashMap()
        hm.put("name", "favour")
        hm.put("age", 21)

        self.assertEqual(hm.get("name"), "favour")
        self.assertEqual(hm.get("age"), 21)

    def test_update_existing(self):
        hm = HashMap()
        hm.put("score", 10)
        hm.put("score", 20)

        self.assertEqual(hm.get("score"), 20)
        self.assertEqual(hm.size(), 1)

    def test_remove(self):
        hm = HashMap()
        hm.put("a", 1)
        hm.put("b", 2)

        hm.remove("a")
        self.assertFalse(hm.contains("a"))
        self.assertTrue(hm.contains("b"))

    def test_missing_key(self):
        hm = HashMap()

        with self.assertRaises(KeyError):
            hm.get("nothing")

    def test_keys_and_values(self):
        hm = HashMap()
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)

        self.assertEqual(sorted(hm.keys()), ["a", "b", "c"])
        self.assertEqual(sorted(hm.values()), [1, 2, 3])

    def test_collision_handling(self):
        # small capacity forces collisions
        hm = HashMap(capacity=2)
        hm.put("a", 1)
        hm.put("b", 2)
        hm.put("c", 3)
        hm.put("d", 4)

        # all should still be retrievable
        self.assertEqual(hm.get("a"), 1)
        self.assertEqual(hm.get("b"), 2)
        self.assertEqual(hm.get("c"), 3)
        self.assertEqual(hm.get("d"), 4)


# run all tests when file is executed directly
if __name__ == "__main__":
    unittest.main(verbosity=2)