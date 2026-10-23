# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):
  if root is None: return -1 

  left_high = how_high(root.left)
  right_high = how_high(root.right)

  return 1 + max(left_high, right_high)