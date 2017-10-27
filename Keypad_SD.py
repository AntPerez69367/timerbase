import sys, math
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

		self.start_button.clicked.connect(self.startTimer)
		#// self.**buttonname**.clicked.connect(self.**functionname**)
		
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
		#get the time from value_box
		#convert the time to hours:mins:seconds
		#send the time 
		time = []
		str1 = self.value_box.toPlainText()
		str1 = int(str1)
		self.clear()
		time = self.convertTime(str1)

		hours = str(time[0])
		mins = str(time[1])
		secs = str(time[2])
		# hh:mm:ss
		self.label1.setText(hours + ":" + mins + ":" + secs)



		#self.convertTime(str)
		## To do
		
		## send the stop command
	def convertTime(self, inputtime):
		print(inputtime)
		#convert input time to seconds, minutes and hours
		# return array with time
		
		# 13050
		# 1  30  50
		# 13050 / 10000 = hours
		# 13050-(hours * 10000)  
		# 3050  / 100 = minutes 
		# 3050 - (minutes * 100)
		# 50 = seconds
		hours = math.floor(inputtime / 10000)
		inputtime = inputtime - (hours * 10000)
		minutes = math.floor(inputtime / 100)
		seconds = inputtime - (minutes*100)

		time = [hours, minutes, seconds]
		print (time)

		##validate the time and make sure its HH MM SS 
		return time

	def validateTime(self, time):
		pass	

	def stopTimer(self):
		pass
		## To do


		
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	display = []
	sys.exit(app.exec_())
