# Проект API для YaTube
### Описание
Учебный проект по Django и DRF.

API для социальной сети блогеров.

### Технологии
* Python 3.9
* Django 3.2
* Django REST framework 3.12.4

## Установка и запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:MPolskov/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
# для Windows:
py -3.9 -m venv venv
# для Linux:
python3.9 -m venv venv
```
```
# для Windows:
source venv/Scripts/activate
# для Linux:
sourse venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить сервер:
```
python manage.py runserver 0.0.0.0:8000
```
### Документация к API проекта Yatube (v1):
```
http://127.0.0.1:8000/redoc/
```
### Автор
Полшков Михаил
