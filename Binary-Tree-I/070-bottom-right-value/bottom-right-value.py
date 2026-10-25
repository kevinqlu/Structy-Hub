# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def bottom_right_value(root):
  queue = deque([root])
  node = None

  while queue:
    node = queue.popleft()

    if node.left is not None:
      queue.append(node.left)

    if node.right is not None:
      queue.append(node.right)

  return 