import re

'''
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio
'''



class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if (type(url) == str):
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL esta vazia.")
        
        padrao = re.compile("(http[s]?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao.match(self.url)
        if not match:
            raise ValueError("A URL nao eh valida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        return url[:indice_interrogacao]     

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = url[indice_interrogacao+1:]
        return url_parametros

    '''
    def get_todos_valores(self):
        for parametro in self.get_url_parametros():
            print("{}: {}".format(parametro, self.get_valor_parametro(parametro)))
    ''' 

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametros().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e = self.get_url_parametros().find("&", indice_valor)
        if(indice_e != -1):
            valor = self.get_url_parametros()[indice_valor:indice_e]
        else:
            valor = self.get_url_parametros()[indice_valor:]
        return valor
    

url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_parametro = extrator_url.get_valor_parametro("moedaDestino")
#valores = extrator_url.get_todos_valores()
print(valor_parametro)
#print(valores)