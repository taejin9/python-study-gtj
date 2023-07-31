# 교재 199p
# 700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지
# 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현

# 함수 정의
# 반환값 없음
# 함수 이름: vending_machine()
# 매개변수 : 정수 money

def vending_machine()
    price=700 #음료수 가격
num = money//price
change = money%price


vending_machine(3000)
#3000원을 넣었을 때 4잔의 음료수, 200원 잔돈