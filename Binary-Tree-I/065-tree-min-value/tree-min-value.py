# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  stack = [root]
  smallest = float('inf')

  while stack:
    node = stack.pop()

    if node.val < smallest:
      smallest = node.val 

    if node.right is not None:
      stack.append(node.right)
    if node.right is not None:
      stack.append(node.right)
      