## Description

A non-empty array is consecutive when every adjacent difference is $1$, or when every adjacent difference is $-1$. The direction must remain the same throughout: `[3,4,5]` and `[9,8]` qualify, whereas `[3,4,3]` and `[8,6]` do not. Every one-element array is consecutive.

Given `nums`, consider every non-empty subsequence obtained by retaining elements in their original relative order. The value of a qualifying subsequence is the sum of its elements. Add the values of all consecutive subsequences, counting different choices of indices separately, and return the result modulo $10^9+7$.
