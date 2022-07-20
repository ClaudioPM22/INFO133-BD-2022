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

def main():
    usuario, contraseña = create_database()
    create_tables(usuario, contraseña)
    try:
        create_foreign_keys(usuario, contraseña)
    except:
        print ("Las claves foráneas ya han sido creadas")
    print("La base de datos se ha creado correctamente")
main()