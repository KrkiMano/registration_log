class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def registration(line):

    if len(line.split(' ')) != 3:
        raise ValueError

    name, e_mail, age = line.split(' ')

    if not name.isalpha():
        raise NotNameError

    if '@' not in line and '.' not in line:
        raise NotEmailError

    if age.isdigit() and not 10 <= int(age) <= 99:
        raise ValueError


def new_file(bad_file, good_file):
    with open('registrations.txt', 'r', encoding='utf8') as source_file, \
            open(bad_file, 'w', encoding='utf8') as bad_file, \
            open(good_file, 'w', encoding='utf8') as good_file:
        for line in source_file:
            line = line[:-1]
            try:
                registration(line)
            except ValueError:
                bad_file.write(f'Не присутсвуют все три поля, поле пустое или ошибка возраста: {line}\n')
            except NotNameError:
                bad_file.write(f'Поле имени содержит не только буквы, но и другие символы: {line}\n')
            except NotEmailError:
                bad_file.write(f'Поле е-мейл не содержит @ и точку: {line}\n')
            else:
                good_file.write(f'{line}\n')


new_file(bad_file='bad.txt', good_file='good.txt')
