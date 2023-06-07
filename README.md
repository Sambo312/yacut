# YaCut

Проект YaCut создает уникальные короткие ссылки на ресурсы сети интернет.

Технологии:

```
Python3.7, Flask2.0, Sqlalchemy 1.4
```

***Чтобы развернуть проект необходимо:***

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:Sambo312/yacut.git
```

```bash
cd yacut
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать файл .env в котором определить переменные с именем приложения, средой выполнения, доступом к БД, а также значение для SECRET_KEY:

```
FLASK_APP=
FLASK_ENV=
DATABASE_URI=
SECRET_KEY=
```

Выполнить миграции:

```bash
flask db init
flask db migrate -m "описание"
flask db upgrade
```

Запуск проекта:

```bash
Flask run
```

**Автор проекта:** [Хомутов Евгений](https://github.com/Sambo312/)
