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

# criando função entrar valores
def entrar_valores(): 
    resultado = eval('9/9')
    
    #passando o valor para tela
    valor_texto.set(resultado) # chamamos a váriavel que recebe valores dinamicamentes.


#criando a label
valor_texto = StringVar() #Alterando o valor de uma label, criando variável que recebe valores de strings dinamicamentes.

app_label = Label(frame_tela, textvariable =valor_texto, width=16, height=2, padx=7, relief= FLAT, anchor='e', justify= RIGHT, font=('Ivy 16'),bg = cor3, fg=cor2) #exibir texto, altura e largura, espaço entre janela,
app_label.place(x=0, y=0) #executando tela, localização da tela, valor_texto variável que recebe o valor de strings dinamicamentes

#criando os botões

b_1 = Button(frame_corpo, text= 'C', width=11, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão clear
b_1.place(x=0, y=0) #executando tela, localização da tela
b_2 = Button(frame_corpo, text= '%', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão módulo
b_2.place(x=118, y=0) #executando tela, localização da tela
b_3 = Button(frame_corpo, text= '/', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão disão
b_3.place(x=177, y=0) #executando tela, localização da tela

b_4 = Button(frame_corpo, text= '7', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão sete
b_4.place(x=0, y=52) #executando tela, localização da tela
b_5 = Button(frame_corpo, text= '8', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão oito
b_5.place(x=59, y=52) #executando tela, localização da tela
b_6 = Button(frame_corpo, text= '9', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão nove
b_6.place(x=118, y=52) #executando tela, localização da tela
b_7 = Button(frame_corpo, text= '*', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão multiplicação
b_7.place(x=177, y=52) #executando tela, localização da tela

b_8 = Button(frame_corpo, text= '4', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão quatro
b_8.place(x=0, y=104) #executando tela, localização da tela
b_9 = Button(frame_corpo, text= '5', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão cinco
b_9.place(x=59, y=104) #executando tela, localização da tela
b_10 = Button(frame_corpo, text= '6', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão seis
b_10.place(x=118, y=104) #executando tela, localização da tela
b_11 = Button(frame_corpo, text= '-', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão menos
b_11.place(x=177, y=104) #executaando tela, localização da tela

b_12 = Button(frame_corpo, text= '1', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão um
b_12.place(x=0, y=156) #executando tela, localização da tela
b_13 = Button(frame_corpo, text= '2', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão dois
b_13.place(x=59, y=156) #executando tela, localização da tela
b_14 = Button(frame_corpo, text= '3', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão trẽs
b_14.place(x=118, y=156) #executando tela, localização da tela
b_15 = Button(frame_corpo, text= '+', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão soma
b_15.place(x=177, y=156) #executando tela, localização da tela

b_16 = Button(frame_corpo, text= '0', width=11, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão zero
b_16.place(x=0, y=208) #executando tela, localização da tela
b_17 = Button(frame_corpo, text= '.', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief= RIDGE) #botão ponto
b_17.place(x=118, y=208) #executando tela, localização da tela
b_18 = Button(frame_corpo, text= '=', width=5, height=2, bg= cor5, fg=cor3,font=('Ivy 13 bold'), relief= RAISED, overrelief= RIDGE) #botão igualdade
b_18.place(x=177, y=208) #executando tela, localização da tela


janela.mainloop() #Executar janela
