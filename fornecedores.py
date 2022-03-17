from tkinter import Tk,Toplevel
from tkinter.ttk import Treeview, Frame
class Fornecedores:
    def __init__(self):
        self.fornecedores = Tk()
    def tela(self):
        self.pedidos.title('Sistema de Registro para pedidos Farmácia Nova')
        self.pedidos.geometry('800x400+300+100')
        self.frameprincipal()

    def framefornecedor(self):
        self.frmFornecedor = Frame(self.fornecedores, bg=self.corframe2)
