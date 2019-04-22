import matplotlib.pyplot


def create_graph():
    x_number = [1, 2, 3]
    y_number = [2, 4, 6]
    matplotlib.pyplot.plot(x_number, y_number)
    matplotlib.pyplot.show()


if __name__ == "__main__":
    create_graph()
