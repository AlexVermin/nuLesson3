valid_separators = (',',';','/')
user_data = {}

for i in range(2):
    user_input = ''
    cur_separator = ''
    is_error = True
    while is_error:
        cur_separator = ''
        is_next_digit = True
        is_error = False
        user_input = input(f'Задайте {i+1}-ю последовательность цифр, разделенных одним из следующих знаков: "," или ";" или "/": ')
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
    user_data[i] = user_input.split(cur_separator)

my_magic_list = []
for x in user_data[0]:
    if x not in user_data[1]:
        my_magic_list.append(x)
print('Результат магии:', my_magic_list)