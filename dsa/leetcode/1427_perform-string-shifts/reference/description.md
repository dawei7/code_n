## Description

You are given a lowercase English string `s` and a matrix `shift`. Each row has the form `[direction, amount]`, where direction `0` requests a left shift and direction `1` requests a right shift.

A one-position left shift removes the first character and appends it to the end. A one-position right shift removes the last character and places it at the beginning. Larger amounts repeat the corresponding cyclic movement, so characters that pass one end of the string reappear at the other.

Apply every operation and return the final string.
