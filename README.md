# Python-DataStructure-and-Algorithm

# Python Tips and Tricks
Different ways to test multiple flags at once
Q : Different ways to test multiple logical condition at once

How to sort a Python dict by value with single line expression
input : dict = {'a': 99, 'b': 0, 'c': 101, 'd': 10, 'e': -1}
expected output :
[('e', -1), ('b', 0), ('d', 10), ('a', 99), ('c', 101)]

python_tipsandtricks_merge_two_dict.py
Merging two dicts with a single expression
Given dictionary:
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
expected output:
>>> z
{'c': 4, 'a': 1, 'b': 3}

# Linked List
linkedlist_nth_to_lastnode.py
Q: find the nth element from last node of a given linked list. 
If nth value is greater than given linked list then through back LookupError.

__LinkedList_CycleCheck.py__
Q: check for cycle in give given linked list if exist return True else False.
  - 1 --> 2 --> 3 --> 1
  - True
  - 1 --> 2 --> 3 --> None
  - False

# Recursion
how to visualize recursion:
here is the diagram for factorical of 5!

![Factorial viz diagram](https://github.com/ecevinoth/Python-DataStructure-and-Algorithm/blob/master/recursion_viz_factorial.png)

__recursion_factorial.py__
Q: find the factorial for given integer

__recursion_cumulative_sum.py__
Q: find the sum of n.
Ex: given input : 4
return : 4 + 3 + 2 + 1

__recursion_word_split_problem.py__
Q: Determine if it is possible to split the given string in a way in which words can be made from the list of words.
Ex: given sting "iLoveIndia" and list of word ["i", "India", "Love"] then your function has to return True else False.

# Queue : Priority Queue
[__queue_priorityqueue.py__]()
Short intro : A priority queue is an abstract data structure ( a data type defined by its behaviour) is like a normal queue but each item has special *key* to quantify its priority.
Ex: Airlines that give luggage on conveyer belt based on the status/ticket class of the passengers. Baggage tagged with *priority/business/first-class* usally arrives earlier than other non-tagged baggage.

implementation of priority queue
1. Using `list`
    - It takes ++O(n log n)++ time to maintain the order when an item is added to the list.
    - Efficient when we have to make very few insertions.
2. Using `heapq`
    - It takes ++O(log n)++ time for insertion and extraction of the smallest element.
    - Suitable for all the case.
3. Using `queue.PriorityQueue`
    - It takes ++O(log n)++, internally use same heapq implementation.
    - It is synchronized - So it supports concurrent process
    - It is `class` interface instead of `function`. Thus, `PriorityQueue` is the classic OOP style of implementing and using Priority Queue.
