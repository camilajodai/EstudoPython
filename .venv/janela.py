import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class janela(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Minha Janela")
        self.setGeometry(10,20,600,400)
        
        
app = QApplication(sys.argv)
tela = janela()
tela.show()
app.exec_()