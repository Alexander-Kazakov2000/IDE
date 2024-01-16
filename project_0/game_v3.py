"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # Счетчик попыток
    count = 0
    # Числа минимального и максимального диапазона соответсвенно 
    a = 1
    b = 101
    # Рандомное число с изменяемым дмапозоном 
    predict = np.random.randint(a, b)
    # Цикл, который завершится, если искомое число будет равняться нашему   
    while number != predict:
        count += 1
        # Если загаданое число больше нашего, то первое число диапазона будет равнятся ему
        if number > predict:
            a = predict
        # Если загаданое число меньше нашего, то второе число диапазона будет равнятся ему
        elif number < predict:
            b = predict
        # Обновляем число
        predict = np.random.randint(a, b)
    # Ваш код заканчивается здесь

    return count
    

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)