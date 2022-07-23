## 🛠 Python_자료형



### ✔ 데이터타입, 숫자형 및 연산자 

* **Boolean / Numbers / String / Bytes / Lists / Tuple / Sets / Dictionaries**



**◾ print(type())** 

```python
v_str1 = "Nice" # <class 'str'>
v_bool = True   # <class 'bool'> 
v_str2 = "Good" # <class 'str'> 
v_float = 10.3  # <class 'float'>
v_int = 7       # <class 'int'>
v_dict = {      # <class 'dict'>
    "name" : "IM",
    "age" : 26
}
v_list = [3, 5, 7]  # <class 'list'>
v_tuple = 3, 5, 7   # <class 'tuple'>
v_set = {7, 8, 9}   # <class 'set'>
```



* **정수 선언** 

```python
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)


result = f3 + i2
print(result, type(result)) #939.5 <class 'float'>
```



* **형 변환 (int, float, complex(복소수))**

```python
a = 5.
b = 43
c = 10

print(type(a), type(b), type(c))
result2 = a + b
print(int(result2)) # 9  
print(float(c))  # 10.0
print(complex(3)) # (3+0j)
print(int(True)) # 1
print(int(False)) # 0
print(int('3'))  # 3
print(complex(False)) # 0j
```



* **단항연산자 / 수치 연산 함수** 

```python
# 단항연산자 
y = 100
y += 100
print(y)

# 수치 연산 함수 
print(abs(-7)) #abs는 절대값을 구하는 함수 

n, m = 10, 20 #n은 10, m은 20으로 할당
n, m = divmod(100, 8) # 100을 8로 나누었을 때 n은 몫, m은 나머지 (divmod 함수!)
print(n, m) # 12 4
```



* **외부모듈, pi, 2진수 변환**

```python
import math

print(math.ceil(5.1)) #ceil() : 5.1보다 작은 정수 출력 
print(math.floor(3.974)) #floor() : 3.874보다 작은 가까운 정수 출력 

#pi
print(math.pi)

# 2진수 변환
print(bin(50)) #0b로 시작
```



---



### ✔ 문자열

* 문자열 생성, 길이
* 이스케이프 문자 
* 문자열 연산
* 문자열 형 변환
* 문자열 함수 
* 문자열 슬라이싱

```python
str1 = "i am girl" #권장
str2 = 'nice time' #권장
str3 = ' '
str4 = str()
str5 = str('ace')

print(len(str1), len(str2), len(str3), str(str4), str(str5))  # 문자열 길이 

escape_str1 = "do you have a \"big\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2) #4칸의 기본적인 공백만큼 출력이 된다. 

# Raw String _ 경로를 표시할때 많이 사용한다. 
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

# 멀틸라인 
multi = \
    """ 
    문자열 
    멀티라인 
    테스트 
    """
print(multi)

#문자열 연산 
str_01 = '*'
str_02= 'abc'
str_03 = "def"
str_04 = "niceyou"

print(str_01 * 100) # * 가 100번 반복한다. 
print(str_02 + str_03) # abcdef
#print(str_01 + 3) #TypeError : can only concatenate str (not"int") to str
print(str_01 * 3) # ***

# str_04라고 지정해준 것은 변경이 불가능한 시퀀스 이기 떄문에 in 사용이 가능하다 (순회하라!)
print('a' in str_04) #a라는 글자가 str_04에 포함되어있니?
print('n' in str_04)
print('z' not in str_04) #z라는 글자가 str_04에 포함되어 있지 않지? 

# 문자열 형 변환
print(str(77) + 'a') #77a
print(str(10.4)) #10.4
```

###  

* **문장열 함수** 

```python
# 문자열 함수 
# a = 'nicemen'
# b = "orange"

# print(a.islower()) #소문자로 되어있니?
# print(b.endswith('e')) #끝글자가 s로 끝나니?
# print(a.capitalize()) #첫글자만 대문자로 바꿔줌 
# print(a.replace('nice', 'good')) #replace_ 특정 부분만 수정해주는 것 
# print(list(reversed(b))) # 글자가 거꾸로 출력 


# 문자열은 한번만 할당이 되면 수정이 불가하다. 

a = 'niceman'
b = "orange"

print(a[0:3]) #0부터 3까지 출력_인덱스! (3인덱스 직전까지) #nic
print(a[0:4]) #nice
print(a[0:7]) #이렇게 작성하는 것보다 다음과 같이 작성!
print(a[0:len(a)])
print(a[0:len(a)-1])
print(a[:4]) #nice
print(a[:]) #niceman
print(b[0:4:2]) #처음부터 4까지 나오는데 2개의 알파벳을 건너뛰기_ 3번째는 스킵한다는 뜻
print(b[1:-2]) #ran
print(b[::-1]) # egnaro
```



---



### ✔ 리스트, 튜플 

> 많은 변수를 사용하는 건 비효율적이다. 자료구조를 이용하여 활용하는 것이 좋다. 
>
> 리스트는 하나의 그릇이라고 생각하자!

* 리스트 특징
* 튜플 특징
* 인덱싱
* 슬라이싱
* 삽입, 삭제, 함수 사용



#### **📌 리스트  (순서 o, 중복 o, 삭제o)**

