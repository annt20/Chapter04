def repeat(s, times):
    res = ''
    for i in range(times):
        res += s
    return res


def main():
    s = repeat('haha', 3)
    print(s)


main()
