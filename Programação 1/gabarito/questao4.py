import os
from questao3 import limparTela

def lerArquivo():
    arq = open("dados.txt",'r')
    lista=arq.readlines()
    arq.close()
    dicionario=dict()

    #converte os dados da string para dicionário
    for linha in lista:
        dados=linha.split(',') #dados separados por vírgula
        dicionario[dados[0]]=[dados[1],dados[2].strip()] # strip() retira o \t \n e demais caracteres de 'espaço'
    return dicionario

'''
Faça um programa que lê um arquivo chamado dados.txt, que armazena o nome, matrícula e o curso de alunos.
Esses dados devem ser carregados em um dicionário.
'''
if __name__=="__main__":
    print(lerArquivo())