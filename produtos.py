from apoio import Apoio
from tkinter import Tk,Toplevel, Frame
from tkinter.ttk import Treeview

class Cadprodutos(Apoio):
    def __init__(self):
        self.janelaprodutos = Toplevel()
        self.padroes()
        self.telaprodutos()
        #self.frmprodutos()
        self.janelaprodutos.mainloop()

    def telaprodutos(self):
        self.janelaprodutos.title('Cadastro de Produtos')
        self.janelaprodutos.geometry('700x400+400+200')
        self.janelaprodutos.grab_set()
        self.janelaprodutos.anchor
        self.frameprodutos()

    def frameprodutos(self):
        self.frmprodutos = Frame(self.janelaprodutos, bg=self.corframe1)
        self.frmprodutos.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)

