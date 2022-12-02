def parse (expression):
    result = []
    number = ''
    for symbol in expression:
        if symbol.isdigit():
            number += symbol
        else:
            if number != '':
                result.append(float(number))
                number = ''
            result.append(symbol)
                
    else:
        if number:
            result.append(float(number))
    return result

def calculate(lst):
    result = 0.0
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index -1] + [result] + lst[index + 2:]
    return result

def braces(result):
    if '(' in result:
        index_open = result.index('(')
        index_close = result.index(')')
        res = calculate(result[index_open:index_close + 1])
        new_list = []
        first_part = result[:index_open]
        if len(first_part) != 0:
            new_list = first_part + [res]
        second_part = result[index_close + 1:]
        if len(second_part) != 0:
            new_list = [res] + second_part
        res = calculate(new_list)
    else:
        res = calculate(result)
    return res
