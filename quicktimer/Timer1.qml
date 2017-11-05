import QtQuick 2.4
import QtQuick.Controls.Material 2.0
import QtQuick.Controls 2.0
import QtQuick.Extras 1.4

PageBackground {
    id: pageBackground
    x: 0
    width: 640
    property alias time: time

    title: time.acceptableInput ? "Timer" : "Invalid Time Input. Try Again"

    function clear(){
        time.text = "00:00:00"   }

    function del(){
        time.undo()
    }

    TextInput {
       id: time
       validator: RegExpValidator {regExp: /^(?:([0-9]?\d|2[0-9]):([0-5]?\d):)?([0-5]?\d)$/}
       y: 30
       height: 115
       color: time.acceptableInput ? "#ffffff" : "red"
       inputMask: "00:00:00"
       text: "00:00:00"
       cursorVisible: false
       readOnly: false
       anchors.horizontalCenter: button2.horizontalCenter
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignLeft
        font.pointSize: 72
        font.family: "Tahoma"
        maximumLength: 8
        selectByMouse: false
        cursorPosition: 0

        }

    MyButton {
        id: buttonCLR
        y: 396
        height: 68
        text: qsTr("Clear")
        font.weight: Font.ExtraBold
        anchors.leftMargin: 37
        anchors.right: parent.right
        anchors.rightMargin: 38
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 23

        onClicked:{
            clear()
            time.cursorPosition = 0
        }
    }

    MyButton {
        id: buttonDel
        y: 321
        height: 68
        text: qsTr("Delete")
        font.weight: Font.ExtraBold
        anchors.right: parent.right
        anchors.rightMargin: 38
        anchors.leftMargin: 37
        anchors.bottom: buttonCLR.top
        anchors.bottomMargin: 25
        onClicked: {
            del()
    }
}
    MyButton {
        id: buttonStart
        font.weight: Font.ExtraBold
        y: 232
        height: 68
        text: qsTr("Start")
        anchors.bottomMargin: 25
        anchors.right: parent.right
        anchors.rightMargin: 38
        anchors.leftMargin: 37
        anchors.bottom: buttonStop.top
        onClicked: {
            timerbase.startClicked(qsTr(time.text))
        }

    }

    MyButton {
        id: buttonStop
        signal stopTimer
        font.weight: Font.ExtraBold
        y: 232
        height: 68
        text: qsTr("Stop")
        anchors.right: parent.right
        anchors.rightMargin: 38
        anchors.leftMargin: 37
        anchors.bottom: buttonDel.top
        anchors.bottomMargin: 25
        onClicked: {
            timerbase.stopClicked()
        }
    }

    MyButton {
        id: button0
        x: 177
        y: 401
        width: 120
        height: 65
        text: qsTr("0")
        font.weight: Font.ExtraBold
        anchors.left: button7.right
        anchors.leftMargin: 30
        anchors.top: button8.bottom
        anchors.topMargin: 6
        onClicked: {

            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1
        }
    }

    MyButton {
        id: button9
        x: 307
        y: 326
        width: 120
        height: 65
        text: qsTr("9")
        font.weight: Font.ExtraBold
        anchors.left: button8.right
        anchors.leftMargin: 30
        anchors.top: button6.bottom
        anchors.topMargin: 6
        onClicked: {

            if (time.cursorPosition != 3 && time.cursorPosition !=6){
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1}
                }
        }


    MyButton {
        id: button8
        x: 177
        y: 326
        width: 120
        height: 65
        text: qsTr("8")
        font.weight: Font.ExtraBold
        anchors.left: button7.right
        anchors.leftMargin: 30
        anchors.top: button5.bottom
        anchors.topMargin: 6
        onClicked: {

            if (time.cursorPosition != 3 && time.cursorPosition !=6){
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1}
          }
}


    MyButton {
        id: button7
        x: 47
        y: 326
        width: 120
        height: 65
        text: qsTr("7")
        font.weight: Font.ExtraBold
        anchors.left: parent.left
        anchors.leftMargin: 30
        anchors.top: button4.bottom
        anchors.topMargin: 6
        onClicked: {

            if (time.cursorPosition != 3 && time.cursorPosition !=6){
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1}
    }
}

    MyButton {
        id: button6
        x: 307
        y: 251
        width: 120
        height: 65
        text: qsTr("6")
        font.weight: Font.ExtraBold
        anchors.left: button5.right
        anchors.leftMargin: 30
        anchors.top: button3.bottom
        anchors.topMargin: 6
        onClicked: {

            if (time.cursorPosition != 3 && time.cursorPosition !=6){
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1}
              }
    }


    MyButton {
        id: button5
        x: 177
        y: 251
        width: 120
        height: 65
        text: qsTr("5")
        font.weight: Font.ExtraBold
        anchors.left: button4.right
        anchors.leftMargin: 30
        anchors.top: button2.bottom
        anchors.topMargin: 6
        onClicked: {
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1
        }
    }

    MyButton {
        id: button4
        x: 47
        y: 251
        width: 120
        height: 65
        text: qsTr("4")
        font.weight: Font.ExtraBold
        anchors.left: parent.left
        anchors.leftMargin: 30
        anchors.top: button1.bottom
        anchors.topMargin: 6
        onClicked: {
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1
        }
    }

    MyButton {
        id: button3
        x: 307
        y: 176
        width: 120
        height: 65
        text: qsTr("3")
        font.weight: Font.ExtraBold
        anchors.left: button2.right
        anchors.leftMargin: 30
        anchors.top: parent.top
        anchors.topMargin: 166
        onClicked: {
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1
        }
    }

    MyButton {
        id: button2
        x: 177
        y: 176
        width: 120
        height: 65
        text: qsTr("2")
        font.weight: Font.ExtraBold
        anchors.left: button1.right
        anchors.leftMargin: 30
        anchors.top: parent.top
        anchors.topMargin: 166
        onClicked: {
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1
        }
    }

    MyButton {
        id: button1
        x: 47
        y: 176
        width: 120
        height: 65
        text: qsTr("1")
        font.weight: Font.ExtraBold
        anchors.left: parent.left
        anchors.leftMargin: 30
        anchors.top: parent.top
        anchors.topMargin: 166
        onClicked: {
            time.insert(time.cursorPosition, text)
            time.cursorPosition += 1
        }
    }
}



