#Rock Paper Scissors

print("Welcome to the game of Rock Paper Scissors!")

import random
count=0                                                 #game count
usc=0                                                   #user score
csc=0                                                   #computer score

rps=['rock','paper','scissors']                         #Possible outcomes
for i in range(5):
    cc=(random.choice(rps))                                 #Computer choice
    uc=input("Enter a choice - rock, paper, or scissors: ") #User choice
    print("You chose",uc.upper(),"and the computer chose",cc.upper(),'\n')
    
    #conditions for a tie:
    if uc.startswith('r') and cc.startswith('r'):
        print("Tie! \n")
        count+=1
    elif uc.startswith('p') and cc.startswith('p'):
        print("Tie! \n")
        count+=1
    elif uc.startswith('s') and cc.startswith('s'):
        print("Tie! \n")
        count+=1
        
    #conditions for a win or loss with user choice rock:   
    elif uc.startswith('r') and cc.startswith('p'):
        print("Computer wins this round! \n")
        count+=1
        csc+=1
    elif uc.startswith('r') and cc.startswith('s'):
        print("User wins this round! \n")
        count+=1
        usc+=1
        
    #conditions for a win or loss with user choice paper:
    elif uc.startswith('p') and cc.startswith('s'):
        print("Computer wins this round! \n")
        count+=1
        csc+=1
    elif uc.startswith('p') and cc.startswith('r'):
        print("User wins this round! \n")
        count+=1
        usc+=1
        
    #conditions for a win or loss with user choice scissors:
    elif uc.startswith('s') and cc.startswith('r'):
        print("Computer wins this round! \n")
        count+=1
        csc+=1
    elif uc.startswith('s') and cc.startswith('p'):
        print("User wins this round! \n")
        count+=1
        usc+=1


print("Final score after 5 rounds is: \n Computer = ",csc,"\n User = ",usc)        
if usc>csc:
    print("Congrats! You won! \n")
elif usc<csc:
    print("Computer wins :( Seems like AI is taking over the world :( \n")
elif usc==csc:
    print("It's a tie \n")