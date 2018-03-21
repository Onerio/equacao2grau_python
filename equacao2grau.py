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
	
	a = float(input('Digite o valor "a":\n'))
	b = float(input('Digite o valor "b":\n'))
	c = float(input('Digite o valor "c":\n'))
	
	print("Valores Recebidos: ( %.2f ) ( %.2f ) ( %.2f )"%(a,b,c))

	# ax² + bx + c = 
	# delta ∆ = b² – 4 * a * c
	
	delta = ((b**2)-4*a*c)
	print(delta)
	#s5df45s4df54sdf4sdf44s54df54sd
	
	return 0

if __name__ == '__main__':
	main()

