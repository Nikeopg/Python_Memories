m, d = map(int, input().split())
days_array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
prev_m = m
prev_d = d - 1

if prev_d == 0:
    prev_m -=1
    if prev_m <= 0:
        prev_m = 12
    prev_d = days_array[prev_m - 1]

next_m = m
next_d = d + 1

if next_d > days_array[next_m - 1]:
    next_d = 1
    next_m += 1
    if next_m == 13:
        next_m = 1

print(f"{str(prev_m).zfill(2)}.{str(prev_d).zfill(2)} {str(next_m).zfill(2)}.{str(next_d).zfill(2)}")


'''Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31'''