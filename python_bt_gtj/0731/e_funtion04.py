### 지역변수 & 전역변수 ###

# 지역(local) 변수
# : 특정함수 또는 메섣 내부에서 선언된 변수
# : 선언된 함수 또는 메서드 내에서만 접근 가능
# : 함수가 종료되면 그 생명 주기도 끝남

def func():
    local_var="난 지역변수"
    print(local_var)

#func()
#print(local_var) # NameError: name 'local_var' is not defined

# 전역(global) 변수
# : 함수 외부에서 선언되며 프로그램 전체에서 접근할 수 있는 변수
# : 함수 내부에서 전역변수를 사용하려면 global 키워드를 사용하여 선언
def func2():
    # 전역변수를 단순히 참조만 하는 경우 global키워드 없이 사용 가능
    print(global_var)

#전역변수 값을 변경하는 경우
a=0
def fun3():
    global a
    a=8
    # global 키워드를 사용해 전역변수임을 확인시킨 후 변경
    return (a)


print(a) #0

print(fun3()) #8
