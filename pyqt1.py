import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
app=QApplication([]) #create instance
w= QWidget()
w.setWindowTitle("Pyqt First app")
w.setGeometry(100,100,280,180)
hellomsg= QLabel("<h1> HELLO WORLD</h1>",parent =w)
hellomsg.move(60,15)
w.show()
sys.exit(app.exec())
