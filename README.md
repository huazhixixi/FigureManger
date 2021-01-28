# For reproduce the results plot using matplotlib

    DataSetting
        x: np.ndarray
        y: np.ndarray
    each row of x, and y represents a line

    LayoutSetting:
        x_axis_name: The lable of x,string
        y_axis_name: The lable of y,string
        legend: The label of each line,a list
        marker

    FigureManger:
    @attr:
        data
        layout
        figure
        axes
    @method:
    plot_line:
        iterate each row of x,y, and each element of the legend and marker
    
    scatter:
        plot in scatter mode.

        

```python
# single line
from FigureManger import FigureManger,DataSetting,Layout
import  numpy as np

layout = Layout('x_axis','y_axis',(),(),('science','ieee','no-latex'))

x = np.array([[1,2,3]])
y = x**2

data = DataSetting(x,y)
fig = FigureManger(data,layout)
fig.plot()

fig.save('Myfigure.fig')

fig2 = FigureManger.load('Myfigure.fig') # auto-reload the data and layout
fig2.plot() # reproduce the figure
# if have legend or marker,just fill the empty tuple

```

