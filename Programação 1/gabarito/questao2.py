import math

def media(vet):
    n=len(vet)
    soma=0
    for vi in vet:
        soma+=vi
    return soma/n

def desvPad(vet, m):
    n=len(vet)
    soma=0
    for vi in vet:
        soma+=math.pow(vi-m,2.0)
    return math.sqrt((1/(n-1)) * soma)


'''
Faça uma função que calcule o desvio padrão de um vetor V contendo n números, dada e expressão abaixo.
Sabendo-se que m é a média do vetor.
'''
if __name__=="__main__":
    vet=[15,8,32,45,7]
    med = media(vet)
    dp = desvPad(vet,med)
    print(f'Média = {med} e desvio padrão = {dp}')

