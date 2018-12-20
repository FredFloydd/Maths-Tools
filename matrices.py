import random
import time
from copy import deepcopy

library = {}

def print_matrix(mat):
	matrix = library[str(mat)]
	name = mat
	if len(matrix) <= 20 and len(matrix[0]) <= 20:
		for x in matrix:
			printable = []
			for n in range(len(matrix[x])):
				printable.append(str(round(matrix[x][n],2)))
			for n in range(len(printable)):
				if len(printable[n]) == 3:
					printable[n] = ' ' + printable[n]
			print('  '.join(printable))
	else:
		print(name + ' is too big to print')
	print()

def add():
	A = library[input('First Matrix: ')]
	B = library[input('Second Matrix: ')]
	if len(A) == len(B) and len(A[0]) == len(B[0]):
		name = input('Name the new matrix: ')
		new = {}
		for x in range(len(A.keys())):
			line = []
			for y in range(len(A[x])):
				line.append(A[x][y] + B[x][y])
			new[x] = line
		library[name] = new
		print()
		print(name + ' =')
		print()
		print_matrix(name)
	else:
		print()
		print('Matrices are not compatible')
		print()

def multiply():
	A = library[input('First Matrix: ')]
	B = library[input('Second Matrix: ')]
	if len(A[0]) == len(B):
		name = input('Name the new matrix: ')
		new = {}
		for row in range(len(A)):
			new[row] = []
			for column in range(len(B[0])):
				new[row].append(0)
		for iteration in range(len(A[0])):
			for x in range(len(new)):
				for y in range(len(new[0])):
					new[x][y] += A[x][iteration] * B[iteration][y]
		library[name] = new
		print()
		print(name + ' =')
		print()
		print_matrix(name)
	else:
		print('Matrices are not compatible')

def create_matrix():
	name = input('Name your matrix: ')
	matrix_name = str(name)
	name = {}
	rows = int(input('How many rows: '))
	col = int(input('How many columns: '))
	for n in range(rows):
		line = []
		for x in range(col):
			value = input('Value: ')
			if float(value) % 1 == 0:
				line.append(int(value))
			else:
				line.append(float(value))
		name[n] = line
	library[matrix_name] = name
	print()
	print(matrix_name + ' =')
	print()
	print_matrix(matrix_name)
	print()

def det_value(mat):
	if len(mat) != len(mat[0]):
		print('Matrix not square')
	else:
		if len(mat) == 2:
			return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
		else:
			lis = []
			first = mat[0]
			for x in range(len(mat[0])):
				minor = {}
				lis.append(first[x])
				for y in range(1, len(mat)):
					minor[y-1] = []
					for z in range(len(mat[0])):
						if z != x:
							minor[y-1].append(mat[y][z])
				first[x] *= (det_value(minor))
			determinant = 0
			for n in range(len(first)):
				determinant += ((-1) ** n) * (float(first[n]))
				mat[0][n] = lis[n]
			return determinant

def det():
	name = input('Matrix: ')
	mat = library[name]
	det = det_value(mat)
	print()
	print('Det ' + name + ' = ' + str(det))
	print()
	
def rand():
	mat = {}
	arr = []
	name = input('Name of Matrix: ')
	rows = int(input('Rows: '))
	col = int(input('Columns: '))
	for i in range(rows*col):
		arr.append(1 + random.randint(0,10)/10)
	for n in range(rows):
		mat[n] = arr[col*n:(col*n+col)]
	library[name] = mat
	print()
	print(name + ' =')
	print()
	print_matrix(name)

def fastdet_value(mat):
	copy = deepcopy(mat)
	det = 1
	for n in range(len((mat))-1):
		if copy[n][n] == 0:
			det = 0
		else:
			for row in range(n, len(copy) - 1):
				factor = copy[row + 1][n] / copy[n][n]
				for x in range(n, len(copy)):
					copy[row+1][x] -= factor * copy[n][x]
	for x in range(len(copy)):
		det *= copy[x][x]
	return det

def fastdet():
	name = input('Matrix: ')
	mat = library[name]
	print()
	print('Det ' + name + ' = ' + str(fastdet_value(mat)))
	print()

def inverse():
	name = input('Which Matrix: ')
	mat = library[name]
	count = 0
	if count == 0:
		matcopy = mat
		count +=1
	if count == 1:	
		if fastdet_value(matcopy) != 0:
			newname = input('Name the new matrix: ')
			multiplier = 1 / fastdet_value(matcopy)
			minormat = {}
			for r in range(len(mat)):
				row = []
				for c in range(len(mat)):
					minor = {}
					for n in range(len(mat)):
						if n < r:
							minor[n] = mat[n][:c] + mat[n][(c+1):]
						if n > r: 
							minor[n-1] = mat[n][:c] + mat[n][(c+1):]
					row.append(((-1) ** r) * ((-1) ** c) * fastdet_value(minor))
				minormat[r] = row
			new = {}
			for n in range(len(mat)):
				new[n] = []
				for m in range(len(mat)):
					new[n].append(minormat[m][n] * multiplier)
			library[newname] = new
			print()
			print(newname + ' =')
			print()
			print_matrix(newname)

def start():
	print('Welcome to the linear algebra toolbox')
	start = True
	while start == True:
		print('What would you like to do?')
		print('C to create, A to add, P to print, M to Multiply, D for Determinant, X for FastDet, R for Random Matrix, I for inverse, E to exit')
		choice = input('Choice: ')
		if choice.upper() == 'E':
			start = False
		if choice.upper() == 'C':
			create_matrix()
		if choice.upper() == 'P':
			Y = input('Print all? Y/N: ')
			if Y.upper() == 'Y':
				print()
				for matrix in library:
					print(matrix + ' =')
					print()
					print_matrix(matrix)
			if Y.upper() == 'N':
				name = input('Which matrix: ')
				print()
				print(name + ' =')
				print()
				print_matrix(name)
		if choice.upper() == 'A':
			add()
		if choice.upper() == 'M':
			multiply()
		if choice.upper() == 'D':
			det()
		if choice.upper() == 'R':
			rand()
		if choice.upper() == 'X':
			fastdet()
		if choice.upper() == 'I':
			inverse()

start()