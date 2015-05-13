import numpy as np
import matplotlib.pyplot as plt

N = 3


ind = np.arange(N) # the x locations for the groups
width = 0.175       # the width of the bars

fig, (ax, ax2) = plt.subplots(2,1, sharex = True, figsize=(10,5))

ax.set_ylim(1000,2200) # outliers only
ax2.set_ylim(0,35) # most of the data

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off') # don't put tick labels at the top
ax2.xaxis.tick_bottom()
fig.subplots_adjust(hspace=0.1)

# no layers, CPL, CPL mixed
noneV = (5.151, 21.33, 0)
rectsNone = ax.bar(ind, noneV, width, color='w')
ax2.bar(ind, noneV, width, color='w')

classCached = (5.231, 21.666, 32.399)
rectsClassCached = ax.bar(ind+width, classCached, width, color='w', hatch='/')
ax2.bar(ind+width, classCached, width, color='w', hatch='/')

classUncached = (6.089, 28.593, 2048.526)
rectsClassUncached = ax.bar(ind+2*width, classUncached, width, color='w', hatch='o')
ax2.bar(ind+2*width, classUncached, width, color='w', hatch='o')

instanceCached = (5.413, 21.481, 16.293)
rectsInstanceCached = ax.bar(ind+3*width, instanceCached, width, color='w', hatch='\\')
ax2.bar(ind+3*width, instanceCached, width, color='w', hatch='\\')

instanceUncached = (5.215, 22.603, 13.751)
rectsInstanceUncached = ax.bar(ind+4*width, instanceUncached, width, color='w', hatch='O')
ax2.bar(ind+4*width, instanceUncached, width, color='w', hatch='O')

# add some text for labels, title and axes ticks
ax2.set_ylabel('Runtime (ms)')
#ax.set_title('Average rendering runtime per frame')
ax.set_xticks(ind+width+0.25)
ax.set_xticklabels( ('no layers', 'control point layer', 'control point layer (mixed)') )
ax2.set_yticks(ax2.get_yticks()[:-1])
ax.set_yticks(ax.get_yticks()[1:])

ax.legend( (rectsNone[0], rectsClassCached[0], rectsClassUncached[0], rectsInstanceCached[0], rectsInstanceUncached[0]), ('without ContextAmber', 'class-specific (cached)', 'class-specific (uncached)', 'instance-specific (cached)', 'instance-specific (uncached)') , loc=2)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        if height == 0:
            ax2.text(rect.get_x()+rect.get_width()/2., height+2, 'n/a',
                ha='center', va='bottom', rotation='vertical')       
        else:
            ax2.text(rect.get_x()+rect.get_width()/2., height+2, '%.2f'%float(height),
                    ha='center', va='bottom', rotation='vertical')

autolabel(rectsNone)
autolabel(rectsClassCached)
autolabel(rectsClassUncached)
autolabel(rectsInstanceCached)
autolabel(rectsInstanceUncached)

d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d,+d),(-d,+d), **kwargs)      # top-left diagonal
ax.plot((1-d,1+d),(-d,+d), **kwargs)    # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d,+d),(1-d,1+d), **kwargs)   # bottom-left diagonal
ax2.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-right diagonal


plt.show()