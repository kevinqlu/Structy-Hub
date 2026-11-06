# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def breadth_first_values(root):
  if root is None:
    return []

  values = []

  queue = deque([root.val])

  while queue:
    node = queue.popleft()

    values.append(node)

    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)
      
  return values 