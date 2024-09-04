# Curso de Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 03/09/24
import os

class Retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    
    def calcular(self, altura, largura):
        perimetro = (altura + largura)*2
        
        return perimetro
    
os.system('cls')

print('/'*70)
print('Calcular o  de um rêntangulo')
print('='*70)

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

resposta = Retangulo(altura, largura)
resultado = resposta.calcular(altura, largura)

print('')
print(f'Seu retangulo possui {resultado:.4f} de pêrimetro')
print('')
print('/'*70)