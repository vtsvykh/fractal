import turtle


def fractal_minkovskogo(depth, length):
    """
    Function for drawing fractal Minkovskogo.
    :param depth: recursion depth
    :param length: step length
    :return:
    """
    if depth == 0:
        turtle.forward(length)
    else:
        fractal_minkovskogo(depth - 1, length / 8)
        turtle.left(90)
        fractal_minkovskogo(depth - 1, length / 8)
        turtle.right(90)
        fractal_minkovskogo(depth - 1, length / 8)
        turtle.right(90)
        fractal_minkovskogo(depth - 1, length / 8)
        fractal_minkovskogo(depth - 1, length / 8)
        turtle.left(90)
        fractal_minkovskogo(depth - 1, length / 8)
        turtle.left(90)
        fractal_minkovskogo(depth - 1, length / 8)
        turtle.right(90)
        fractal_minkovskogo(depth - 1, length / 8)

def main_paint_mink():
    """
    Main function for fractal Minkovskogo.
    :return:
    """
    turtle.tracer(0)
    fractal_minkovskogo(3, 2000)
    turtle.update()
    turtle.done()

if __name__ == '__main__':
    main_paint_mink()