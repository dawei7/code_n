# Guided Example: Count the Number of Fair Pairs

## 1. What makes a pair fair

Given a 0-indexed array and two integers `lower` and `upper`, a pair $(i, j)$ is fair when the indices are distinct and ordered, $0 \le i < j < n$, and the two values sum inside a closed interval:

$$
\text{lower} \le \text{nums}[i] + \text{nums}[j] \le \text{upper}
$$

Ordered index pairs are counted, which matters twice over: $(i, j)$ and $(j, i)$ are not two different fair pairs, because only $i < j$ is admissible; and two equal values sitting at different positions are two different pairs, because identity comes from the positions, not from the values.

## 2. Why sorting is allowed

The fairness test reads only the two **values** `nums[i]` and `nums[j]`. It never inspects what sits between them, and no rule depends on the original arrangement. Sorting therefore preserves every count: it is a bijection of the positions, and each unordered pair of positions maps to an unordered pair of sorted positions carrying the same two values, hence the same sum. The set of sums available to the algorithm is unchanged, only the label of each position is.

After sorting, the values satisfy $\text{nums}[0] \le \text{nums}[1] \le \dots \le \text{nums}[n-1]$, and that is the property the rest of the method exploits: for a fixed left value $x$, the partners that make the sum admissible form a **contiguous block** of positions, because the value window

$$
W(x) = [\text{lower} - x, \; \text{upper} - x]
$$

is an interval, and a sorted array's elements inside an interval occupy consecutive positions. Counting the partners therefore reduces to locating the two ends of that block.

## 3. Worked instance: the first official sample

Take `nums = [0, 1, 7, 4, 4, 5]`, `lower = 3`, `upper = 6`, whose required count is `6`. Sorting gives a non-decreasing array that we can index by position:

| Sorted position | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Value | 0 | 1 | 4 | 4 | 5 | 7 |

Now every left position $i$ is visited once, and for each of them the admissible partner window is computed and its two ends are located:

| Left position $i$ | `nums[i]` | Partner window $W(\text{nums}[i])$ | First $j$ with value at least the lower end | First $k$ with value at least the upper end plus one | Pairs counted $k - j$ |
|---|---|---|---|---|---|
| 0 | 0 | `[3, 6]` | 2 | 5 | 3 |
| 1 | 1 | `[2, 5]` | 2 | 5 | 3 |
| 2 | 4 | `[-1, 2]` | 3 | 3 | 0 |
| 3 | 4 | `[-1, 2]` | 4 | 4 | 0 |
| 4 | 5 | `[-2, 1]` | 5 | 5 | 0 |
| 5 | 7 | `[-4, -1]` | 6 | 6 | 0 |
| **Total** | — | — | — | — | **6** |

Two conventions in that table carry the whole derivation:

- The search for the lower end looks for the first position whose value is **at least** `lower - nums[i]`, so the block starts there and the lower bound is inclusive.
- The search for the upper end looks for the first position whose value is **at least** `upper - nums[i] + 1`. That is the half-open trick: the closed interval $[L, U]$ is the same set as the half-open interval $[L, U+1)$, so the first excluded position is found by a single uniform "at least" search. The number of admissible partners is then exactly the gap $k - j$.

Both searches begin at position $i + 1$, which enforces $i < j$ and keeps each unordered pair from being counted twice.

For $i = 0$ the block is positions $2, 3, 4$ — values `4`, `4`, `5` — and the three sums are $0+4 = 4$, $0+4 = 4$, $0+5 = 5$, all inside `[3, 6]`. For $i = 2$ the window `[-1, 2]` contains no value at or after position 3, so the gap is zero: the value `4` is simply too large to pair with another `4` under this upper bound, even though a partner exists.

## 4. The same six pairs in original indexing

The count is six, and the official sample identifies which index pairs they are:

| Pair of original indices | `nums[i]` | `nums[j]` | Sum | Inside `[3, 6]`? |
|---|---|---|---|---|
| (0, 3) | 0 | 4 | 4 | yes |
| (0, 4) | 0 | 4 | 4 | yes |
| (0, 5) | 0 | 5 | 5 | yes |
| (1, 3) | 1 | 4 | 5 | yes |
| (1, 4) | 1 | 4 | 5 | yes |
| (1, 5) | 1 | 5 | 6 | yes |

Compare this with the sorted positions that produced the same count — $i = 0$ paired with positions $2, 3, 4$ and $i = 1$ paired with positions $2, 3, 4$. The position labels differ, yet the multiset of value sums $\{4, 4, 5, 5, 5, 6\}$ is identical, which is the sorting argument made concrete. Duplicate value `4` appears at original indices 3 and 4 and at sorted positions 2 and 3; each copy is a distinct endpoint and each contributes its own pair.

## 5. Why the count is exact

The method rests on one invariant, stated for the sorted array.

> **Invariant.** For a fixed left position $i$, the admissible partners are exactly the positions $j$ with $j > i$ whose value lies in $W(\text{nums}[i])$, and because the array is non-decreasing those positions form one contiguous block whose length is $k - j$, where $j$ and $k$ are the first positions at or after $i + 1$ whose values reach the two ends of the window.

*Soundness.* Every counted partner satisfies $j > i$ by construction of the search range, and its value lies in the window, so `nums[i] + nums[j]` is between `lower` and `upper` inclusive. No counted pair is unfair.

