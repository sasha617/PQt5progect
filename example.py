from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

app=QApplication([])

window=QWidget()
window.setWindowTitle('Перша програма')


window.setWindowIcon(QIcon('icons8-ace-of-hearts-32.png'))
window.setStyleSheet('beckground-color:	#90EE90;')


window.resize(1300,1300)
window.move(200,250)


window.show()

app.exec_()

