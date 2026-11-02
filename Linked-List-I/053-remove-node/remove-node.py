# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    
