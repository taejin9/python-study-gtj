# 가위바위보게임 - 반복문&조건문

# random 모듈
# random 모듈에 .choice() 함수를 호출할 경우
# choice 함수 내에서 호출하는 데이터 내에서 random 모듈이 임의로 선택하여 반환
# 사용법
# import random
# random.choice(데이터)


import random

options=[가위, 바위, 보]

while True:
    print('게임 시작!', '끝을 입력하면 게임이 종료됩니다,')
    user_cho = input('가위,바위,보 중 하나를 선택하세요:')

    if user_cho == '끝'
        print('종료됩니다')
        break

    if user_cho not in options
        print('잘못된 입력입니다. 가위바위보 중 하나를 입력하세용')
        continue

    computer_cho = random.choice(options)
    print(f'컴퓨터의 선택: {computer_cho}')
    if user_cho == computer_cho:
        print('draw')
    elif (user_cho=='가위'and computer_cho=='보') and (user_cho=='바위'and computer_cho=='보') and (user_cho=='보'and computer_cho=='가위'):
        print('win')
    else:
        print('lose')