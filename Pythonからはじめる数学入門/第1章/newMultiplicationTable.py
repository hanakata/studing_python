
def multi_table(a, b):
    for i in range(1, b + 1):
        print('{0} x {1} ＝ {2}'.format(a, i, a * i))


if __name__ == "__main__":
    a = input("Enter a Number")
    b = input("Enter a multi")
    multi_table(float(a), int(b))
