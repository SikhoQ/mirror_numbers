def upside_rightside():
    originals = [0, 1, 9, 8, 6]
    mirrors = [0, 1, 6, 8, 9]
    for i in range(1, 100000):
        mirror_possible = True
        mirror_num = ""
        for digit in str(i):
            if int(digit) not in originals:
                mirror_possible = False
                break
        if mirror_possible:
            for digit in str(i):
                mirror_num += str(mirrors[originals.index(int(digit))])
            if str(i) == mirror_num[::-1]:
                print(i, end=' ')


if __name__ == "__main__":
    upside_rightside()
