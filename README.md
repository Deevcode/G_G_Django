# G_G_Django
Proyecto Guetto Garden integrado con Django y Oracle.

                CONFIGURACIONES GENERALES DEL PROYECTO

INSTALAR DEPENDENCIAS DEL PROYECTO

1. Lo primero que debe hacer sera generar los modulos necesarios para ejecutar el proyecto, para esto devera acceder a la caprta /Django en la cual habra un archivo documento de texto que salla [    requierements.txt   ], ejecutando la siguiente sentencia en la consola de comandos (cmd).

                                        pip install -r requierements.txt      

CONEXION A LA BASE DE DATOS ORACLE 19C EXPRESS EDITION

2. Lo segundo que debe hacer sera crear el usuario para en la base de datos, en la consola de comandos (cmd), debera ejecutar la siguente sentencia 

                                        slqplus 


2. 1 Crear el usuario en la base de datos oracle

                        CREATE USER c##tienda IDENTIFIED BY tienda;
                        GRANT CONNECT, RESOURCE TO c##tienda;
                        ALTER USER c##tienda DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;


2. 2 Antes de conectarse a la base de datos debera borrar todas las tablas de la base de datos.

                                        DROP USER c##tienda CASCADE;


2. 3 Luego debera conectarse a la base de datos ORACLE XE

CREANDO SUPER USUARIO ADMIN DEL SITIO

3. Crear super usuario ADMIN

                            python manage.py createsuperuser

                                    User: Jordaan23
                                    Pass: Casita1760


4. Luego debe ejecutar la sentencia makemigrations y migrate.

                                python manage.py migrate
                                python manage.py makemigrations


5. Luego debera insertar las categorias a los productos de manera manual que se encunetra en un archivo json, dentro de la carpeta /Django , debera ejecutar la siguiente instruccion.

                            python manage.py loaddata mydata

                                    (RESGISTRO EN JSON)

Esta instruccion creara las categorias de los productos, en la seccion de agregar poductos se vera reflejado la carga de 3 categorias (plantas, herramientas, tierra)

6. Finalmente iniciar el servidor.

                        python manage.py runserver



 CREAR Y ACCEDER A TOKENS

La consola de comandos es capaz de generar token a los usuarios a travez del modulo HTTPIE 
1.. INSTALACION:

                          pip install httpie


2.. GENERAR TOKEN:

                (http http://localhost:8000/api_generate_token/ username="Jordaan23" password="Casita176")


3.. CHECKIAR EL TOKEN EN EL ADMIN DE DJANGO EN SECCION DE TOKENS
4.. AUTORIZAR A VER EL CONTENIDO DE LA API EN CONSOLA:

                http://localhost:8000/api/producto/ "Authorization: Token ab9ed0c536303b0b1501171bf0e7278adf1c305e"
5.. SE DEBE PODER VER EL CONTENIDO DE LA API.