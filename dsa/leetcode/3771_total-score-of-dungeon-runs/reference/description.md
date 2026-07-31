## Description

You are given a positive integer `hp` and two positive, 1-indexed integer arrays, `damage` and `requirement`, of the same length $n$.

A dungeon contains trap rooms numbered from $1$ through $n$. Upon entering room $i$, first subtract `damage[i]` from the current health. After that subtraction, the room awards one point exactly when the remaining health is at least `requirement[i]`.

For each starting room $j$, define `score(j)` by beginning with the full `hp` and visiting rooms $j,j+1,\ldots,n$ in order. Return `score(1) + score(2) + ... + score(n)`, the combined score across every possible starting room.
