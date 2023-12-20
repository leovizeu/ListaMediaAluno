import tkinter as tk
from tkinter import END, ttk
import pandas as pd

class principal_rad:
    def __init__(self, win):
        #componentes
        self.lbl_nome=tk.Label(win, text='Nome: ')
        self.lbl_nota1=tk.Label(win, text='Nota 1:')
        self.lbl_nota2=tk.Label(win, text='Nota 2:')
        self.lbl_media=tk.Label(win, text='Média:')
        self.txt_nome=tk.Entry(bd=3)
        self.txt_nota1=tk.Entry()
        self.txt_nota2=tk.Entry()
        self.btn_calcular=tk.Button(win, text='Calcular Média', command=self.calcular_media)
        #Componentes da Treeview
        self.dados_colunas = ('Aluno', 'Nota 1', 'Nota 2', 'Média', 'Situação')
        
        self.tree_medias = ttk.Treeview(win, 
                                       columns=self.dados_colunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.tree_medias.yview)
        
        self.verscrlbar.pack(side ='right', fill ='x')
        
        self.tree_medias.configure(yscrollcommand=self.verscrlbar.set)
        
        self.tree_medias.heading("Aluno", text="Aluno")
        self.tree_medias.heading("Nota 1", text="Nota 1")
        self.tree_medias.heading("Nota 2", text="Nota 2")
        self.tree_medias.heading("Média", text="Média")
        self.tree_medias.heading("Situação", text="Situação")
        

        self.tree_medias.column("Aluno",minwidth=0,width=100)
        self.tree_medias.column("Nota 1",minwidth=0,width=100)
        self.tree_medias.column("Nota 2",minwidth=0,width=100)
        self.tree_medias.column("Média",minwidth=0,width=100)
        self.tree_medias.column("Situação",minwidth=0,width=100)

        self.tree_medias.pack(padx=10, pady=10)
        
        #Posicionamento dos componentes na janela
        
        self.lbl_nome.place(x=100, y=50)
        self.txt_nome.place(x=200, y=50)
        
        self.lbl_nota1.place(x=100, y=100)
        self.txt_nota1.place(x=200, y=100)
        
        self.lbl_nota2.place(x=100, y=150)
        self.txt_nota2.place(x=200, y=150)
        
        self.btn_calcular.place(x=100, y=200)
        
        self.tree_medias.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=250)
        
        self.id = 0
        self.iid = 0
        
        self.carregar_dados_iniciais ()
        
#-----------------------------------------------------------------------------
        
    def carregar_dados_iniciais(self):
        try:
            fsave = 'planilhaAlunos.xlsx'
            dados = pd.read_excel(fsave)
            nn=len(dados['Aluno'])
            for i in range(nn):
                nome = dados['Aluno'][i]
                nota1 = str(dados['Nota 1'][i])
                nota2 = str(dados['Nota 2'][i])
                media = str(dados['Média'][i])
                situacao = dados['Situação'][i]
                self.tree_medias.insert('', END, 
                                    iid=self.iid,
                                    values = (nome, 
                                                nota1, 
                                                nota2,
                                                media,
                                                situacao))
                self.iid = self.iid + 1
                self.id = self.id + 1
        except Exception:
            print("Ainda não existem dados a serem carregados")
            
    #Salvar dados para uma planilha excel
            
    def salvar_dados(self):
      try:          
        fsave = 'planilhaAlunos.xlsx'
        #fsave = 'planilhaAlunos.csv'
        dados=[]
        
        
        for line in self.tree_medias.get_children():
          lstDados=[]
          for value in self.tree_medias.item(line)['values']:
              lstDados.append(value)
              
          dados.append(lstDados)
          
        df = pd.DataFrame(data=dados,columns=self.dados_colunas)
        
        planilha = pd.ExcelWriter(fsave)
        df.to_excel(planilha, 'Inconsistencias', index=False)                
        
        planilha.save()
        print('Dados salvos')
      except Exception:
       print('Não foi possível salvar os dados')   
       
    #Imprime os dados do aluno
        
    def calcular_media(self):
        try:
            nome = self.txt_nome.get()
            nota1 = float(self.txt_nota1.get())
            nota2 = float(self.txt_nota2.get())
            media, situacao = self.verificar_situacao(nota1, nota2)
            self.tree_medias.insert('', END,
                                iid = self.iid,
                                values = (nome, 
                                            nota1, 
                                            nota2,
                                            media,
                                            situacao))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.salvar_dados()
        except Exception:
            print("Entre com valores válidos")
        finally:
            self.txt_nome.delete(0, 'end')
            self.txt_nota1.delete(0, 'end')
            self.txt_nota2.delete(0, 'end')

    #calcula a média e verifica qual é a situação do aluno
    
    def verificar_situacao(self, nota1, nota2):
        media = (nota1 + nota2) / 2
        if (media >= 7):
            situacao = 'Aprovado'
        elif (media >= 5):
            situacao = 'Recuperação'
        else:
            situacao = 'Reprovado'
        
        return media, situacao

janela = tk.Tk()
principal = principal_rad(janela)
janela.title('Cálculo de Média')
janela.geometry('820x600+10+10')
janela.mainloop()