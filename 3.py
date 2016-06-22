# intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
# intervals = [[1, 3], [3, 6]]
intervals = [[1, 7], [3, 6], [20, 23], [8, 18], [10, 12], [9, 10]]


def answer(intervals):
	intervals = merge(intervals)
	total = 0
	for interval in intervals:
		total += (interval[1] - interval[0])
	return total


def merge(i):
	i.sort()
	for ix, val in enumerate(i):
		pix = ix - 1
		if len(i) > 1:
			if max(i[ix][0], i[pix][0]) <= min(i[ix][1], i[pix][1]):
				i[ix] = [min(i[ix][0], i[pix][0]), max(i[ix][1], i[pix][1])]
				del i[pix]
				i = merge(i)
	return i
