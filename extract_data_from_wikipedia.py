import wikipedia #py -3.8-64 c:/Users/Andrés/Desktop/Untitled-1.py
import pageviewapi
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
wikipedia.set_lang("es")

consulta = wikipedia.summary("Miguel bosé")

ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)

q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)

result = q_a_es(question="¿cuál es su nombre?", context= consulta)
print("su nombre es: " + result["answer"])

ola=pageviewapi.per_article('es.wikipedia', result["answer"], '20220705', '20220705',access='all-access', agent='all-agents', granularity='daily')


result = q_a_es(question="¿cuál es su profesión?", context= consulta)
print("su profesión es: " + result["answer"])

result = q_a_es(question="¿cuál es su año de nacimiento?", context= consulta)
print("nació el año " + result["answer"])


print("su popularidad es: " + str(ola["items"][0]["views"]))