from split import split
from type_ import typ 
from convert import convert
from vars import takenvar ,adminvar

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
arr= split(exp)
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
if len(var) > 0:
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