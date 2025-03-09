#factorial     5!  = 5 x 4 x 3 x 2 x 1 

N = int(input("Enter postive number "))

fact = 1

# loop 
for i in range(1, N+1):
    fact = fact * i  

print(fact) 
    