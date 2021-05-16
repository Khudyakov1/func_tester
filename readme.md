# Что это?
Скрипт на python, который прогоняет программы по тестам, написанным самим пользователем
![image](functional_testing.png)
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
## Способы:
- PARENT
>Доступ к директории с программой происходит из родительской директории файла *main.py*
- CURRENT
>Доступ к директории с программой происходит из директории, в которой находится файл *main.py*
- ABSOLUTE
>Пользователь вводит абсолютный адрес директории с программой
# Настройки тестирования для отдельных задач
Так как в при тестировании разных задач могут быть необходимы разные режимы тестирования, в приложении предусмотрена настройка тестирования. При запуске тестирования в тестируемой директории появится файл *config.ft*. Его содержимое будет выглядеть так:
```
strict_string: False
result_word: ""
app_name: "app.exe"
coverage: True
style_check: True
cleanup: True
flags: "-Wall -Werror -Wextra -Wpedantic -Wvla -Wfloat-equal -Wfloat-conversion --coverage -lm"
compiler: "gcc"
tests_folder: "func_tests"
positive_test_mask: "pos_*_*.txt"
negative_test_mask: "neg_*_*.txt"
```
В нём можно указать настройки тестирования для данной директории. При последующем запуске будут использованы параметры, указанные в файле.

<u>Параметры, являющиеся строка должны указываться в двойных кавычках!</u>
- **strict_string**
> Строгая проверка строк. Если *False*, будут сравниваться только числа
- **result_word**
> Подстрока, с которой начинается сравнение результатов
- **coverage**
> Выводить информацию о покрытии
- **style_check**
> Выводить информацию о стилевом тестировании
- **cleanup**
> Удалить файлы, созданные во время работы приложения
- **flags**
> Флаги, с которыми компилируется программа пользователя
- **compiler**
> Компилятор, используемый для компиляции
- **tests_folder**
> Поддиректория, в которой хранятся тесты
- **positive_test_mask**
> Маска, с помощью которой выполняется поиск файлов для позитивных тестов
- **negative_test_mask**
> Маска, с помощью которой выполняется поиск файлов для негативных тестов

# Пример работы
```
Input folder name: lab_03_05_00
Build successful

Positive testing unsuccessful
Test pos_04_in.txt has failed:
  Expected result  | Recieved_result 
  678 21 9 12      | 678 21 9 12     
  58 12 34 161     | 58 12 34 161    
  12 34 3 3        | 12 34 3 3       
* 123 34 1 6       | 123 34 1 5      

Negative testing successful

Coverage:
File 'main.c'
Lines executed:100.00% of 70
Creating 'main.c.gcov'

Style check:
/home/.../lab_03_05_00/main.c(21,12): Incorrect lexema's first symbol register (is upper, but expected is lower)
/home/.../lab_03_05_00/main.c(21,12): Incorrect register of lexema, (upper, but expected lower)
``` 