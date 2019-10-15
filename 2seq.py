valid_separators = (',',';','/')
cur_separator = ''
user_input = ''
is_error = True
while is_error:
    cur_separator = ''
    is_next_digit = True
    is_error = False
    user_input = input('Задайте последовательность цифр, разделенных одним из следующих знаков: "," или ";" или "/": ')
    for char in user_input:
        if is_next_digit:
            if not char.isdigit():
                is_error = True
                print('    Обнаружен не цифровой символ.')
                break
            else:
                is_next_digit = False
        else:
            if char.isdigit():
                print('    Обнаружена цифра на месте разделителя.')
                is_error = True
                break
            else:
                if '' == cur_separator:
                    if char in valid_separators:
                        cur_separator = char
                    else:
                        print(f'    Символ "{char}" не является разрешенным разделителем.')
                        is_error = True
                        break
                else:
                    if char != cur_separator:
                        print('    Использование различных разделителей не допускается')
                        is_error = True
                        break
                is_next_digit = True
    if not is_error and cur_separator == user_input[-1:]:
        is_error = True
        print('    После разделителя не задана цифра.')

    if is_error:
        print('    Попробуйте ввести корректную строку данных...')

print(f'Символ "{cur_separator}" выбран разделителем.')
my_list = user_input.split(cur_separator)
my_unique_list = []
for x in my_list:
    if 1 == my_list.count(x):
        my_unique_list.append(x)
print('Список уникальных элементов:', my_unique_list)