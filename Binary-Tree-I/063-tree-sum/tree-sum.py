# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def tree_sum(root):
  if root is None:
    return 0

  queue = deque([root])
  total = 0

  while queue:
    node = queue.popleft()
    