# coding=utf-8
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def flat_generator(list_):
	for elem in list_:
		for i in elem:
			yield i


for item in flat_generator(nested_list):
	print(item)