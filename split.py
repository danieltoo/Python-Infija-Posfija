def split(exp):#  SEPARA LOS OPERADORES Y OPERANDOS 
	num = False
	arr = []
	temp =""
	for i in exp:
		#  Separa operadores y guarda posibles operadores en elarreglo
		if (i=='+' or i=='-' or i=='*' or i=='/' or i=='^' or i=='(' or i==')'):
			if temp!="": 
				arr.append(temp)
				temp=""
			arr.append(i)
		#  Separa numeros en una cadena temporal
		elif (ord(i) >=48 and ord(i)<=57):
			temp+=i
		#  Hace el efecto de separar posibles variables 34te
		elif (ord(i) >=65 and ord(i) <=90 ) or (ord(i) >=97 and ord(i) <=122 ):
			temp+=i
		#  En caso de no ser un caracter reconocido 
		else:
			print("Caracter no reconocido",i)
			return []
	#  Guardo lo que haya quedado al final en la variable temporañ
	if temp!="":
		arr.append(temp)
	return arr