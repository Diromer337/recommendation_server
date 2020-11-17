# recommendation_server
Рекомендательный API на Python без использования сторонних библиотек
## Запуск
```
python3 server.py
```
Сервер запускается на http://127.0.0.1:8000/  
### API
#### GET /?sku={product}
Пример запроса:
```
GET /?sku=ciIU7uSa0M
```
Пример ответа:
```
{"rec": ["Pe5VZBsptw", "OtgK7hQG3D", <...>, "zD0skCK5N9", "zaapPGwK0t", "ziuSpglnBy"]}
```
