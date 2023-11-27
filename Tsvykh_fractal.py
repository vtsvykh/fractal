import turtle


def fractal(depth, lenght):
    if depth == 0:
        return
    else:
        fractal(depth - 1, lenght - 10)
        turtle.circle(lenght)
        turtle.right(20)


def main_paint_fractal():
    turtle.tracer(0)
    fractal(30, 100)
    turtle.update()
    turtle.done()


if __name__ == '__main__':
    main_paint_fractal()
