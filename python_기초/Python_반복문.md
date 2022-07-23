## 🛠Python_반복문 



### ✔  반복문_for, while

* python 코딩의 핵심 
* 시퀀스 type  반복
* continue, break
* for - else 구문
* 자료구조 변환



**🔹 while**

```python
v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1
```



**🔹 for**

```python
for v2 in range(10):     #0부터 9까지의 범위
    print("v2 is :", v2)


for v3 in range(1, 11):
    print("v3 is :", v3)
```



**🔹 1 ~ 100 합**

```python
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1, 100))) #range 함수를 이용하여 효율성있게 합 구하기 
print('1 ~ 100 : ', sum(range(1, 1000, 2))) #1~100 까지 중에서도 짝수의 합 구하기 

```



**🔹 시퀀스 (순서가 있는) 자료형 반복** 

**🔹 문자열, 리스트, 튜플, 집합, 사전** 

**🔹 iterable 리턴 함수 : range, reverse, enumerate, filter, map, zip**

```python
names = ['su', 'pa', 'cho', 'yoo', 'chou']

for name in names:
    print("You are : ", v)

word = "dreams"

for s in word:
    print("word : ", s)

my_info = {
    "name": "su",
    "age": 20,
    "city": seoul
}
```



#### **🔥 암기!**

```python
# 기본 값은 키
for key in my_info:
    print("my_info", key) 
# 값
for key in my_info.values():
    print("my_info", key)
# 키
for key in my_info.keys():
    print("my_info", key)
# 키 and 값
for k, v in my_info.items():
    print("my_info", k, v)
```



```python
# 소문자는 대문자로, 대문자는 소문자로


name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())
```



**🔹 break**

```python
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")
```



**🔹 for-else (반복문이 정상적으로 수행된 경우 else 블럭 수행)**

```python
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33!")
else:
    print("Not found 33.....")

```



**🔹 continue**

```python
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))


name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))

```

