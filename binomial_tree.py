import turtle



def paint_tree(depth, lenght):
    """
    Function for drawing binomial tree.
    :param depth: recursion depth
    :param lenght: step length
    :return:
    """
    if depth == 0:
        return
    else:
        turtle.colormode(255)
        turtle.pencolor(0, 255 // depth, 0)
        turtle.forward(lenght)
        turtle.right(20)
        paint_tree(depth - 1, lenght / 1.1)
        turtle.pencolor(0, 255 // depth, 0)
        turtle.left(40)
        paint_tree(depth - 1, lenght / 1.1)
        turtle.pencolor(0, 255 // depth, 0)
        turtle.right(20)
        turtle.backward(lenght)


def main_paint_tree():
    """
    Main function for drawing binomial tree.
    :return:
    """
    turtle.ht()
    turtle.tracer(0)
    turtle.pu()
    turtle.goto(0, -200)
    turtle.pd()
    turtle.left(90)
    paint_tree(2, 100)
    turtle.update()
    turtle.done()

if __name__ == '__main__':
    main_paint_tree()