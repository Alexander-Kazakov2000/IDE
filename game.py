import numpy as np
number = np.random.randint(1, 101)
count = 0

# comment
while True:
    count+=1
    user_number = int(input("Введите число:"))
    if user_number > number:
        print ('Ваше число больше загаданого.')
    elif user_number < number:
        print ('Ваше число меньше загаданого.')
    else:
        print (f'Вы угдали загаданное число {number}, за {count} попыток')
        break
    
