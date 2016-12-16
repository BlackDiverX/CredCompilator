CredCompilator
==============

Набор утилит для создания сложных комбинаций слов из нескольких словарей.

Системные требования
---------
Требуется установленный Python.

Структура проекта:

| Файл/директория| Описание |
| ---------------| -------- |
| wordlists/ | словари русских имен и фамилий в транслите |
| cred-append.py | утилита для добавления текста в начало или конец строки |
| cred-compilator.py | утилита для создания всех комбинация слов из двух словарей |
| README.md | этот файл |
| LICENSE | лицензия |




Начало работы
-------------

###cred-compilator.py

Утилита для создания всех комбинация слов из двух словарей.

Синтаксис:

    python cred-compilator.py <InFile1> <InFile2> <break> <format> <OutFile>
    <InFile1> - входной файл 1;
    <InFile2> - входной файл 2;
    <break> - разделитель между словами. Чтобы создать список без разделителя, нужно вместо разделителя поставить '';
    <format> - формат вывода[unix|win|mac]. Устаналивает формат перевода строки;
    <OutFile> - файл результатов.

Пример:

    cred-compilator.py Name.txt Family.txt . unix Result.txt
    Результат:
    Список вида: имя.фамилия

###cred-append.py

Утилита для добавления текста в начало или конец строки.

Синтаксис:
    
    python cred-append.py <InFile> <append-text> <position> <format> <OutFile>
    <InFile> - входной файл;
    <append-text> - текст для добавления в конец строки;
    <position> - добавление в начало [start] или конец [end] строки;
    <format> - формат вывода[unix|win|mac]. Устаналивает формат перевода строки;
    <OutFile> - файл результатов.

Пример:

    python cred-append.py Logins.txt a end unix Result.txt

Что дальше
----------
Посетите наш сайт, посвященный обучению тестированию на проникновение.

Команда сайта BlackDiver.Net

[http://BlackDiver.Net](http://blackdiver.net)


