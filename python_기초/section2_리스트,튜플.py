# 리스트, 튜플 _데이터 부분에 대해 더 잘 활용할 수 있다. 

#많은 변수를 사용하는건 비효율적이다. 자료구조를 이용하여 활용하는 것이 좋다. 
#리스트는 하나의 그릇이라고 생각하면 된다. 

# 리스트 (순서 o, 중복 o, 삭제o)
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


# 튜플!! (순서 o, 중복 o, 수정x, 삭제x) _ 고객 계좌번호 등 변경되면 오류가 생기는 것들(중요한 정보들)

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
