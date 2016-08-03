def takenvar(var): #AGREGA LOS VALORES A LAS VARIABLES 
	values = {}
	for i in var:
		print ("Ingresa el valor de ",i )
		v = int(input())
		values[i]=v
	return values #retorna el nuevo diccionario con los valores correspondientes 



def adminvar(arr,var): 
	for i in range(len(arr)):
		try:
			arr[i]=var[arr[i]]
		except Exception:
			if (arr[i]=='+' or arr[i]=='-' or arr[i]=='*' or arr[i]=='/' or arr[i]=='^' or arr[i]=='(' or arr[i]==')'):
				pass
			else:
				arr[i]=int(arr[i])
	return arr
