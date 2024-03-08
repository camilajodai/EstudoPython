import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton,QVBoxLayout

class janelacontroles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(15,20,500,400)
        
        #criar um layout p organizar os componentes
        layout = QVBoxLayout()
        
        
        #label p o título da janela
        label_titulo = QLabel("Gerenciar os Clientes")
        label_titulo.setStyleSheet("QLabel{font-size: 30pt;color:#600;font-weight:bold}")
        
        #criar elementos de texto p pedir ao usuario c dados dos clientes, criaremos as labels
        label_nome = QLabel("Nome do Cliente: ")
        label_nome.setStyleSheet("QLabel{font-size: 15pt;color:#000;font-weight:bold}")
        label_email = QLabel("E-mail: ")
        label_email.setStyleSheet("QLabel{font-size: 15pt;color:#000;font-weight:bold}")
        label_telefone = QLabel("Telefone: ")
        label_telefone.setStyleSheet("QLabel{font-size: 15pt;color:#000;font-weight:bold}")
        
        #criar elementos p q os usuarios possam escrever o que as labels estao pedindo
        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{font-size: 15pt;padding:10px;border-radius:10px}")
        edit_email = QLineEdit()
        edit_email.setStyleSheet("QLineEdit{font-size: 15pt;padding:10px;border-radius:10px}")
        edit_telefone = QLineEdit()
        edit_telefone.setStyleSheet("QLineEdit{font-size: 15pt;padding:10px;border-radius:10px}")
        
        #criar um controle de botao p realizar um possivel cadastro
        btn_cadastro = QPushButton("Cadastrar")
        
        layout.addWidget(label_titulo)
        #add os controles de label e edit ao layout
        layout.addWidget(label_nome)
        layout.addWidget(edit_nome)
        
        layout.addWidget(label_email)
        layout.addWidget(edit_email)
        
        layout.addWidget(label_telefone)
        layout.addWidget(edit_telefone)
        
        layout.addWidget(btn_cadastro)
        
        #layoout na janela
        self.setLayout(layout) 
        
app = QApplication(sys.argv)
tela = janelacontroles()
tela.show()
app.exec_()
        