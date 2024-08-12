import requests
from healthCheck.variaveis import var

#resp1 = ''


def checksite():
    try:
        response = requests.get(var.url, timeout=5)
        response.raise_for_status()
        print('pagina conectada', response.text)
        resp1 = True
    except requests.exceptions.Timeout:
        print('Tempo de conexão expirou')
        resp1 = False
    #except requests.exceptions.RequestException as e:
        #print('erro ao tentar acessar', e)
        #resp1 = False
    except Exception as e:
        print('erro ao tentar acessar 3', e)
        resp1 = False

    return resp1