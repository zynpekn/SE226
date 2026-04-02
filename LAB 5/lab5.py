#TASK 1 
def factorial(x) :
    if x==0 or x==1 :
        return 1 
    return x * factorial(x-1) 

#TASK 2 
term = lambda x, n : (x**n) / factorial(n)

def exp_x(x,n):
    total = 0
    i=0
    while i<n:
        total += term(x,i)
        i+=1
        return total 
    
    x = float ( input ("x: "))
    n = int ( input ("n: "))
    print(exp_x(x,n))

#TASK 3 
S = 0

def calc_series(n) :
    global S 
    if n == 0 :
        return 
    
    calc_series(n-1)
    term = ((-1) ** ( n+1 )) / n
    S+=term

    n= int(input("n: "))
    S=0
    calc_series(n)
    print(S)

