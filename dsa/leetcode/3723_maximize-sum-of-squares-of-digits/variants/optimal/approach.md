## General

First test feasibility. Each of the `num` digits is at most `9`, so no result exists when `sum > 9 * num`. Because `sum` is positive, every feasible construction has a nonzero leading digit once its digits are arranged in descending order.

To maximize the square sum, concentrate the digit sum as strongly as possible. Suppose two digits satisfy $0 < a \leq b < 9$. Moving one unit from $a$ to $b$ changes their contribution by

$$
(a-1)^2 + (b+1)^2 - a^2 - b^2 = 2(b-a+1) > 0.
$$

Thus any distribution with two non-extreme positive digits can be improved. Repeating the exchange produces as many `9` digits as possible, followed by at most one remainder from `1` through `8`, with all other digits equal to `0`.

The score depends only on the digit multiset. Among permutations of the maximizing multiset, descending order gives the numerically greatest integer, satisfying the tie-break. Therefore the answer consists of `sum // 9` copies of `9`, then the nonzero remainder if present, then enough zeros to reach exactly `num` digits.

## Complexity detail

Let $d = \texttt{num}$. Arithmetic and feasibility checking take $O(1)$ time, while emitting the required $d$-character result takes $O(d)$ time and space. Apart from the returned string and temporary string construction, auxiliary state is $O(1)$.

## Alternatives and edge cases

- **Evenly distribute the sum:** Convex squaring rewards concentration, so balanced digits generally produce a smaller score.
- **Dynamic programming by position and sum:** It can optimize the score but is unnecessary and far too large for the source bounds.
- **Sum above capacity:** If `sum > 9 * num`, return `""` immediately.
- **Sum divisible by nine:** No remainder digit is emitted; use only `9` digits followed by zeros.
- **Tie among permutations:** Put larger digits first to obtain the maximum integer without changing the score.
- **Exact length:** Append all necessary zeros; they contribute nothing to the digit sum or score but still count as digits after the nonzero prefix.
