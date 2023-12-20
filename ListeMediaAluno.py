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