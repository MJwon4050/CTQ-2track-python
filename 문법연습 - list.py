#[]=목록(list), 순서는 앞에서부터 0,1,2...
s = [1, 'four', 9, 16, 25]
print(s) #1,four,9,16,25
print(s[1]) #four
print (len(s)) #s라는 리스트의 길이
s[1] = 4 #s의 1번째 값은 4라고 명시.
print(s) #1,4,9,16,25
del s[2] #s의 2번째 값을 삭제
print(s) #1,4,16,25
s.append('minjaewon') #리스트명.append(값) = 끝에 새 값 추가
print(s) #1,4,16,25,minjaewon
