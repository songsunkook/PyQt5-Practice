import sys
from Color import Color
from PyQt5.QtWidgets import *

class MyApp(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    btn1 = QPushButton('quit',self)
    btn1.resize(btn1.sizeHint())
    btn1.move(50,50)
    btn2 = QPushButton('ddd',self)
    btn2.resize(btn2.sizeHint())
    btn2.move(100,50)
 #   layout = QVBoxLayout()
 #   layout.addWidget(QLabel('red',self))
 #   layout.addWidget(QLabel('blue',self))
 #   layout.addWidget(QLabel('green',self))
 #   layout.addWidget(Color('red'))
 #   layout.addWidget(Color('green'))
 #   layout.addWidget(Color('blue'))
 #   layout.addWidget(btn1)
 #   layout.addWidget(btn2)
 #   widget=QWidget()
 #   widget.setLayout(layout)
 #   self.setCentralWidget(widget)

    self.setWindowTitle("ddd")
    self.move(300,300)
    self.resize(400,200)
    self.show()

app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec())