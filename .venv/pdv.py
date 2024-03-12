# este programa exibe uma janela de pdv (ponto de venda), neste pdv estamos demonstrando um caixa de uma padaria
# vamos importar a biblioteca de sistema para executar a janela
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QTableWidget,QTableWidgetItem,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QPixmap

class PDV(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(5,50,1580,800)
        self.setWindowTitle("Caixa PDV - Padaria Legal")
        
        
        # criacao do layout principal que irá dividir a tela em duas colunas onde a coluna da esquerda terá uma label e a coluna da direita terá outra label
        layout_hor_principal = QHBoxLayout()
        
        # vamos criar duas labels que representarão as colunas sendo uma label coluna da esquerda e a outra da direita
        label_col_esquerda = QLabel()
        label_col_direita = QLabel()
        
        # configurar a largura e a cor de fundo da coluna da esquerda
        label_col_esquerda.setStyleSheet("QLabel{background-color:#CF9259}")
        label_col_esquerda.setFixedWidth(790)
        
        label_col_direita.setStyleSheet("QLabel{background-color:#CF9259}")
        label_col_direita.setFixedWidth(790)
        
        # vamos adicionar as duas labels a tela
        layout_hor_principal.addWidget(label_col_esquerda)
        layout_hor_principal.addWidget(label_col_direita)
        
        # adicionar o layout prinipal a tela
        self.setLayout(layout_hor_principal)
        
        # --------------------------------------------------------------------------------------------------------------
        # trabalhando com a coluna da esquerda
        # definir o layout vertical da coluna da esquerda
        layout_ver_col_esquerda = QVBoxLayout()
        
        # criar uma label para adicionar uma imagem
        label_img = QLabel()
        label_img.setPixmap(QPixmap("padaria.jpg"))
        # ajudar o tamanho da imagem ao tamanho da label
        label_img.setScaledContents(True)
        
        # adicionar a label que está com a imagem ao layout da esquerda
        layout_ver_col_esquerda.addWidget(label_img)
        
        label_codigo = QLabel("Código do produto:")
        label_codigo.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_codigo)
        
        edit_codigo = QLineEdit()
        edit_codigo.setStyleSheet("QLineEdit{padding: 10px; font-size:15pt}")  
        layout_ver_col_esquerda.addWidget(edit_codigo)
        # ----------------------------------------------------------------
        label_nome = QLabel("Nome do produto:")
        label_nome.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_nome)
        
        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{padding: 10px; font-size:15pt}")  
        layout_ver_col_esquerda.addWidget(edit_nome)
        # ----------------------------------------------------------------
        label_descricao = QLabel("Descrição do produto:")
        label_descricao.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_descricao)
        
        edit_descricao = QLineEdit()
        edit_descricao.setStyleSheet("QLineEdit{padding: 10px; font-size:15pt}")  
        edit_descricao.setFixedHeight(120)
        layout_ver_col_esquerda.addWidget(edit_descricao)
        # ----------------------------------------------------------------
        label_qnt = QLabel("Quantidade do produto:")
        label_qnt.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_qnt)
        
        edit_qnt = QLineEdit()
        edit_qnt.setStyleSheet("QLineEdit{padding: 10px; font-size:15pt}")  
        layout_ver_col_esquerda.addWidget(edit_qnt)
        # ----------------------------------------------------------------
        label_preco = QLabel("Preço Unitário do produto:")
        label_preco.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_preco)
        
        edit_preco = QLineEdit()
        edit_preco.setStyleSheet("QLineEdit{padding: 10px; font-size:15pt}")  
        layout_ver_col_esquerda.addWidget(edit_preco)
        # ----------------------------------------------------------------
        label_subt = QLabel("Sub Total do produto:")
        label_subt.setStyleSheet("QLabel{font-size:15pt; color:white}")
        layout_ver_col_esquerda.addWidget(label_subt)
        
        edit_subt = QLineEdit("Tecle F3 para calcular o subtotal")
        edit_subt.setStyleSheet("QLineEdit{padding: 10px; font-size:15pt}")  
        edit_subt.setEnabled(False)
        layout_ver_col_esquerda.addWidget(edit_subt)
            
        # ----------------------------------------------------------------
        #vms trabalhar c a coluna direita
        tabela = QTableWidget()
        # vms definira qnt de linhas e colunas
        tabela.setColumnCount(5)
        tabela.setRowCount(10)
        # definir o cabeçalho das colunas
        cabecalho = ["Código","Nome do produto","Quantidade","Preço unitário","Preço Total"]
        # Add o cabeçalho na tabela
        tabela.setHorizontalHeaderLabels(cabecalho)
        
        # adicionar no layout da direita
        layout_ver_col_direita = QVBoxLayout()
        layout_ver_col_direita.addWidget(tabela)
        label_col_direita.setLayout(layout_ver_col_direita)
            
        label_total = QLabel("Total a pagar:")
        label_total.setStyleSheet("QLabel{font-size:25pt;color:White}")
        layout_ver_col_direita.addWidget(label_total)
        
        edit_total = QLineEdit("0,00")
        edit_total.setStyleSheet("QLineEdit{padding: 20px; font-size:30pt}")
        edit_total.setEnabled(False)
        layout_ver_col_direita.addWidget(edit_total)
            
        # vamos adicionar o layout vertical da esquerda a label da coluna da esquerda
        label_col_esquerda.setLayout(layout_ver_col_esquerda)
        
        
        
app = QApplication(sys.argv)
janela = PDV()
janela.show()
app.exec_()