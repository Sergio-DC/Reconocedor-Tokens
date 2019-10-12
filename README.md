# Reconocedor de Tokens

## Archivos
El proyecto esta compuesto por un script de python llamado 'tokens.py'
y un archivo txt  llamado 'matriz2.txt' el cual tiene la matriz de transición.
Además se adjunta un archivo para ingresar la expresiones artiméticas  llamado 
'input.txt'.

## Requisitos
- Tener una versión de python (v2.7.14 o superior) 

## Instalación de Python
1. Visita el sitio web de python: https://www.python.org/downloads/
2. Descarga la versión de tu preferencia
3. Ejecuta el instalador y da siguiente en el asistente
4. **Marca la casilla "Añadir Python X.X al PATH".** Esto te permitirá ejecutar Python directamente desde el símbolo del sistema.

## Ejecutar el programa
1. Abre una terminal que apunte a la dirección donde se encuentra el archivo 'tokens.py'
2. Crea un txt con el nombre de 'input.txt' , este contendrá las expresiones aritméticas y comentarios
3. Ejecuta el siguiente comando `python tokens.py` para iniciar el programa

## Entrada
![enter image description here](https://lh3.googleusercontent.com/99sdL42a7rfcAs8vMp0Li5gqxUzi2kS3Y7EsJ7vS38EkAh0Gf_WoD8ovM0HPOmItTGy0pAh1R7mc)

## Salida
![enter image description here](https://lh3.googleusercontent.com/Q5aY97Bs1glBIygDdVZznYvlTiJbsTntybu6ZcxQ2Bh_dFGypSe68K-fYsKlFyvTUWMPvbeWcaBS)

## Diagrama del autómata
![enter image description here](https://lh3.googleusercontent.com/zHTvdW47aJCIYSgOkgh8_rNCHGd8YZ_3ZcqsoVwBYmafkJSCO45sA_27IErHlRn6YrmQoxFin-2s)
## Matriz de Transición
![enter image description here](https://lh3.googleusercontent.com/h5toy6lxZqZQp9wMDeQdNIm5xxnMeeQs84F9X9lfv3VgAMakPnZ4vhq2hkYeZUcVw3RbgHPNL0g3)
## ¿Cómo se construyo la matriz?
Primero se diseño el AFD y a partir de este se lograron obtener las relaciones existentes entre estados y símbolos
para posteriormente implementar la matriz, algunos estados no conectan con el estado de error 20 en el diagrama del AFD
esto con el fin de no saturar el diagrama de arcos pero en la tabla de transiciones se establecio.
## ¿Cómo se lee la matriz?
Para leer la matriz me apoye en la implementación que realizo el profesor en clase.

Se guardaron los símbolos en una ED de tipo diccionario que se encuentran en la primera fila del archvio 'matriz2.txt'
Y además se guardaron los valores de la matriz en una lista bidimensional

Es importante señalar que cada columna de la matriz representa un simbolo mientras que las filas representan los estados.
Los estados no están alineados o empatados a los valores de los subíndices de filas de la lista bidimensional por lo que en la
implementación puede que no tenga mucho sentido los valores que tome la variable 'estado' en algunas situaciones.

Para movernos de un estado a otro en la matriz/lista bidimensional primero leemos un caracter del archivo 'input.txt' y de acuerdo
a este símbolo buscamos en la lista de 'símbolos'(es un diccionario) su valor númerico, el cuál nos
servira para realizar la transición de un estado a otro a partir del símbolo (Nota: el estado se inicializo en 0).
Este proceso se realiza repetidas veces hasta que terminemos de leer por completo el archivo de entrada.

