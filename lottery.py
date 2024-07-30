from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        number = randint(1, 46)  # 1부터 46까지의 랜덤한 숫자 생성
        if number not in numbers:  # 중복 체크
            numbers.append(number)
    return numbers


def draw_winning_numbers():
    win_numbers = []
    while len(win_numbers) < 6:
        numbers = randint(1, 46)
        if numbers not in win_numbers:
            win_numbers.append(numbers)
            win_numbers = sorted(win_numbers)

        extra_num = randint(1, 46)
        while extra_num in win_numbers:
            extra_num = randint(1, 46)

    win_numbers.append(extra_num)
    return win_numbers


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1
    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
