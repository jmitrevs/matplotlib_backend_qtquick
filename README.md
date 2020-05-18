# matplotlib_backend_qtquick
This package implements a QtQuick backend for matplotlib. It started from [maplotlib_qtquick_playground](https://github.com/fcollonval/matplotlib_qtquick_playground), written by Frédéric Collonval, but it has been updated to work with the current version (3.2.1) of matplotlib.

## Usage

In order to use matplotlib plots with QtQuick, do the following:

1. In your main.py, use `QtQml.qmlRegisterType` to register `FigureCanvasQtQuickAgg` under whichever name you want to use.
1. In your QML files, instantiate an object with the QML type defined above. Its `objectName` property specifies the name of the object that can be found in the QML engine. It can be retrieved in python with `win.findChild(QtCore.QObject, "spectFigure")`, for example, where `"spectFigure"` is the `objectName` in this case.
1. One can then pass this object as needed. This is the FigureCanvasQtQuickAgg object. The figure can be found in its `figure` property.

For interactive plots, if you want to use the toolbar, to the `Bridge` class add slots like:

```python
    @QtCore.Slot()
    def zoom(self, *args):
        """activate zoom tool."""
        self.toolbar.zoom(*args)
```

One can also connect to Matplotlib events:

```python
       self._figure.canvas.mpl_connect('button_press_event', self.onClick)
       self._figure.canvas.mpl_connect('scroll_event', self.onScroll)
```

and provide the callbacks, for example:

```python
    def onClick(self, event):
        """
        Handle mouse clicks in the three slices:
        set the slice to what is clicked.
        """
        if event.button == MouseButton.LEFT:
            if event.inaxes == self.axeses[0]:
                self.x = self._findBin(self.xAxis, event.xdata)
                self.y = self._findBin(self.yAxis, event.ydata)
                self.setSlice()
            elif event.inaxes == self.axeses[1]:
                self.x = self._findBin(self.xAxis, event.xdata)
                self.z = self._findBin(self.zAxis, event.ydata)
                self.setSlice()
            elif event.inaxes == self.axeses[2]:
                self.y = self._findBin(self.yAxis, event.xdata)
                self.z = self._findBin(self.zAxis, event.ydata)
                self.setSlice()

    def onScroll(self, event):
        """
        Handle mouse scroll in the three slices
        - scroll the independent variable
        """
        if event.inaxes == self.axeses[0]:
            self.z += int(event.step)
            self.setSlice()
        elif event.inaxes == self.axeses[1]:
            self.y += int(event.step)
            self.setSlice()
        elif event.inaxes == self.axeses[2]:
            self.x += int(event.step)
            self.setSlice()
```

Please let me know if you have any suggestions or better ways I should do this.

## Examples

The example in the `examples` directory gives a simple example of how to use this backend, including interactions.
