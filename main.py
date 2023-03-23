from selenium import webdriver
from time import sleep
import win32com as win32


navegador = webdriver.Chrome()
navegador.get('https://www.google.com')

lista_moedas = ('Dólar', 'Euro', 'Libra Esterlina', 'Dólar Australiano', 'Dólar Canadense', 'Franco Suíço')
moedas = list()
cotacoes = list()

for moeda in lista_moedas:
    link = f'https://www.remessaonline.com.br/cotacao/cotacao-{moeda}'.replace('ó', 'o').replace('í', 'i').replace(' ', '-').replace('ç', 'c').lower()
    navegador.get(link)
    sleep(1)
    valor = navegador.find_element('xpath', '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/div[2]/form/div[2]/input').get_attribute('value')
    print(f'{moeda} está: {valor} reais')
    moedas.extend([moeda])
    cotacoes.extend([valor])

result = list(zip(moedas, cotacoes))
print(result)

#outlook = win32.Dispatch('Outlook.Application')
#email = outlook.Create.Item(0)

#email.To = 'gustavodynia98@gmail.com'
#email.Subject = 'Teste de WebScraping'
#email.HTMLBody = f'''<p>Olá, segue no corpo do email as cotações das moedas solicitadas.</p>

#<p>{result[0][0]} está {result[0][1]} reais</p>
#<p>{result[1][0]} está {result[1][1]} reais</p>
#<p>{result[2][0]} está {result[2][1]} reais</p>
#<p>{result[3][0]} está {result[3][1]} reais</p>
#<p>{result[4][0]} está {result[4][1]} reais</p>
#<p>{result[5][0]} está {result[5][1]} reais</p>

#<p>Atenciosamente,</p>
#<p>Gustavo</p>'''

#email.Send()
