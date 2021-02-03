import matplotlib.pyplot as plt
from typing import List, Tuple
import numpy as np
from dataclasses import dataclass


@dataclass
class DataSetting:
    x: np.ndarray
    y: np.ndarray


@dataclass
class Layout:
    x_axis_name: str
    y_axis_name: str
    legend: Tuple
    markers: Tuple
    style: Tuple = ('science', 'ieee', 'grid', 'no-latex')


class FigureManger:

    def __init__(self, data: DataSetting, layout: Layout,keyword):
        self.data = data
        self.layout = layout
        self.figure = None
        self.axes = None
        self.keyword = keyword


    def plot(self):
        x = self.data.x
        y = self.data.y
        assert x.ndim == 2
        assert y.ndim == 2

        with plt.style.context(self.layout.style):
            cnt = 0
            fig, axes = plt.subplots()
            for x_row, y_row in zip(x, y):
                if self.layout.markers:
                    try:
                        axes.plot(x_row, y_row, label=self.layout.legend[cnt], marker=self.layout.markers[cnt])
                    except IndexError:
                        axes.plot(x_row, y_row, marker=self.layout.markers[cnt])
                else:
                    try:
                        axes.plot(x_row, y_row, label=self.layout.legend[cnt])
                    except IndexError:
                        axes.plot(x_row, y_row)

                cnt += 1
            if self.layout.legend:
                axes.legend()
            axes.set_xlabel(self.layout.x_axis_name)
            axes.set_ylabel(self.layout.y_axis_name)
        plt.tight_layout()
        plt.show()
        self.figure = fig
        self.axes = axes

    @classmethod
    def load(cls, name):

        import joblib
        data = joblib.load(name)['data']
        layout = joblib.load(name)['layout']
        keyword = joblib.load(name)['keyword']
        return cls(data, layout,keyword)

    def save(self, name):
        import joblib
        joblib.dump(dict(data=self.data, layout=self.layout,keyword = self.keyword), name)

    def update_layout(self,layout):
        for key in layout:
            if hasattr(self.layout,key):
                setattr(self.layout,key,layout[key])
