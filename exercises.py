# This is a master file for all Python exrcises.
# To add changes for commit/once you made your local commits, you can then push it to your remote GitHub.
   # git add .
   # git commit -m "write some message"
   # git push
   
#---------------

# Q1 Tables

def tables(m, n):
    for a in range(m, m+1):
        for i in range(1, n+1):
            b = a*i
            print(f"{a} * {i} = {b}")
#tables(3,10)

# Q2

# Q3

# Q4

# Q5 FizBizz

#n = input("Enter the number >" )
#print(f"you entered {n}")
        
def fizzbizz(o):
    for i in range(1, o+1):
        if i%15 == 0:
            print('fizzbizz')
        elif i%3 == 0:
            print('fizz')
        elif i%5==0:
            print('bizz') 
        else:
            print(f"{i}")

fizzbizz(int(input("Enter the number> ")))
