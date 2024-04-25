![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/0a161fb9-e45e-45c6-8991-ede8651d0c6c)1. Primeros pasos en la configuracion Linux.
- prueba inicial de teclado, volver a los comandos anteriores a través de las flechas, y desplazamiento de derecha a izquierda del comando:

![Captura desde 2024-04-23 19-56-04](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/4aead450-eac8-40f2-9f08-042cc60f7b7e)

- Con *pwd* visualizamos la ruta en la que nos encontramos, con *ls* se muestran las carpetas dentro de la ruta, y con *cd* se cambia la ruta en la que nos encontramos:

![Captura desde 2024-04-23 19-59-36](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/b2cefe72-ac5c-464d-b41e-0b91fd3a5d3f)

- *cd* tiene diferentes formas para cambiar la ruta, con *cd <nueva_ruta>* se cambia completamente la ruta, en caso de que no sea continuación de la ruta actual, con *cd ..* se desplaza hacia atrás de la ruta, con *cd .<nueva_ruta>* se añade la nueva ruta a la ruta en la que nos encontramos en caso de que exista la nueva ruta en la ruta que nos encontramos:

![Captura desde 2024-04-23 20-03-18](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/7d5bb66e-66d3-4a88-9d1f-c6209c0d7b16)

- Comenzamos una exploración a través de diferentes rutas que se encuentran en nuestro ordenador, y vamos revisando las carpetas que se encuentran dentro de cada ruta:

![Captura desde 2024-04-23 21-05-24](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/4acdd27a-12fb-4f2d-81e3-7ca391ce1627)
![Captura desde 2024-04-23 21-06-08](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/3dafca50-075c-4167-affb-820e463cc88b)
![Captura desde 2024-04-23 21-08-23](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/82482fa8-83c8-4f72-a3bb-7dbceac7268a)
![Captura desde 2024-04-23 21-10-11](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/072b635e-f5a9-4fef-a810-a2986d5d50bf)
![Captura desde 2024-04-23 21-10-42](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/489876c3-1850-4f1e-a8ac-cdb01e1fa552)
![Captura desde 2024-04-23 21-11-32](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/aad2602a-5306-4db7-86b7-3db61a003bc3)
![Captura desde 2024-04-23 21-12-33](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/0abcdf74-84cb-4994-a5b0-4d035e515be9)

2. Comenzamos con la manipulacion de archivos y directorios.

Los comando *cp, rm, mv* no se ejecutaran si los arhivos o directorios que selecionamos no existen.

- Usando el comando *cp*, podemos hacer copias de archivos dentro del directorio actual, y pegar estas copias en un nuevo directorio:

![Captura desde 2024-04-24 14-58-14](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/77016a05-23fa-4957-a351-eab78d9553de)

- El comando *mv* se puede entender como la funcion *cortar*, copiando los archivos seleccionados de nuestro directorio a otro, y eliminando los archivos del directorio actual:

![Captura desde 2024-04-24 15-02-55](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/f16f4d84-e2f8-4b49-84a0-5d4144db0132)

- Con el comando *rm* eliminamos los archivos que queramos de nuestro directorio:

![Captura desde 2024-04-24 15-27-12](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/ecf1dea0-d7dc-4bac-adf8-21b341715def)

- Con el comando *mkdir* podemos crear un nuevo directorio, y con el comando *rm -r* se pueden eliminar los directorios, a traves de su ruta:

![Captura desde 2024-04-24 15-28-00](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/34bdcad9-0fe9-4aff-a86f-1c94bc02e72d)

3. Trabajando con comando.

- analizamos con *type* el tipo de datos que botara cada comando:

![Captura desde 2024-04-24 20-48-51](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/9cc7db34-98ee-4af8-a031-40dd745fbbf9)

- Utilizamos *which* para ver la ubicacion exacta donde se ejcuta el comando, y el *help -m* para ver una mejor descripcion del comando:

