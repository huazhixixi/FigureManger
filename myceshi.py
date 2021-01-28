from FigureManger import FigureManger,DataSetting,Layout
import  numpy as np

layout = Layout('x_axis','y_axis',('xixi',),('o',),('science','ieee','no-latex'))

x = np.array([[1,2,3]])
y = x**2

data = DataSetting(x,y)
fig = FigureManger(data,layout)
fig.plot()