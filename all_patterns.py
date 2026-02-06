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

# p12
# 1      1
# 12    21
# 123  321
# 12344321
def p12(o):
    for i in range (1,o+1):
        for j in range(1,i+1):
            print(j,end='')
        for k in range(2*(o-i)):
            print('-',end='')
        for l in range(i,0,-1):
            print(l,end='')
        print()

# p13 (added spaces just for clarity)
# 1                 
# 2  3
# 4  5  6
# 7  8  9 10
# 11 12 13 14 15
def p13(p):
    start = 1
    for i in range(p):
        for j in range(i+1):
            print(start,end='')
            start = start+1
        print()

# p14
# A
# AB
# ABC
# ABCD
# ABCDE
def p14(q):
    ch = 'A'
    for i in range(q):
        for j in range(i+1):
            if j==0:
                ch = 'A'
                print(ch,end='')
            else:
                ch = chr(ord(ch)+1)
                print(ch,end='')
        print()

# Alternate method of p14() is p14a()
def p14a(q):
    for i in range(q):
        for ch in range(ord('A'),ord('A')+i+1):
            print(chr(ch),end='')
        print()

# p15
# ABCDE
# ABCD
# ABC
# AB 
# A
def p15(r):
    ch='A'
    for i in range(r):
        for j in range(r,i,-1):
            if(j==r):
                ch='A'
                print(ch,end='')
            else:
                ch = chr(ord(ch)+1)
                print(ch,end='')
        print()

# Alternate method of p15() is p15a()
def p15a(r):
    for i in range(r):
        for ch in range(ord('A'),ord('A')+r-i):
            print(chr(ch),end='')
        print()
 
# p16
# A 
# BB
# CCC
# DDDD
# EEEEE
def p16(s):
    ch = 'A'
    for i in range(s):
        for j in range(i+1):
            print(ch,end='')
        ch = chr(ord(ch)+1)
        print()

# p17
#    A   
#   ABA  
#  ABCBA
# ABCDCBA
def p17(t):
    for i in range(t):
        for j in range(t-i-1):
            print(' ',end='')
        for ch in range(ord('A'),ord('A')+i+1):
            print(chr(ch),end='')
        for ch2 in range(ord('A')+i-1,ord('A')-1,-1):
            print(chr(ch2),end='')
        print()
