from keyboard import *

from apoio import Apoio
from tkinter import Toplevel, Frame, Label, messagebox, DISABLED, ACTIVE
from tkinter import ttk, END
from tkinter.ttk import Style
from bancopedidos import TbProdutos
from pyautogui import press
from completa import Entautotexto
from awesometkinter import Button3d

class Cadprodutos(Apoio, Entautotexto):
    def __init__(self):
        self.janelaprodutos = Toplevel()
        # self.con =self.abredb(self.host, self.usuario, self.senha, self.banco,3306)
        # if self.con== False:
        #     messagebox('Atenção','Falha ao tentar abrir o banco de dados')
        # self.cursor = self.con.cursor()
        self.padroes()
        self.telaprodutos()
        self.janelaprodutos.mainloop()
    def encerra(self):
        self.janelaprodutos.destroy()
    def telaprodutos(self):
        self.janelaprodutos.title('Cadastro de Produtos')
        self.janelaprodutos.geometry('700x600+400+50')
        self.janelaprodutos.grab_set()
        self.janelaprodutos.anchor
        self.janelaprodutos.protocol("WM_DELETE_WINDOW", self.encerra)

        self.frameprodutos()
    def frameprodutos(self):
        self.corfundo = self.corframe4
        self.frmprodutos = Frame(self.janelaprodutos, bg=self.corfundo)
        self.frmprodutos.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)
        self.labelprodutos()
        self.botoes()

    def labelprodutos(self):
        self.lbbarra = Label(self.frmprodutos, text='Código de barras', font=self.fonte16, bg=self.corfundo, fg=self.corlt2,
                             relief='solid', bd=0)
        self.lbbarra.place(x=10, y=1)
        self.enbarra = ttk.Entry(self.frmprodutos, width=25, font=self.fonte16)
        self.enbarra.place(x=10, y=28)
        self.enbarra.focus()
        self.enbarra.bind('<Return>',self.testebarra)
        self.lbdescricao = Label(self.frmprodutos, text='Descrição', font=self.fonte16, bg=self.corfundo, fg=self.corlt2,
                                 relief='solid', bd=0)
        self.lbdescricao.place(x=10, y=60)

        self.endescricao = ttk.Entry(self.frmprodutos, font=self.fonte16 , width=40)
        self.endescricao.place(x=10, y=88)
        self.endescricao.bind('<Return>',self.proximo)

        self.lbtipo = Label(self.frmprodutos, text='Tipo', font=self.fonte16, bg=self.corfundo, fg=self.corlt2,
                                 relief='solid', bd=0)
        self.lbtipo.place(x=500, y=60)

        lista = ('Ético', 'Generico/Similar', 'HPC')
        self.entipo = ttk.Combobox(self.frmprodutos, width=14, font=self.fonte16, values=lista, validate='key')
        self.entipo.place(x=500, y=88)
        self.entipo.bind('<Return>', self.proximo)
        self.mostra_lista()
    def botoes(self):
        style = Style()
        style.configure('TButton', font=self.fonte10n)

        self.btsalva = Button3d(self.frmprodutos, text='Salvar', bg=self.corfundo, command=self.salvar , state=DISABLED)
        self.btsalva.place(x=10, y=130, width=120, height=35)

        self.btexcluir = Button3d(self.frmprodutos, text='Excluir', bg=self.corfundo, style='TButton', command=self.excluir, state=DISABLED)
        self.btexcluir.place(x=135, y=130, width=120, height=35)
        self.btnovo = Button3d(self.frmprodutos, text='Novo', bg=self.corfundo, command=self.novo)
        self.btnovo.place(x=260, y=130, width=120, height=35)
    def salvar(self):
        if self.endescricao.get() == '':
            if not messagebox.askyesno("Atenção", "A descrição não foi preenchida desseja Proseguir e salvar este registro?"):
                self.endescricao.focus()
                return False
        pesquisa = TbProdutos.select().where(TbProdutos.cod_produto== self.enbarra.get())
        if pesquisa.count != 0:
        #if self.ptab(operacao='p', tabela='tb_produtos', chave='Cod_produto', vlchave=f"'{self.enbarra.get()}'"):
            if messagebox.askyesno("Atenção","Registro existente, gostaria de salvar alterações" ):
                atualiza = TbProdutos.update(medicamento=self.endescricao.get(),
                                             tipo=self.entipo.get(),
                                            ).where((TbProdutos.cod_produto == self.enbarra.get()))
                atualiza.execute()

        # valor = []
                # valor.append(f"'{self.enbarra.get()}'")
                # valor.append(f"'{self.endescricao.get()}'")
                # valor.append(f"'{self.entipo.get()}'")
                # self.ptab(valores=valor, operacao='a', tabela='tb_produtos', campos=['Cod_produto', 'Medicamento', 'Tipo'], chave='Cod_produto',
                #           vlchave= f"'{self.enbarra.get()}'")
        else:
            #valorc = (f"'{self.enbarra.get()}','{self.endescricao.get()}','{self.entipo.get()}'")
            TbProdutos.create(cod_produto=self.enbarra.get(), medicamento=self.endescricao.get(), tipo=self.entipo.get())
            #self.ptab(operacao='c', valores=valorc, tabela='tb_produtos', campos=f'(Cod_produto, Medicamento, Tipo)')

        self.atualizalista()
        self.limpa()
    def excluir(self):
        # if self.ptab(operacao='p', tabela='tb_produtos', chave='Cod_produto', vlchave=f"'{self.enbarra.get()}'"):
        if messagebox.askyesno("Atenção", "O registro será excluido permanentemente desaja proseguir?"):
            linha_excluir = TbProdutos.get(TbProdutos.cod_produto == self.enbarra.get())
            linha_excluir.delete_instance()
            # self.ptab(operacao='e', tabela='tb_produtos', chave='Cod_produto', vlchave=f"'{self.enbarra.get()}'")
        self.atualizalista()
        self.limpa()
        self.enbarra.focus()
    def novo(self):
        self.limpa()
        self.enbarra.focus()
    def limpa(self):
        self.enbarra.delete(0, END)
        self.endescricao.delete(0, END)
        self.entipo.delete(0, END)
        self.btsalva.config(state=DISABLED)
        self.btexcluir.config(state=DISABLED)
        self.enbarra.focus()
    def atualizalista(self):
        # self.con = self.abredb(self.host, self.usuario, self.senha, self.banco, 3306)
        # if self.con == False:
        #     messagebox('Atenção', 'Falha ao tentar abrir o banco de dados')
        # self.cursor = self.con.cursor()
        self.listatv.delete(*self.listatv.get_children())
        # self.cursor.execute('select cod_produto,medicamento,tipo,venda from tb_produtos order by medicamento;')
        dados = TbProdutos.select().order_by(TbProdutos.medicamento).dicts()
        dados = list(dados)
        for x in dados:
            if x =='':
                x='nada'
            self.listatv.insert('', END, values=x)
    def duploclick(self, evento):
        self.limpa()
        self.listatv.selection()
        for x in self.listatv.selection():
            col1, col2, col3, col4 = self.listatv.item(x, 'values')
            self.enbarra.insert(END, col1)
            self.endescricao.insert(END, col2)
            self.entipo.insert(END, col3)
        self.btsalva.config(state=ACTIVE)
        self.btexcluir.config(state=ACTIVE)
    def filtradf(self,condicao):
        pass
    def mostra_lista(self):
        # self.con = self.abredb(self.host, self.usuario, self.senha, self.banco, 3306)
        # if self.con == False:
        #     messagebox('Atenção', 'Falha ao tentar abrir o banco de dados')
        # self.cursor = self.con.cursor()
        # sql = 'select cod_produto,medicamento,tipo,venda from tb_produtos order by medicamento asc'
        # self.cursor.execute(sql)
        res = TbProdutos.select(TbProdutos.cod_produto, TbProdutos.medicamento, TbProdutos.tipo, TbProdutos.venda).dicts()
        self.df = self.geradf(res)
        titulos = ['Código de barras', 'Descrição', 'Tipo', 'venda']
        medida_colunas = [30, 100, 400, 60]
        self.df.columns = titulos
        self.listatv = self.criatreeview(self.frmprodutos, "Relação de produtos", self.corframe1, self.corlt2, self.fonte11,
                                       170, 10, 400, 670, titulos, self.df, medida_colunas, True, True)
        self.listatv.bind("<Double-1>",self.duploclick)
    def proximo(self,evento):
        press(['tab'])
    def testebarra(self, *args):
        if len(self.enbarra.get()) == 0:
            return False
        if self.enbarra.get() in "'\/!@#$%&*(){}[]|":
            messagebox.showwarning("Atenção", "não devem ser usados caracteres especiais  para o código de barras\n'{[(!@#$%¨&*)]}")
            return False
        tabela = TbProdutos.select().where(TbProdutos.cod_produto == self.enbarra.get())
        if tabela.count != 0:
        #if self.ptab(operacao='p', tabela='tb_produtos', chave='Cod_produto', vlchave=f"'{self.enbarra.get()}'"):
            self.endescricao.insert(END, tabela.get().medicamento)
            self.entipo.insert(END, tabela.get().tipo)
            print('passei na validação da barra')
            self.btexcluir.config(state=ACTIVE)
        self.btsalva.config(state=ACTIVE)
        self.enbarra.focus()
        press(['tab'])

