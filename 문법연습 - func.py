#code...
a=1
b=2
c=3
s=a+b+c
r=s/3
print(r)
#code...

#def 새 함수 만들기
'''
def average ():
    a=1
    b=2
    c=3
    s=a+b+c
    r=s/3
    print(r)

average()
'''

'''
#input에 대해
#parameter(매개변수)
def average (a,b,c):
    s=a+b+c
    r=s/3
    print(r)
#argument(입력값)
average(10,20,30)
'''


def average (a,b,c):
    s=a+b+c
    r=s/3
    return r

print(average(10,20,30))
