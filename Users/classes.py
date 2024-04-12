from valid import *

class User:
    login = Login()
    password = Password()
    phone = Phone()
    email = Email()
    
    count_users = 0
    def __init__(self, login:str, password:str, phone:int, email:str) -> None:
        self.login = login
        self.password = password
        self.phone = phone
        self.email = email
        User.count_users += 1
        
    def __repr__(self) -> str:
        return f'Роль - {self.__class__.__name__}, Логин - {self.login.title()}, E-mail - {self.email}, phone - {self.phone}'
    
    def _change_password(self, new_password):
        self.password == new_password
    
    
    
    


class Admin(User):
    def __init__(self, login: str, password: str, phone: int, email: str, admin_code:str = 'A1S2D3F4G5Hero') -> None:
        super().__init__(login, password, phone, email)
        self.admin_code = admin_code
    
    def __repr__(self) -> str:
        return f'Роль - {self.__class__.__name__}, Логин - {self.login.title()}, E-mail - {self.email}, phone - {self.phone}'
    
    
    
