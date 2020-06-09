"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class Node():
	def __init__(self,val):
		self.val = val
		self.next = None
class Linked_list():
	def __init__(self):
		self.head = None
	def add(self,val):
		new_node = Node(val)
		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node
	def display(self):
		result = []
		current = self.head
		while current:
			result.append(str(current.val))
			current = current.next
		return '->'.join(result)
	def reverse(self):
		current = self.head
		prev = None
		while current:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node
		self.head = prev
	def reverse_recursive(self,head):
		if not head or not head.next:
			return head
		p = self.reverse_recursive(head.next)
		head.next.next = head
		head.next = None
		self.head = p
		return p

obj=Linked_list()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
print(obj.display())
obj.reverse_recursive(obj.head)
print(obj.display())
obj.reverse()
print(obj.display())