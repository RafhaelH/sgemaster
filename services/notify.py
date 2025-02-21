import requests


class Notify:

    def __init__(self):
        self.__base_url = 'http://localhost:8001'

    def send_order_event(self, data):
        try:
                response = requests.post(
                    url=f'{self.__base_url}/api/v1/webhooks/order/',
                    json=data,
                )
                # Verifica se a resposta é bem-sucedida (status code 200-299)
                response.raise_for_status()

                # Verifica se o conteúdo da resposta é JSON antes de tentar converter
                if response.headers.get('Content-Type') == 'application/json':
                    return response.json()
                else:
                    return {'message': 'Resposta não contém JSON.', 'status_code': response.status_code}

        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
