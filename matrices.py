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


def create_matrix(name):
  matrix_name = str(name)
  name = {}
  rows = int(input('How many rows: '))
  col = int(input('How many columns: '))
  for n in range(rows):
    line = []
    for x in range(col):
      line.append(int(input('Value: ')))
    name[n] = line
  print(matrix_name + ' =')
  print_matrix(name)
  library[matrix_name] = name

def start():
	print('Welcome to the linear algebra toolbox')
	start = True
	while start == True:
		print('What would you like to do?')
		print('C to create, A to add, P to print, E to exit')
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
				print()


			



start()