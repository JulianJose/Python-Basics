#!/usr/bin/python3
# pw.py: Um progroma para repositório de senhas que não é seguro.

import sys
import pyperclip

PASSWORDS= {'email': "PN7#6K*tS*xn}SwytA5wAcVsKkNX8m",
	    'blog': "EfOEN8ypmDK5#Vk5Dr9CJ#Xw2[Rx2H",
	    'luggage': "4[UNGw8J@{[u7T@oS[xGd@GZd{6XU"}

if len(sys.argv) < 2:
	print("""Número de argumentos insuficiente.
		 python pw.py [conta] [senha]""")
	sys.exit()

CONTA = sys.argv[1] # Primeiro argumento da linha de comando.

if CONTA in PASSWORDS:
	pyperclip.copy(PASSWORDS[CONTA])
	print("Senha para {} copiada para o a área de transferência".format(CONTA))

elif len(sys.argv) == 3:
	PASSWORDS[CONTA] = sys.argv[2]
	print("Conta e senha adicionada")
        print("Senha para {} copiada para o a área de transferência".format(CONTA))
        pyperclip.copy(PASSWORDS[CONTA])

