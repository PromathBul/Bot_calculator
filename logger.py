def log(update, context, separate_expression, result):
    expression = ' '.join(map(str, separate_expression))
    with open('users_info.csv', 'a', encoding= 'UTF-8') as data:
        data.write(f'{update.effective_chat.id}, {update.effective_chat.last_name}, {update.effective_chat.first_name}, {expression} = {result}\n')
