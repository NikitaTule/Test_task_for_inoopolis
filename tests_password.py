def check_digits(string):
    """Проверка есть ли в строке цифра"""
    for char in string:
        if char.isdigit():
            return True
    return False


def check_uppercase_letters(string):
    """Проверка есть ли в строке буква в верхнем регистре"""
    for char in string:
        if char.isalpha() and char.isupper():
            return True
    return False


def check_lowercase_letters(string):
    """Проверка есть ли в строке строчная буква"""
    for char in string:
        if char.isalpha() and char.islower():
            return True
    return False


def check_special_characters(string):
    """Проверка наличия спец символов"""
    special_characters = ["!", "@", "#", "$"]
    for char in special_characters:
        if char in string:
            return True
    return False


def check_password(username, password):
    """Проверка логина и пароля на схожесть"""
    if username.lower() in password.lower():
        return False
    return True


def test_password(password, email):
    assert len(password) >= 8, print('Пароль должен содержать не менее 8 символов')
    assert check_uppercase_letters(password) is True, print('Пароль должен содержать хотя бы одну заглавную букву')
    assert check_lowercase_letters(password) is True, print('Пароль должен содержать хотя бы одну строчную букву')
    assert check_digits(password) is True, print('Пароль должен содержать хотя бы одну цифру')
    assert check_special_characters(password) is True, print('Пароль должен содержать хотя '
                                                             'бы один специальный символ из перечисленных: !, @, #, $')
    assert check_password(email, password) is True, print('Пароль не должен содержать подстроку,'
                                                          ' совпадающую с частью имени ')


test_password('пароль', 'логин')
