import csv
from president_set import Presidents
from user import User
import inflect


def main():
    us = get_user_name()
    introduction(us)
    #training()
    #match_trainings_set()


'''
The user name is needet to store their score in a csv file, so the user can
see their improvements over time.  

:input type str:
'''
def get_user_name() -> str:
    user = input("Tell me your Username: ").strip()
    us = User(user)
    return us
'''
This is probably subject to revision, later in developement. For now it is just
a information on what this is all about. 

:input str:
'''

def introduction(us):
    print("MemRaise")
    print(f"Hello {us.name} I am Memi and I will help you to improve your Memory")
    print("What is this all about? With my help, you will gradually improve your memorie skills.")
    print("This version has only one trainig set. All presidents of the united states of america.")
    mode = input("Please choose a mode: train or match: ")
    choose_mode(mode, us)
    
'''
This is the training mode, for now the function is very simple. But I am thinking on a better implementation,
that is more fun to do. I don't want it to be boring.

:input empty str:
'''
def training():
    presidents = Presidents()
    p = inflect.engine()
    for president in presidents.presidents:
        number = president["number"]
        print(f"{president['name']} was the {p.ordinal(number)} President.")
        go = input("Press Enter to get to the next president! ")
        print()
        if go == " " or go != "":
            continue
        
   
'''
This is the match mode, it will ask the user for each president according to their 
ordinal number. If the user succeeds, the score will increase by  one. If the user looses, 
it is the end of the game. 
The current score will be stored into the user class and then saved to a csv file.
  
:input str:
'''      
def match_trainings_set(us):
    presidents = Presidents()
    current_pres = presidents.create_match_set()
    score = 0
    p = inflect.engine()
    while True:
        for president in presidents.presidents:
            current_pres_num = president["number"]
            name = input(f"Who is the {current_pres_num}th President? ")
            correct_name = current_pres.get(current_pres_num)
            if name == correct_name:
                score = score +1
                print("Correct")
                continue
            else:
                print(f"Your answer was incorrect, the {current_pres_num}th President was {correct_name}! Better luck next time :) ")
                break
        break
    us.score = score
    us.save_score()
    print(f"You knew {us.score} {p.plural('President', score)}, keep up with the training :)")


'''
This is at the moment just to switch between the modes. It will eventually get more items to choose from.

'''  
def choose_mode(mode, us):
    match mode:
        case "train":
            for _ in range(3):
                print()
            training()
        case "match":
            for _ in range(3):
                print()
            match_trainings_set(us)
        case _:
            print("Invalid Mode: Please type train or match")     
            


if __name__ == "__main__":
    main()