import mysql.connector
import random
from requests_html import HTMLSession
import spacy
import warnings
warnings.filterwarnings("ignore")

nlp = spacy.load("es_core_news_md")
print("spacy OK")

import wikipedia
wikipedia.set_lang("es")
import pageviewapi
print("wikipedia OK")
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
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
def format_date(date):
    return(date.split("T")[0])

def insert_data(usuario, contraseña, listaurl, listatitulo, listafecha, listacontenido, n ):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = usuario,
        password = contraseña,
        database = "biobio_test"
    )
    mycursor = mydb.cursor()
    for i in range(int(n)):
        url = listaurl[i]
        titulo = listatitulo[i]
        fecha = listafecha[i]
        contenido = listacontenido[i]
        val = (url, titulo, fecha, contenido)
        sql = ("INSERT INTO noticia (URL, Titulo, fecha_publicaion, Contenido) VALUES (%s, %s, %s, %s)")
        mycursor.execute(sql, val)
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
        insert_data(usuario, contraseña)
    session = HTMLSession()

    ## URL que escrapear
    URL = "https://elcontraste.cl/secci%C3%B3n/region/"

    ## Simular que estamos utilizando un navegador web
    USER_AGENT_LIST = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    headers = {'user-agent':random.choice(USER_AGENT_LIST) }

    response = session.get(URL,headers=headers)
    n='10'
    listaTitulos=[]
    listaURL=[]
    listaDate=[]
    listaCuerpoNoticia=[]
    listaPersonas=[]
    listaPersonasBase=[]
    ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

    tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
    model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)

    q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)
    """
    result = q_a_es(question="¿De donde es?", context=texto)
    print(result["answer"])
    """
    #doc = nlp(texto)
    print("--------------------")




    for i in range(int(n)):
        #/html/body/div[3]/div/div/div/main/div[1]/article[2]/div/header/h2/a
        #/html/body/div[3]/div/div/div/main/div[1]/article[]/div/header/h2/a
            xpath_title="/html/body/div[3]/div[1]/div/div/main/div[1]/article["+str(i+1)+"]/div/header/h2/a"
            xpath_date="/html/body/div[3]/div[1]/div/div/main/div[1]/article["+str(i+1)+"]/div/header/div[2]/span[2]/time[1]/@datetime"
            xpath_URL="/html/body/div[3]/div[1]/div/div/main/div[1]/article["+str(i+1)+"]/div/header/h2/a/@href"
            title = response.html.xpath(xpath_title)[0].text
            url = response.html.xpath(xpath_URL)[0]
            fecha = response.html.xpath(xpath_date)[0]
            listaTitulos.append(title)
            listaURL.append(url)
            listaDate.append(format_date(fecha))
            responseURL = session.get(listaURL[i],headers=headers)
            cuerpo_Noticia = responseURL.html.find('p')
            listaCuerpoNoticia.append((cuerpo_Noticia[1].text)+'\n'+(cuerpo_Noticia[2].text)+'\n'+cuerpo_Noticia[3].text)
            persona = nlp(listaCuerpoNoticia[i])
            for ent in persona.ents:
                if ((ent.label_ == "PER") and (" " in ent.text)):
                    
                    #persona mencionada
                    person = ent.text
                    print(person)
                    listaPersonas.append(person)
                    print("--------------------")
            listaPersonasBase.append(listaPersonas)
            listaPersonas=[]
    print('\n'.join(map(str, listaTitulos)))
    print('\n'.join(map(str, listaURL)))
    print('\n'.join(map(str, listaDate)))
    print('\n ***************************************************************************    '.join(map(str, listaCuerpoNoticia)))
    print('\n')
    print(cuerpo_Noticia[5].text)
    print('\n')
    responseURL = session.get("https://elcontraste.cl/peligroso-ex-gendarme-fue-detenido-por-robo-en-mulchen-quedo-libre/13/07/2022/",headers=headers)
    cuerpo_Noticia = responseURL.html.find('p')
    print(cuerpo_Noticia[1].text)
    print(cuerpo_Noticia[2].text)
    print(cuerpo_Noticia[3].text)
    insert_data(usuario, contraseña, listaURL, listaTitulos, listaDate, listaCuerpoNoticia, n)
main()  