## Description

You are given an array `rectangles` where `rectangles[i] = [l_i, w_i]` represents the `i^th` rectangle of length `l_i` and width `w_i`.



You can cut the `i^th` rectangle to form a square with a side length of `k` if both `k <= l_i` and `k <= w_i`. For example, if you have a rectangle `[4,6]`, you can cut it to get a square with a side length of at most `4`.



Let `maxLen` be the side length of the **largest** square you can obtain from any of the given rectangles.



Return *the **number** of rectangles that can make a square with a side length of *`maxLen`.
