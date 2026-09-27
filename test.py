# unit tests for algorithm solutions

import unittest
from algo_prac_sol import (
    linear_search, binary_search,
    bubble_sort, merge_sort, quick_sort,
    factorial, fibonacci, fibonacci_memo,
    reverse_string, is_palindrome, two_sum,
    find_max, remove_duplicates, fizzbuzz,
    TreeNode, inorder_traversal, preorder_traversal,
    postorder_traversal, tree_height,
    bfs, dfs, has_path
)


class TestSearching(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(linear_search([1, 2, 3, 4], 99), -1)

    def test_binary_search(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search(arr, 7), 3)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 99), -1)


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(bubble_sort([]), [])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(merge_sort([3, 3, 3]), [3, 3, 3])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(quick_sort([10]), [10])


class TestRecursion(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_memo(self):
        # 40 would take forever without memoization
        self.assertEqual(fibonacci_memo(40), 102334155)


class TestArraysStrings(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("a man a plan a canal panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_two_sum(self):
        result = two_sum([2, 7, 11, 15], 9)
        self.assertEqual(sorted(result), [0, 1])

    def test_find_max(self):
        self.assertEqual(find_max([3, 1, 4, 1, 5, 9]), 9)
        self.assertIsNone(find_max([]))

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 1, 4]), [1, 2, 3, 4])

    def test_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result[2], "fizz")       # 3
        self.assertEqual(result[4], "buzz")       # 5
        self.assertEqual(result[14], "fizzbuzz")  # 15


class TestTrees(unittest.TestCase):

    def setUp(self):
        # build a test tree:
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)

    def test_inorder(self):
        self.assertEqual(inorder_traversal(self.root), [4, 2, 5, 1, 3])

    def test_preorder(self):
        self.assertEqual(preorder_traversal(self.root), [1, 2, 4, 5, 3])

    def test_postorder(self):
        self.assertEqual(postorder_traversal(self.root), [4, 5, 2, 3, 1])

    def test_tree_height(self):
        self.assertEqual(tree_height(self.root), 3)
        self.assertEqual(tree_height(None), 0)


class TestGraphs(unittest.TestCase):

    def setUp(self):
        # build a simple graph
        self.graph = {
            "a": ["b", "c"],
            "b": ["d"],
            "c": ["d"],
            "d": ["e"],
            "e": []
        }

    def test_bfs(self):
        result = bfs(self.graph, "a")
        self.assertEqual(result[0], "a")
        self.assertIn("e", result)

    def test_dfs(self):
        result = dfs(self.graph, "a")
        self.assertEqual(result[0], "a")
        self.assertIn("e", result)

    def test_has_path(self):
        self.assertTrue(has_path(self.graph, "a", "e"))
        self.assertFalse(has_path(self.graph, "e", "a"))


if __name__ == "__main__":
    unittest.main(verbosity=2)