## Description

You are given a zero-indexed array `words` whose strings are all unique.

An ordered pair of indices $(i,j)$ is a palindrome pair precisely when all three conditions hold:

- $0 \le i,j < \texttt{words.length}$,
- $i \ne j$, and
- concatenating `words[i] + words[j]` produces a palindrome.

Return an array containing every palindrome pair. The algorithm must run in

$$
O\!\left(\sum_i \lvert\texttt{words[i]}\rvert\right)
$$

time.
