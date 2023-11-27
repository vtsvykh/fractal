import turtle


def fractal(depth, radius):
    """
    Function for drawing fractal.
    :param depth: recursion depth
    :param radius: radius of circle
    :return:
    """
    if depth == 0:
        return
    else:
        fractal(depth - 1, radius - 10)
        turtle.circle(radius)
        turtle.right(20)


def main_paint_fractal():
    """
    Main gunction for drawing fractal.
    :return:
    """
    turtle.tracer(0)
    fractal(30, 100)
    turtle.update()
    turtle.done()


if __name__ == '__main__':
    main_paint_fractal()
