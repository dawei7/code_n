## Description

You are given an integer array `nums` and a positive limit `maxVal`. You may replace any array element with any positive integer at most `maxVal`; each element whose value changes contributes one unit to the modification cost.

After all replacements, choose one index whose final value is co-prime with the final value at every other index. Two integers are co-prime when their greatest common divisor is $1$.

Let `selectedValue` be the chosen index's final value and `modificationCost` be the number of changed elements. The resulting score is `selectedValue - modificationCost`. Return the largest score achievable by choosing the modifications and selected index optimally.
