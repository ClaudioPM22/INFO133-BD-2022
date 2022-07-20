import random
from requests_html import HTMLSession

def format_date(date):
        return(date.split("T")[0])

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
for i in range(int(n)):
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

print('\n'.join(map(str, listaTitulos)))
print('\n'.join(map(str, listaURL)))
print('\n'.join(map(str, listaDate)))
print('\n ***************************************************************************    '.join(map(str, listaCuerpoNoticia)))
