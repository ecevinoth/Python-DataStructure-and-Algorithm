# Python-DataStructure-and-Algorithm

# Python Tips and Tricks
## Different ways to test multiple flags at once
Q : Different ways to test multiple logical condition at once

## How to sort a Python dict by value with single line expression
__expected output :__ dict = {'a': 99, 'b': 0, 'c': 101, 'd': 10, 'e': -1}
__expected output :__ 
[('e', -1), ('b', 0), ('d', 10), ('a', 99), ('c', 101)]

## python_tipsandtricks_merge_two_dict.py
Merging two dicts with a single expression
__Given dictionary:__
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
__expected output :__
>>> z
{'c': 4, 'a': 1, 'b': 3}

# Linked List
## linkedlist_nth_to_lastnode.py
__Q:__ find the nth element from last node of a given linked list. 
If nth value is greater than given linked list then through back LookupError.

## LinkedList_CycleCheck.py
__Q:__ check for cycle in give given linked list if exist return True else False.
  - 1 --> 2 --> 3 --> 1
  - __True__
  - 1 --> 2 --> 3 --> None
  - __False__

# Recursion
how to visualize recursion:
here is the diagram for factorical of 5!

![Factorial viz diagram](https://github.com/ecevinoth/Python-DataStructure-and-Algorithm/blob/master/recursion_viz_factorial.png)

## recursion_factorial.py
__Q:__ find the factorial for given integer

## recursion_cumulative_sum.py
__Q:__ find the sum of n.
__Ex:__ given input : __4__
return : __4 + 3 + 2 + 1__

## recursion_word_split_problem.py
__Q:__ Determine if it is possible to split the given string in a way in which words can be made from the list of words.
__Ex:__ given sting "iLoveIndia" and list of word ["i", "India", "Love"] then your function has to return True else False.
