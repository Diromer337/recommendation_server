# recommendation_server
Рекомендательный API на Python без использования сторонних библиотек
## Запуск
Может занять некоторое время
```
python3 server.py
--Finder init successful--
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
Пример запроса (необязательный параметр power):
```
GET /?sku=J9cMivKBtJ&power=1
```
Пример ответа:
```
{"rec": ["5YBG6Gikju", "2yglPxOupM", "QRke1nzPrQ", "ZboAsFCjLw", "qyc9QV0DS8"]}
```
### Время ответа на запрос
Не кэшированный запрос
![test](/images/no_cache.png)
Кэшированный запрос
![test](/images/cache.png)
### CSV файл
Структура файла:
```
sku1,recom1,0.1
sku2,recom2,0.2
...
```
Для сортировки файла раскоментируйте строчку
```
# os.system('LC_ALL=C sort -o {file} {file}'.format(file=self.file))
```
Отсортированный файл: https://drive.google.com/file/d/1RsWiurNGjYExml4RRF5W4yN0T-1iVZwr/view?usp=sharing
### Масштабирование сервиса
Реализация асинхронности, деление приложения на несколько инстансов и балансер, подключение NoSQL, например Redis. В случае увеличения размера данных по рекомендации, например до соразмерного количеству товаров (около 1млн), при моём подходе это должно незначительно увеличить время ответа (в рамках 500мс) и совсем не затронуть оперативную память, но лучше использовать NoSQL решения.
