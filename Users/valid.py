import re

class Login:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if len(value) < 5:
            raise ValueError("Логин не может содержать меньше 5 символов")
        self.value = value

class Email:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        regex = r"^\S+@\S+\.\S+$"
        if not re.match(regex, value):
            raise ValueError("Некорректный email")
        self.value = value

class Password:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        regex = "^(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        if not re.match(regex, value):
            raise ValueError("Пароль должен содержать как минимум 8 символов(букв и цифр)")
        self.value = value

class Phone:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if len(str(value)) != 11:
            raise ValueError("Некорректный номер телефона\nПример: 88005553535")
        self.value = value