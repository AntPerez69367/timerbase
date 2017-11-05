import QtQuick 2.7
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0



ApplicationWindow {
    id: window
    visible: true
    width: 800
    height: 480
    title: qsTr("Timer Base")
    Material.theme:  Material.Dark


    readonly property bool inPortrait: window.width < window.height

    StackLayout {
        id: swipeView
        anchors.leftMargin: 164
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: parent.top
        currentIndex: 0

        Timer1 {

        }

        Settings{

        }

        About{

        }

    }



    Drawer{
        id: mainMenu
        x: 0
        y: 0
        width: 164
        height: 480

        modal: inPortrait

        position: inPortrait ? 0 : 1
        dragMargin: 2
        edge: Qt.TopEdge
        z: 2
        visible: !inPortrait

        background: Rectangle {
            PageBackground {
                height: 480
                width: 164

            }
        }


        ColumnLayout {
            x: 24
            y: 134
            z: 3

            TabButton {
                text: qsTr("Timer")
                Layout.preferredHeight: 48
                Layout.preferredWidth: 117
                z: 2
                font.weight: Font.Bold
                onClicked: swipeView.currentIndex = 0
            }

            TabButton {
                text: qsTr("Settings")
                Layout.preferredHeight: 48
                Layout.preferredWidth: 117
                z: 3

                font.weight: Font.Bold
                onClicked: swipeView.currentIndex = 1
            }

            TabButton {
                text: qsTr("About")
                Layout.preferredHeight: 48
                Layout.preferredWidth: 117
                z: 4
                font.weight: Font.Bold
                onClicked: swipeView.currentIndex = 2
            }
        }

        ColumnLayout {
        x: 31
        y: 403
        anchors.horizontalCenter: parent.horizontalCenter

        Label {
            id: btDescr
            text: qsTr("Bluetooth Status")
            color: "white"
        }

        Label {
            id: btStatus
            text: qsTr("Disconnected")
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            color: btStatus.text.toString() == "Connected" ? "green" : "red"
        }
    }

        ListView {
            id: listView
            width: 164
            z: 4
            headerPositioning: ListView.OverlayHeader
            header: Pane {
                id: header
                z: 2
                width: parent.width

                contentHeight: logo.height
                background: Rectangle {
                    PageBackground {
                        height: 120
                        width: 164

                    }
                }

                Image {
                    id: logo
                    width: parent.width
                    source: "images/bt-logo.PNG"
                    fillMode: implicitWidth > width ? Image.PreserveAspectFit : Image.Pad

                }

                MenuSeparator {
                     visible: !listView.atYBeginning
                }
            }
            model: 10
            ScrollIndicator.vertical: ScrollIndicator { }
        }
    }

    Connections {
        target: timerbase

        // Sum signal handler
        onUpdateStatus: {
            // sum was set through arguments=['sum']
            btStatus.text = status
        }
     }
}



