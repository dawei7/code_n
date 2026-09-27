# Guided Example: Number of Subarrays Having Even Product

## 1. The instance we will solve

Given a 0-indexed integer array `nums`, we must count how many of its subarrays — that
is, how many of its contiguous non-empty blocks `nums[i..j]` — have a product that is
even. Products grow explosively, so the interesting part of the problem is finding a
way to decide the parity of a block without ever computing it.

The instance we trace is the first official example:

- `nums = [9, 6, 7, 13]`
- required output: `6`

It is a good representative because only one element is even and it sits in the
middle. The trace therefore shows all three regimes at once: a prefix of odd numbers
that contributes nothing, an even element that certifies every block containing it,
and a run of odd numbers after it whose blocks are certified only because the even
element is still inside them. The array has $\binom{4}{2} + 4 = 10$ subarrays in
total, of which 6 have an even product.

## 2. A product is even exactly when one factor is even

The whole problem collapses on one elementary fact about divisibility: an integer is
even exactly when $2$ divides it. Therefore

$$
2 \mid \prod_{k=i}^{j} \text{nums}[k] \iff \exists\, k \in [i, j] \text{ with } 2 \mid \text{nums}[k],
$$

because a product is divisible by $2$ precisely when at least one factor is. Written
with parity classes, let

$$
p(k) = \text{nums}[k] \bmod 2 \in \{0, 1\}.
$$

Then the product of `nums[i..j]` is even if and only if $p(k) = 0$ for at least one
$k$ in $[i, j]$. Equivalently, a subarray has an **odd** product exactly when every
element inside it is odd.

Two consequences matter immediately.

1. Adding more elements cannot destroy evenness: extending an even-product block
   keeps it even, however long the extension is.
2. Odd-product blocks are exactly the blocks that lie completely inside a maximal
   run of odd values. Those blocks are easy to count and easy to subtract, which
   gives a second, complementary route to the same answer.

## 3. Counting by right endpoint: the invariant of the last even index

Fix a right endpoint $j$. Every subarray ending at $j$ is determined by its left
endpoint $i \le j$. The block `nums[i..j]` is even exactly when some even value lies
in positions $i$ through $j$, so define

$$
L_j = \max\{\, k \le j : p(k) = 0 \,\},
$$

the index of the rightmost even value at or before $j$, and set $L_j = -1$ when no
even value exists at or before $j$. Because $L_j$ is the *rightmost* even position
before $j$, a left endpoint $i \le j$ gives an even product precisely when
$i \le L_j$: any such $i$ includes position $L_j$, and any $i > L_j$ starts after the
last even value, so it contains only odd numbers.

Hence the number of valid blocks ending at $j$ is

$$
c_j = \begin{cases} L_j + 1 & \text{if } L_j \ge 0, \\ 0 & \text{if } L_j = -1, \end{cases}
$$

and the answer is $\sum_{j=0}^{\ell-1} c_j$ where $\ell$ is the length of `nums`.
Each $L_j$ is maintained in constant time while scanning left to right:

$$
L_j = \begin{cases} j & \text{if } p(j) = 0, \\ L_{j-1} & \text{if } p(j) = 1, \end{cases}
\qquad L_{-1} = -1 .
$$

This is the invariant the method maintains: after processing position $j$, the stored
value is exactly the largest index at or before $j$ that holds an even number, or
$-1$ if none exists.

## 4. Worked trace on nums = [9, 6, 7, 13]

First, enumerate every subarray of the traced array and record the actual product.
This confirms the expected answer by direct computation, so the fast method can be
checked against it afterwards.

| `nums[i..j]` | indices | product | parity |
|:---|:---|:---|:---|
| `[9]` | `0..0` | `9` | odd |
| `[9, 6]` | `0..1` | `9 * 6 = 54` | even |
| `[9, 6, 7]` | `0..2` | `9 * 6 * 7 = 378` | even |
| `[9, 6, 7, 13]` | `0..3` | `9 * 6 * 7 * 13 = 4914` | even |
| `[6]` | `1..1` | `6` | even |
| `[6, 7]` | `1..2` | `6 * 7 = 42` | even |
| `[6, 7, 13]` | `1..3` | `6 * 7 * 13 = 546` | even |
| `[7]` | `2..2` | `7` | odd |
| `[7, 13]` | `2..3` | `7 * 13 = 91` | odd |
| `[13]` | `3..3` | `13` | odd |

