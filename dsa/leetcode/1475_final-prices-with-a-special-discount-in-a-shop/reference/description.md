## Description

You are given an integer array `prices` where `prices[i]` is the price of the `i^th` item in a shop.

There is a special discount for items in the shop. If you buy the `i^th` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.

Return an integer array `answer` where `answer[i]` is the final price you will pay for the `i^th` item of the shop, considering the special discount.
