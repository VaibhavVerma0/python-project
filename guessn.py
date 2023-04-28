import random as r
name=input("what is your name")
print("welcome")
print(name,"game begins")
print("--------------------")
num=r.randrange(1,10)
guess=100
i=0
score=0
while i<guess:
    guess_num=int(input("guess the number between 1 and 10::"))
    i+=1
    if guess_num<num:
        print("try again, guess is low\n")
        
    
    if guess_num>num:
        print("try again, guess is high\n")
        
    if guess_num==num:
        score+=10
        break
if num==guess_num:
    print(name,"you won")
    print(name,f"you guess the number in {i} attempts")
    print("your score is -->", score*i)





  
