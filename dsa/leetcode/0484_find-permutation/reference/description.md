## Description

A permutation `perm` of the integers from $1$ through $n$ can be represented by a string `s` of length $n - 1$.
Each character describes the relationship between two adjacent permutation values:

- `s[i] == "I"` means `perm[i] < perm[i + 1]`.
- `s[i] == "D"` means `perm[i] > perm[i + 1]`.

Given `s`, reconstruct and return the lexicographically smallest permutation that it represents.
