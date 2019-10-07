#Simbologia
# 0: Digito
# 1: Otro Simbolo(blanco, salto de linea)
import os

print "Current Dir: ", os.getcwd() + "/matriz2.txt"

mainFile = os.getcwd() + "/matriz2.txt"

# Metodos
#next() # Lee una linea
with open(mainFile) as f:
    simbolos = next(f).split(',')
    M = [[int(x) for x in line.split()] for line in f]

print(simbolos)
print(M)

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

# for p in range(longitud):
#     c = archivo[p] # Leemos cada caracter del archivo 'ejemplo.txt'
#     estado = M[estado][mapa[c]]# Matriz que representa la funcion de transicion
#     print("mapa: ", mapa[c])
#     if estado == 2: # Estado de aceptacion de token
#         print("token: ", token)
#         token = '' # Limpiamos el token
#         estado = 0 # Volvemos al estado inicial
#         p = p - 1
#     elif estado != 0:# Si el caracter es distinto del blanco lo concatenamos con el caracter anterior para formar un token
#         token += c
p = 0

while p < longitud :
    c = archivo[p] # Leemos cada caracter del archivo 'ejemplo.txt'
    estado = M[estado][mapa[c]]# Matriz que representa la funcion de transicion
    if estado == 2: # Estado de aceptacion de token
        print("token: ", token)
        token = '' # Limpiamos el token
        estado = 0 # Volvemos al estado inicial
        p = p - 1
    elif estado == 3: #Suma
        token += c
        print("token: ", token)
        token = ''
        estado = 0
    elif estado == 4:
        token += c
        print("token: ", token)
        token = ''
        estado = 0
    elif estado == 5: # espacios en blanco
        estado = 0
    elif estado != 0:# Si el caracter es distinto del blanco lo concatenamos con el caracter anterior para formar un token
        token += c
    p+=1
    

    # El error se debe al token $ que no lo encuentra en el mapa
        
