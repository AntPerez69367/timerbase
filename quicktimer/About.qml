import QtQuick 2.4
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

PageBackground {
    color: "#191919"
    title: "About"

    RowLayout {
    }

    ColumnLayout {
        x: 42
        y: 89
        width: 557
        height: 312

        Label {
            id: label
       color: "white"
            text: qsTr("Bluetooth Timer Base")
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            font.underline: true
            font.pointSize: 44

        }

        Label {
            id: label1
           color: "white"
            text: qsTr("This software was created to control the bluetooth presentation timer display. ")
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }

        GridLayout {
            width: 211
            rowSpacing: 23
            columnSpacing: 17
            rows: 2
            columns: 2
            Layout.fillWidth: true
            Layout.preferredWidth: -1
            Layout.fillHeight: false
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter

            Label {
                id: label2
                color: "#ffffff"
                text: qsTr("Senior Design Team:")
                font.pointSize: 10
                Layout.alignment: Qt.AlignRight | Qt.AlignTop
                font.weight: Font.Bold
            }


            ColumnLayout {
                x: 133
                y: 27
                width: 90
                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter

                Label {
                    id: label3
                    color: "#ffffff"
                    text: qsTr("Anthony Perez")
                    font.pointSize: 10
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                    horizontalAlignment: Text.AlignRight
                }

                Label {
                    id: label4
                    color: "#ffffff"
                    text: qsTr("Javier Rodriguez")
                    font.pointSize: 10
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                }

                Label {
                    id: label5
                    color: "#ffffff"
                    text: qsTr("Jose Martinez")
                    font.pointSize: 10
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                }

                Label {
                    id: label6
                    color: "#ffffff"
                    text: qsTr("Michael Montalvan")
                    font.pointSize: 10
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                }
            }

            Label {
                id: label7
                color: "#ffffff"
                text: qsTr("Mentor:")
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                font.bold: true
                font.pointSize: 9
            }

            Label {
                id: label8
                color: "#ffffff"
                text: qsTr("Dr. Alexander Pons")
                font.pointSize: 10
            }


        }
    }

}
