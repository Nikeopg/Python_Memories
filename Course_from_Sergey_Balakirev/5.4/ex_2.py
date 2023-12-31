"""
Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:
+7(xxx)xxx-xx-xx
где x - это цифра. Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.
Sample Input:
+7(123)456-78-99
Sample Output:
ДА
"""

number = input()
n = '1234567890'
lst = ['+', '7', '(', n, n, n, ')', n, n, n, '-', n, n, '-', n, n]
for i, m in enumerate(number):
    if m not in lst[i]:
        print('НЕТ')
        break
else:
    print('ДА')

print(lst)