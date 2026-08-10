## General

Computing Hamming distance separately for every pair repeats the same bit comparisons many times. The total can instead be counted one bit position at a time. At a fixed bit, a pair contributes one exactly when one number has zero there and the other has one.

The exact solution examines 32 bit positions. For each position, it counts how many array entries contain a one, derives how many contain zero, and adds the product of those counts.

**Count differing pairs at one bit**

Suppose the array has `n` positions. At bit `i`, let `a` be the number of values whose bit is one. Then `b = n - a` values have zero there.

To form an unordered pair that differs at this bit, choose one position from the one-group and one from the zero-group. There are

$$
a\cdot b
$$

such pairs. No division by two is needed: choosing from two distinct groups gives each unordered pair exactly once. There is no alternate selection order inside this product that creates the same pair again.

Pairs whose two bits are both zero or both one contribute nothing at this position and are not included.

**Extract a bit**

For value `x`, the expression

`x >> i & 1`

shifts bit `i` into the least significant position and masks away every other bit. The result is integer zero or one. Summing this expression across `nums` produces `a` directly.

Python operator precedence interprets it as `(x >> i) & 1`. Parentheses could improve readability but do not change the exact behavior.

**Why adding across bits gives total Hamming distance**

The Hamming distance of one pair is the sum of one-unit indicators over all bit positions where it differs. Summing over pairs and then bits gives the same result as summing over bits and then pairs:

$$
\sum_{\{u,v\}}\sum_i [u_i\ne v_i]
=
\sum_i\sum_{\{u,v\}}[u_i\ne v_i].
$$

The inner sum on the right is exactly `a * b`. Therefore adding that product for every bit counts every pair's every differing position once.

**Trace `[4,14,2]`**

Using four visible bits:

```text
 4 = 0100
14 = 1110
 2 = 0010
```

- At bit zero, all values have zero, so `a = 0` and contribution is zero.
- At bit one, `14` and `2` have one while `4` has zero, so `a = 2`, `b = 1`, contribution two.
- At bit two, `4` and `14` have one while `2` has zero, again contributing two.
- At bit three, only `14` has one, contributing `1 * 2 = 2`.

Total contribution is six, matching the sum of the three pairwise distances.

For `[4,14,4]`, the two equal `4` occurrences are distinct array positions but differ at no bits from each other. At positions where `14` differs from `4`, one side has count one and the other count two, correctly accounting for both pairs involving `14`.

**Why 32 iterations are sufficient**

Every input is nonnegative and at most one billion, which uses fewer than 32 binary positions. Any higher conceptual positions are zero for every number and would contribute `0 * n = 0`. Checking positions `0..31` covers all possible set bits safely.

The method does not mutate the numbers while shifting because `x >> i` creates a temporary value inside the generator.

**Why this avoids quadratic pair enumeration**

There are about $n^2/2$ pairs but only a fixed 32 bit positions. Grouping all pairs by their bit values counts many pair contributions with one multiplication. The computation therefore scales linearly with array length for this bounded integer width.

## Complexity detail

Let $B=32$ be the checked width and $n$ the array length. The outer loop has $B$ iterations, and each generator scans all `n` values. Time complexity is $O(nB)$, matching the manifest. With fixed $B=32$, this simplifies to $O(n)$.

The generator is lazy, and only scalar counts and loop variables are stored. Auxiliary space is $O(1)$. The input is read without modification.

For arbitrary-size integers, one would set $B$ from the maximum bit length, giving $O(n\log V)$ time for maximum value $V$.

## Alternatives and edge cases

- **Enumerate every pair:** XOR and population count is simple but costs $O(n^2B)$ time.
- **Store a 32-entry count array:** Count one-bits while scanning each number, then sum products. It has the same time and constant bounded space; the exact source instead computes each bit immediately.
- **Binary-string conversion:** Formatting every number into 32 characters adds allocation and parsing overhead without changing the counting idea.
- **Single element:** Every bit has either `a = 0` or `b = 0`, so the total is zero because no pair exists.
- **All values equal:** Each bit group is all zero or all one, so every product is zero.
- **Duplicate positions:** They remain separate choices in `a` and `b`, as required, even when their mutual distance is zero.
- **Zeros:** All their bits belong to the zero group and pair correctly with set bits of other values.
- **Leading zero positions:** They contribute zero and need no special handling.
- **Answer size:** Python accumulation cannot overflow; the source also guarantees the final result fits a signed 32-bit integer.
