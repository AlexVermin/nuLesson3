list_len = None
while not (list_len is not None and list_len.isdigit()):
    if list_len is not None:
        print('  Не является целым числом, попробуйте ещё раз...')
    list_len = input('Введите количество элементов в списке: ')
list_len = int(list_len)
if list_len > 15:
    print('А терпения-то хватит, столько вводить?.. Ограничимся 15-ю штуками.')
    list_len = 15

my_list = []
for idx in range(list_len):
    cur_elem = None
    while not (cur_elem is not None and cur_elem.isdigit()):
        if cur_elem is not None:
            print('  Не является целым числом, попробуйте ещё раз...')
        cur_elem = input(f'Введите {idx + 1:d}-й элемент списка(только целое число): ')
    my_list.append(int(cur_elem))

print('В итоге, введённый список:', my_list)
print('Применяем особую магию...')
my_list.sort()
print('Получили:', my_list)