*Completeness.* Take any fair pair and look at its two positions in the sorted array; let $p < q$ be the smaller and larger. At the iteration with left position $p$, the value `nums[q]` lies in $W(\text{nums}[p])$ because the pair is fair, and $q > p$, so $q$ falls inside the located block and the pair is counted. The same pair is not counted anywhere else: at every other left position at least one of its two endpoints is excluded, either because the position is not in the search range or because its value is outside that iteration's window.

Since no pair is counted twice and none is missed, the accumulated total equals the number of fair pairs exactly. Duplicate values do not disturb this: positions remain distinguishable even when their values agree, so the block length counts copies rather than distinct values.

## 6. Boundary behaviour

| Instance | Sorted values | Bounds | Result | Why it is instructive |
|---|---|---|---|---|
| All values equal | `[2, 2, 2, 2]` | `lower = upper = 4` | 6 | Every unordered pair of distinct positions sums to 4, so all $\binom{4}{2} = 6$ pairs qualify |
| Window below every sum | `[1, 2, 3]` | `lower = upper = 1` | 0 | The smallest achievable sum is 3, so every window is empty and no block is ever found |
| Narrowest closed window | `[0, 0]` | `lower = upper = 0` | 1 | The single pair sits on both bounds simultaneously, testing inclusive behaviour at each end |
| Fewer than two elements | `[5]` | `lower = 0`, `upper = 10` | 0 | The constraint $i < j$ cannot be met, so the search range of the only left position is empty |
| Negative values | `[-3, -1, 0, 2, 4]` | `lower = -2`, `upper = 1` | 4 | Sums below `lower` are now the common case; a scan that stops as soon as a sum looks small is wrong |
| Extreme magnitudes | `[-1000000000, 0, 1000000000]` | `lower = -10^9`, `upper = 10^9` | 3 | Sums of magnitude $10^9$ land exactly on the inclusive bounds |
| Maximum size | $n = 10^5$ equal values | a bound matching $2x$ | about $5 \times 10^9$ | The count itself can exceed the range of a 32-bit integer |

The negative-value row is the one that breaks naive scanning. With negatives present, the sum `nums[i] + nums[j]` is not monotone in the raw value of the left operand, so a loop that breaks out when the sum first exceeds `upper` can stop before it has seen the admissible partners. The window formulation has no such problem: it converts the two-sided sum condition into a one-sided membership condition on a sorted array, where monotonicity is guaranteed by the sort.

## 7. Other strategies and their trade-offs

| Strategy | Idea | Time | Extra space | Assessment |
|---|---|---|---|---|
| Sort, then binary search both window ends per left position | as derived above | $O(n \log n)$ | $O(1)$ beyond the sorted array | The method derived here; two uniform "at least" searches per endpoint |
| Sort, then a shrinking two-pointer sweep | keep a right cursor that only moves left as the left position advances | $O(n \log n)$ | $O(1)$ | Same bound; the cursor moves monotonically because a larger left value can only shrink the admissible block |
| Count sums at most $U$ and at most $L - 1$, then subtract | two one-sided counting problems | $O(n \log n)$ | $O(1)$ | Equivalent reformulation: the closed window is the difference of two half-lines |
| Insert one by one into a Fenwick tree over compressed values | query how many already-inserted values fall in the window | $O(n \log n)$ | $O(n)$ | Respects original order, but carries more machinery for the same asymptotic cost |
| Test every unordered pair | direct enumeration | $O(n^2)$ | $O(1)$ | Correct, but at $n = 10^5$ it inspects about $5 \times 10^9$ pairs |

## 8. Traps this instance exposes

- **Counting ordered pairs, or self-pairs.** Restricting each search to positions after $i$ is what makes the answer a count of unordered pairs of distinct positions. Dropping that restriction doubles the count and adds spurious pairs where a value is paired with itself.
- **Treating the upper bound as exclusive.** The condition is `nums[i] + nums[j] <= upper`, so the upper end of the partner block is included. Searching for the first value strictly greater than `upper - nums[i]` locates the same end, but mixing the two conventions — for instance searching for `upper - nums[i]` and treating the result as the first excluded position — silently drops every pair whose sum equals `upper` exactly. The sample has such pairs: sums of `6` are counted.
- **Forgetting that sorting is permitted.** Attempting to preserve original order is unnecessary work: nothing in the fairness test depends on position order beyond the requirement that the two positions differ and be ordered, and any ordering of the two endpoints of the same pair can serve as the pair's representative.
- **Assuming monotone sums in the original array.** With negative values, neither the sum nor the array is sorted, so early termination heuristics are unsound.
- **Confusing value identity with position identity.** Duplicate values such as the two `4`s contribute distinct pairs; deduplicating values would return `5` instead of `6` here.
- **Accumulating in a narrow type.** The maximum count is $\binom{10^5}{2} = 4\,999\,950\,000$, which does not fit a 32-bit signed integer in fixed-width languages.
- **Ignoring the degenerate length.** With one element or none, the answer is `0`, and every search range is empty rather than invalid.

## 9. Time and auxiliary space

Let $n$ be the length of `nums`.

- **Sorting.** $O(n \log n)$ comparisons, performed once.
- **Per left position.** Two binary searches over the suffix of the sorted array, each $O(\log n)$, plus a constant-time subtraction.
- **Total time complexity.** $O(n \log n) + O(n \log n) = O(n \log n)$, which fits $n \le 10^5$ comfortably.
- **Auxiliary space complexity.** $O(1)$ beyond the sorted array itself. The two positions located per iteration are single integers, and the only accumulator is the answer. If the caller's array must be preserved, sorting a copy costs $O(n)$ extra space, which is the sole avoidable memory in the method.