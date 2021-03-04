def minimum(a, b, c):
    smallest = 0
    if a > b:
        smallest = b
    else:
        smallest = a
    if smallest > c:
        smallest = c
    return smallest


def main():
    print('Smallest value is: ', minimum(0, 11, 9))


main()
