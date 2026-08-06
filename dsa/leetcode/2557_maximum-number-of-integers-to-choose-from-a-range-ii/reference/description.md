## Description

You are given an integer array `banned`, an upper bound `n`, and a sum limit `maxSum`. Choose any number of distinct integers from the inclusive range $[1,n]$. A value may be chosen at most once, and no value that occurs in `banned` may be included.

The sum of the chosen integers must not exceed `maxSum`. Return the maximum possible number of integers in such a selection. Repeated occurrences of the same banned value still forbid only that one integer; the objective is the number selected, not the number of different valid selections.
