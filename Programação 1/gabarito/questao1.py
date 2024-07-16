import math

def areaFx(inicio,fim,fx,dx):
    area=0
    base=dx #a base é constante
    x=inicio
    while x<fim:
        altura=math.fabs(fx(x)) #evita área negativa
        area+=base*altura
        x+=dx
    return area

def func1grau(x): return 2*x+10
def func2grau(x): return x*x+2*x-10
def funcSeno(x): return math.sin(x)
def funcConst10(x): return 10

if __name__=="__main__":
    inicio=0
    fim=10
    dx=0.0001
    print(f'Início = {inicio}, Fim = {fim}, delta x = {dx}')
    print(f'Área 1º grau = {areaFx(inicio,fim,func1grau,dx)}')
    print(f'Área 2º grau = {areaFx(inicio,fim,func2grau,dx)}')
    print(f'Área Seno = {areaFx(inicio,fim,funcSeno,dx)}')
    print(f'Área Cte = {areaFx(inicio,fim,funcConst10,dx)}')
