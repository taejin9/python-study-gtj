#1.
#(교과서) if문: 임의의 수를 입력하면 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요
#관계 연산자, 논리 연산자

#2.
#(교과서) if문: 미세먼지 저감 활동의 일환으로 차량 2부제를 실시하고자 합니다
#사용자로부터 차량번호를 입력받아 차량번호가 짝수로 끝나면 '운행가능'
#아니면 '운행불가'를 출력하는 프로그램을 구현하세요
#단, 차량번호는 '237가 1234'와 같은 형식으로 입력받는다고 가정합니다

#1.
a= int(input('임의의 수를 입력하세요:'))
b= int(input('임의의 수를 입력하세요:'))
c= int(input('임의의 수를 입력하세요:'))
L=0

if a>=b:  #a가 가장 클 때
    if b>=c:
        L=a
        print(L)
    if b<=c and a>=c:
        L=a
        print(L)
elif a<=b: #b
    if a>=c:
        L=b
        print(L)
    if a<=c and c<=b:
        L=b
        print(L)
else #c
    L=c
    print(L)

print('가장 큰 수는', L , '입니다')

#2.
carn = input('차량 번호를 입력하세요(예: 237가 1234):')

#입력받은 차량 번호에서 마지막 숫자를 추출
last_digit = int(carn[-1]) #문자열 형태를 정수형으로 변경

#마지막 숫자 홀짝 판별
if last_digit % 2 == 0:
    print('운행가능')
else:
    print('운행불가')