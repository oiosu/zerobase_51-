# 딕셔너리 : 순서x, 중복x, 수정o, 삭제o
# key, value (JSON) => MongDB

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


# 정말 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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


# 집합 set
# 순서x, 중복x

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