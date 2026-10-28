# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  if root is None:
    return []

  stack = [root] 

  while stack: 
    node = stack.pop()

    if node.right is not None:
      stack.append(node.right)

    if node.left is not None:
      stack.append(node.left)

  return stack
