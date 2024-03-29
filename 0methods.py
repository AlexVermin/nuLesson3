"""
квадратными скобками [] выделены необязательные параметры

list:
    .append(<новый_элемент>)
    .remove(<элемент>)
    .insert(<индекс>, <новый_элемент>)
    .sort([key = <пользовательская_функция_сортировки>])
    .clear()
dict:
    .keys()
    .items()
    .clear()
    .get(key[, <значение_ключа_умолчательное>])
    .values()
set:
    .add(<новый_элемент>)
    .clear()
    .discard(<элемент>),
    .isdisjoint(<множество_2>)
    .issubset(<множество_2>)
    .issuperset(<множество_2>)
str:
    .replace(<что_искать>, <чем_заменить>)
    .split([<разделитель>])
    .find(<что_искать>[, <начальная_позиция>[, <конечная_позиция>]]) - если заданы <начальная_позиция> и
        <конечная_позиция>, то они интерпретируются как индексы для среза исходной строки:
            str[<начальная_позиция>:<конечная_позиция>]
    .lower()
    .upper()
    .title()
"""
