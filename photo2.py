import requests
def fox():
    url = 'https://randomfox.ca/floof'


    responce = requests.get(url)
    if responce:
        return responce.json().get('image')
    else:
        return 'No photo'
if __name__ == '__main__':
    print(fox())