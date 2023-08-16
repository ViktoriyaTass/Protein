import numpy as np
import random
import sys




def calculating (random1,random2,op1):
       if op1=="*":
         actResult=random1*random2
       if op1=="+":
         actResult=random1+random2
       if op1=="-":
         actResult=random1-random2
       return actResult

def random_numbers(level):
    if level==1 :
      random1=random.randint(1,9)
    if level==2:
      random1=random.randint(10,19)
    if level==3:
      random1=random.randint(20,99)
    return random1


level=0
operator=['+','-','*']
##user enter his data;
print("Whats level do you want?")
level=int(input())

correct=3
i=0
while i<correct:
   if level ==1 or 2 or 3:
     random1=random_numbers(level)
     random2=random_numbers(level)
     random3=random_numbers(level)
     op1=random.choice(operator)
     op2=random.choice(operator)
   else:
      exit()

   print("What is ("+str(random1) + str(op1) + str(random2)+")" + str(op2) +str(random3) + "?" )
   answer=int(input())

   actResult=calculating(random1,random2,op1)
   actResult=calculating(actResult,random3,op2)
   

   if answer==actResult:
      correct=correct-1
      print("Good Job!!!")
   else : 
      print("Try again")
    

print("Good Morning!!!!!")
