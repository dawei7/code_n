## Description

Start with `arr`, the strictly increasing list of all integers in `[1,n]`, and repeatedly eliminate values as follows:

1. Traverse from left to right, removing the first value encountered and then every other remaining value through the end.
2. On the next pass, traverse from right to left, removing the rightmost value and then every other remaining value.
3. Keep alternating those two directions until one value remains.

Return the final surviving value.
