# This is a master file for all Python exrcises.

def tables(m, n):
    for a in range(m, m+1):
        for i in range(1, n+1):
            b = a*i
            print(f"{a} * {i} = {b}")
tables(3,10)
