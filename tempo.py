import requests

API_KEY = '0301be6bf40e071db66921ef5d104c70'
Cidade = 'Fortaleza'
Link = f'http://api.openweathermap.org/data/2.5/weather?q={Cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(Link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f'{round(temperatura, 2)}° C')
