#this program uses plotly
import random
import plotly
from plotly.graph_objs import *

faces = [1,2,3,4,5,6]
count = [0,0,0,0,0,0] # stores the counts for each number i.e. counts[0] stores count for the number 1

for i in range(100):
    r = random.randint(1,6)
    count[r-1]=count[r-1]+1

plotly.offline.plot({
    "data": [Bar(x=faces, y=count)],
    "layout": Layout(title="Dice Results")
})
