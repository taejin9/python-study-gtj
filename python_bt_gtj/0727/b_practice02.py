#if문 복습 예제
#: 영화 평점을 입력받아, 이 평점에 따라 다른 메세지를 출력하는 프로그램
# 8점 이상이면 '좋은 영화'
# 5이상 8미만이면 '괜찮은 영화'
# 5미만이면 '기대 이하' 출력

rating = float(input('영화 평점을 입력하세요'))

if rating>=8
    print('좋은 영화')
elif rating>=5  # 8미만 조건 누락 - 프로그래밍에서는 위에서 아래로 코드 인식하기 때문에 첫번째 if문 조건에서 8이상인 수들은 이미 위에서 걸러짐!!!
    print('괜찮은 영화')
else rating<5
    print('기대 이하')