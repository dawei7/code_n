## Description

You are given a digit string `s` of length $m$ and an array `queries`. Each query is a pair `[l_i, r_i]` that selects the inclusive substring `s[l_i..r_i]`.

Process every selected substring from left to right. Remove its zero digits while keeping every nonzero digit in its original order, then concatenate the retained digits to form an integer `x`. When the substring contains no nonzero digit, use `x = 0`.

Let `sum` denote the sum of the digits retained in `x`. The result for that query is `x * sum`.

Return the results in query order as an array `answer`, where `answer[i]` belongs to the $i^{\text{th}}$ query. Because a concatenated value and its product can be large, reduce every result modulo $10^9+7$.
