from selenium import webdriver
from time import sleep
import smtplib
import email.message


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

def enviar_email():
    corpo_email = f'''
    <p>Olá, segue abaixo as cotações atualizadas das moedas solicitadas:</p>
    
    <p>{result[0][0]}: {result[0][1]} reais</p>
    <p>{result[1][0]}: {result[1][1]} reais</p>
    <p>{result[2][0]}: {result[2][1]} reais</p>
    <p>{result[3][0]}: {result[3][1]} reais</p>
    <p>{result[4][0]}: {result[4][1]} reais</p>
    <p>{result[5][0]}: {result[5][1]} reais</p>
    
    <p>Essa cotação é automatizada, valores recém atualizados.</p>'''
    msg = email.message.Message()
    msg['Subject'] = 'Cotações de moedas atualizadas'
    msg['From'] = 'gustavodynia98@gmail.com'
    msg['To'] = 'gustavodynia98@gmail.com'
    #password deve ser gerado e alterado para a execução do programa.
    with open('senha.txt', 'r') as file:
        password = file.read().strip()
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso.')

enviar_email()
