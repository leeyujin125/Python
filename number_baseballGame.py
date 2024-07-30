from random import randint

# 사용자에게 숫자 3개를 입력받고, 입력받은 숫자가 컴퓨터가 랜덤으로 고른 숫자와 일치하는지 맞추는 게임
# 숫자와 위치가 동일하면 스트라이크, 숫자만 동일하면 볼
# 숫자와 위치가 완전히 동일한 3 스트라이크가 되기 전까지 게임이 계속 됨
# 마지막에 시도한 횟수를 알려줌

# 랜덤 숫자 3개 뽑기
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

# 숫자 입력받기
def take_guess():
    new_guess = []
    while len(new_guess) < 3:
        try:
            num = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요 (0-9): "))
            if num < 0 or num > 9:
                print("범위를 벗어나는 숫자입니다. 0에서 9 사이의 숫자를 입력하세요.")
            elif num in new_guess:
                print("이미 입력한 숫자입니다. 다른 숫자를 입력하세요.")
            else:
                new_guess.append(num)
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자만 입력하세요.")

    return new_guess

# 점수 맞히기
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count

# 게임 시작
ANSWER = generate_numbers()
tries = 0

while True:
    guesses = take_guess()
    strike_count, ball_count = get_score(guesses, ANSWER)
    tries += 1

    print(f"{strike_count} 스트라이크, {ball_count} 볼")

    if strike_count == 3:
        print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")
        break