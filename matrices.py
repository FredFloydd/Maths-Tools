import random
import time

library = {}

def print_matrix(matrix):
	for x in matrix:
		printable = []
		for n in range(len(matrix[x])):
			printable.append(str(matrix[x][n]))
		for n in range(len(printable)):
			if len(printable[n]) == 1:
				printable[n] = ' ' + printable[n]
		print('  '.join(printable))
	print()

def add(A,B):
	if len(A) == len(B) and len(A[0]) == len(B[0]):
		name = input('Name the new matrix: ')
		new = {}
		for x in range(len(A.keys())):
			line = []
			for y in range(len(A[x])):
				line.append(float(A[x][y] + B[x][y]))
			new[x] = line
		print()
		print(name + ' =')
		print_matrix(new)
		library[name] = new
	else:
		print()
		print('Matrices are not compatible')
		print()

def multiply(A,B):
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
		print(name + ' =')
		print_matrix(new)
	else:
		print('Matrices are not compatible')

def create_matrix(name):
  matrix_name = str(name)
  name = {}
  rows = float(input('How many rows: '))
  col = float(input('How many columns: '))
  for n in range(rows):
    line = []
    for x in range(col):
      line.append(float(input('Value: ')))
    name[n] = line
  print()
  print(matrix_name + ' =')
  print_matrix(name)
  library[matrix_name] = name

def det(mat):
	if len(mat) != len(mat[0]):
		print('Matrix not square')
	else:
		if len(mat) == 2:
			return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
		else:
			first = mat[0]
			for x in range(len(mat[0])):
				minor = {}
				for y in range(1, len(mat)):
					minor[y-1] = []
					for z in range(len(mat[0])):
						if z != x:
							minor[y-1].append(mat[y][z])
				first[x] *= float(det(minor))
			determinant = 0
			for n in range(len(first)):
				determinant += ((-1) ** n) * float(first[n])
			return determinant

def fastdet(mat):
	det = 1
	for n in range(len(mat)-1):
		for row in range(n, len(mat) - 1):
			factor = mat[row + 1][n] / mat[n][n]
			for x in range(n, len(mat)):
				mat[row+1][x] -= factor * mat[n][x]
	for x in range(len(mat)):
		det *= mat[x][x]
	return det

def start():
	print('Welcome to the linear algebra toolbox')
	start = True
	while start == True:
		print('What would you like to do?')
		print('C to create, A to add, P to print, M to Multiply, D for Determinant, X for FastDet, R for Random Matrix, E to exit')
		choice = input('Choice: ')
		if choice.upper() == 'C':
			name = input('Name your matrix: ')
			create_matrix(name)
		if choice.upper() == 'E':
			start = False
		if choice.upper() == 'P':
			Y = input('Print all? Y/N: ')
			if Y.upper() == 'Y':
				print()
				for matrix in library:
					print(matrix + ' =')
					print_matrix(library[matrix])
					print()
			if Y.upper() == 'N':
				name = input('Which matrix: ')
				print()
				print(name + ' =')
				print_matrix(library[name])
		if choice.upper() == 'A':
			mat1 = library[input('First Matrix: ')]
			mat2 = library[input('Second Matrix: ')]
			add(mat1, mat2)
		if choice.upper() == 'M':
			mat1 = library[input('First Matrix: ')]
			mat2 = library[input('Second Matrix: ')]
			multiply(mat1, mat2)
		if choice.upper() == 'D':
			name = input('Matrix: ')
			mat = library[name]
			print()
			print('Det ' + name + ' = ' + str(det(mat)))
			print()
		if choice.upper() == 'R':
			mat = {}
			arr = []
			name = input('Name of Matrix: ')
			rows = int(input('Rows: '))
			col = int(input('Columns: '))
			random.seed(2)
			for i in range(rows*col):
				arr.append(random.randint(1,10))
			for n in range(rows):
				mat[n] = arr[col*n:(col*n+col)]
			print()
			print(name + ' =')
			print_matrix(mat)
			print()
			library[name] = mat
		if choice.upper() == 'X':
			name = input('Matrix: ')
			mat = library[name]
			start = time.time()
			print()
			print('Det ' + name + ' = ' + str(fastdet(mat)))
			end = time.time()
			print('Time = ' + str(end - start))
			print()




start()