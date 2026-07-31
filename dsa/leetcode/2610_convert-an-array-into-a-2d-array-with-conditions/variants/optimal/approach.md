## General

If a value occurs $f$ times, its copies must occupy $f$ different rows because a row cannot repeat that value. Therefore the maximum frequency of any value is a lower bound on the number of result rows.

Process `nums` while recording how many copies of each value have already appeared. The first occurrence of a value goes into row zero, the second into row one, and in general occurrence number $k+1$ goes into row $k$. Create a new row exactly when an occurrence index equals the current number of rows.

Each row receives at most one copy of any value because distinct occurrences use distinct row indices. Every input occurrence is appended exactly once. If the largest frequency is $F$, the construction creates exactly rows $0$ through $F-1$, so it uses $F$ rows and meets the unavoidable lower bound. The produced matrix is consequently valid and has the minimum possible row count.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. With expected constant-time hash-table operations, each element is processed once, for $O(n)$ time. The frequency table and returned matrix together store $O(n)$ values, so the space complexity is $O(n)$.

## Alternatives and edge cases

- **Count first, then distribute:** Building a complete frequency map and placing each value into that many rows is also $O(n)$, but the online occurrence-index construction needs only one pass over `nums`.
- **Scan rows for an available position:** Trying rows one by one and testing membership is correct, but repeated linear membership checks can make the method $O(n^2)$.
- **One repeated value:** If all elements are equal, every row contains one element and the number of rows equals `nums.length`.
- **All values distinct:** Every occurrence index is zero, so all values fit into a single row.
- **Output flexibility:** Row order and element order are not prescribed; validity depends on the multiset, row-wise distinctness, and minimum row count.
