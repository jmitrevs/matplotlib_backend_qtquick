import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12

import Backend 1.0

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 800
    height: 600
    title: qsTr("QtQuick backend test")

    // So that the test exits in 5 seconds
    Timer {
        id: exitTimer
        interval: 5000
	running: true
        onTriggered: mainWindow.close()
    }
    
    FigureCanvas {
        id: mplView
        objectName : "figure"
        dpi_ratio: Screen.devicePixelRatio

	anchors.fill: parent
    }
}
