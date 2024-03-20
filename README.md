<a id = "anchor"></a>
# Вычислитель отличий – программа, которая определяет разницу между двумя структурами данных.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/akasmall/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/akasmall/python-project-50/actions) <a>[![Maintainability](https://api.codeclimate.com/v1/badges/e87f520bf3e5d384a34f/maintainability)](https://codeclimate.com/github/akasmall/python-project-50/maintainability)</a> <a>[![Test Coverage](https://api.codeclimate.com/v1/badges/e87f520bf3e5d384a34f/test_coverage)](https://codeclimate.com/github/akasmall/python-project-50/test_coverage)</a>
<!-- [![Actions Status PyCI](https://github.com/akasmall/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/akasmall/python-project-50/actions)  -->

## Обзор
Проект создан в целях получения практического опыта разработки на языке Python на курсе компании __Хекслет__.
CLI-утилита сравнивает два конфигурационных файла, принимая на вход через командную строку два аргумента — пути до этих файлов.
Результат сравнения файлов может выводиться в разных форматах: plain ("плоский"), stylish (стильный) или json ("JSON-формат"). 

[Посмотреть видео проекта](#project-50)

---
## Требования
###### Для установки и запуска проекта, необходимы:
~~~sh
1. python версии 3.10 и выше
2. pyyaml = "^6.0.1" и выше
3. poetry версии 1.6.1 и выше
~~~
## Как установить
##### 1. [установить **python**](https://github.com/Hexlet/ru-instructions/blob/main/python.md)
###### 2. установить **pip**, с версии python 3.4 идет в пакете и/или обновить **pip**
~~~
$ # проверка pip
python3 -m pip --version
$ # если требуется обновление, то так:
python3 -m pip install --upgrade --user pip
~~~
###### 3. [установить менеджер пакетов **poetry**](https://python-poetry.org/docs/)
после установки 
~~~
$ # проверить что работает и версию
poetry --version
~~~

###### 4. создание виртуального окружения в директории проекта
~~~
$ # выполните команду
poetry config virtualenvs.in-project true
~~~
###### 5. склонируйте [репозиторий проекта](https://github.com/akasmall/python-project-50) с GitHub
~~~
git clone git@github.com:akasmall/python-project-50.git
~~~
###### 6. Подключите в зависимости библиотеку **pyyaml** командой
```
poetry add pyyaml
```
###### 7. собирите проект
```
make build
```

###### 8. установите проект
```
make package-install
```

## Как запускать вычислитель отличий
 
* без опции -- format
* **poetry** run **gendiff** [path to file]**file1.json** [path to file]**file2.json**
* **poetry** run **gendiff** [path to file]**file1.yml** [path to file]**file2.yml**

* c опцией -- format
* **poetry** run **gendiff** --format **stylish** [path to file]**file1.json** [path to file]**file2.json**
* **poetry** run **gendiff** --format **plain** [path to file]**file1.json** [path to file]**file2.json**
* **poetry** run **gendiff** --format **json** [path to file]**file1.json** [path to file]**file2.json**

* **poetry** run **gendiff** --format **stylish** [path to file]**file1.yml** [path to file]**file2.yml**
* **poetry** run **gendiff** --format **plain** [path to file]**file1.yml** [path to file]**file2.yml**
* **poetry** run **gendiff** --format **json** [path to file]**file1.yml** [path to file]**file2.yml**

## Видео - вычислитель отличий
<a id = "project-50"></a>
[![asciicast](https://asciinema.org/a/UnQFbHqQCM44yemjNwruhDxp4.svg)](https://asciinema.org/a/UnQFbHqQCM44yemjNwruhDxp4)


[Вверх](#anchor)