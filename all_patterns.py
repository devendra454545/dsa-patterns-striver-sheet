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
def p7(g):
    for i in range(g):
        for j in range(g-1-i):
            print(' ',end='')
        for k in range((2*i)+1): 
            print('*',end='')
        print()

# p8
# *********
#  *******
#   *****
#    ***
#     *       
def p8(h):
    for i in range(h):
        for j in range(i):
            print(' ',end='')
        for k in range(2*(h-i)-1):
            print('*',end='')
        print()

# p9
#     *    
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *       
def p9(l):
    for i in range(2*l):
        if i < l:
            for j in range(l - i - 1):
                print(' ', end='')
            for k in range((2 * i) + 1):
                print('*', end='')
            print()
        else:
            p = i - l + 1
            for j in range(p):
                print(' ', end='')
            for k in range(2 * (l - p) - 1):
                print('*', end='')
            print()

# p10
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
def p10(m):
    for i in range(2*m - 1):
        if i < m:
            for j in range(i + 1):
                print('*', end='')
        else:
            for j in range(2*m - i - 1):
                print('*', end='')
        print()

# p11
# 1
# 01
# 101
# 0101
# 10101
def p11(n):
    for i in range(n):
        for j in range(i+1):
            if ((i%2==0 and j%2==0)or(i%2==1 and j%2==1)):
                print('1',end='')
            else:
                print('0',end='')
        print()

