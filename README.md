<a name="Начало"></a>

# Rating Analysis

Cкрипт для обработки csv-файла

- [Описание](#Описание "Перейти")
- [Примеры запуска скрипта, тестов и csv-файла](#Примеры "Перейти")
- [Технологии](#Технологии "Перейти")
- [Запуск проекта на локальной машине](#Запуск "Перейти")
- [Запуск тестов](#Запуск_теста "Перейти")
- [Автор](#Автор "Перейти")

<a name="Описание"></a>

## Описание

Скрипт читает файлы с данными о рейтингах товаров и формирует отчеты.
Формируется один отчёт ```average-rating```. Отчёт включает в себя список брендов и средний рейтинг бренда, бренды сортируются по рейтингу. Название файлов и название отчета передается в виде параметров ```--files``` и ```--report```. Отчёт формируется по всем переданных файлам, а не по каждому отдельно.

Содержимое файлов всегда валидно, в архитектуру заложена возможность добавления новых отчётов, код покрыт тестами написанными на ```pytest```.

[Вернуться в начало](#Начало "Перейти")

<a name="Примеры"></a>

## Примеры запуска скрипта, тестов и csv-файла

> __Пример запуска скрипта__

![Пример запуска скрипта](/images_for_readme%20/image_script.png)

> __Пример запуска тестов__

![Пример запуска тестов](images_for_readme%20/image_tests.png)

> __Пример csv-файла__

![Пример csv-файла](images_for_readme%20/image_csv.png)

[Вернуться в начало](#Начало "Перейти")

<a name="Технологии"></a>

## Технологии

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org "Перейти")
[![PrettyTable](https://img.shields.io/badge/PrettyTable-1000?style=for-the-badge&logo=&logoColor=00c7fc&labelColor=4d22b3&color=5e30eb)](https://pypi.org/project/prettytable/ "Перейти")
[![Pytest](https://img.shields.io/badge/Pytest-1000?style=for-the-badge&logo=pytest&logoColor=ffffff&labelColor=be38f3&color=7b219f)](https://pypi.org/project/pytest/ "Перейти")


[Вернуться в начало](#Начало "Перейти")


<a name="Запуск"></a>

## Запуск проекта на локальной машине

- __Склонируйте репозиторий__

```python
git clone git@github.com:dmsnback/rating_analysis.git
```

- __Установите и активируйте виртуальное окружение__

Для ```Windows```

```python
python -m venv venv
```

Для ```Mac/Linux```

```python
python3 -m venv venv
```

Для ```Windows```

```python
source venv/Scripts/activate
```

Для ```Mac/Linux```

```python
source venv/bin/activate
```

- __Установите зависимости из файла__ ```requirements.txt```


> Обновите pip

Для ```Windows```

```python
python -m pip install --upgrade pip
```

Для ```Mac/Linux```

```python
python3 -m pip install --upgrade pip
```

> Установите зависимости

```python
pip install -r requirements.txt
```

- __Запустите скрипт__

> Файлы ```csv``` должны находится в папке ```files```, название файлов указывается после параметра ```--files```, название отчета указывается после параметрв ```--report```

Для ```Windows```

```python
python main.py --files products1.csv products2.csv --report average-rating 
```

Для ```Mac/Linux```

```python
python3 main.py --files products1.csv products2.csv --report average-rating 
```

> После запуска скрипта в терминале отобразится отчет в виде таблицы

![Пример запуска скрипта](images_for_readme%20/image_script.png)

[Вернуться в начало](#Начало "Перейти")

<a name="Запуск_теста"></a>

## Запуск тестов

> Находясь в корневом каталоге проекта выполните команду:

```python
pytest -v
```

> Пример запуска тестов

![Пример запуска тестов](images_for_readme%20/image_tests.png)

[Вернуться в начало](#Начало "Перейти")





## License

[MIT](https://choosealicense.com/licenses/mit/)

<a name="Автор"></a>

## Автор

- [Титенков Дмитрий](https://github.com/dmsnback "Перейти")

[Вернуться в начало](#Начало "Перейти")
