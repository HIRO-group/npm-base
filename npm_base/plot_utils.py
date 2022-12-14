# https://github.com/samfway/samplotlib/blob/master/samplotlib/util.py


from matplotlib import rcParams

ALMOST_BLACK = '#222222'

rcParams['axes.edgecolor'] = ALMOST_BLACK
rcParams['axes.labelcolor'] = ALMOST_BLACK
rcParams['lines.color'] = ALMOST_BLACK
rcParams['xtick.color'] = ALMOST_BLACK
rcParams['ytick.color'] = ALMOST_BLACK
rcParams['text.color'] = ALMOST_BLACK


def custom_ax_setup(ax):
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.spines['bottom'].set_color()
    ax.spines['top'].set_color(ALMOST_BLACK)
    ax.spines['right'].set_color(ALMOST_BLACK)
    ax.spines['left'].set_color(ALMOST_BLACK)

    ax.tick_params(axis='x', colors=ALMOST_BLACK)
    ax.tick_params(axis='y', colors=ALMOST_BLACK)

    ax.yaxis.label.set_color(ALMOST_BLACK)
    ax.xaxis.label.set_color(ALMOST_BLACK)

    ax.title.set_color(ALMOST_BLACK)
