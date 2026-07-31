## General

Every nonzero decimal digit factors only into $2$, $3$, $5$, and $7$. Factor `t` into required exponents $(r_2,r_3,r_5,r_7)`. If a factor remains afterward, no zero-free digit product can be divisible by `t`, so the answer is `"-1"`.

**Packing missing factors into digits.** Digits `5` and `7` are the only single digits containing their respective primes, so each missing exponent needs one such digit. For the $2$ and $3$ exponents, a memoized constant-size dynamic program considers digits `2`, `3`, `4`, `6`, `8`, and `9`. For every residual pair it chooses first the sequence with the fewest non-one digits and then the lexicographically smallest sorted sequence among ties.

For a suffix of fixed length, minimizing the number of factor-carrying digits maximizes the number of leading `1` digits. That is lexicographically optimal because `1` contributes no factors. Sort the packed factor digits after those leading ones to obtain the smallest suffix with enough prime exponents.

**Keep the longest possible prefix.** If `num` is already zero-free and its digit exponents cover the requirement, return it. Otherwise, a same-length answer must differ at some position where its digit is larger. Its unchanged prefix cannot contain zero, so no position after the first zero is eligible.

Scan eligible positions from right to left. Maintain the factor exponents contributed by the prefix before the current position. Try replacement digits in increasing order above the current digit. A replacement is feasible exactly when the shortest factor pack for the remaining exponents fits in the suffix slots. The first feasible choice is globally smallest: it preserves the longest prefix, uses the smallest possible increased digit, and fills the suffix lexicographically minimally.

If no same-length answer exists, choose the smallest feasible length: the maximum of the factor-pack length and the mandatory `len(num) + 1` digits. A longer decimal string is numerically larger than `num`; leading ones followed by the minimal sorted factor pack make it the smallest valid number of that length.

## Complexity detail

Let $n=\lvert\texttt{num}\rvert$. Because $t\le10^{14}$, its prime-exponent state space is bounded independently of $n$; the memoized factor-packing work is $O(1)$ under the source contract. Each input position is visited a constant number of times and at most nine replacement digits are tested, giving $O(n)$ time.

The constructed strings and prefix material use $O(n)$ space. The benchmark size is the input length $n$. Its all-`9` inputs force a complete right-to-left scan before a longer answer is built. The calibrated slower method recomputes prefix factors from the beginning at every candidate position, requiring $O(n^2)$ time.

## Alternatives and edge cases

- **Increment integers one by one:** `num` may have 200,000 digits, so numeric enumeration is neither representable nor fast enough.
- **Full digit DP over position and exponent states:** It can model the problem, but storing position states multiplies the large input length by a factor state space that the greedy suffix construction avoids.
- **Fixed greedy conversion of exponents:** Simple rules can minimize digit count yet choose the wrong lexicographic tie, such as preferring `66` over `49` for $2^2 3^2$.
- **Unsupported prime factor:** Any factor outside $\{2,3,5,7\}$ makes every zero-free digit product invalid.
- **Zero in `num`:** An unchanged prefix may extend only up to, but not through, the first zero.
- **Already valid input:** Equality is permitted, so a valid `num` must be returned unchanged.
- **More digits required:** When the compact factor pack does not fit, the answer length may exceed `len(num) + 1`.
- **Numeric versus string order:** Length is compared before lexicographic order; any longer positive decimal string is numerically larger.
