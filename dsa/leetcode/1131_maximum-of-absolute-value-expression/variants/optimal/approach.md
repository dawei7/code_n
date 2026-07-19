## General
**Expand each absolute value by signs.** For fixed indices, the expression equals the maximum over sign choices $s_1,s_2,s_3 \in \{-1,1\}$ of

$$
s_1(\texttt{arr1[i]}-\texttt{arr1[j]})
+s_2(\texttt{arr2[i]}-\texttt{arr2[j]})
+s_3(i-j).
$$

For a fixed sign triple, define $F(k)=s_1\texttt{arr1[k]}+s_2\texttt{arr2[k]}+s_3k$. The best ordered pair for that triple is simply $\max F-\min F$.

**Reduce eight forms to four.** Negating all three signs negates every $F(k)$ but leaves its range unchanged. Each form with $s_3=-1$ therefore has the same range as the all-sign-negated form with $s_3=1$. It is enough to scan the four choices for $(s_1,s_2)$ while using `+ index`.

**Track only extrema.** For each of those four forms, scan corresponding positions of the two arrays, compute `value = s1 * arr1[index] + s2 * arr2[index] + index`, and retain its minimum and maximum. Their difference is the best pair under that sign form. Taking the largest of the four ranges covers the sign pattern selected by every possible index pair, so it equals the original maximum.

## Complexity detail
Four scans each process all $n$ positions with constant work, giving $O(n)$ time. Only the current minimum, maximum, and answer are stored for each sign choice, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Compare every index pair:** Direct evaluation is simple and correct but takes $O(n^2)$ time.
- **Store all transformed values:** Computing and sorting each sign form also works, but uses $O(n)$ space and $O(n \log n)$ time when only extrema are needed.
- **Negative array values:** Sign expansion handles them without any separate cases.
- **Equal points at distinct indices:** Even when both array coordinates match, the index term contributes their distance.
- **Repeated extrema:** Only the range matters; it is harmless if several indices attain the same minimum or maximum.
