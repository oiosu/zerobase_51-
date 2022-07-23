## 🛠 Print 함수의 이해 

### ✔ print()

* 가장 기본적인 output(출력) 함수
* 기본적으로 출력하는 함수
* seperator, end 옵션 사용
* escape code 사용법 



```python
# 기본 출력 : 문법적 중요, 텍스트 의미
print('Hello Python!')  
print("Hello Python!")  
print("""Hello Python!""")
print('''Hello Python!''')
```



* **seperator 옵션 사용** 

```python
print('T', 'E', 'S', 'T', sep='')  
# TEST
print('2019', '02', '19', sep='-') 
# 2019-02-19
print('niceman', 'google.com', sep='@') 
#niceman@google.com
```



* **end 옵션 사용** 

```python
print('Welcome To', end=' ') #Welcome To
print('the black parade', end=' ') #Welcome To the black parade
print('piano notes') # Welcome To the black parade piano notes
```



* **format 사용 [], {}, ()** 

👉 다양하게 활용할 수 있는 방법에 대해 익숙해 질 수 있도록 하기

👉 맵핑하는 구조도 잘 생각하기 

```python
print('{} and {}'.format('You', 'Me')) 
#You and Me
print('{0} and {1} and {0}'.format('You', 'Me')) 
#You and Me and You 
print("{a} are {b}".format(a='you', b='me'))
#you are me
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))
#You are Niceman
```



* **만약 format()을 사용하고 싶지 않다면?**
  * **format()보다 정확하다.** 
  * **%d(정수), %f(소수), %s(문자)**

```python
print("%s's favorite number is %D" % ('sukyung', 3))

# %5d : 5자리 정수 
# %4.2f : 정수자리는 4자리, 소수는 2자리 
print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) 
#Test1: 776, Price: 6534.12

# {}로 묶으면 더 확실하게 정보를 넣을 수 있으며 %를 넣지 않아도 된다. 
print("Test1: {0:5d}, Price:{1:4.2f}".format(776, 6534.123)) 
#Test1: 776, Price:6534.12

print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123)) 
#Test1:   776, Price: 6534.12
```



```python
v_str1 = "Nice" # <class 'str'>

v_bool = True  # <class 'bool'> 

v_str2 = "Good" # <class 'str'> 

v_float = 10.3  # <class 'float'>

v_int = 7    # <class 'int'>

v_dict = {    # <class 'dict'>

  "name" : "IM",

  "age" : 26

}

v_list = [3, 5, 7]  # <class 'list'>

v_tuple = 3, 5, 7  # <class 'tuple'>

v_set = {7, 8, 9}  # <class 'set'>
```

```python
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\n')
print('\t\t\ttest')
```



```python
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
```



---



### ✔ python 다양한 문법 기초 실습 

* 인코딩(입력, 출력)
* 변수
* 조건문
* 함수, 클래스, 인스턴스(객체)
* 정보 출력



```python
import this
```

 The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```python
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

#utf-8
#utf-8
```



* **출력문** 

```python
print('My name is READY')
```



* **변수(어떤 값을 할당) 선언** 

```python
myName = 'READY'
```



* **조건문**

```python
if myName == 'READY': #만약 내이름이 READY 라면 
    print('ok')       # ok를 출력해줘
```



* **반복문 (구구단)**

```python
for i in range(1, 10): #1, 10 범위안에서 
    for j in range(1, 10):  #1, 10 범위안에서 
        print('%d * %d = ' %(i, j), i*j) #정수 곱하기 정수 = 범위안에서 돌면서?순회하면서 i와 j을 곱한 값을 출력해줘 
```



* **변수 선언(한글)_권장 사항은 아님**

```python
이름 = "좋은 사람"
print(이름)
```



* **함수 선언**

```python
def greeting():
    print('hello!')

greeting()
```



* **⭐가장 중요한 class! 클래스** 

```python
# 클래스 선언
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

# 정보 값 출력
print(id(cookie))
print(dir(cookie))
print(cookie.__class__)
print(cookie.__hash__)




1249529208736
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
<class '__main__.Cookie'>
<method-wrapper '__hash__' of Cookie object at 0x00000122EDBE9FA0>
```

