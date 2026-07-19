## General
**Make every line sum cheap.** Build independent prefix tables for rows, columns, diagonals running down and right, and diagonals running down and left. A subtraction in the appropriate table then gives the sum of any complete row segment, column segment, or diagonal segment of a candidate square in constant time.

**Search in answer order.** Try side lengths from $S$ down to $2$. For a chosen side length, enumerate every possible top-left corner. Use one diagonal as the candidate target sum and reject the square immediately if the other diagonal differs. Then inspect all of its row sums and column sums through the prefix tables. If every one equals the target, the square is magic. Because side lengths are examined from largest to smallest, the first accepted square is globally optimal.

If no candidate of side at least $2$ succeeds, return $1$. This fallback is valid because the problem explicitly makes every $1 \times 1$ square magic.

## Complexity detail
Building the four prefix tables takes $O(MN)$ time and space. For a fixed side length $k$, there are $(M-k+1)(N-k+1)$ positions. Each position needs constant-time diagonal checks and at most $2k$ constant-time row and column queries. Summed over all $1 \le k \le S$, this is $O(MNS^2)$ time in the worst case. The prefix tables occupy $O(MN)$ space.

## Alternatives and edge cases
- **Direct summation:** Recomputing each candidate's row, column, and diagonal sums from the matrix is simpler, but it adds another factor of $k$ to the expensive validation path.
- **Only row and column prefixes:** Diagonals could still be summed cell by cell, but diagonal prefix tables make all four kinds of line query uniform and allow earlier rejection.
- **Non-distinct entries:** A uniform square is magic; uniqueness is never part of the contract.
- **Rectangular matrices:** Candidate side length is limited by $S = \min(M, N)$, while positions still span both matrix dimensions.
- **Partial equality:** Equal diagonal sums, or equal row sums alone, are insufficient. Every row, every column, and both diagonals must share one sum.
- **Single row or column:** No square larger than one fits, so the answer is immediately $1$.
