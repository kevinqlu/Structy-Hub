# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  curr = head 
  prev = None

  while curr:
    if head.val == curr.val:
      return True
    curr = curr.next
  return False
