import os,sys,io,math
from re import *
from math import *
from array import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
from statistics import *
from collections import *


def solve():
    I=lambda:[*map(int,sys.stdin.readline().split())]
    IP=lambda:map(int,input().split())
    IS=lambda:input()
    IN=lambda:int(input())
    IF=lambda:float(input())

    def f():
        n=IS()
        s=0
        for i in n:s+=int(i)
        if s%10==0:return (n+'0')
        return n+str(10-(s%10))


    for _ in range(IN()):
        print(f())


if __name__ == "__main__":
    solve()
