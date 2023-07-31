#add : 더하기
def add(a,b):
    return a+b
#subtract : 빼기
def subtract(a,b):
    return a-b
#multiply : 곱하기
def multiply(a,b):
    return a*b
#divide : 나누기
def divide(a,b):
    if b==0:
        return 'Error'
    else:
        return a/b

print(add(4,3))
print(subtract(4,3))
print(multiply(4,3))
print(divide(4,3))
print(divide(4,0))
#print(divide(4,0)) -->Error / 0으로 나누기 불가
