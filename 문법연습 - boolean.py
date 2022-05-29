#숫자표현
print(1)

#문자표현
print('Hello world')

#Boolean은 참, 거짓으로 나눠짐
print(True) #참
print(False) #거짓

#연산자 + : 좌항과 우항을 더함
print(1+1) #2가 나옴
print('Hello'+'world') #Hello world가 나옴

#비교연산자 : 좌항과 우항을 비교해서 Boolean을 만들어 냄.
print(1==1) #True
print(1<2) #True
print(2<1) #False(2가 1보다 크기 때문)

#Membership operator
print('world' in 'Hello world') #True(world가 Hello world 안에 포함되는가?)

#파일의 유무
import os.path
print(os.path.exist('문법연습 - boolean.py')) #True
