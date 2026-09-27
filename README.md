# custom data structures library

a python library implementing core data structures from scratch to understand how they work under the hood. includes unit tests for each structure.

## structures implemented
- arraylist (dynamic array)
- linkedlist (singly linked)
- stack (lifo)
- queue (fifo)
- hashmap (key-value store with collision handling)

## time complexity reference
| structure | access | search | insert | delete |
|-----------|--------|--------|--------|--------|
| arraylist | o(1)   | o(n)   | o(1)*  | o(n)   |
| linkedlist| o(n)   | o(n)   | o(1)** | o(1)** |
| stack     | o(n)   | o(n)   | o(1)   | o(1)   |
| queue     | o(n)   | o(n)   | o(1)   | o(1)   |
| hashmap   | -      | o(1)*  | o(1)*  | o(1)*  |

\* amortized
\** if pointer to node is known

## how to run tests
1. ensure python 3 is installed
2. open terminal in this folder
3. run: python test_data_structures.py

## technologies used
- python 3
- unittest (built-in testing framework)