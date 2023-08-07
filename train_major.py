'''
Here will be the training section for the major system.
First letters of pi
3.1415926535 8979323846 2643383279 5028841971 6939937510
Digit   Letter
0       s,z
1       t,d,th
2       n
3       m
4       r
5       l
6       j,ch, sh
7       c,k,g, q, ck
8       v,f,ph
9       p, b
'''
class Major:
    def __init__(self):
        self.link = ""
        self.number = {}
        self.count = 0
    
    
    
    def train_numbers(self):
        for i in self.number:
            char = input(f"What are the characters or character for {i}: ").strip()
            if char == self.number[i]:
                self.count += 1
                print("correct")
            else:
                print(f"It was {self.number[i]}")
            
        
    
    
    def create_major_system(self):
        a = [0,1,2,3,4,5,6,7,8,9]
        b = ["s,z", "t,d,th", "n", "m", "r", "l", "j,ch,sh", "c,k,g,q,ck", "v,f,ph", "p,b"]
        for i in range(len(a)):
            self.number[i] = b[i]
            
         


m = Major()   
m.create_major_system()
print(m.number)
m.train_numbers()    

