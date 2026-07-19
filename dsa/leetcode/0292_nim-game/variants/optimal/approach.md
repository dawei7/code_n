## General
**Work backward from the end**

Piles of one, two, or three stones are immediately winning. A pile of four is different: every move leaves an immediately winning pile for the opponent. This is the first losing position.

**The four-stone rhythm**

After either player removes `x` stones, the other can remove $4 - x$. Together the two turns consume exactly four stones. Consequently, a player who hands the opponent a multiple of four can restore that situation after every response.

If `n` is not divisible by four, the first player removes $n \bmod 4$ stones and establishes this rhythm. If `n` is divisible by four, every opening move breaks the multiple, and the opponent establishes the rhythm instead. This proves that the losing piles are exactly `4, 8, 12, ...`.

## Complexity detail
Testing $n \bmod 4$ uses constant time and space regardless of the pile size.

## Alternatives and edge cases
- Dynamic programming can label every pile from `1` through `n`, but costs $O(n)$ time and space to rediscover the same pattern.
- A recursive game tree repeats equivalent pile sizes and is much more expensive without memoization.
- The contract begins with a positive pile, so there is no zero-stone case to define.
