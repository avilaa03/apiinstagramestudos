import requests

user_id = '61332774068'  # Substitua pelo ID da sua publicação
access_token = 'EAALpZAgFrRJMBO2WAWtIDZAIZAWEPx9Y2P9kRJ7vXFgVooHvlDLwJnBZCyGdqkscYzeEz08hpLpsMm0uSNRapJL2JZAZBip0SzbYBrdeoBqvb5bt0gLKZB1X8eJW4yDUavZCtud0IMbQVfkKxuGpmwzjnHjYM19djrDUZBO55ogjFJMkTySABmuIIOoyHBEkgvjbZCvRdxtZBK94iR3Sa1duTZC8oZCn0ZBd6G7whFY5UZD'  # Substitua pelo seu token de acesso
fields = "id"
url = f'https://graph.facebook.com/{user_id}/media?access_token={access_token}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Lançará uma exceção se a resposta for um erro HTTP

    ids = response.json()

    # Itera sobre os comentários e os imprime
    for id in ids['data']:
        print(f"ID da publicação: {id['id']}")
except requests.exceptions.RequestException as e:
    print(f"Erro durante a solicitação: {e}")
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except ValueError as e:
    print(f"Erro ao analisar a resposta JSON: {e}")