![Captura desde 2024-04-24 20-53-49](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/e62b732e-d5f7-4e84-8116-5242a0058440)

- Con el *mkdir --help* se despliega las opciones de ayuda que podemos tener:

![Captura desde 2024-04-24 21-00-32](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/9d9e4bd5-775f-49d7-8ce3-f3ad289b9220)

- Usnado el comando *man ls*, se despliega una pestaña llena de informacion de este comando, desde el nombre, una sinopsys, descripcion con comandos en orden alfabetico, el author, bugs reportados, el copyright:

![Captura desde 2024-04-24 21-05-29](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/ee1edcec-1bda-4615-b2b2-714c12b7d798)
![Captura desde 2024-04-24 21-05-43](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/d6510ac8-6143-4fa0-bee9-9d6b71b6e015)
![Captura desde 2024-04-24 21-05-57](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/fe2d3aa7-6e73-4f8b-9c69-3a68eefd4b73)
![Captura desde 2024-04-24 21-06-14](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/35358784-a339-4979-bef2-99795b8fb835)
![Captura desde 2024-04-24 21-06-44](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/f1acedb7-0979-4ad7-b850-b2f43a6164fb)
![Captura desde 2024-04-24 21-07-12](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/eed97691-1c6b-4940-a564-b1234703b16a)


- al utilizar el comando *ls > file_list.txt* se crea un archivo *file_list.txt* donde se alamacena la salida del *ls*, y cada ves que se ejecute, el archivo se sobreescribe:

![Captura desde 2024-04-24 21-38-03](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/25331076-a26e-4a35-ab1b-30af6ffd224a)

- al utilizar el comando *ls >> file_list.txt* se añadira la salida del *ls* al final del archivo *file_list.txt*

![Captura desde 2024-04-24 21-47-17](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/09110a25-ace9-4776-9884-37af1c452714)

- el comando *sort < file_list.txt*, mostrara de forma ordenada los elementos dentro de *file_list.txt*:

![Captura desde 2024-04-24 21-49-46](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/20b361cb-0909-4297-9cf6-4337af5253cc)

- el comando *sort < file_list.txt > sorted_file_list.txt* creara un nuevo archivo *sorted_file_list.txt* con los elementos ordenados de *file_list.txt*:

![Captura desde 2024-04-24 21-52-07](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/059292ab-306a-405f-91a9-47c576e80614)

- el comando *ls -l | less* muestra el *ls* ordenado en *less*:

![Captura desde 2024-04-24 22-23-55](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/6103b12b-0aba-4ba3-b552-bf4019b8cb95)

- Vemos los 10 archivos más nuevos en el directorio actual:

![Captura desde 2024-04-24 22-29-04](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/60435945-11ab-4f6d-a0f4-8acfde9aee64)

- Visualizamos una lista de directorios con su tamaño, ordenados desde el mas pesado:

![Captura desde 2024-04-24 22-29-15](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/3d4ac20a-d11a-470a-aa07-bea7b62e5db0)

- El total de archivos en este directorio:

![Captura desde 2024-04-24 22-29-35](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/f76e4570-2c7e-4330-9982-b972b37f25c8)

4. Impresion con Echo.

- Para imprimir usamos *echo <texto>*, y si usamos *<echo * >* o *<echo $(ls)>* imprimimos los archivos y directorios dentro del directorio en el que nos encontramos:
![Captura desde 2024-04-24 22-37-24](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/197db84d-f9de-43b2-8571-bf489269dd23)

