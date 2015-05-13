#!/usr/bin/env python
# make a horizontal bar chart

from pylab import *
val = [1043.0/1000, 3058.0/1000, 211.0/1000, 2654.0/1000]    # the bar lengths
pos = arange(4)+.5    # the bar centers on the y axis

figure(1)
barh(pos,val, align='center', color='w', hatch=' ')
yticks(pos, ('instance-specific,\n global activation', 'instance-specific,\n object activation', 'class-specific,\n global activation', 'class-specific,\n object activation'))
xlabel('Runtime (milliseconds)')
grid(False)

show()