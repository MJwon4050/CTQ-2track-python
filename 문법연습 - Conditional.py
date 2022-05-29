#조건문 어쩌구가 True면 저쩌구가 실행됨
if 어쩌구 :
    저쩌구
#input
user_id = input('id?')#id?라는 질문 출력
user_pwd = input('password?')#password?라는 질문 출력
if user_id == 'minjaewon': #만약 id?라는 답이 minjaewon이면
    if user_pwd == 'CTQ2022' : #패스워드도 물어보는데
        print('안녕하세요.') #CTQ2022를 입력하면 안녕하세요.가 나옴
#else는 input값이 false라면 실행되는 커맨드
    else:
        print('비밀번호가 틀렸습니다.')#비번을 틀렸을시에 뜨는 문구
else:
    print('아이디가 틀렸습니다.')#아이디를 틀렸을 시에 뜨는 문구
