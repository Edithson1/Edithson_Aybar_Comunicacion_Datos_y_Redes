1. Primeros pasos en la configuracion Linux.
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


