# Section_print()
# 참고 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력 : 문법적 중요, 텍스트 의미
print('Hello Python!')  
print("Hello Python!")  
print("""Hello Python!""")
print('''Hello Python!''')

print()

# separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')  # TEST
print('2019', '02', '19', sep='-') # 2019-02-19
print('niceman', 'google.com', sep='@') #niceman@google.com

print()

# end 옵션 사용
print('Welcome To', end=' ') #Welcome To
print('the black parade', end=' ') #Welcome To the black parade
print('piano notes') # Welcome To the black parade piano notes

print()

# format 사용 [], {}, () => 가장 중요 
print('{} and {}'.format('You', 'Me')) #You and Me
print('{0} and {1} and {0}'.format('You', 'Me')) #You and Me and You 
print("{a} are {b}".format(a='you', b='me')) #you are me
print('{var1} are {var2}'.format(var1='You', var2='Niceman')) #You are Niceman

print()

# 만약 format()를 사용하고 싶지 않다면, 다음과 같이 사용한다. 
# format()보다 정확하다. 
# %d(정수), %f(소수), %s(문자)
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


# 참고 : Escape 코드 참고 예제 
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\n')
print('\t\t\ttest')


"""
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
...

"""