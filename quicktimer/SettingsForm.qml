import QtQuick 2.4
import QtQuick.Controls 2.0
import QtQuick.Extras 1.4
import QtQuick.Layouts 1.0
import QtQuick.LocalStorage 2.0
import "storage.js" as Settings


PageBackground {
    id: settingsform
    width: 640
    border.width: 0
    title: "Settings"

    function storeSettings() { // executed maybe on destruction 
        Settings.set("survey_name", surveyName.text)
        Settings.set("slide_length", parseInt(Math.round(sliderSetLength.value)))
        Settings.set("survey_enabled", toggleSurvey.checked)
        storeButton.text = "Saved!"
    }

   RowLayout {
        y: 83
        width: 514
        height: 40
        transformOrigin: Item.Center
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.leftMargin: 40
        anchors.left: parent.left
        spacing: 6

        Switch {
            id: toggleSurvey
            text: "Enable Survey"
            checked: Settings.get("survey_enabled", false)
            z: 2
            Layout.preferredHeight: 40
            Layout.preferredWidth: 200
            font.bold: true
            font.weight: Font.Bold
            enabled: true
            font.pointSize: 12


            contentItem: Text {
                wrapMode: Text.NoWrap
                font: toggleSurvey.font
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignVCenter

                color: "white"
                text: "Enable Survey"
            }
        }

        TextField {
            id: surveyName
            x: 226
            text: Settings.get("survey_name", "SurveyName")
            font.capitalization: Font.AllLowercase
            opacity: toggleSurvey.checked ? 1.0 : 0.0
            font.pointSize: 12
            horizontalAlignment: Text.AlignHCenter
            onTextChanged: {
                storeButton.text = "Save"
            }
        }
    }


    Slider {
        id: sliderSetLength
        x: 40
        y: 182
        width: 560
        height: 48
        stepSize: 1
        to: 300
        value: (Settings.get("slide_length", 100))


    }

    Label {
        id: label
        x: 40
        y: 157
        text: qsTr("Slide Length:")
        font.bold: true
        font.pointSize: 12
        color: "white"
    }

    Label {
        id: slideLength
        x: 271
        y: 231
        width: 34
        height: 19
        font.bold: true
        font.pointSize: 12
        text: Math.round(sliderSetLength.value)
        color: "white"
        horizontalAlignment: Text.AlignRight
        anchors.horizontalCenterOffset: -116
        anchors.verticalCenterOffset: -73
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        padding: 0
        font.letterSpacing: 0
        font.wordSpacing: 5
        onTextChanged: {
            storeButton.text = "Save"
        }
    }

    Label {
        id: label1
        x: 227
        y: 157
        text: qsTr("Seconds")
        font.bold: true
        font.pointSize: 12
        color: "white"
    }

    MyButton {
        id: storeButton
        x: 486
        y: 384
        text: "Save"
        onClicked: {
            storeSettings()

        }

    }

}
