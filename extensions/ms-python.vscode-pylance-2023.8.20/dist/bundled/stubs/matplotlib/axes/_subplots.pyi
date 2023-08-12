from matplotlib.gridspec import GridSpec, SubplotSpec
from matplotlib.figure import Figure

class SubplotBase:
    def __init__(self, fig: Figure, *args, **kwargs) -> None: ...
    def get_subplotspec(self) -> SubplotSpec: ...
    def set_subplotspec(self, subplotspec: SubplotSpec)-> None: ...
    def get_gridspec(self) -> GridSpec: ...
    def label_outer(self) -> None: ...

subplot_class_factory = ...
Subplot = ...