# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 06/09/2024
import os


class Loop:
    def __init__(self, em_loop):
        self.em_loop = em_loop
        
        

class Fparasair(Loop):
    def laco(self):
        while True:

            # tranformar tudo digitado em minusculo e Entrada
            nome = str(input('Digite um nome [digite "f" para Sair]: ')).lower()
            # Condicional e Saída
            if nome != 'f':
                print('Estou em looping... para sair digite "f"')
            else:
                print('')
                print('Você digitou "f" para sair do looping!')
                print('/'*70)
                break
                

os.system('cls')

print('/'*70)
print('Digitar f ate sair, se não continua em looping')
print('='*70)
nome = str

looping = Fparasair.laco(nome)