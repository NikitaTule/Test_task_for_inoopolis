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


def test_password(password, email=None):
    assert len(password) >= 8, print('Пароль должен содержать не менее 8 символов')
    assert check_uppercase_letters(password) is True, print('Пароль должен содержать хотя бы одну заглавную букву')
    assert check_lowercase_letters(password) is True, print('Пароль должен содержать хотя бы одну строчную букву')
    assert check_digits(password) is True, print('Пароль должен содержать хотя бы одну цифру')


test_password('33333333333333')
