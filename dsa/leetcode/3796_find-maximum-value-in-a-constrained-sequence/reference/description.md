## Description

You are given an integer `n`, a list `restrictions`, and an array `diff` of length `n - 1`. Construct a length-`n` sequence `a[0], a[1], ..., a[n - 1]` subject to all of these rules:

- `a[0] = 0`.
- Every sequence value is non-negative.
- Across edge `i`, neighboring values satisfy `abs(a[i] - a[i + 1]) <= diff[i]` for every `0 <= i <= n - 2`.
- Each pair `[idx, maxVal]` in `restrictions` imposes `a[idx] <= maxVal`.

Among all valid sequences, maximize the largest value occurring anywhere in the sequence. Return that largest value for an optimal construction.
