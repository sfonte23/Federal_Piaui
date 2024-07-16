from questao4 import lerArquivo

def buscarCurso(dicionario, curso):
    for matricula in dicionario:#dicionario == 'matricula':[nome,curso]
#        print(dicionario[matricula]) 
        if dicionario[matricula][1].upper()==curso.upper():
            nome=dicionario[matricula][0]
            curso=dicionario[matricula][1]
            print(matricula,nome,curso)

'''
Faça uma função que dado um dicionário que armazena o nome, matrícula e o curso de alunos,
retorna todos os dados dos alunos de um determinado curso.
'''
if __name__=="__main__":
    dicionario=lerArquivo()
    buscarCurso(dicionario,"CSTGD")

''' Por segurança. Sei que irei apagar o arquivo dados.txt nos testes.
11,Wener,CSTGD	
22,Arlino,LC	
33,Ramon,SI	
44,Ivenilton,CSTGD	
55,Imperes,CSTGD
66,Keylla,CC	

'''