import random
Question =input('Question:   ')
random_numer = random.randint(1, 9)

if random_numer==1:
    print("Yes - definitely.")
elif random_numer==2:
    print("It is decidedly so.")  
elif random_numer==3:
    print("Without a doubt")      
elif random_numer==4:
    print("Reply hazy, try again.")    
elif random_numer==5:
    print("Ask again later")
elif random_numer==6:
    print("Better not tell you now.")
elif random_numer==7:
    print("My sources say no.")
elif random_numer==8:
    print("Outlook not so good.")
else:
    print("Very doubtful.")                

