# p1
# ****
# ****
# ****
# ****
def p1(a):
    for i in range(a):
        for j in range(a):
            print('*', end="")
        print()  

# p2
# *
# **
# ***
# ****
# ***** 
def p2(b):
    for i in range(b):
        for j in range(i+1):
            print('*',end="")
        print()   

# p3
# 1
# 12
# 123
# 1234
# 12345
def p3(c):
    for i in range(c):
        for j in range(i+1):
            print(j+1,end='')
        print()

# p4
# 1
# 22
# 333
# 4444
# 55555
def p4(d):
    for i in range(d):
        for j in range(i+1):
            print(i+1,end='')
        print()

# p5
# *****
# ****
# ***
# **
# *
def p5(e):
    for i in range(e):
        for j in range(e-i):
            print('*',end='')
        print()           

# p6
# 12345
# 1234
# 123
# 12
# 1
def p6(f):
    for i in range(f):
        for j in range(1,f+1-i):
            print(j,end='')
        print()

# p7
#     *    
#    ***
#   *****
#  *******
# *********
