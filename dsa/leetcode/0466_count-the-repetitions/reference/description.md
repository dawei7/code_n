## Description

Write `[s, n]` for the string formed by concatenating `n` copies of `s`. For example, `str = ["abc", 3]` represents `"abcabcabc"`.

Say that a string `x` can be obtained from a string `y` when deleting zero or more characters from `y`, without changing the order of the remaining characters, produces `x`. Thus, `"abc"` can be obtained from `"abdbec"` by deleting the intervening characters `"dbe"`.

Given strings `s1` and `s2` and positive integers `n1` and `n2`, let `str1 = [s1, n1]` and `str2 = [s2, n2]`. Return the largest integer `m` for which `[str2, m]` can be obtained from `str1`.
