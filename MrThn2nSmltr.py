#!/usr/bin/env python

list=['abc','xyz','aba','1221']
n=0
for word in list:
    if len(word)>1 and word[0]==word[-1]:    #[-1] last Index
        n+=1
print(n)


