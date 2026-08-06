## Description

You are given a **binary string** `s`, and a **2D** integer array `queries` where `queries[i] = [first_i, second_i]`.

For the `i^th` query, find the **shortest substring** of `s` whose **decimal value**, `val`, yields `second_i` when **bitwise XORed** with `first_i`. In other words, `val ^ first_i == second_i`.

The answer to the `i^th` query is the endpoints (**0-indexed**) of the substring `[left_i, right_i]` or `[-1, -1]` if no such substring exists. If there are multiple answers, choose the one with the **minimum** `left_i`.

*Return an array* `ans` *where* `ans[i] = [left_i, right_i]` *is the answer to the* `i^th` *query.*

A **substring** is a contiguous non-empty sequence of characters within a string.
