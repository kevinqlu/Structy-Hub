# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  current = head
  values = []

  while current:
    values.append(head.val)
    current = current.next
  return values