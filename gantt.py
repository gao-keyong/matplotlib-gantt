import enum
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np


def gantt(category_names, results):
    fig, gnt = plt.subplots(figsize=(11.69, 8.27))

    lables = list(results.keys())
    num_lables = len(lables)
    data = list(results.values())
    max_time = max([sum(seg)
                   for lable in data for segs in lable for seg in segs])

    yticks = np.linspace(num_lables*10+5, 15, num_lables)

    gnt.set_ylim(0, num_lables*10+20)
    gnt.set_xlim(0, max_time+20)

    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Process')

    gnt.set_yticks(yticks)
    gnt.set_yticklabels(lables)

    category_colors = plt.get_cmap('Greys')(
        np.linspace(0.15, 0.85, len(category_names)))

    gnt.grid(False)

    seg_height = 6

    for i, data in enumerate(data):
        y_lb = yticks[i]-3
        y_ub = y_lb+seg_height
        for (segs, name, color) in zip(data, category_names, category_colors):
            gnt.broken_barh(segs, (y_lb, seg_height), fc=color)
            inner_text_color = 'black' if color[0] > 0.5 else 'white'
            for j, seg in enumerate(segs):
                gnt.text((2*seg[0]+seg[1])/2, (y_lb+y_ub)/2, name+'\n'+str(seg[1]),
                         color=inner_text_color, ha='center', va='center')
                if j == 0 and seg[0] != 0:
                    gnt.text(seg[0], y_ub+1, str(seg[0]),
                             ha='center', va='bottom')
                gnt.text(seg[0]+seg[1], y_ub+1, str(seg[0]+seg[1]),
                         ha='center', va='bottom')

    fakebar = [mpatch.Rectangle((0, 0), 1, 1, fc=category_color)
               for category_color in category_colors]

    gnt.legend(fakebar, category_names)

    return plt
