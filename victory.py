import random

my_data = {
    1: {'fio': 'Евгения Кафельникова', 'b_day': '18.02.1974'},
    2: {'fio': 'Икера Касильяса', 'b_day': '20.05.1981'},
    3: {'fio': 'Михаэля Шумахера', 'b_day': '03.01.1969'},
    4: {'fio': 'Хелены Бонэм Картер', 'b_day': '26.05.1966'},
    5: {'fio': 'Тома Йорка', 'b_day': '07.10.1968'},
    6: {'fio': 'Киану Ривза', 'b_day': '02.09.1964'},
    7: {'fio': 'Элвиса Пресли', 'b_day': '08.01.1935'},
    8: {'fio': 'Клаудии Шиффер', 'b_day': '25.08.1970'},
    9: {'fio': 'сэра Алекса Фергюссона', 'b_day': '31.12.1941'},
    0: {'fio': 'Николь Кидман', 'b_day': '20.06.1967'},
}
my_months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}
my_days = {
    1: 'первого',
    2: 'второго',
    3: 'третьего',
    4: 'четвёртого',
    5: 'пятого',
    6: 'шестого',
    7: 'седьмого',
    8: 'восьмого',
    9: 'девятого',
    10: 'десятого',
    11: 'одиннадцатого',
    12: 'двенадцатого',
    13: 'тринадцатого',
    14: 'четырнадцатого',
    15: 'пятнадцатого',
    16: 'шестнадцатого',
    17: 'семьнадцатого',
    18: 'восемьнадцатого',
    19: 'девятьнадцатого',
    20: 'двадцатого',
    30: 'тридцатого',
    '2': 'двадцать',
    '3': 'тридцать'
}
print('Добро пожаловать в "Викторину"!')
print('  Обращаем Ваше внимание, что ответы необходимо вводить в формате DD.MM.YYYY,')
print('    где DD - день, MM - месяц, YYYY - год.')
print('  Допустимым раделителем в дате является символ точки (.)')
print('  Ответ, введённый в неверном формате, не принимаются. Понадобится ввести его корректно.')
print('Итак, ПРИСТУПАЕМ!')
MAX_ANSWERS = 5
is_playing = True
while is_playing:
    print('#'*80)
    print('Новый раунд!')
    cur_answers = 0
    cur_questions = random.sample(list(my_data), MAX_ANSWERS)
    for idx in cur_questions:
        # print(idx, my_data[idx]['q'], my_data[idx]['a'])
        user_input = ''
        is_correct_input = False
        while not is_correct_input:
            user_input = input(f"  Введите дату рождения {my_data[idx]['fio']}: ")
            if user_input[:2].isdigit() and '.' == user_input[2:3] and user_input[3:5].isdigit() and '.' == user_input[5:6] and user_input[6:].isdigit():
                is_correct_input = True
            else:
                is_correct_input = False
                print('    Нарушен формат ввода, попробуйте снова.')
        if user_input == my_data[idx]['b_day']:
            cur_answers += 1
            print(f'  + правильно')
        else:
            written_date = ''
            m_day = int(my_data[idx]['b_day'][:2])
            m_day_digit = int(my_data[idx]['b_day'][1:2])
            if m_day < 21 or m_day == 30:
                written_date = my_days[m_day]
            elif m_day < 30:
                written_date = f'{my_days["2"]} {my_days[m_day_digit]}'
            else:
                written_date = f'{my_days["3"]} {my_days[m_day_digit]}'
            written_date = f'{written_date} {my_months[my_data[idx]["b_day"][3:5]]} {my_data[idx]["b_day"][6:]} года'
            print(f'  - не угадали, правильный ответ: {written_date}')

    print('-' * 80)
    print('Ваши результаты в этом раунде:')
    print(f'     правильных ответов: {cur_answers}')
    print(f'       неверных ответов: {MAX_ANSWERS-cur_answers}')
    print('-' * 80)
    once_again = None
    while True:
        if once_again is not None:
            print('  Пожалуйста, введите допустимое значение...')
        else:
            once_again = input('Ещё разок?.. (Y/y/Д/д - повторить, N/n/Н/н - выйти)')
            if once_again in 'YyДд':
                break
            elif once_again in 'NnНн':
                is_playing = False
                break
print('#'*80)
print('Спасибо за игру!')