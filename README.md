# G_G_Django
Proyecto Guetto Garden integrado con Django y Oracle.
 
 1. Lo primero que debe hacer sera generar los modulos necesarios para ejecutar el proyecto, para esto devera acceder a la caprta /Django en la cual habra un archivo documento de texto que salla [    requierements.txt   ], ejecutando la siguiente sentencia en la consola de comandos (cmd).

                         [       pip install -r requierements.txt      ]



2.Lo segundo que debe hacer sera crear el usuario para en la base de datos, en la consola de comandos (cmd), debera ejecutar la siguente sentencia 

                         [   slqplus ]
                         
                         
2.1 Luego debera crear el usario en la base de datos

2.2 En caso de tener creado el usario eliminarlo.


[  drop user c##prueba CASCADE;  ]


2.3 Crear el usuario

               [   create user c##prueba identified by "1234";
                  grant connect, resource to c##prueba;
                 alter user c##prueba default tablespace users quota unlimited on users; ]



3.Luego debe ejecutar la sentencia makemigrations y migrate.


                      [  python manage.py migrate  ]


                     [  python manage.py makemigrations  ]


4..Luego debera insertar las categorias a los productos de manera manual que se encunetra en un archivo json, dentro de la carpeta /Django , debera ejecutar la siguiente instruccion.

                         [  python manage.py loaddata mydata  ]




Esta instruccion creara las categorias de los productos, en la seccion de agregar poductos se vera reflejado la carga de 3 categorias (plantas, herramientas, tierra)

Finalmente iniciar el servidor.

                            [  python manage.py runserver  ]


 
 
