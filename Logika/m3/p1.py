with open('text.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)

    data = file.read()
    print(data)

author = input('вкажіть автора ')

with open('text.txt', 'r', encoding='utf-8') as file:
    file.write(f'({author})')


