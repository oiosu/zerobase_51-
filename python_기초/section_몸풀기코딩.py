
# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

#출력문 
print('My name is READY')

#변수(어떤 값을 할당) 선언
myName = 'READY'

#조건문 
if myName == 'READY': #만약 내이름이 READY 라면 
    print('ok')       # ok를 출력해줘

#반복문 (구구단)
for i in range(1, 10): #1, 10 범위안에서 
    for j in range(1, 10):  #1, 10 범위안에서 
        print('%d * %d = ' %(i, j), i*j) #정수 곱하기 정수 = 범위안에서 돌면서?순회하면서 i와 j을 곱한 값을 출력해줘 

# 변수 선언(한글)_권장 사항은 아님
이름 = "좋은 사람"
print(이름)

#함수 선언 
def greeting():
    print('hello!')

greeting()

# 클래스 선언(가장중요)
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

# 정보 값 출력
print(id(cookie))
print(dir(cookie))
print(cookie.__class__)
print(cookie.__hash__)