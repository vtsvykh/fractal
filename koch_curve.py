import turtle


def koch_curve(depth, lenght):
    """
    Function for drawing Koch_curve.
    :param depth: recursion depth
    :param length: step length
    :return:
    """
    if depth == 0:
        turtle.forward(lenght)
    else:
        koch_curve(depth - 1, lenght / 3)
        turtle.left(60)
        koch_curve(depth - 1, lenght / 3)
        turtle.right(120)
        koch_curve(depth - 1, lenght / 3)
        turtle.left(60)
        koch_curve(depth - 1, lenght / 3)


def main():
    """
    Main function for drawing Koch_curve.
    :return:
    """
    turtle.ht()
    turtle.tracer(0)
    koch_curve(3, 500)
    turtle.update()
    turtle.done()


if __name__ == '__main__':
    main()
