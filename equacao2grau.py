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
	
	a = float(input('Digite o valor "a": '))
	b = float(input('Digite o valor "b": '))
	c = float(input('Digite o valor "c": '))

	#print("Valores Recebidos: ( %.2f ) ( %.2f ) ( %.2f )\n\n----------------------\n"%(a,b,c))
	print('\n');

	if a!=0: 

		print('EQUAÇÃO DO SEGUNDO GRAU\n');

		delta = ((b**2)-4*a*c)
		print('valor delta: ',delta)

		if delta <0: 

			print('Solução no domínio dos números complexos')
			delta = delta*(-1)

			xi = (-b)/(2*a)
			xii = (delta**0.5)/(2*a)
			print("Valor X1: ",xi," + ",xii," i")
			print("Valor X2: ",xi," - ",xii," i")

		elif delta >=0 :

			 xi = ((-b+delta**0.5)/(2*a))
			 xii = ((-b-delta**0.5)/(2*a))
			 print("Valor X1: %.2f \nValor X2 %.2f "%(xi,xii))

	else:

		print('EQUAÇÃO DO PRIMEIRO GRAU\n');

		if b!=0:

			print("o valor de X: %.2f "%((c*-1/b)))

		else:
			
			if c == 0:
				print('Qualquer valor de x satisfaz a igualdade')
			elif c != 0:
				print('Nenhum valor de x satisfaz a igualdade')

	return 0

if __name__ == '__main__':
	main()

