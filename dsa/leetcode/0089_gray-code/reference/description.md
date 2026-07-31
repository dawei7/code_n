## Description

An $n$-bit Gray-code sequence contains $2^n$ integers and must satisfy every condition below:

- Each integer lies in the inclusive range $[0,2^n-1]$.
- The first integer is `0`.
- No integer appears more than once.
- The $n$-bit binary forms of every adjacent pair differ in exactly one bit.
- The binary forms of the final and first integers also differ in exactly one bit, closing the sequence into a cycle.

Given `n`, return any valid $n$-bit Gray-code sequence.
