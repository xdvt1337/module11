import requests
url = 'https://jsonplaceholder.typicode.com/posts/2'
r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    print("Заголовок:", data['title'])
    print("Текст:", data['body'])
else:
    print("Ошибка:", r.status_code)