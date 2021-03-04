file_test = open('Demonstrate', 'r')
line = file_test.readline()
while line != '':
    print(line, end='')
    line = file_test.readline()

file_test.close()
