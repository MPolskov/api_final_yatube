### Описание проекта:
Учебный проект - блог.
Позволяет создавать посты, которые смогут видеть другие люди.
Зарегистрированные пользователи смогут комментировать Ваши посты.
Также реализована функция подписки на авторов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:MPolskov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
Для Linux:
```
python3 -m venv env
```
```
source env/bin/activate
```
Для Windows:
```
py -m venv venv
```
```
source venv/Scripts/activate
```
---
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Примеры API-запросов:
Получение публикаций:
```
http://127.0.0.1:8000/api/v1/posts/
```
Ответ:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
