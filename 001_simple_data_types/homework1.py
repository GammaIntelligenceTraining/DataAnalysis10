# Написать программу которая:
#
# 1. Вычисляет возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)
# 2. Найти недостающую часть кода (code_2):
#    - найдите остаток от x деленого на y
#    - полученый результ умножьте на 13
#    - извлеките квадратный корень из полученного результата (аналогично возведению в степень 0.5)
#    - возьмите целую часть от результата
# 3. Соединить код в отдельную переменную
# пример:
# 475-12-967
# 4. Вывести строку используя доступные переменные:
# пример:
# Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.


# years
current_year = 2023
year_of_birth = 1988



# code parts
code_1 = '354'
code_3 = 132

# name
user_name = 'John'
user_surname = 'Smith'

# code 2 data
x = 152
y = 132

age = current_year - year_of_birth
code_2 = str(int((x % y * 13) ** 0.5))
code = code_1 + '-' + code_2 + '-' + str(code_3)

print('Hello ' + user_name + ' ' + user_surname + '. You are ' + str(age) + ' years old. Your secret code is ' + code + '.')