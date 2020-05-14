"""
An integration test to create a plot using the qtquick backend.
"""
import sys
from pathlib import Path
import unittest
import numpy as np
from matplotlib_backend_qtquick.backend_qtquick import (
    NavigationToolbar2QtQuick)
from matplotlib_backend_qtquick.backend_qtquickagg import (
    FigureCanvasQtQuickAgg)
from matplotlib_backend_qtquick.qt_compat import QtGui, QtQml, QtCore


class DisplayBridge(QtCore.QObject):
    """ A bridge class to interact with the plot in python
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # The figure and toolbar
        self.figure = None
        self.toolbar = None

    def updateWithCanvas(self, canvas):
        """ initialize with the canvas for the figure
        """
        self.figure = canvas.figure
        self.toolbar = NavigationToolbar2QtQuick(canvas=canvas)

        # make a small plot
        self.axes = self.figure.add_subplot(111)
        self.axes.grid(True)

        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)

        self.axes.plot(x, y)
        canvas.draw_idle()


class TestBackend(unittest.TestCase):
    """ The actual test class
    """

    def test_basicPlotting(self):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QtGui.QGuiApplication(sys.argv)
        engine = QtQml.QQmlApplicationEngine()

        # instantate the display bridge
        displayBridge = DisplayBridge()

        # Expose the Python object to QML
        context = engine.rootContext()
        context.setContextProperty("displayBridge", displayBridge)

        # matplotlib stuff
        QtQml.qmlRegisterType(FigureCanvasQtQuickAgg, "Backend", 1, 0, "FigureCanvas")

        # Load the QML file
        qmlFile = Path(Path.cwd(), Path(__file__).parent, "main.qml")
        engine.load(QtCore.QUrl.fromLocalFile(str(qmlFile)))

        win = engine.rootObjects()[0]
        displayBridge.updateWithCanvas(win.findChild(QtCore.QObject, "figure"))

        # execute and cleanup
        app.exec_()
