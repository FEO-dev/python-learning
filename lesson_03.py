secret = 7
count = 0
while True:
    guess = int (input ("Введите целое число от 1 до 50!"))
    count = count + 1
    if guess != secret:
        print ("Не угадал, попробуй ещё!")
    else:
        print ("Угадал!")
        print ("Количество попыток", count)
        break
