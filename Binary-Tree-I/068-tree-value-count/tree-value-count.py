# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def tree_value_count(root, target):

  if root is None:
    return 0 

  count = 0

  queue = deque([root])

  while queue:
    node = queue.popleft()

    if root.val == target:
      count += 1

    if node.left is not None:
      queue.append(node.left)

    if node.right is not None:
      queue.append(node.right)

  return count
