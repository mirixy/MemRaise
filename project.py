import csv
from president_set import Presidents
import inflect
def main():
    training()
    #match_trainings_set()



def get_user_name():
    return input("Tell me your Username: ")

def introduction(user):
    print("MemRaise")
    print(f"Hello {user} I am Memi and I will help you to improve your Memory")
    print("What is this all about? With my help, you will gradually improve your memorie skills.")
    print("This version has only one trainig set. All presidents of the united states of america.")
    

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
        
   
        
def match_trainings_set():
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
                score += 1
                print("Correct")
                continue
            else:
                print(f"Your answer was incorrect, the {current_pres_num}th President was {correct_name}! Better luck next time :) ")
                break
        break
    print(f"You knew {score} {p.plural('President', score)}, keep up with the training :)")
    
            
            


if __name__ == "__main__":
    main()