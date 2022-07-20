import random
from requests_html import HTMLSession
import spacy
nlp = spacy.load("es_core_news_md")
print("spacy OK")

import wikipedia
wikipedia.set_lang("es")
import pageviewapi
print("wikipedia OK")
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
    
session = HTMLSession()
# EL sitio que se utilizo para escrapear las noticias es
# https://sabes.cl/region-del-biobio/
## URL para scrapear el contenido de la noticia
URL = "https://sabes.cl/2022/07/16/municipio-de-chiguayante-compromete-construccion-de-un-parque-en-terreno-utilizado-por-fesiluz/"

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
"""
/html/body/article/section[2]/div/div/div[1]/div[1]/div[2]/p[1]
/html/body/article/section[2]/div/div/div[1]/div[1]/div[2]/p[2]
"""
def listaATexto(text):
    parrafo = ""
    for i in text:
        parrafo = parrafo + i
    return parrafo

sigue = True
i = 1
text = []
while(sigue):
    try:
        xpath_text = '/html/body/article/section[2]/div/div/div[1]/div[1]/div[2]/p['+ str(i) +']/text()'
        parrafo = response.html.xpath(xpath_text)[0]
        text.append(parrafo)
        i +=1
    except(IndexError):
        sigue = False


#print('\n'.join(map(str,text)))
texto = listaATexto(text)
print(texto)


ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)

q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)
"""
result = q_a_es(question="¿De donde es?", context=texto)
print(result["answer"])
"""
import warnings
warnings.filterwarnings("ignore")

doc = nlp(texto)

print("--------------------")

for ent in doc.ents:
    if ((ent.label_ == "PER") and (" " in ent.text)):
        
        #persona mencionada
        person = ent.text
        print(person)
        
        print("--------------------")