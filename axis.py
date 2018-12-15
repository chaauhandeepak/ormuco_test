from matplotlib import axis
import matplotlib.pyplot as pyplot

def center_origin(axis):
    '''Center the axis in the middle of the picture'''
    axis.spines['right'].set_color('none')
    axis.spines['top'].set_color('none')
    axis.xaxis.set_ticks_position('bottom')
    axis.spines['bottom'].set_position(('data',0))
    axis.yaxis.set_ticks_position('left')
    axis.spines['left'].set_position(('data',0))

def render(lines):
    figure = pyplot.figure(figsize=(4,4))
    axis = figure.add_subplot(1, 1, 1)

    center_origin(axis)

    for (x1, y1), (x2, y2) in lines:
        axis.add_line(pyplot.Line2D((x1, x2), (y1, y2), color='red'))

    axis.set_xlim(-1.2, 1.2)
    axis.set_ylim(-1.2, 1.2)
    return figure

if __name__ == '__main__':
    render([((1, 0), (0, 1)),
            ((1, 0), (-1, 0)),
            ((1, 0), (0, -1))]).show()
    input('block > ')
    pyplot.Line2D((x1, x2), (y1, y2), color='red', zorder = 1)
