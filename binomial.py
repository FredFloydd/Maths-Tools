from time import sleep
from math import factorial

def ncr(n, r):
	nfac = factorial(n)
	rfac  = factorial(r)
	nrfac = factorial(n - r)
	return int(nfac / (rfac * nrfac))

print()
print('(a + bx)^c')
print()
print('Tnsert values for a, b and c:')
print()
a = float(input('a: '))
b = float(input('b: '))
c = int(input('c: '))

series = []
coefficients = []
for n in range(c + 1):
	coefficients.append(ncr(c, n))
	coefficients[n] = coefficients[n] * (b ** n)
	coefficients[n] = coefficients[n] * (a ** (c-n))
	series.append(str(coefficients[n]) + 'x^%d' %(n))

print()
print(' + '.join(series))
