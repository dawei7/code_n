## Description

You are given three integer arrays, `a`, `b`, and `c`. Form a triplet by independently choosing one element from each array, so every index combination `(i, j, k)` represents the values `(a[i], b[j], c[k])`.

For each such triplet, compute `a[i] XOR b[j] XOR c[k]`. A set bit is a binary digit equal to one. Count and return the index triplets whose XOR result contains an even number of set bits. Repeated values at different indices represent distinct choices and therefore contribute separately.
