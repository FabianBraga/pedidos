from tkinter import Button, PhotoImage, Tk, Frame, Label
from fornecedores import Cadfornecedores
from produtos import Cadprodutos
#from bancodedados import Dados
import base64


class Pedidos(Cadfornecedores, Cadprodutos):
    def __init__(self):
        self.pedidos = Tk()
        self.padroes()
        self.tela()
        self.pedidos.mainloop()
    def tela(self):
        self.pedidos.title('Sistema de Registro para pedidos Farmácia Nova')
        self.pedidos.geometry('630x200+300+100')
        self.pedidos.resizable(0,0)
        self.frameprincipal()
    def chamafornecedor(self):
        Cadfornecedores.__init__(self)
    def chamaproduto(self):
        Cadprodutos.__init__(self)
    def frameprincipal(self):
        self.btpedido = PhotoImage(data=base64.b64decode(self.imgpedido))
        self.btpedido = self.btpedido.subsample(4, 4)
        self.btcompras = PhotoImage(data= base64.b64decode(self.imgcompras))
        self.btcompras = self.btcompras.subsample(4, 4)
        self.btfornecedor = PhotoImage(data= base64.b64decode(self.imgfornecedor))
        self.btfornecedor = self.btfornecedor.subsample(4, 4)
        self.btprodutos = PhotoImage(data= base64.b64decode(self.imgprodutos))
        self.btprodutos = self.btprodutos.subsample(4, 4)

        self.frameprincipal = Frame(self.pedidos)
        self.frameprincipal.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)

        self.bt_pedidos = Button(self.frameprincipal, image=self.btpedido, command=self.chamafornecedor)
        self.bt_pedidos.place(x=20, y=20, width=140, height=140)
        self.lb_pedidos = Label(self.frameprincipal, text='Pedidos', bg = self.corframe4, fg = self.corlt2, font= self.fonte12,
        width = 15)
        self.lb_pedidos.place(x=20, y=160)

        self.bt_compras = Button(self.frameprincipal, image=self.btcompras, command=self.chamafornecedor)
        self.bt_compras.place(x=170, y=20, width=140, height=140)
        self.lb_compras = Label(self.frameprincipal, text='Compras', bg = self.corframe4, fg = self.corlt2, font= self.fonte12,
                                width=15)
        self.lb_compras.place(x=170, y=160)

        self.bt_produtos = Button(self.frameprincipal, image=self.btprodutos, command=self.chamaproduto)
        self.bt_produtos.place(x=320, y=20, width=140, height=140)
        self.lb_produtos = Label(self.frameprincipal, text='Produtos', bg = self.corframe4, fg = self.corlt2, font= self.fonte12,
                                width=15)
        self.lb_produtos.place(x=320, y=160)

        self.bt_fornecedor = Button(self.frameprincipal, image=self.btfornecedor, command=self.chamafornecedor)
        self.bt_fornecedor.place(x=470, y=20, width=140, height=140)
        self.lb_fornecedor = Label(self.frameprincipal, text='Fornecedor', bg = self.corframe4, fg = self.corlt2, font= self.fonte12,
        width = 15)
        self.lb_fornecedor.place(x=470, y=160)


if __name__ == '__main__':
    DASH = Pedidos()