```python
# 선언 
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'banana', 'orange'] #중첩 가능 
e = [10, 100, ['pen', 'banana', 'orange']] #중첩 가능 

# 인덱싱_원하는 데이터를 활용과 응용 가능 
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

#슬라이싱 
print(d[0:3])
print(d[0:1])
print(e[2][1:3])

#연산 
print(c + d) # [1, 2, 3, 4, 10, 100, 'pen', 'banana', 'orange']
print(c * 3) 
#print(c[0] + 'hi') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(c[0]) + 'hi') # 1hi (str로 형변환)

# 리스트 수정, 삭제 
c[0] = 77
print(c) #[77, 2, 3, 4]

c[1:2] = [100, 1000, 10000] 
print(c) # [77, 100, 1000, 10000, 3, 4]

c[1] = ['a', 'b', 'c']
print(c) #[77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

# 삭제 del
del c[1]
print(c) #[77, 1000, 10000, 3, 4]

del c[-1]
print(c) #[77, 1000, 10000, 3]

print()
print()

```



* **리스트 함수** 

```python
# 리스트 함수 
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 끝부분에 6 추가하기 
y.sort() # 오름차순으로 정렬 
y.reverse() # 반대로 출력
y.insert(2, 7) # append와 insert 차이점 알고 있기!
y.remove(2) #삭제하는 함수 (del과의 차이점은, del은 원하는 인덱스 값을 삭제, remove는 원하는 값을 삭제)
y.pop() #맨 마지막 값을 삭제  LIFO! 스택!

ex = [88, 77]
y.extend(ex) #끝부분에 값이 추가(extend는 연장이라는 뜻)
y.append(ex) # 리스트 자체가 삽입 (extend vs append)

# 삭제 : del, remove, pop
```



---



### 📌 튜플 (순서 o, 중복 o, 수정x, 삭제x)

> 고객 계좌번호 등 변경되면 오류가 생기는 것들(변하지 않는 중요한 정보들)



```python
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c')) #중복 선언 가능
# del c[2] # TypeError : 'tuple' object doesn't support item deletion

print(c[2])
print(c[3])
print(d[2][3])
print(d[2][1])

#슬라이싱 
print(d[2:])
print(d[2][0:2])

# 연산 
print(c + d)
print(c * 3)


# 튜플 함수 
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z) # z에 3이 있나요? 
print(z.index(3)) # 내가 찾고자 하는 인덱스 값을 출력해준다. 
print(z.index(5))
print(z.count(1)) # 1은 몇개가 있어?

```



---



### 📌 딕셔너리 (순서x, 중복x, 수정o, 삭제o)

> key, value (JSON) => MongDB

* 딕셔너리 특징
* 딕셔너리 추가 
* 자료형 반환

```python
#  선언 
a = {'name': 'su', 'phone': '010', 'birth': 89766} 
#key : name, phone, birth 
#value : su, 010, 89766 
b = {0: 'hello', 1: 'coding'}
#어떠한 데이터 값도 파이썬에서는 딕셔너리에 넣을 수 있다. 
c = {'arr': [1, 2, 3]} 

#print(type(a)) #dic

# 출력
print(a['name']) #su
#print(a['name1']) # KeyError : 'name1' 

#get이라는 메소드를 사용하면 안전하게 조회가 가능하다. 
print(a.get('name'))
print(a.get('address')) #오류없이 none 출력됨
print(c['arr'])
print(c['arr'][1:3]) #[2, 3]

# 딕셔너리 추가 
a['address'] = 'Seoul'
print(a) 
#{'name': 'su', 'phone': '010', 'birth': 89766, 'address': 'Seoul'} / 순서가 없기 떄문에 출력시 순서가 다르게 나올 수 있다. 

a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3)
print(a)

```



```python
# ⭐정말 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# keys, values, items(key+value)
print(a.keys()) #key만 리스트 형식으로 출력
#print(a.keys()[0]) #TypeError : 'dict_keys' object does not support indexing

# 형 변환 해주기!!!
print(list(a.keys()))
temp = list(a.kety())
print(temp[1:3])

print(a.values())
print(list(a.values))

print(a.items())
print(list(a.items())) #list안에 튜플이 있는 형태로 출력 
print(1 in b)
print(2 in b)
print('nmae' in a)
print('name2' in a)
print('name2' not in a)

```



---



### 📌 집합 set (순서x, 중복x)

* 집합 특징 
* 집합 자료형 함수 
* 자료형 반환

```python
a = set()
b = set([1, 2, 3, 4,])
c = set([1, 2, 3, 4, 6, 6])

print(type(a)) #set
print(c) #{1, 4, 5, 6} 중복을 허용하지 않기 때문에 6이 2개임에도 불구하고 1개만 출력

#슬라이싱_형변환하여 사용
t = tuple(b)
print(t)

l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) #교집합
print(s1 & s2) #교집합 

print(s1 | s2) #합집합
print(s1.union(s2)) #합집합 / 중복되는 값들은 제거!

print(s1 - s2) #차집합
print(s1.difference(s2)) #차집합 


# 추가 & 제거 
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7) #중복되기 때문에 결과값이 그래로임.

print(s3)

s3.remove(15)
print(s3)

print(type(set)) #set
```

