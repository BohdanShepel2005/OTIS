import math
 
def func(x):
    if x ->=_ 1:
        answer = 2/x+2,31*math.pow(math.e,2*x)
    elif x > -1:
        answer = math.asin(0,2*x+0,3)
    elif x <= -1:
        answer = math.cos(x+0,4*math.log(x+0,2))
 
    return answer
 
x = float(input("Введите х: "))
 
print(func(x))