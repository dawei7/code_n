## Description

You are given integers `n`, `m`, and `k`. Consider every length-`n` array whose elements are selected independently from the inclusive range `[1, m]`. For each adjacent index $i$, evaluate `(arr[i] * arr[i + 1]) - arr[i] - arr[i + 1]`.

An array is **k-even** when that expression is even at exactly `k` of the $n-1$ adjacent positions. Count all possible k-even arrays. Different value choices or positions form different arrays, and the answer must be returned modulo $10^9+7$.
