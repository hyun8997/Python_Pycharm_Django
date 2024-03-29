print()

'''
open(file, mode, , ...)
첫 번째 파라미터(file) : 파일의 상대경로
두 번째 파라미터(mode) : 파일을 여는 모드 옵션
 - r : 기본값. 읽기 전용
 - w : 파일 쓰기. 파일이 이미 존재한다면 해당 파일을 비움
 - x : 배타적 생성. 파일이 이미 존재한다면 opne() 실패
 - a : 파일 쓰기. 파일이 이미 존재한다면 파일의 끝에 내용을 덧붙임
 - b : 바이너리 모드로 열기
 - t : 텍스트 모드로 열기
 - + : 읽기와 쓰기를 모두 다
'''

f = open('good.txt', 'r', encoding='UTF8')  # 한글을 넣어서 엔코딩 처리 없으면 에러남

# 파일 전체 읽기
read = f.read()

# 파일 한 행 읽기
#read = f.readline()

# 파일 전체를 읽은 후 리스트로 리턴
#read = f.readlines()  # 읽어서 리스트로


# 자바 io는 while 안에서 끝을 찾을 때 까지 한줄씩 읽어야 했음
# 파이선은 처음 open을 하면 자동으로 이터레이팅 함, 자동으로 읽고있음
#
# file 객체는 순회가능(iterator)하므로 for 문에 리스트 대신 바로 file 객체를 넣을 수 있음
# for line in f:
#     print(line)

# 파일을 읽고 닫지 않으면 화면에 출력이 안되었으나 지금은 출력을 해줌 - 닫는게 권장
f.close()

print(read)
#print(read[4])   # 리스트로 리턴된거 인덱스로 출력


f2 = open('good2.txt', 'r', encoding='UTF8')  # 이 파일은 ANSI로 엔코딩 되어있음
                                            # 한글 쓸거면 파일 다 utf8로 저장하는게 편함
print(f2.read())

# 자료들을 볼때 단계 생략된거같으면 튜플 사용한것임

#------------------------------------------------------------------------------
# 파일을 열고 닫는 과정을 자동으로 해주고 그 과정에서 오류가 발생하면 알아서 처리
# with구문
with open('good.txt', encoding='UTF8') as f:
    print(f.readline())








































