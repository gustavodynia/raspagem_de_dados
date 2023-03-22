from selenium import webdriver
from time import sleep


navegador = webdriver.Chrome()
navegador.get('https://www.google.com')

lista_moedas = ('Dólar', 'Euro', 'Libra Esterlina', 'Dólar Australiano', 'Dólar Canadense', 'Franco Suíço')

for moeda in lista_moedas:

    link = f'https://www.remessaonline.com.br/cotacao/cotacao-{moeda}'.replace('ó', 'o').replace('í', 'i').replace(' ', '-').replace('ç', 'c').lower()

    navegador.get(link)
    sleep(1.5)
    valor = navegador.find_element('xpath', '//*[@id="root"]/div[2]/div/div[1]/div/div[3]/div[2]/form/div[2]/input').get_attribute('value')
    print(f'{moeda} está: {valor}')
