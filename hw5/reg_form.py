"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    !!! Для решения необходимо использовать функции и рекyрсию, а не циклы. !!!
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
        Программа выводит сообщение:
        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********
"""
from string import punctuation


def input_phone(): 
    number = input('Введите ваш телефон: ')
    number = re.sub(r'\D', '', number)
    number = '380' + number[-9:]
        if len(final_number) != 12
            return input_phone()
        else:
            return final_number

        
def input_email():
    email = input('Введите ваш email:')
    at_sign = 0
    if len(email) >= 6:
        for i in email:
            if i =='@':
                at_sign += 1
        if at_sign != 1:
            return input_email() 
        else:
            return email
    else:
        return input_email()

    
def input_password():
    upper, lower, digit, punct = 0, 0, 0, 0
    password = input('Введите пароль:')
    for i in password:
        if i.isspace():
            return input_password()
        elif i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.digit():
            digit += 1
        else:
            punct += 1
    if len(password) < 8:
        return input_password()
    else:
        if lower >= 1 and upper >= 1 and digit >= 1 and punct >= 1:
            return password
        else:
            return input_password()


def password_check():
    password = input_password()
    password2 = input('Подтвердите пароль:') 
    if password2 == password: 
        return password2
    else:
        return password_check()        

    
def main():
    phone = input_phone()
    email = input_email()
    password = password_check() 
    print(
    'Поздравляем с успешной регистрацией! '+ '\n' +
    'Ваш номер телефона: ' + phone + '\n' +
    'Ваш email: ' + email + '\n' +
    'Ваш пароль: ' + password
    )
    
    
main()
