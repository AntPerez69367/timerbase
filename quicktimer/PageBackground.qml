import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0

Rectangle {
    id: rectangle1

    Material.theme:  Material.Dark



    width: 800
    height: 480
    color: "#191919"
    clip: true
    transformOrigin: Item.Center
    property alias title: label.text

    Label {
        id: label
        x: 8
        y: 15
        text: qsTr("")
        anchors.horizontalCenter: parent.horizontalCenter
        font.family: "Arial"
        font.pointSize: 18
        color: "white"

    }

    Rectangle {
        id: rectangle
        x: 523
        y: -71
        width: 400
        height: 200
        color: "#3a3a3a"
        scale: 1.3
        rotation: 41
    }
}
