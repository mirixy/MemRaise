import csv
from datetime import date
class User:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    
    @property  
    def score(self):
        return self._score
    
    @score.setter
    def score(self,n):
        self._score =  n
    
    
    def save_score(self):
        dt = date.today()
        with open("score.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["date","name", "score"])
            #writer.writeheader()  # Remove the '#' to write the fieldnames on top of a new csv file! After the csv is created, put the # in again.
            writer.writerow({"date": dt, "name": self.name, "score": self.score})