# Can Make Arithmetic Progression From Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1502 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) |

## Problem Description
### Goal

An arithmetic progression is a sequence in which the difference between every pair of consecutive elements is the same. The common difference may be positive, negative, or zero; only equality across all adjacent differences matters.

Given an integer array `arr`, determine whether its elements can be rearranged so that the resulting sequence is an arithmetic progression. Every array occurrence must be used exactly once. Return `true` when at least one such ordering exists and `false` otherwise; the input order itself does not need to satisfy the progression.

### Function Contract
**Inputs**

Let $n=\lvert\texttt{arr}\rvert$.

- `arr`: an integer array with $2 \le n \le 1000$.
- Every value lies in $[-10^6,10^6]$.
- Values need not be distinct and may arrive in any order.

**Return value**

Return `true` if all $n$ occurrences can be reordered into a sequence with one constant adjacent difference. Otherwise return `false`. The app-local implementation does not mutate `arr`.

### Examples
**Example 1**

- Input: `arr = [3,5,1]`
- Output: `true`
- Explanation: Reordering to `[1,3,5]` gives common difference $2$; reversing that order gives common difference $-2$.

**Example 2**

- Input: `arr = [1,2,4]`
- Output: `false`
- Explanation: No ordering of these three values has equal adjacent differences.

**Example 3**

- Input: `arr = [7,7,7]`
- Output: `true`
- Explanation: Every adjacent difference is zero.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Derive the only possible positive step from the endpoints**

Any valid progression can be read in ascending order without changing whether it exists. Its first value must then be `min(arr)` and its last value must be `max(arr)`. If the common difference is $d$, moving across the $n-1$ gaps gives

$$
\max(\texttt{arr})-\min(\texttt{arr})=(n-1)d.
$$

Therefore the span must be divisible by $n-1$, and when it is divisible the nonnegative difference is forced: there is no second candidate step to try.

If the span is zero, every value equals the minimum and the array always forms a zero-difference progression. Handle that case before the distinct-value reasoning below.

**Describe the complete target set**

For a positive difference, the only valid ascending progression is

$$
\min(\texttt{arr}),\ \min(\texttt{arr})+d,\ \ldots,\ \min(\texttt{arr})+(n-1)d.
$$

Put all input values in a hash set. A positive-step progression has $n$ distinct positions, so first require the set to contain exactly $n$ values. This rejects duplicates even when their minimum, maximum, and span happen to look plausible.

Then generate each of the $n$ required terms and test expected constant-time membership in the set. If every term exists, the input contains exactly the forced progression because both collections have $n$ distinct values. If any term is absent, no rearrangement can repair that gap.

**Why these tests are sufficient**

Suppose the method returns `true`. In the zero-span branch all values are equal, so any ordering has difference zero. Otherwise, divisibility supplies an integer $d>0$, cardinality proves there are no duplicate occurrences, and membership proves every term from the forced sequence exists. Ordering those terms by increasing index produces a valid progression using every input occurrence.

Conversely, any valid arrangement can be reversed if necessary so its difference is nonnegative. Its endpoints are the array minimum and maximum, which forces the same $d$. With $d=0$ the span branch accepts; with $d>0$ the progression has exactly the distinct target terms checked by the set. Thus every valid input is accepted.

#### Complexity detail

Finding the minimum and maximum, building the set, checking its cardinality, and testing all $n$ target terms each take $O(n)$ expected time. Hash-set membership is expected $O(1)$ per term. The set stores at most $n$ values, giving $O(n)$ auxiliary space.

The implementation leaves `arr` unchanged. Integer arithmetic is exact over the stated bounds.

#### Alternatives and edge cases

- **Sort and compare adjacent gaps:** Sorting reveals the progression directly and uses concise code, but costs $O(n\log n)$ time and may mutate the input when performed in place.
- **Linear membership in the original array:** Derive the same target terms but search the list separately for each one. It is correct, yet takes $O(n^2)$ time on progressions whose matches occur late.
- **Index each value by normalized offset:** Check that every value's offset from the minimum is divisible by $d$ and maps to a unique index. This is also linear but needs careful handling of $d=0$ and duplicate positions.
- **Two elements:** Any pair is an arithmetic progression because it has only one adjacent difference.
- **All values equal:** The common difference is zero; duplicates are required rather than disqualifying.
- **Duplicates with a nonzero span:** A positive-difference progression has distinct terms, so any duplicate makes the answer false.
- **Span not divisible by $n-1$:** No integer common difference can connect the minimum and maximum in exactly $n-1$ steps.
- **Negative values:** Minimum, span, divisibility, and set membership work without a special sign rule.
- **Descending input:** Input order is irrelevant; the method checks the canonical ascending progression without sorting.
- **Extreme values:** The largest possible span is $2\cdot10^6$, which remains safe for the platform integer types and Python integers.

</details>
