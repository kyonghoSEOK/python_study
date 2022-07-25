"""
# 입력 메세지 출력
name = input()
print(f'my name is {name}')
print()

name = input("내 이름은 : ")
print(f'my name is {name}')
"""


"""
# input 은 기본적으로 문자열 취급받는다
my_money = input("내돈 : ")
your_money = input("상대방 돈 : ")

print(f'돈을 합치면 {my_money + your_money} 이다.')
"""

year = int(input("현재 연도 : "))
birth = int(input("태어난 연도 : "))
print("현재 나이는 %d" %(year - birth))
