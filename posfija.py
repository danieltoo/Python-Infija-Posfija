
def separar(exp):#  SEPARA LOS OPERADORES Y OPERANDOS 
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

def takenvar(var): #AGREGA LOS VALORES A LAS VARIABLES 
	values = {}
	for i in var:
		print ("Ingresa el valor de ",i )
		v = int(input())
		values[i]=v
	return values #retorna el nuevo diccionario con los valores correspondientes 

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
			

"""
		____________MAIN___________
"""		
Jer = {
	"+":1,
	"-":1,
	"*":2,
	"/":2,
	"^":3,
	")":0,
	"(":6
}
print ("Simbolos aceptados:")
simb = "\t Numeros Enteros \n\t Letras Mayusculas \n\t Letras Minusculas \n\t Operadres : + - * / ^ \n\t Separadores : ( )\n"
print (simb)
exp = input ("Ingresa la exp \n")
arr= separar(exp)
if arr==[]:
	exit()

oper, num , var = typ(arr)

#print ("arr" , arr)
print ("opers", oper)
print ("number", num)
#print ("vars", var)

if len(var) > 0:
	print("Se encontaron varibales ")
	var = takenvar(var)
print("var", var)
pos = convert(arr, Jer)
postext= ""



for i in range (len(pos)):
	postext+=pos[i]
print("Expresion Infija :", exp, "Expresion Posfija", postext)
posvar = adminvar(pos,var)
postextvar =""
for i in range (len(posvar)):
	if i == len(posvar)-1:
		postextvar+=str(posvar[i])
	else:
		postextvar+=str(posvar[i])+","
print("Expresion Posfija Con valores:", postextvar)



"""
numbers 48-57
( 40
) 41
* 42
+ 43
- 45
/ 47
^ 94
mayus 65 - 90
min 97 - 122"""