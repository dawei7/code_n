## Description

A **stepping number** is an integer whose adjacent decimal digits always have an absolute difference of exactly $1$. The rule compares every pair of consecutive digit positions; it is not enough for the difference to be merely at most $1$. A single-digit value has no adjacent pair and therefore satisfies the rule automatically.

- For example, `321` is a stepping number, while `421` is not.

Given integers `low` and `high`, return a sorted list containing every stepping number in the inclusive range `[low, high]`. Values equal to either bound belong in the result whenever they satisfy the digit rule.
