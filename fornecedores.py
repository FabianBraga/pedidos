from apoio import Apoio
from tkinter import Tk,Toplevel, Frame
from tkinter.ttk import Treeview

class Cadfornecedores(Apoio):
    def __init__(self):
        self.janelafornecedor = Toplevel()
        self.padroes()
        self.telafornecedor()
        #self.frmFornecedor()
        self.janelafornecedor.mainloop()

    def telafornecedor(self):
        self.janelafornecedor.title('Cadastro de fornecedores')
        self.janelafornecedor.geometry('700x400+400+200')
        self.framefornecedor()

    def framefornecedor(self):
        self.frmFornecedor = Frame(self.janelafornecedor, bg=self.corframe2)
        self.frmFornecedor.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)

if __name__ == '__main__':
    b = Cadfornecedores()
