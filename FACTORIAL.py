#import time module
# USE NESTED FUNTION TO PRINT FACTORIAL NUMBER WITH TIME
import time
# here,function define
def fact_time(fa_ti):
    def inside():
        begin = time.time()
        fa_ti(int(input('enter the number')),1)
        end = time.time()
        print('total time taken:',fa_ti.__name__,end-begin) #use name for to print its real name means factorial

    return inside
#here I write code of factorial and use sleep funtion for hold 2 sec
def factorial(x,a):
    for i in range(1,x+1):
        time.sleep(2)
        a=a*i
    print(a)

time_fact=fact_time(factorial)
time_fact()