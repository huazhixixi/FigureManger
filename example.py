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
