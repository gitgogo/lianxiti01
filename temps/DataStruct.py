# 单向链表
class Node:
	def __init__(self, item):
		self.item = item
		self.next = None


class SingleList:
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head is None

	def add(self, item):
		node = Node(item)
		node.next = self._head
		self._head = node

	def items(self):
		cur = self._head
		while cur is not None:
			yield cur.item
			cur = cur.next

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next is not None:
				cur = cur.next
			cur.next = node

	def length(self):
		if self.is_empty():
			return 0
		else:
			cur = self._head
			count = 0
			while cur is not None:
				count += 1
				cur = cur.next
		return count

	def insert(self, index, item):
		if index <= 0:
			self.add(item)
		elif index >= self.length() -1:
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			for i in range(index-1):
				cur = cur.next
			node.next = cur.next
			cur.next = node

	def remove(self, item):
		cur = self._head
		if cur.item == item:
			self._head = cur.next
			return 1
		while cur.next is not None:
			if cur.next.item == item:
				if cur.next.next is not None:
					cur.next = cur.next.next
					return 1
				else:
					cur.next = None
					return 1
			else:
				cur = cur.next
		else:
			return -1

	def find(self, item):
		cur = self._head
		count = 0
		while cur is not None:
			if cur.item == item:
				break
			else:
				count += 1
		return count


# 堆数据结构-完全二叉树结构；二叉树遍历



if __name__ == '__main__':
	single_list = SingleList()
	single_list.add(Node(2))