Exactly six rows are even, matching the expected output. Now run the single sweep
that produces the same count without any multiplication. The column $L_j$ is the
rightmost even index seen so far, and $c_j = L_j + 1$ (or $0$ when $L_j = -1$).

| $j$ | `nums[j]` | parity | $L_{j-1}$ before the step | $L_j$ after the step | $c_j$ | running total |
|:---|:---|:---|:---|:---|:---|:---|
| 0 | `9` | odd | `-1` | `-1` | 0 | 0 |
| 1 | `6` | even | `-1` | `1` | 2 | 2 |
| 2 | `7` | odd | `1` | `1` | 2 | 4 |
| 3 | `13` | odd | `1` | `1` | 2 | 6 |

Reading the table: position 0 is odd, so no block ending there can be even and the
counter stays at 0. Position 1 is even, so it becomes the last even index; the two
blocks ending at 1 are `nums[0..1]` and `nums[1..1]`, both even. Positions 2 and 3
are odd, but the last even index stays at 1, so exactly the two blocks
`nums[0..j]` and `nums[1..j]` ending at each of those positions are even. The totals
$0, 2, 4, 6$ agree exactly with the enumeration table.

## 5. Invariant and correctness of the sweep

**Invariant.** Just after processing position $j$, the single stored value equals
$\max\{k \le j : p(k) = 0\}$, or $-1$ when that set is empty.

**Maintenance.** If $p(j) = 0$, position $j$ is even and is the newest index, so it
supersedes every earlier candidate and the stored value becomes $j$. If $p(j) = 1$,
position $j$ is not even and cannot be the maximum, so the stored value is unchanged.
Both cases are constant work and preserve the invariant.

**Exactly-once counting.** Define for each right endpoint $j$ the set
$S_j = \{i : 0 \le i \le j \text{ and } \text{nums}[i..j] \text{ is even}\}$. By the
invariant, $\lvert S_j \rvert = c_j$: when $L_j \ge 0$ the qualifying left endpoints
are exactly $i \in \{0, 1, \dots, L_j\}$, and when $L_j = -1$ the set is empty.
Because every subarray has exactly one right endpoint, the family $\{S_j\}$ partitions
the set of even-product subarrays, so summing $c_j$ counts each one once and none
twice.

**Completeness.** Let `nums[i..j]` be any subarray with an even product. By section 2
it contains an even position $k$ with $i \le k \le j$, so $L_j \ge k \ge i$, hence
$i \le L_j$ and the subarray is counted at endpoint $j$. **Soundness.** If
$i \le L_j$, then position $L_j$ lies in `nums[i..j]` and is even, so the product is
even by section 2. The count therefore equals the number of even-product subarrays
exactly, which is the required result.

Note also what the argument does *not* use: the magnitude of any product, the number
of even elements inside a block, or the order of the even and odd values. Only the
existence of one even element matters, which is why a single index of state suffices.

## 6. The complement view: subtracting the odd runs

An odd-product subarray is a block whose elements are all odd, so it must lie inside
a maximal run of consecutive odd values. If a maximal odd run has length $r$, it
contains exactly $\binom{r+1}{2} = \frac{r(r+1)}{2}$ subarrays, all with odd products,
and each such subarray belongs to exactly one run.

| Maximal odd run in `[9, 6, 7, 13]` | length $r$ | odd-product subarrays $\frac{r(r+1)}{2}$ |
|:---|:---|:---|
| `[9]` at index 0 | 1 | 1 |
| `[7, 13]` at indices 2–3 | 2 | 3 |
| total odd-product subarrays | — | 4 |

There are $10$ subarrays in total, so the complement gives $10 - 4 = 6$, the same
answer. This second route is worth knowing because it explains the shape of the
problem: the difficulty is localised entirely in the odd runs, and every subarray
that touches an even value is automatically good.

