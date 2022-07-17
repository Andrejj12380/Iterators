# coding=utf-8
from itertools import chain

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], ]


class FlatIterator(list):

	def __init__(self, list_):
		super().__init__()
		self.list = list_
		self.it = iter(list_)

	def __iter__(self):
		return self

	def __next__(self):
		next_ = next(self.it)
		if isinstance(next_, list):
			self.it = chain(self.it, next_[:])
			return next(self)
		return next_


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)