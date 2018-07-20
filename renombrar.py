#agradecimiento a: https://electrocooking.wordpress.com/2016/06/17/como-renombrar-ficheros-masivamente-con-python/
import os

start=1 #Comienzo de renombre
extension=".txt" #Poner el formato de los ficheros a renombrar

list=0
nombres = []  #creamos una variable listado vacia para guardar los nombres
numero = []   #creamos una variable listado vacia para guardar el numero de las fotos
for item in os.listdir("."): #si ponemos "." significa que hara el listado en el mismo directorio donde esta el fichero de python
	# si queremos poner una direccion como por ejemplo C:\\Fotos\\RivieraMaya ponemos simpre doble barra para que python no se confunda
    if item[-4:] == extension:  #Si queremos filtro solo los archivos JPG, para un formato ejemplo de .py, la extensión debe ser: -3
        list += 1
        nombres.append(item) #guardamos cada nombre de archivo del directo destino en esta variable
        numero.append(item[4:8])  # guardamos el numero del archivo

#print("Numero de elementos",list)
#print ("Listado de Todos los nombres", nombres)

#print ("Nombre Original",nombres[0:488])  #mostramos por patalla los nombres originales


numerodestino = [] # guardamos el numero de destino
cambio = []		   # guardamos el nombre de destino

for index,i in enumerate(range(start,start+list)):  #index es el numero de registro y i es el numero del rango 1014 a 1502
    numerodestino.append(i) # guardamos en un array todos los numeros de destino
    print(numerodestino)
    if nombres[index][-4:] == extension:  # filtramos si es un archivo JPG
        cambio.append("00" + str(numerodestino[index]) + extension)  #creamos el nombre del archivo destino con DSC_ convertimos a string el numero y añadimos la extension
    
    #print (nombres[index])  #mostramos por pantalla los nombre originales
    print (cambio[index])   #mostramos por pantalla los nombres de destino
    #print (numerodestino[index])  #nos muestra la extension del archivo original

    #Descomentar la siguente línea cuando ya estemos seguros que realiza la funcion correctamente
        
    #os.rename(nombres[index], cambio[index])  #aqui ponemos los nombre originales y los nombres destino, ejemplo pasa la imagen DSC_0001.JPG a este nombre DSC_1014.JPG

