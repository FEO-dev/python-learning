password = "python123"
user_password = input ("Введите пароль    ")
if user_password == password:
    print ("Доступ разрешен")
else:
    print ("Доступ запрещен")
    if len (user_password) <= len (password):
        print ("Пароль слишком короткий")
    else:
        print ("Пароль слишком длинный")
