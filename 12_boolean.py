
class myclass():
  def __len__(self):#0. len은 parameter의 길이를 평가해준다. 
    return 0 #0. 이 함수는 무조건 return 0이도록 설계

myobj = myclass() #1. myClass 로 myobj 생성, 함수 설계상 return 0
print(bool(myobj)) #2. bool로 myobj의 boolean을 체크, 0 니까 False


def myFunction():
  return True

print(myFunction())

x = 100
print(isinstance(x,int))