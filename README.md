# matplotlib_backend_qtquick
This package implements a QtQuick backend for matplotlib. It started from [maplotlib_qtquick_playground](https://github.com/fcollonval/matplotlib_qtquick_playground), written by Frédéric Collonval, but it has been updated to work with the current version (3.2.1) of matplotlib.

## Usage

In order to use matplotlib plots with QtQuick, do the following:

1. In your main.py, use `QtQml.qmlRegisterType` to register `FigureCanvasQtQuickAgg` under whichever name you want to use.
1. In your QML files, instantiate an object with the QML type defined above. Its `objectName` property specifies the name of the object that can be found in the QML engine. It can be retrieved in python with `win.findChild(QtCore.QObject, "spectFigure")`, for example, where `"spectFigure"` is the `objectName` in this case.
1. One can then pass this object as needed. This is the FigureCanvasQtQuickAgg object. The figure can be found in its `figure` property.

The test in the ``tests`` directory gives a simple example of how to use this backend.

Please let me know if you have any suggestions or better ways I should do this.
