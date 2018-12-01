from time import sleep
from math import factorial

def ncr(n, r):
	nfac = factorial(n)
	rfac  = factorial(r)
	nrfac = factorial(n - r)
	return nfac / (rfac * nrfac)

triangle = range(int(input('How many rows do you want? ')))

for row in range(len(triangle)):
	series = []
	for r in range(row + 1):
		series.append(str(int(ncr(row, r))))
	print(' '.join(series))


