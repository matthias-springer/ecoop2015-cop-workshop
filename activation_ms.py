#!/usr/bin/env python
# make a horizontal bar chart

from pylab import *
val = [1043.0/1000, 3058.0/1000, 211.0/1000, 2654.0/1000]    # the bar lengths
pos = arange(4)+.5    # the bar centers on the y axis

figure(1)
barh(pos,val, align='center', color='w', hatch='O')
yticks(pos, ('instance-wide,\n global activation', 'instance-wide,\n object activation', 'class-wide,\n global activation', 'class-wide,\n object activation'))
xlabel('Runtime (milliseconds)')
grid(False)

show()