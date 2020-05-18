import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.12

import Backend 1.0

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 800
    height: 600
    title: qsTr("QtQuick backend test")

    
    FigureCanvas {
        id: mplView
        objectName : "figure"
        dpi_ratio: Screen.devicePixelRatio
	    anchors.fill: parent
    }

    footer: ToolBar {
        RowLayout {
            ToolButton {
                text: qsTr("home")
                onClicked: {
                    displayBridge.home();
                }
            }

            Button {
                text: qsTr("back")
                onClicked: {
                    displayBridge.back();
                }
            }

            Button {
                text: qsTr("forward")
                onClicked: {
                    displayBridge.forward();
                }
            }

            ToolSeparator{}

            Button {
                id: pan
                text: qsTr("pan")
                checkable: true
                onClicked: {
                    if (zoom.checked) {
                        zoom.checked = false;
                    }
                    displayBridge.pan();
                }
            }

            Button {
                id: zoom
                text: qsTr("zoom")
                checkable: true
                onClicked: {
                    if (pan.checked) {
                        // toggle pan off
                        pan.checked = false;
                    }
                    displayBridge.zoom();
                }
            }
            ToolSeparator {}
            TextInput {
                id: location
                readOnly: true
                text: displayBridge.coordinates
            }
        }
    }

}
