import os

def limparTela(): #perfumaria pra deixar "bunitin"
    nomeSistOp= os.name
    if nomeSistOp == 'nt':
        os.system('cls') #windows
    else:
        os.system('clear') #outros

def receberDados(lista):
    matricula=input('Informe a matricula do aluno:')
    nome=input('Informe o nome do aluno:')
    curso=input('Informe o nome do curso:')
    lista.append([matricula,nome,curso])

def escreverArquivo(texto):
    arq = open("dados.txt",'w')
    arq.write(texto)
    arq.close()


def exec():
    teclasValidas='SNsn'
    lista=[]

    continuar=True
    while continuar: #verifica se o usuário quer novo cadastro
        limparTela()
        receberDados(lista)
        ehTeclaInvalida=True
        while ehTeclaInvalida: #verifica se pressiou tecla s ou n
            tecla=input('Deseja continuar [S/N]?')
            if tecla in teclasValidas: #se pressionou s ou n
                ehTeclaInvalida=False
                if tecla in 'sS':
                    continuar=True
                    print("Acrescentando mais um cadastro.")
                else:
                    continuar=False
                    print("Finalizando cadastro.")
            else:
                ehTeclaInvalida=True
                print("Tecla inválida! Tente Novamente.")

    relatorio=""
    for v in lista: #relatório
       relatorio+=(f'{v[0]},{v[1]},{v[2]}\n')

    print(relatorio)
    escreverArquivo(relatorio)
    print('Arquivo gravado com sucesso!')

'''
Faça um programa que recebe e armazena o nome, matrícula e o curso de alunos em uma lista.
Após armazenar, o programa deve gravar todos os dados num arquivo dados.txt.
'''
if __name__=="__main__":
    exec()