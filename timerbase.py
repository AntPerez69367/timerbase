from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import bluetooth


class TimerBase(QObject):
    def __init__(self):
        QObject.__init__(self)

    updateStatus = pyqtSignal(str, arguments=['status'])

    @pyqtSlot(str, str, str)
    def startClicked(self, arg1, arg2, arg3):
        print("Clicked Start: " + arg1)
        time = arg1.split(":")
        time = list(map(int, time))
        print(arg2 + " " + arg3)

        # print(time)
        self.updateStatus.emit("Connected")

    @pyqtSlot()
    def stopClicked(self):
        print("Clicked Stop")
        self.updateStatus.emit("Disconnected")

    # Bluetooth Functions
    def findTimer(self):
        target = "btTimer"
        target_address = None

        # look for nearby bluetooth devices
        nearby_devices = bluetooth.discover_devices()

        # check to see if any of the devices match the target
        for bdaddr in nearby_devices:
            if target == bluetooth.lookup_name(bdaddr):
                target_address = bdaddr
                break

        # if it does match return the address, if not return nothing
        if target_address is not None:
            print("found target device with addres ", target_address)
            return target_address
        else:
            print("could not find bluetooth device")
            return None

        # send the time to the timer
    def sendTime(self, value, bdaddr):
        # To do
        port = 1

        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((bdaddr, port))

        except bluetooth.btcommon.BluetoothError as err:
            # Error handler TO DO
            print(err)
            pass

        # send timer data
        # sock.send("Timer stuff here ")


# Main Function
if __name__ == "__main__":
    import sys

    # Create an instance of the application
    app = QGuiApplication(sys.argv)

    # Create a calculator object
    timerbase = TimerBase()

    # Create QML engine
    engine = QQmlApplicationEngine()

    # Create Context
    ctx = engine.rootContext()

    # And register it in the context of QML
    ctx.setContextProperty("timerbase", timerbase)

    # Load the qml file into the engine
    engine.load("quicktimer/main.qml")

    # Exit the program
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
