#Simbologia
# 0: Digito
# 1: Otro Simbolo(blanco, salto de linea)
import os
import sys

mainFile = os.getcwd() + "/matriz2.txt"

# Metodos
with open(mainFile) as f:
    simbolos = next(f).split(',')
    M = [[int(x) for x in line.split()] for line in f]

#print(simbolos)
#print(M)

f = open('./ejemplo2.txt', 'r')
archivo = f.read() 		# lee todo el archivo a tokenizar
archivo += '$'                  # agregamos $ para representar EOF
longitud = len(archivo) 	# longitud del archivo
estado = 0                      # estado inicial
token = ''                      # token inicial

mapa = {}
# Creamos un array(llamado mapa) que clasifica/separa los 'digitos' asignandoles un 0
# Al alfabeto y underscore
# e.g mapa = [0,0,0,..., (10)0, 1, 1, 1]
for i in range(len(simbolos)):
    for c in simbolos[i]:# recooremos primero digitos, luego alfabeto
        mapa[c]=i

p = 0

while p < longitud :
    c = archivo[p] # Leemos cada caracter del archivo 'ejemplo.txt'
    estado = M[estado][mapa[c]]# Matriz que representa la funcion de transicion
    if estado == 2: # Estado de aceptacion de token
        print("token: ", token)
        token = '' # Limpiamos el token
        estado = 0 # Volvemos al estado inicial
        p = p - 1
    elif estado == 4:#Punto
        token += c
        estado = estado - 1
    elif estado == 5: # Mostramos el num real
        if str(c).isdigit():
            token += c
        else:
            p -= 1
        print("token: ", token)
        token = ''
        estado = 0
    elif estado == 6: #Suma
        token += c
        print("token: ", token)
        token = ''
        estado = 0
    elif estado == 7: #Resta
        token += c
        print("token: ", token)
        token = ''
        estado = 0
    elif estado == 8: #Mult
        token += c
        print("token: ", token)
        token = ''
        estado = 0 
    elif estado == 9: #Division
        token += c
        if archivo[p+1] == '/':
            estado = 6
        else:
            print("token: ", token)
            token = ''
            estado = 0
    elif estado == 10: # espacios en blanco
        estado = 0
    elif estado == 11: # Igual/Asignacion
        if c != '\n':
            token += c
            print("token: ", token)
        token = ''
        estado = 0
    elif estado == 12: # Parentesis izquierdo
        if c != '\n':
            token += c
            print("token: ", token)
        token = ''
        estado = 0
    elif estado == 13: # Parentesis Derecho
        if c != '\n':
            token += c
            print("token: ", token)
        token = ''
        estado = 0
    elif estado == 14: #Auxiliar (Notacion Cientifica)
        token += c
        estado = 4
    elif estado == 15: #Auxiliar (Notacion Cientifica)
        token+=c
        estado = 5
    elif estado == 16: # Comentario (Se entra por estado 9)
        while p < len(archivo):
            c = archivo[p]

            if c != '\n' and c != '$':
                token += c
            else:
                print("token: ", token)
                token = ''
                estado = 0
                break
            p += 1
    elif estado == 17:
        token += c
        c = archivo[p+1]
        if c.isalpha() or c.isdigit() or c == '_':
            estado = 7
        else:
            print("token: ", token)
            estado = 0
            token = ''
    elif estado == 18:
        while p < len(archivo):
            c = archivo[p]

            if c.isdigit() or c.isalpha() or c == '_':
                token += c
            else:
                estado = 0
                print("token: ", token)
                p -= 1
                token = ''
                break
            p += 1
    elif estado == 19: #^
        token += c
        print("token: ", token)
        token = ''
        estado = 0 
    elif estado == 20:
        print("Error")
    elif estado != 0:# Si el caracter es distinto del blanco lo concatenamos con el caracter anterior para formar un token
        if c != '\n':
            token += c
    p+=1
        
