import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0

Button {

    id: control

     contentItem: Text {
         text: control.text
         style: Text.Raised
         font: control.font
         opacity: enabled ? 1.0 : 0.3
         color: control.down ? "#ffffff" : "#ffffff"
         horizontalAlignment: Text.AlignHCenter
         verticalAlignment: Text.AlignVCenter
         elide: Text.ElideRight
      }


    background: Rectangle {
             color: "#424242"
             implicitWidth: 100
             implicitHeight: 40
             border.color: "#26282a"
             border.width: 1
             radius: 50

             }
         }
