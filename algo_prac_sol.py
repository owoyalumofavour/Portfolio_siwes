# algorithm solutions repository
# each function includes time and space complexity in its docstring


# ============================================================
# searching algorithms
# ============================================================

def linear_search(arr, target):
    """
    search through a list one by one.
    time: o(n)
    space: o(1)
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search(arr, target):
    """
    search a sorted list by halving the range.
    time: o(log n)
    space: o(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # find middle index
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # target is in the right half
            left = mid + 1
        else:
            # target is in the left half
            right = mid - 1

    return -1


# ============================================================
# sorting algorithms
# ============================================================

def bubble_sort(arr):
    """
    repeatedly swap adjacent elements that are out of order.
    time: o(n^2)
    space: o(1)
    """
    n = len(arr)
    # make a copy so we don't modify the original
    result = arr.copy()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # if no swaps happened, the list is already sorted
        if not swapped:
            break

    return result


def merge_sort(arr):
    """
    divide the list in half, sort each half, then merge them.
    time: o(n log n)
    space: o(n)
    """
    # base case: list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # split the list in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    helper for merge_sort. merges two sorted lists into one.
    time: o(n)
    space: o(n)
    """
    result = []
    i = j = 0

    # compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    """
    pick a pivot and partition the list around it.
    time: o(n log n) average, o(n^2) worst
    space: o(log n) for recursion
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# ============================================================
# recursion problems
# ============================================================

def factorial(n):
    """
    calculate n! using recursion.
    time: o(n)
    space: o(n) for call stack
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    calculate the nth fibonacci number.
    time: o(2^n) - very slow for large n
    space: o(n) for call stack
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo=None):
    """
    fibonacci with memoization - much faster.
    time: o(n)
    space: o(n)
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# ============================================================
# array and string problems
# ============================================================

def reverse_string(s):
    """
    reverse a string using two pointers.
    time: o(n)
    space: o(n)
    """
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


def is_palindrome(s):
    """
    check if a string reads the same forwards and backwards.
    time: o(n)
    space: o(1)
    """
    # clean the string - remove spaces and lowercase
    cleaned = "".join(c.lower() for c in s if c.isalnum())

    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def two_sum(nums, target):
    """
    find two numbers that add up to target. returns their indices.
    time: o(n)
    space: o(n)
    """
    seen = {}

    for i, num in enumerate(nums):
        # calculate what number we need to find
        complement = target - num

        # if we've already seen it, we found the answer
        if complement in seen:
            return [seen[complement], i]

        # otherwise store this number
        seen[num] = i

    return []


def find_max(arr):
    """
    find the largest number in a list.
    time: o(n)
    space: o(1)
    """
    if not arr:
        return None

    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num

    return max_val


def remove_duplicates(arr):
    """
    remove duplicates from a list while keeping order.
    time: o(n)
    space: o(n)
    """
    seen = set()
    result = []

    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def fizzbuzz(n):
    """
    classic fizzbuzz problem. returns a list of strings.
    time: o(n)
    space: o(n)
    """
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))

    return result


# ============================================================
# tree problems
# ============================================================

class TreeNode:
    """a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    """
    visit left, then root, then right.
    time: o(n)
    space: o(n)
    """
    if not root:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


def preorder_traversal(root):
    """
    visit root, then left, then right.
    time: o(n)
    space: o(n)
    """
    if not root:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)


def postorder_traversal(root):
    """
    visit left, then right, then root.
    time: o(n)
    space: o(n)
    """
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]


def tree_height(root):
    """
    calculate the height of a binary tree.
    time: o(n)
    space: o(n)
    """
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


# ============================================================
# graph problems
# ============================================================

def bfs(graph, start):
    """
    breadth-first search. visits neighbors level by level.
    time: o(v + e) where v = vertices, e = edges
    space: o(v)
    """
    visited = set()
    queue = [start]
    order = []

    while queue:
        # take from the front of the queue
        node = queue.pop(0)

        if node not in visited:
            visited.add(node)
            order.append(node)

            # add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return order


def dfs(graph, start, visited=None):
    """
    depth-first search. explores as deep as possible before backtracking.
    time: o(v + e)
    space: o(v)
    """
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


def has_path(graph, start, end):
    """
    check if a path exists between two nodes.
    time: o(v + e)
    space: o(v)
    """
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node == end:
            return True

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append(neighbor)

    return False