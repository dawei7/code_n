## Description

You are given an integer array `nums` and a binary string `s` of the same length. Index `i` initially holds a token exactly when `s[i]` is `1`.

You may move tokens any number of times subject to one rule: a token currently at an index `i > 0` may move to `i - 1` only if that token has never moved before. Thus, each token may either stay at its initial index or move left by one position, but it cannot move twice.

After all chosen moves, an index is covered when at least one token occupies it. Return the maximum possible sum of `nums[i]` over the covered indices.
