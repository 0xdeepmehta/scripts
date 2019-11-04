import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
app = QApplication(sys.argv)
root = QWidget()
root.resize(320, 240)
root.setWindowTitle("Hello PyQt5")
btn = QPushButton("Hello", root)
btn.setToolTip("Click Me")
btn.move(100, 70)
root.show()
