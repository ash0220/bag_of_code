# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=[1,2,3]
print(a)
for i in range(len(a)):
    print(a[i])
    
dict_prime={}
for i in range(1,101):
        if i==1 or i%2==0:
            dict_prime[i]='non_prime'
        else:
            flag=0
            for j in range(2,i):
                if i%j==0:
                    flag=1
                    dict_prime[i]='non_prime'
                    break
                dict_prime[i]='prime'
                
dict_prime[2]='prime'
inp=input('enternumber')
print(dict_prime[int(inp)])


list=['p','c',1997,1]
list[0:2]=[2001]
print(list)

