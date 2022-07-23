# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 데이터타입, 숫자형 및 연산자 

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

"""
더하기 + 
뺴기 - 
곱하기 * 
나누기 / 

// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""

# 정수 선언
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


# 형 변환 (int, float, complex(복소수))

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


# 단항연산자 
y = 100
y += 100
print(y)

# 수치 연산 함수 
print(abs(-7)) #abs는 절대값을 구하는 함수 

n, m = 10, 20 #n은 10, m은 20으로 할당
n, m = divmod(100, 8) # 100을 8로 나누었을 때 n은 몫, m은 나머지 (divmod 함수!)
print(n, m) # 12 4

#외부 모듈
import math

print(math.ceil(5.1)) #ceil() : 5.1보다 작은 정수 출력 
print(math.floor(3.974)) #floor() : 3.874보다 작은 가까운 정수 출력 

#pi
print(math.pi)

# 2진수 변환
print(bin(50)) #0b로 시작

