#!/usr/bin/python3

import os
import time

os.system("clear")

senha = input("Qual é a senha? Digite 'dica' para obter uma dica: ").upper()
    
if senha == "RELÓGIO":
    print("Você descobriu a senha!")
    exit()
    
if senha == "DICA":
    senha_dica = input("Dica: conta as horas. Qual é a senha? ").upper()
    if senha_dica == "RELÓGIO":
        print("Você descobriu a senha!")
        exit()
    if senha_dica != "RELÓGIO":
        print("Essa não é a senha!")
        exit()        
    
if senha != "RELÓGIO" and "DICA":
    print("A senha não é essa!")
    exit()


    
