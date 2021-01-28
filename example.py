# %%

#lineplot
from FigureManger import FigureManger,DataSetting,Layout
import  numpy as np

layout = Layout(x_axis_name='x_axis',y_axis_name='y_axis',
legend=('xixi',),markers=('o',),style=('science','ieee','no-latex'))

x = np.array([[1,2,3]])
y = x**2

data = DataSetting(x,y)
fig = FigureManger(data,layout)
fig.plot()
# %%
# multiple lineplot
from FigureManger import FigureManger,DataSetting,Layout
import  numpy as np

layout = Layout(x_axis_name='x_axis',y_axis_name='y_axis',
legend=('xixi','xixi2'),markers=('o','*'),style=('science','ieee','no-latex'))

x = np.array([[1,2,3],[4,5,6]])
y = x**2

data = DataSetting(x,y)
fig = FigureManger(data,layout)
fig.plot()

# %%
from FigureManger import FigureManger,DataSetting,Layout
import  numpy as np

layout = Layout(x_axis_name='x_axis',y_axis_name='y_axis',
legend=(),markers=(),style=('science','ieee','no-latex'))

x = np.array([[1,2,3]])
y = x**2

data = DataSetting(x,y)
fig = FigureManger(data,layout)
fig.plot()

#%%

from FigureManger import FigureManger,DataSetting,Layout
import  numpy as np

layout = Layout(x_axis_name='x_axis',y_axis_name='y_axis',
legend=('xixi','xixi2','xixi3','xixi4'),markers=(),style=('science','ieee','scatter','no-latex'))

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y = x**2

data = DataSetting(x,y)
fig = FigureManger(data,layout)
fig.plot()
fig.save("ceshi.fig")

#%%
# reproduce the plot and update the layout
fig = FigureManger.load("ceshi.fig")
fig.update_layout(
    {
        "legend":("xx1","xx2","xx3","xx4"),

    "x_axis_name":"x_axis_change"},

)

fig.plot()