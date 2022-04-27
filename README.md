# note-keeper
Тестовое задание на предприятие "Серверсталь"

Прежде чем начать работу вам нужно иметь установленный интерпритатор __Python__ и платформу __Node JS__ для запуска javascript сценариев.
Если всё установленно, то дальше переходим в папку __'note-keeper'__  и запукаем следующие команды:

Установка, конфигурирование и запуск Python окружения:

#### Linux
```console
python -m venv env
. env/bin/activate
pip install flask-cors flask
flask run --port 5000
```
#### Windows
```console
py -m venv env
. env/Scripts/activate
pip install flask-cors flask
flask run --port 5000
```

Далее нужно перейти в папку __'client'__:

```console
cd client
```

И запускаем следующие команды(установка и запуск JavaSciprt окружения):

#### Linux and Windows
```console
npm i 
npm run dev
```