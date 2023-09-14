import requests

id_publicacao = '17972876807594786'  # Substitua pelo ID da sua publicação
access_token = 'EAALpZAgFrRJMBO2WAWtIDZAIZAWEPx9Y2P9kRJ7vXFgVooHvlDLwJnBZCyGdqkscYzeEz08hpLpsMm0uSNRapJL2JZAZBip0SzbYBrdeoBqvb5bt0gLKZB1X8eJW4yDUavZCtud0IMbQVfkKxuGpmwzjnHjYM19djrDUZBO55ogjFJMkTySABmuIIOoyHBEkgvjbZCvRdxtZBK94iR3Sa1duTZC8oZCn0ZBd6G7whFY5UZD'  # Substitua pelo seu token de acesso

url = f'https://graph.facebook.com/{id_publicacao}/comments?access_token={access_token}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Lançará uma exceção se a resposta for um erro HTTP

    comentarios = response.json()

    # Itera sobre os comentários e os imprime
    for comentario in comentarios['data']:
        print(f"Data e Hora de Post: {comentario['timestamp']}")
        print(f"Comentário: {comentario['text']}")
        print(f"ID: {comentario['id']}")

except requests.exceptions.RequestException as e:
    print(f"Erro durante a solicitação: {e}")
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except ValueError as e:
    print(f"Erro ao analisar a resposta JSON: {e}")
