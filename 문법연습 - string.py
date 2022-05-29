#' or " 안에 넣어야 정상. 나눠져있는 이유는 ' 중복 대비
#\은 escape.
#\n은 줄바꿈.
#'''는 직관적(?)으로 쓰게 만듦.
print('hello world') #hello world가 나옴
print("hello world") #5번 줄과 동일
print("hell'o' world") #hell'o' world가 나옴
#escape
print("Hello'o' \"w\"orld") #Hell'o' "w"orld가 나옴
#new line
print('H\ne\nl\nl\no') #Hello가 모두 줄바꿈
#docstring
print('''
H
e
l
l
o
''') #11번 줄과 동일
