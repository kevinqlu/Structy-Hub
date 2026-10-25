# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  leaves = []
  _leaf_list(root, leaves)
  return leaves

def _leaf_list(root, leaves):
  if root is None:
    return 

  if root.left is None and root.right is None:
    leaves.append(root.val)

  _leaf_list(root.left, leaves)
  _leaf_list(root.right, leaves)
