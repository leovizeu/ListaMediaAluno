from tkinter import *
from tkinter import ttk
import pandas as pd

janela = Tk()
principal = PrincipalRAD(janela)
janela.title('Cálculo de Média')
janela.geometry('820x600+10+10')
janela.mainloop()

class PrincipalRAD:
    def __init__(self, win):
        #componentes
        self.lblNome=tk.Label(win, text='Nome do Aluno:')
        self.lblNota1=tk.Label(win, text='Nota 1:')
        self.lblNota2=tk.Label(win, text='Nota 2:')
        self.lblMedia=tk.Label(win, text='Média:')
        self.txtNome=tk.Entry(bd=3)
        self.txtNota1=tk.Entry()
        self.txtNota2=tk.Entry()
        self.btnCalcular=tk.Button(win, text='Calcular Média', command=self.calcularMedia)
        #Componentes da Treeview
        self.dadosColunas = ('Aluno', 'Nota 1', 'Nota 2', 'Média', 'Situação')
        self.treeMedias = ttk.Treeview(win, 
                                       columns=self.dadosColunas, 
                                       selectMode='browse')
        self.verscrlbar = ttk.Scrollbar(win, 
                                        orient="vertical", 
                                        command=self.treeMedias.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)