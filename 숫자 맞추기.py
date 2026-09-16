import random

while True:
    answer = random.randint(1, 100)
    attempts = 0

    print("숫자 맞추기 게임을 시작 할 것이다.")
    print("맞추지 못하면 죽음 뿐.")

    while True:
        try:
            guess = int(input("1부터 100까지의 숫자를 입력하거라: "))
        except ValueError:
            print("숫자만 입력하거라.")
            continue   

        if guess < 1 or guess > 100:
            print("1부터 100까지의 숫자만 입력하거라.")
            continue    

        attempts += 1
        if attempts == 8:
            print("기회는 끝났다.")
            print("죽어라.")
            break

        if guess > answer:
            print("너무 높다. 더 낮은 숫자를 입력하거라.")
        elif guess < answer:
            print("너무 낮다. 더 높은 숫자를 입력하거라.")
        else:
            print(f"축하한다! {attempts}번 만에 맞췄다.")
            print("살아남은 것을 축하한다.")
            break
    again = input("다시 하겠는가? (네/아니요): ")

    if again.lower() != "네":
        print("게임을 종료한다. 다음에 또 하거라.")
        break
