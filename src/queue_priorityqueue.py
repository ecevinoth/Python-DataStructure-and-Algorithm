"""
Topic : Queue - Priority Queue implementation
Date : 2019/12/26
Author : ecevinoth
"""

# 1. Using `list`
customers = []

customers.append((2, "Harry"))  # item1 name with priority
customers.append((3, "Charles"))
customers.sort(reverse=True)

customers.append((1, "Riya"))
customers.sort(reverse=True)

customers.append((4, "Stacy"))
customers.sort(reverse=True)

print("using list method")
while customers:
    # pop items from from
    print(customers.pop(0))


# 2. Using `heapq`
import heapq

customers = []

# by default heapq only has min heap. but there are ways tto use as a max heap.
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))

print("using heapq method")
while customers:
    print(heapq.heappop(customers))


# 3. Using `queue.PriorityQueue`
from queue import PriorityQueue

customers = PriorityQueue()

customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))

print("using PriorityQueue() class")
for i in range(customers.qsize()):
    print(customers.get())
