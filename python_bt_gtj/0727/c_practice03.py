#1
#(교) 1부터 5사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램을 구현

#range함수 - 세 개의 인자(범위 시작점, 범위 끝점, 간격)
for i in range(5, 0, -1): # 역순으로 해야하기 때문에 1이 아니라 -1
    print(i)
# #1
# a=5
#
# for a>1 and a<5
#     a -= 1
#     print(a)


#2
#(교) 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤
# 그 숫자만큼 '과일 이름'을 입력받아 basket 리스트에 저장하는 프로그램을 구현

num = int(input'입력할 과일의 개수:'))

#basket 빈 리스트 생성
basket= []

#입력받은 숫자만큼 반복하면서 과일 이름을 입력 받고 리스트에 추가
for i in range(num):
    fruit=input('과일 이름:')
    basket.append(fruit)

print('과일 바구니:', basket)