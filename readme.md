# Что это?
Скрипт на python, который прогоняет программы по тестам, написанным самим пользователем
# Как пользоваться
Рекомендуется зайти в директорию, где хранятся папки с программами и склонировать данный репозиторий:
```
git clone https://github.com/Khudyakov1/func_tester.git
```
Чтобы работала проверка на стиль кода надо поместить файлы *Rules.txt* и *CodeChecker.exe* в директорию *func_tester*. *CodeChecker.exe* получается с помощью компиляции проекта [CodeChecker](https://git.iu7.bmstu.ru/IU7-Projects/CodeChecker), файл *Rules.txt* находится в этом же репозитории.

Дальше достаточно запустить файл *main.py*:
```
python3 main.py
```
# Способы адресации
Предусмотрено три способа адресация, поменять их можно, изменив значение параметра **ADDRESS_STYLE**, в файле *main.py*:
```python
ADDRESS_STYLE = 'PARENT' # 'PARENT' / 'CURRENT' / 'ABSOLUTE'
```
## PARENT
Доступ к директории с программой происходит из родительской директории файла *main.py*
## CURRENT
Доступ к директории с программой происходит из директории, в которой находится файл *main.py*
## ABSOLUTE
Пользователь вводит абсолютный адрес директории с программой
# Названия файлов
Меняя параметры **APP_NAME** и **FILE_NAME**, можно изменять, какие файлы будет программа искать (**FILE_NAME** - название файла с исходным кодом, **APP_NAME** - название файла, которые будет получаться при компиляции)

В строке
```python
run_tests.run(FILE_NAME, APP_NAME, directory=directory, positive_test_mask='pos_*_*.txt')
```
Можно указать маски файлов для позитивных и негативных файлов. Первый символ * будет заменён на число, второй на тип файла (*in*, *out*).
Например если указать маску как *'positive_test_*_*.txt'* программа будет искать тесты в виде *positive_test_01_in.txt*.

# Пример работы
```
Input folder name: lab_03_04_00
Build successful

Positive testing unsuccessful
Testpos_03_in.txt has failed:
  Expected result  | Recieved_result 
* 102              | 101             

Negative testing successful

Coverage:
File 'main.c'
Lines executed:100.00% of 37
Creating 'main.c.gcov'

Style check:
/.../lab_03_04_00/main.c(20,12): Incorrect lexema's first symbol register (is upper, but expected is lower)
/.../lab_03_04_00/main.c(20,12): Incorrect register of lexema, (upper, but expected lower)
``` 