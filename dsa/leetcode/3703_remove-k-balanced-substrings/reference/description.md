## Description

You are given a string `s` containing only `(` and `)`, together with an integer `k`.

A string is **k-balanced** when it consists of exactly `k` consecutive opening parentheses followed immediately by exactly `k` consecutive closing parentheses. Equivalently, it is `'(' * k + ')' * k`; for example, `k = 3` gives `"((()))"`.

In each round, remove every non-overlapping k-balanced substring currently present in `s`, then concatenate the pieces that remain. Repeat these rounds until the string contains no k-balanced substring. Return the final string.
