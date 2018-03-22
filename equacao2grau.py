#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  equacao2g.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():
	
	a = 0.0; b=0.0; delta=0.0;
	xi = 0.0; xii = 0.0;
	
	a = float(input('Digite o valor "a":'))
	b = float(input('Digite o valor "b":'))
	c = float(input('Digite o valor "c":'))

	print("Valores Recebidos: ( %.2f ) ( %.2f ) ( %.2f )\n\n----------------------\n"%(a,b,c))

	if a!=0: 

		delta = ((b**2)-4*a*c)
		print('valor delta: ',delta)

		if delta <0: 

			print('Solução no domínio dos números complexos')
			delta = delta*(-1)

			xi = (-b)/(2*a)
			xii = (delta**0.5)/(2*a)
			print("Valor X1: ",xi," + ",xii," i")
			print("Valor X2: ",xi," - ",xii," i")

		else:

			if delta >=0 :

				 xi = ((-b+delta**0.5)/(2*a))
				 xii = ((-b-delta**0.5)/(2*a))
				 print("Valor X1: ( %.2f )\nValor X2 ( %.2f )"%(xi,xii))

	else:

		print('Temos que analisar os valores de b e c para equação do 1º Grau.');

	if b!=0:

		print('faz a do primeiro')

	else:
		if b == 0:

			if c == 0:
				print('Qualquer valor de x satisfaz a igualdade')
			else:
				if c != 0:
					print('Nenhum valor de x satisfaz a igualdade')

	return 0

if __name__ == '__main__':
	main()

