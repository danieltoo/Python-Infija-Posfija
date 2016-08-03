def typ(arr):  # ALMACENA LOS TIPOS DE DATOS EN LOS 3 ARREGLOS
	oper = []
	num = []
	var = {}   #Las variables se guardan en un diccionario parapoder almacenar lo sus valores
	cont=1
	for i in arr:
		#Guarda los operandos en un arreglo
		if (i=='+' or i=='-' or i=='*' or i=='/' or i=='^' or i=='(' or i==')'):
			oper.append(i)
		#En caso de no ser operandos 
		else :
			v = False
			# identifica si tiene una letra, es decir es una variable 
			for x in i :
				if (ord(x) >=65 and ord(x) <=90)  or (ord(x) >=97 and ord(x) <=122):
					v = True
			# Si encuentra una variable le agrega temporalmente el valor 0 
			if v:
				var[i]=0
			else:#si no  es variable entonces es un numero
				num.append(i)
	return oper , num , var