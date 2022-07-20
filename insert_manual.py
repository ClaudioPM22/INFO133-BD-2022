import mysql.connector

def create_database():
    usuario = input("Ingrese su usuario local de MariaDB: ")
    contraseña = input ("Ingrese la contraseña correspondiente a su usario de MariaDB: ")
    while True:
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user = usuario,
                password = contraseña
            )
            break
        except:
            print("Usuario o contraseña incorrector, por favor, ingreselos nuevamente")
            usuario = input("Ingrese su usuario local de MariaDB: ")
            contraseña = input ("Ingrese la contraseña correspondiente a su usario de MariaDB: ")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS biobio_test")
    return usuario, contraseña

def create_tables(usuario, contraseña):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = usuario,
        password = contraseña,
        database = "biobio_test"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS medio_de_prensa (id_medio INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(100)," 
                    "Fecha_Creación DATE, URL VARCHAR(500), Región VARCHAR(4), País VARCHAR(10), Idioma VARCHAR(20), Tipo VARCHAR(10))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS noticia (id_noticia INT AUTO_INCREMENT PRIMARY KEY, URL VARCHAR(500), Titulo VARCHAR(300)," 
                    "fecha_publicaion DATE, Contenido TEXT, id_medio INT, id_persona INT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS personas (id_persona INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(100), Profesion VARCHAR(50)," 
                    "Fecha_nacimiento DATE, Nacionalidad VARCHAR(30), Popularidad INT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS dueños (id_dueños INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(100), Tipo VARCHAR(10), Fecha_adquisicion DATE)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS menciona (id_noticia INT, id_persona INT, PRIMARY KEY (id_noticia,id_persona))")

def create_foreign_keys(usuario, contraseña):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = usuario,
        password = contraseña,
        database = "biobio_test"
    )
    mycursor = mydb.cursor()
    mycursor.execute("""
    alter table noticia  
    add constraint fk1
    foreign key(id_medio) 
    references medio_de_prensa(id_medio)
    on delete set null
    on update set null
    """)

def insert_data(usuario, contraseña):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = usuario,
        password = contraseña,
        database = "biobio_test"
    )
    mycursor = mydb.cursor()
    tabla = input("Ingrese el nombre de la tabla a la que quiere agregar datos (medio_de_prensa, noticia, dueños, personas): ")
    if (tabla == "medio_de_prensa"):
        nombre = input ("Ingrese el nombre del medio de prensa: ")
        fecha = input ("Ingrese la fecha de creación del medio prensa YYYY-MM-DD: ")
        url = input ("Ingrese la url del medio de prensa: ")
        region = input ("Ingrese la region del medio de prensa (en numeros romanos): ")
        pais = input ("Ingrese el país del medio de prensa: ")
        idioma = input ("Ingrese el idioma del medio de prensa: ")
        tipo = input ("Ingrese el tipo del medio de prensa (regional o local): ")
        val = (nombre, fecha, url, region, pais, idioma, tipo)
        sql = ("INSERT INTO medio_de_prensa (Nombre, Fecha_Creación, URL, Región, País, Idioma, Tipo) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        mycursor.execute (sql,val)
        mydb.commit()

    if (tabla == "noticia"):
        url = input("Ingrese la url de la noticia: ")
        titulo = input("Ingrese el titulo de la noticia: ")
        fecha = input("Ingrese la fecha de publicacion de la noticia YYYY-MM-DD: ")
        contenido = input ("Ingrese el contenido de la noticia: ")
        val = (url, titulo, fecha, contenido)
        sql = ("INSERT INTO noticia (URL, Titulo, fecha_publicaion, Contenido) VALUES (%s, %s, %s, %s)")
        mycursor.execute(sql, val)
        mydb.commit()

    if (tabla == "personas"):
        nombre = input ("Ingrese el nombre de la persona: ")
        profesion = input ("Ingrese la profesion de la persona: ")
        fecha = input ("Ingrese la fecha de nacimiento de la persona YYYY-MM-DD: ")
        nacionalidad = input ("Ingrese la nacionalidad de la persona: ")
        popularidad = input ("Ingrese la popularidad de la persona: ")
        val (nombre, profesion, fecha, nacionalidad, popularidad)
        sql = "INSERT INTO personas (Nombre, Profesion, Fecha_nacimiento, Nacionalidad, Popularidad) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql,val)
        mydb.commit()

    if (tabla == "dueños"):
        nombre = input("Ingrese el nombre del dueño: ")
        tipo = input ("Ingrese el tipo (persona o empresa): ")
        fecha = input ("Ingrese la fecha de adquisición YYYY-MM-DD: ")
        val = (nombre, tipo, fecha)
        sql = "INSERT INTO dueños (Nombre, Tipo, Fecha_adquisicion) VALUES (%s, %s, %s)"
        mycursor.execute(sql,val)
        mydb.commit()

def main():
    usuario, contraseña = create_database()
    create_tables(usuario, contraseña)
    try:
        create_foreign_keys(usuario, contraseña)
    except:
        print ("Las claves foráneas ya han sido creadas")
    print("La base de datos se ha creado correctamente")
    pregunta = input("Le gustaría ingresar datos? S/N= ")
    if (pregunta == "S"): pregunta = True
    else: 
        pregunta = False
        print("El programa ha finalizado")
    while (pregunta):
        insert_data(usuario, contraseña)
        pregunta = input("Le gustaría ingresar datos? S/N= ")
        if (pregunta == "S"): pregunta = True
        if (pregunta == "N"): 
            pregunta = False
            print("El programa ha finalizado")
main()  