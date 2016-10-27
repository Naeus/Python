from collections import deque
items = deque([1, 2])
print(items)
items.append(3) # deque == [1, 2, 3]
print(items)
print(items.rotate(1)) # The deque is now: [3, 1, 2]
print(items)
print(items.rotate(-1)) # Returns deque to original state: [1, 2, 3]
print(items)
print(items.popleft()) # deque == [2, 3]
