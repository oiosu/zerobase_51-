## 🛠Python_조건문 



### ✔ 조건문 if

* 조건문 기본 형식 
* 관계 연산자 실습 ( >, >=, <, <=, ==, !=)
* 논리연산자 실습(and or not)
* 다중 조건문(if / elif / else)
* 중첩 조건문 



```python
print(type(True))
print(type(False))

#예1
if True:
    print("yes")
#예2
if False:
    print("no")

#예2
if False:
    print("no")
else:
    print('yes2')

```



```python
#관계연산자
# >, >=, >. <=, == ,!=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
```





**🔹 참 거짓 종류 (True, False)**

**🔹 참 : "내용", [내용], (내용), {내용}, 1, True**

**🔹  거짓 : "", [], (), {}, 0, False**

```python
# 참 거짓 종류 (True, False)
# 참 : "내용", [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False

city = ""

if city:
    print("False")
else:
    print("True")
```



```python
# 논리연산자 
# and or not / (and = 교집합)

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or :', a > b or c > b)
print('not : ', not a > b)
print(not False)
print(not True)

```



```python
# 산술, 관계, 논리 연산자 
# 우선순위 : 산술 > 관계 > 논리 순서로 적용 
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("죄송합니다. 불합격입니다.")
```



```python
# 다중조건문_흐름제어(위에서부터 아래로)
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
elif num >= 70:
    print("num 등급 C", num)
else:
    print("꽝")
```



```python
# 중첩조건문
age = 20
height = 175

if age >= 20:  #키에 대한 조건
    if height >= 170:
        print("a지망 가능")
    elif height >= 160:
        print("b지망 가능")
    else:
        print("지원불가")
else:
    print("20세 이상 지원 가능")  #나이에 대한 조건
```

