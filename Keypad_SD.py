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
        def home(self):
        btn = QtGui.StartButton("Start", self)
        btn.clicked.connect(self.start_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
    self.show()
    
    def start_application(self):
        sys.start()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.start(app.exec_())


run()

# Trying to set and stop and resert the time with this code

    
    def __init__(self):
        QtGui.QKeypad_SD.__init__(self)
        self.initUI()
    
    def initUI(self):
        
        self.timer = QtCore.QTimer(self)
        
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.setDigitCount(8)
        
        self.time = QtGui.QTimeEdit(self)
        self.timer.timeout.connect(self.Time)
        
        self.set = QtGui.QPushButton("Set",self)
        self.set.clicked.connect(self.Set)
        
        self.stop = QtGui.QPushButton("Stop",self)
        self.stop.clicked.connect(lambda: self.timer.stop())
        
        grid = QtGui.QGridLayout(self)
        
        grid.addWidget(self.lcd,3,0)
        grid.addWidget(self.time,0,0)
        grid.addWidget(self.set,1,0)
        grid.addWidget(self.stop,2,0)
        
        centralwidget = QtGui.QWidget()
        
        self.setCentralWidget(centralwidget)
        
        centralwidget.setLayout(grid)
            
            self.setGeometry(300,300,280,170)
    
def Set(self):
    global t,h,m,s
        
        t = self.time.time()
        self.lcd.display(t.toString())
        
        self.timer.start(1000)
        
        h = t.hour()
        m = t.minute()
        s = t.second()
    
    def Time(self):
        global t,h,m,s
        
        if s > 0:
            s -=1
        else:
            if m > 0:
                m -= 1
                s = 59
            elif m == 0 and h > 0:
                h -= 1
                m = 59
                s = 59
            else:
                self.timer.stop()

    stop = QtGui.QEnterPTTime.warning(self,"Time is up","Time is up")
        
        time = ("{0}:{1}:{2}".format(h,m,s))
        
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)

def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


		pass
    
		
		
		## send the stop command
	def stopTimer(self):
		pass
		## To do


        ## Progress Bar
self.progress = QtGui.QProgressBar(self)
    self.progress.setGeometry(200, 80, 250, 20)
    
    self.btn = QtGui.QPushButton("Time",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)
        
        self.show()
    
    
    def download(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)



def enlarge_window(self, state):
    if state == QtCore.Qt.Checked:
        self.setGeometry(50,50, 1000, 600)
        else:
        self.setGeometry(50, 50, 500, 300)
		
if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   window = MyApp()
   window.show()
   display = []
   sys.exit(app.exec_())