## 7. Traps and boundary behaviour

| Trap or boundary | Concrete instance | Correct reading | Answer |
|:---|:---|:---|:---|
| Multiplying the blocks out | any array of length $10^5$ with values near $10^5$ | products have astronomically many digits; parity alone decides | use indices, never products |
| Believing evenness needs an even *count* of even values | `nums = [9, 6, 7, 13]` | one even element is enough, so `nums[0..3]` is even | 6 |
| All values odd | `nums = [7, 3, 5]` | every block is odd, no block qualifies | 0 |
| All values even | `nums = [2, 4, 6]` | every block qualifies, $1 + 2 + 3$ blocks ending at 0, 1, 2 | 6 |
| Single even element | `nums = [100000]` | the only block is even | 1 |
| Single odd element | `nums = [9]` | the only block is odd | 0 |
| Even value first, then only odds | `nums = [2, 1, 1, 1]` | the last even index stays 0, so each endpoint contributes 1 | 4 |
| Even value last, then nothing | `nums = [1, 3, 5, 7, 8]` | only endpoint 4 contributes, and it contributes 5 | 5 |
| Two even values | `nums = [1, 2, 3, 4]` | the last even index moves from 1 to 3, changing the contribution from 2 to 4 | 8 |
| Several separated evens and long odd runs | `nums = [1, 1, 2, 1, 1, 1, 4, 1]` | contributions are $0, 0, 3, 3, 3, 3, 7, 7$ | 26 |
| Duplicate odd values only | `nums = [9, 9]` | both blocks are odd | 0 |

The alternative formulations below all solve the same problem; the table states what
each one tracks and what it costs.

| Method | What it tracks | Time | Notes |
|:---|:---|:---|:---|
| Enumerate every block and test its product | nothing | $O(n^2)$ blocks, plus growing products | correct but far too slow for $n = 10^5$ |
| Sweep with the last even index | one integer, $L_j$ | $O(n)$ | the method traced above; no products are formed |
| Parity dynamic programming | two counters, even-ending $E_j$ and odd-ending $O_j$ | $O(n)$ | for even `nums[j]`: $E_j = E_{j-1} + O_{j-1} + 1$ and $O_j = 0$; for odd `nums[j]`: $E_j = E_{j-1}$ and $O_j = O_{j-1} + 1$; the answer is $\sum_j E_j$ |
| Complement over odd runs | lengths of maximal odd runs | $O(n)$ | answer $= \frac{n(n+1)}{2} - \sum_{\text{runs}} \frac{r(r+1)}{2}$, useful when odd runs are few and long |
| Sliding window keyed on the leftmost even value | two pointers | $O(n)$ | symmetric to the last-even sweep; the window must shrink when the only even value leaves it |

For the traced array, the parity recurrence gives $E = 0, 2, 2, 2$ at the four
endpoints, summing to $6$, which agrees with the sweep and with the enumeration.

## 8. Complexity: time and auxiliary space

Let $n$ be the length of `nums`. The method makes a single left-to-right pass. At
each position it performs one parity test, at most one assignment to the stored
index, one addition, and one comparison of integers bounded by $n$, all constant
work. The total time is therefore

$$
O(n),
$$

with no multiplication, division, or big-integer arithmetic anywhere; the largest
integer the method ever manipulates is the running total, which is bounded by
$\frac{n(n+1)}{2} \le \frac{10^5 \cdot (10^5+1)}{2}$, a value that fits comfortably
in a 64-bit integer. By comparison, the largest subarray product of $10^5$ factors
near $10^5$ would have about $5 \cdot 10^5$ decimal digits, which is exactly the
obstacle the parity reduction removes.

Auxiliary space is

$$
O(1),
$$

because the sweep keeps only two scalars: the rightmost even index $L_j$, which is
$-1$ or an index in $[0, n-1]$, and the running count of qualifying subarrays. The
input array is read in place and is never copied or transformed, so the extra memory
does not grow with $n$. The complement formulation also runs in $O(n)$ time and
$O(1)$ space, since it only tracks the length of the current odd run and accumulates
$\frac{r(r+1)}{2}$ when that run ends.
