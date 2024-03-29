print()

"""
# 같은 문자열에서 특정한 값을 바꾸고자 할 때
ex)
"오늘은 월요일입니다"

"오늘은 화요일입니다"
"""

# 문자열 format 기법 - keyword : %
'''
#  문자열 format code
 - %s : 문자열(string)
 - %c : 문자 1개 (character)
 - %d : 정수 (integer)
 - %f : 부동소수 (floating-point)
 - %o : 8진수
 - %x : 16진수
 - %% : 문자 %
'''

# 1) 숫자 또는 문자열 바로 대입
print('오늘 기온은 12도 입니다')
print('오늘 기온은 %d도 입니다' % 11)

print('오늘 기온은 %s도 입니다' % '십')

# 2) 변수로 대입
cel = 9

str = "오늘 기온은 %d도 입니다"

print(str % cel)

# 3) 한 개 이상의 값 format 가능
str2 = '오늘 기온은 %d도 입니다. %s 준비하세요'

print(str2 % (9, '우산'))
# % 뒤에 괄호를 사용하고 콤마로 각각 구분하면 됨
# 문자 데이터 입력시 따옴표 반드시 필요

# 4) %%
#str3 = '천재는 %d% 노력으로 이루어진다' # 에러 발생
str3 = '천재는 %d%% 노력으로 이루어진다'

print(str3 % 99)

print('--------------------------------------')
# 포맷코드를 숫자와 함께 사용하기
# 1) 공백
print('%15s' % 'hi') # 전체 문자열 길이가 15인 공간에서 왼쪽부터 공백을 두고 hi를 정렬해라

print('%-15s' % 'hello')  # 반대로도 가능

# 2) 소수점 표현하기

# 소수점 원하는 자리까지만 표현하고 싶을 때 (반올림 처리)
print('%0.5f' % 3.142545554)

print('%15.5f' % 3.142544456)
# 전체 15자리 자리수 중 오른쪽으로 정렬하고 공백주기





















