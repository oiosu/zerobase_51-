# string 문자 
# 문자열, 문자열 연산, 슬라이싱
# 가장 많은 분야에서 사용 

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
















