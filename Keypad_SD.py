import sys
from PyQt5 import QtGui, uic, QtWidgets, QtCore

Ui_MainWindow, QtBaseClass = uic.loadUiType("working_keypad.ui")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		
		self.button_0.clicked.connect(self.buttonClicked)
		self.button_1.clicked.connect(self.buttonClicked)
		self.button_2.clicked.connect(self.buttonClicked)
		self.button_3.clicked.connect(self.buttonClicked)
		self.button_4.clicked.connect(self.buttonClicked)
		self.button_5.clicked.connect(self.buttonClicked)
		self.button_6.clicked.connect(self.buttonClicked)
		self.button_7.clicked.connect(self.buttonClicked)
		self.button_8.clicked.connect(self.buttonClicked)
		self.button_9.clicked.connect(self.buttonClicked)
		self.delete_button.clicked.connect(self.clear)
    
    ## test stuff here written by jose blah blah blah code
	
	## anthony was here
		
	def buttonClicked(self):
		clickedButton = self.sender()
		digitValue = int(clickedButton.text())
		
		
		self.value_box.setText(self.value_box.toPlainText() + str(digitValue))

	
	def backspace(self):
		pass
		
	def clear(self):
		self.value_box.clear()
		
	def findTimer(self):
		target = "btTimer"
		target_address = None
		
		# look for nearby bluetooth devices
		nearby_devices = bluetooth.discover_devices()

		# check to see if any of the devices match the target
		for bdaddr in nearby_devices:
			if target == bluetooth.lookup_name( bdaddr ):
				target_address = bdaddr
				break
		
		#if it does match return the address, if not return nothing
		if target_address is not None:
			print ("found target device with addres ", target_address)
			return target_address
		else:
			print ("could not find bluetooth device")
			return None
		
		## send the time to the timer	 
	def sendTime(self, value, bdaddr):
		## To do
		port = 1
		
		try:
			sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
			sock.connect((bdaddr, port))
		
		except bluetooth.btcommon.BluetoothError as err:
			# Error handler TO DO
			pass
		
		#send timer data
		#sock.send("Timer stuff here ")
		# send the start command	
	
	def startTimer(self):
		pass
		## To do
		
		## send the stop command
	def stopTimer(self):
		pass
		## To do
		
if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   window = MyApp()
   window.show()
   display = []
   sys.exit(app.exec_())
