def convert(arr, Jer): #CONVIERTE LA NOTACION
	pos =[]
	arr.append(")") #agregamos un parentesis para limitar el termino de los valores 
	pila = ["("]
	for t in range(len(arr)):
		#Es operador 
		if (arr[t]=='+' or arr[t]=='-' or arr[t]=='*' or arr[t]=='/' or arr[t]=='^' or arr[t]=='(' or arr[t]==')'):
			if len(pila) >= 1: #Para evitar errores de desbordamiento
				x = len(pila)-1 
				for i in range(x): # Recorre la pila
					if (Jer[arr[t]]<= Jer[pila[x]]): # si la jerarquia del operador es menor o igual a la de
						# los operadores que ya se encuentran dentro de la pila entonces 
						if (pila[x]!='(' and pila[x]!=')'): # si no son abierto o cerrado
							pos.append(pila[x]) # Guardan su valor en la notacion
							pila.pop() # Borra el elemento de la pila
						else: # si son abierto o cerrado solo los borra para no meterlos en la notación
							pila.pop() #elimina el elemento
					x-=1
				pila.append(arr[t])
			else: # si es el primer operador lo mete a la pila sin revisar Jerarquia
				pila.append(arr[t]) 
		else: # En caso de que sea un numero o variable entra directamente a la notación
			pos.append(arr[t])
	return pos