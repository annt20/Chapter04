def main():
    my_file = open('demonstrate', 'r')
    line = my_file.readline()
    count = 0
    total = 0
    while line != '':
        count += 1
        total += int(line)
        line = my_file.readline()
    average = total / count
    my_file.close()
    print(average)


main()
