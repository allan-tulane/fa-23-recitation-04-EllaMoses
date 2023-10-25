from main import *

import random

# 4 pts
def test_qsort_fixed():
	assert(qsort([5,4,3,2,1], lambda a: a[0])) == [1,2,3,4,5]

	# adding more tests below
	assert(qsort([2,3,4,2,1], lambda a: a[0])) == [1,2,2,3,4]
	assert(qsort([202, 100, 0, -1, 6], lambda a: a[0])) == [-1, 0, 6, 100, 202]
	assert(qsort([], lambda a: a[0])) == []
	assert(qsort([1], lambda a: a[0])) == [1]

# 4 pts
def test_qsort_random():
	assert(qsort([5,4,3,2,1], lambda a: random.choice(a))) == [1,2,3,4,5]

	# adding more tests below
	assert(qsort([2,3,4,2,1], lambda a: a[0])) == [1,2,2,3,4]
	assert(qsort([202, 100, 0, -1, 6], lambda a: a[0])) == [-1, 0, 6, 100, 202]
	assert(qsort([], lambda a: a[0])) == []
	assert(qsort([1], lambda a: a[0])) == [1]
