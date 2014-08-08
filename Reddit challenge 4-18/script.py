__author__ = 'ddsnowboard'
main = 1000
differs = True
while True:
    main += 1
    s = str(main)
    s1 = s[0: 2]
    s2 = s[2:]
    for i in range(0, len(s) - 1):
        if s.find(s[i]) == s.rfind(s[i]):
            differs = True
        else:
            differs = False
            break

    i2 = int(s2)
    i1 = int(s1)
    if ((i2 + i1) ** 2 == main and differs and main != 3025) or main > 10000:
        break
print(main)


def torn(given):
    part1 = given[0: 2]
    part2 = given[2:]
    int2 = int(part2)
    int2 = int(part1)
    different = True
    for i in range(0, len(given) - 1):
        if given.find(given[i]) == given.rfind(given[i]):
            different = True
        else:
            different = False
            break

    if (int2 + int2) ** 2 == int(given) and different:
        print(True)
    else:
        print(False)
torn(input("Number, please: "))