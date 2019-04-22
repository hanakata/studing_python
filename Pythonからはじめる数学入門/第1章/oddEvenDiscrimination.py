def factors(b):
    if b % 2 == 0:
        print("this number is even")
        increment(b)
    else:
        print("this number is odd")
        increment(b)


def increment(b):
    for i in range(2, 20, 2):
        print(str(b + i) + " ")


if __name__ == "__main__":
    b = input('Your Number Please:')
    try:
        b = float(b)
    except:
        print("please enter a integer")
        exit()

    if b > 0:
        factors(int(b))
    else:
        print("please enter a positive integer")
