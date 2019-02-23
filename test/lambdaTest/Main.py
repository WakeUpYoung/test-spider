

if __name__ == '__main__':
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    print(filter(lambda x: x % 3 == 0, foo))
    print(map(lambda x: x * 2 + 10, foo))
    print([x * 2 + 10 for x in foo])

