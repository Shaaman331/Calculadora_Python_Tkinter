#importando tkinter
from tkinter import *
from tkinter import ttk
from turtle import width
from tkinter import font
#cores
cor1 = '#3b3b2b' #black/preta
cor2 = '#0de0c0'  #green/verde
cor3 = '#38576b' #Azul carregado
cor4 = '#ECEFF1' #grey/cinza
cor5 = '#FFAB40' #orange/laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318') 
janela.config(bg=cor1) #cor de fundo preta

#criando os frames
frame_tela = Frame(janela, width=235, height=50, bg = cor3) #largura , altura janela fundo azul
frame_tela.grid(row=0, column=0) #linha, coluna

frame_corpo = Frame(janela, width=235, height=268) #largura , altura
frame_corpo.grid(row=1, column=0) #linha, coluna

# variavel global todos_valores onde são armazenados os valores digitados na tela
todos_valores = ''

#criando a label
valor_texto = StringVar() #Alterando o valor de uma label, criando variável que recebe valores de strings dinamicamentes.

# criando função entrar valores
def entrar_valores(event): # criando evento onde passa todos os valores 
    
    global todos_valores # todos os valores passam a ser executados na tela
    
    todos_valores = todos_valores + str(event) 
    
    #passando o valor para tela
    valor_texto.set(todos_valores) # chamamos a váriavel que recebe valores dinamicamentes.

# criando função para calcular 
def calcular():
    global todos_valores # declaramos variável global para manter todos os valoes em todas funções todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado)) #apresentar resultado somente na calculadora
    todos_valores = str(resultado)
#criando função para limpar tela
def limpar_tela():
    global todos_valores # declaramos variável global para manter todos valores em todas funções todos_valores
    todos_valores = ''
    valor_texto.set('')
    

app_label = Label(frame_tela, textvariable =valor_texto, width=16, height=2, padx=7, relief= FLAT, anchor='e', justify= RIGHT, font=('Ivy 16'),bg = cor3, fg=cor2) #exibir texto, altura e largura, espaço entre janela,
app_label.place(x=0, y=0) #executando tela, localização da tela, valor_texto variável que recebe o valor de strings dinamicamentes

#criando os botões

b_1 = Button(frame_corpo,command= limpar_tela, text= 'C', width=11, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão clear
b_1.place(x=0, y=0) #executando tela, localização da tela
b_2 = Button(frame_corpo, command= lambda :entrar_valores('%'), text= '%', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão módulo
b_2.place(x=118, y=0) #executando tela, localização da tela, integrando valores com a função lambda 
b_3 = Button(frame_corpo, command= lambda :entrar_valores('/'),text= '/', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão disão
b_3.place(x=177, y=0) #executando tela, localização da tela, integrando valores com a função lambda

b_4 = Button(frame_corpo, command= lambda :entrar_valores('7'),text= '7', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão sete
b_4.place(x=0, y=52) #executando tela, localização da tela, integrando valores com a função lambda
b_5 = Button(frame_corpo, command= lambda :entrar_valores('8'),text= '8', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão oito
b_5.place(x=59, y=52) #executando tela, localização da tela, integrando valores com a função lambda
b_6 = Button(frame_corpo, command= lambda :entrar_valores('9'),text= '9', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão nove
b_6.place(x=118, y=52) #executando tela, localização da tela, integrando valores com função lambda
b_7 = Button(frame_corpo, command= lambda :entrar_valores('*'),text= '*', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão multiplicação
b_7.place(x=177, y=52) #executando tela, localização da tela, integrando valores com a função lambda

b_8 = Button(frame_corpo, command= lambda :entrar_valores('4'),text= '4', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão quatro
b_8.place(x=0, y=104) #executando tela, localização da tela, integrando valores com a função lambda
b_9 = Button(frame_corpo, command= lambda :entrar_valores('5'),text= '5', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão cinco
b_9.place(x=59, y=104) #executando tela, localização da tela, integrando valores com a função lambda
b_10 = Button(frame_corpo, command= lambda :entrar_valores('6'),text= '6', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão seis
b_10.place(x=118, y=104) #executando tela, localização da tela, integrando valores com a função lambda
b_11 = Button(frame_corpo, command= lambda :entrar_valores('-'),text= '-', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão menos
b_11.place(x=177, y=104) #executaando tela, localização da tela, integrando valores com a função lambda

b_12 = Button(frame_corpo, command= lambda :entrar_valores('1'),text= '1', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão um
b_12.place(x=0, y=156) #executando tela, localização da tela, integrando valores com a função lambda
b_13 = Button(frame_corpo, command= lambda :entrar_valores('2'),text= '2', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão dois
b_13.place(x=59, y=156) #executando tela, localização da tela, integrando valores com a função lambda
b_14 = Button(frame_corpo, command= lambda :entrar_valores('3'),text= '3', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão trẽs
b_14.place(x=118, y=156) #executando tela, localização da tela, integrando valores com a função lambda
b_15 = Button(frame_corpo, command= lambda :entrar_valores('+'),text= '+', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão soma
b_15.place(x=177, y=156) #executando tela, localização da tela, integrando valores com a função lambda

b_16 = Button(frame_corpo, command= lambda :entrar_valores('0'),text= '0', width=11, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão zero
b_16.place(x=0, y=208) #executando tela, localização da tela, integrando valores com a função lambda
b_17 = Button(frame_corpo, command= lambda :entrar_valores('.'),text= '.', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão ponto
b_17.place(x=118, y=208) #executando tela, localização da tela, integrando valores com a função lambda
b_18 = Button(frame_corpo, command= calcular,text= '=', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão igualdade
b_18.place(x=177, y=208) #executando tela, localização da tela, integrando valores com a função calcular


janela.mainloop() #Executar janela