- Luego del echo, con *< D* >*, se imprime todos los que empiecen con la letra "D", Con *< * s >* se imprime todos los que terminen con la "s", [[:upper:]]* imprime todos los que empiecen con mayuscula, y /usr/*/share imprime los directorios que empiecen con /user y terminen con /share:

![Captura desde 2024-04-24 22-41-36](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/3cab8ac2-d766-43f1-abd7-dfb878023fcc)

- Con <echo ~> se imprime el directorio de origen:

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/6bd22b54-32d5-491a-bcbf-e5f76606eaea)

- Usando *<echo $((expression))>* imprimimos el resultado de la expresion de nuestra preferencia, aqui algunos ejemplos:
 
![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/f2afc931-800c-402d-aaae-c17665d22e46)

-Usando *<echo {lsita})>* imprimimos una lista de nuestra eleccion, esta impresion se puede convinar con mas texto, como en estos ejemplos:

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/d188b4f2-d190-4c13-a99d-aba9931d0b40)

- Tambien se pueden usar las listas para crear directorios, en el siguiente ejemplo se crea y se ingresa al directorio *archivos*, y dentro del directorio archivos se crean directorios, cuyos nombres empiezan con (2017, 2018 o 2019), y teminan con (01, 02, ..., 12):

![Captura desde 2024-04-24 22-59-23](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/7cf066fe-bc96-41dc-b4d8-7f07a3313872)

![Captura desde 2024-04-24 22-59-38](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/df8c5bcc-4cdc-40e2-94c3-fd103bc2fa44)

- Usando *printenv | less*, se desplegara una lista de variables con sus impresiones que podemos usar:
![Captura desde 2024-04-24 23-04-23](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/6888bb4b-eba3-45e8-bb0c-4a3bb8265e10)
![Captura desde 2024-04-24 23-04-45](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/0f5eb8ac-e621-4c27-add6-e3e5d9be7875)

- Con *ls -l $(which cp) y ls -l `which cp`* se mostrara informacion detalla del archivo al que apunta el cp:

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/e7a17ba6-cf4b-429a-a088-99207c6b66cc)

- El comando echo suele proporciona un mecanismo el cual suprime selectivamente las expansiones no deseadas:

![Captura desde 2024-04-24 23-17-23](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/4de3eea1-b143-4b0e-ae9a-6c81fb9c3060)

- Con el uso de comillas, se pueden selecionar archivos o directorios con el nombre dividido, ademas tablien se imprimen los mensajes completos dentro de las comillas, e imprimir por filas si es requerido como con el comando "$(cal)":

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/90a2b3db-c25a-4730-bd39-269fc54157a3)

- La impresion de varion comando combinados cambia dependiendo si es solo, se imprime segun lo requerido; con comillas dobles se omiten la impresion de los nombres de los archivos y directorios; y con comillas simples se imprime el texto tal cual dentro de las comillas.

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/f642b325-dc67-4560-9e1a-0efc2515e5cf)

- Algunas interaciones entre el comando *<echo -e>* y diversos mensajes entre comillas doble con texto que contienen comandos especificos; con /n se genera un espacio luego de la impresion; con \ se crea un espacio entre las palabras; para que cierta secciòn del texto se imprima con comillas hay que cerra las comillas, escribir el texto, y volver a abrir las comillas; y si hay \\, este se convierte en \.

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/8e16a347-7195-419a-8681-b8936f747992)

-Con *xload* abrimos la representacion grafica de la carga del sistema, pero no deja hacer modificacion al terminal, pero con *xload &* si podemos ejecutar a la vez que modificamos el terminal, con *ps* se observan las pestañas de la grafica abierta, con *jobs* se ve la cantidad de graficas en ejecucion, y con *kill number* detenemos la grafica de dicho numero:
![Captura desde 2024-04-24 23-46-09](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/05340833-40a2-4868-8208-39cc38c840f1)
![Captura desde 2024-04-24 23-46-18](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/72dc8ce2-a653-4985-bb14-2e9da6bf2096)

- Con *ps x | grep bad_program*, se ve el proceso en ejecucion, y con *kill -SIGTERM o kill -SIGKILL*, tambien se pueden eliminar estos procesos:

![imagen](https://github.com/Edithson1/Edithson_Aybar_Comunicacion_Datos_y_Redes/assets/152218004/8f02af0e-59ca-4fe6-8cb7-ee872a2873c8)
