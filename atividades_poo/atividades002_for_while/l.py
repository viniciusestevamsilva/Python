# Curso Desenvolvimento de sistemas
# Autor : Vinícius Estevam da Silva
# Data 09/09/2024
import os


class Dados:
    def __init__(self, nome, senha, seuID):
        self.nome = nome
        self.senha = senha
        self.seuID = seuID
        

class Info(Dados):
    def infomacoes(nome, senha, seuID):
        while (True):
            cadastro = nome + senha + seuID
            print('='*70)
            dados = str(input('Digite dados [digite sua "senha" e "nome" para Sair]: ')).lower()
            
            if (dados != cadastro):
                print('Estou armazenando dados ,para sair digite os dados do cadastro.')
                print('='*70)
            else:
                print('-'*70)
                print('Você saiu de banco de dados.')
                
                break
                
print('/'*70)
print('Digitar seus dados para sair')
print('='*70)
print('')

nome = (input('Digite seu nome: '))
senha = (input('Digite sua senha: '))
seuID = (input('Digite seu ID: '))

verificar = Info.infomacoes(nome, senha, seuID)

print('/'*70)