## General

**Two different kinds of information are required**

The answer combines a global condition and an ordering condition:

- a value is eligible only if its total frequency in the entire array is exactly one; and
- among eligible even values, the one with the earliest original index wins.

The first condition cannot generally be decided when a value is first encountered. An even number seen near the beginning may occur again near the end and lose uniqueness. The source therefore uses two passes: count all values first, then scan the original order.

**Build complete frequencies**

`cnt = Counter(nums)` creates a mapping from each distinct array value `x` to its total number of occurrences. After this statement,

$$
\texttt{cnt}[x]
=\left|\{i:\texttt{nums}[i]=x\}\right|.
$$

Because the counter is built from the full array before any candidate is selected, `cnt[x] == 1` exactly captures global uniqueness. It does not merely mean “not seen before.”

For the first example `[3,4,2,5,4,6]`, the counter records frequency two for value four and frequency one for two and six. Value four is even but ineligible; two and six are both eligible.

**Scan in original order for the priority rule**

The second loop reads `nums` from left to right. For each value `x`, it checks

`x % 2 == 0`

and

`cnt[x] == 1`.

The remainder condition is the exact divisibility-by-two definition of evenness. Both conditions must hold.

As soon as they do, the method returns `x`. Since every earlier array position has already been examined and rejected, this occurrence has the smallest index among all globally unique even values. No later value can have higher priority.

If the loop ends, every element failed parity, uniqueness, or both. The method returns minus one, the required no-answer sentinel.

Notice that the function returns the even value, not its index. The scan order is used only to choose which value to return.

**Why a one-pass immediate return is unsafe**

Suppose the array begins with four. At index zero, it is even and has not appeared earlier, but a later four may exist. Returning immediately would be wrong for `[4,2,4]`: four is not unique, while two is.

One-pass strategies are possible only if they delay the final decision or maintain extra ordered candidate information while counts change. The simple two-pass method is clearer: complete frequencies make eligibility immutable during the priority scan.

**Invariant of the selection pass**

Before examining index `i`:

- `cnt` stores exact full-array frequencies;
- no position smaller than `i` contains a globally unique even value; otherwise the method would already have returned; and
- every unexamined candidate has index at least `i`.

If `nums[i]` is unique and even, the second statement proves it is the earliest answer. If it fails, advancing to `i+1` preserves the statement. Reaching the end proves that no answer exists.

This directly covers ties in values. A value with frequency one has only one index, while a repeated even value is excluded at all of its indices. There is no separate tie-breaking comparison to implement.

**Bounded-domain interpretation**

The values are restricted to integers from one through one hundred. Although the source uses a hash-based `Counter`, at most one hundred keys can exist. Relative to a growing array length, this is a fixed amount of frequency storage.

A frequency array of length 101 would express the same bounded-domain idea with direct indexing. The dynamic counter is convenient and still has the same asymptotic bound under the official constraints.

For `nums=[4,4]`, both positions see `cnt[4]=2`, so neither qualifies and the method returns minus one. For an all-odd array, every element fails the parity test regardless of frequency. For `[8,3,6]`, both eight and six are unique and even, and the first scan position returns eight.

**Source dependency**

The exact solution requires `Counter` from `collections`. The execution environment must make that name available. Counter lookups for keys already drawn from `nums` always return their stored positive frequency.

## Complexity detail

Let `N` be the array length and `U` its number of distinct values. Building the counter takes expected `O(N)` time. The selection pass visits at most `N` elements, with expected constant-time hash lookup per element. Total expected time is `O(N)`, matching the manifest.

The counter stores `O(U)` entries in a domain-independent analysis. Here `1\le nums[i]\le100`, so `U\le100` and the storage is `O(1)` with respect to `N`. This is the interpretation behind the manifest's `O(1)` space. If the value range were unbounded, the exact same source would instead require `O(U)` auxiliary space.

The return value and loop state are constant size. Early return may shorten the second pass but does not change the worst-case time.

## Alternatives and edge cases

- **Fixed array of 101 counts:** Count by value directly, then perform the same original-order scan. This gives deterministic `O(N+100)` time and explicit `O(1)` bounded-domain space.
- **One pass with first positions and counts:** Record each value's count and earliest index, then scan the at-most-100 value domain for the eligible even value with minimum first index. This is correct but stores more state than the simple second pass.
- **Return the first even value immediately:** Incorrect because a later duplicate may make it non-unique.
- **Use a set of seen values only:** A set distinguishes seen from unseen but not frequency one from frequency two or more. Exact counts are necessary.
- **Sort unique even candidates by value:** The priority is array index, not numerical value. Sorting values can choose the wrong answer.
- **Return an index:** The contract asks for the element value. The scan order determines priority, but the returned object is `x`.
- **First element later duplicated:** Its counter value exceeds one, so it is skipped even though it is the earliest even occurrence.
- **Multiple unique evens:** The left-to-right early return selects the earliest index, not the smallest even number.
- **Repeated even values:** Every occurrence is rejected because its full frequency is greater than one.
- **Unique odd value:** It remains in the counter but fails the parity condition.
- **No valid value:** Minus one is safe as a sentinel because all input values are positive.
- **Value zero:** It is excluded by the stated range, though it is mathematically even and the source would treat it as such if supplied.
- **Generalized value domain:** Without the one-to-one-hundred bound, describe counter memory as `O(U)` rather than constant.
- **Hash-table qualification:** Counter operations are expected constant time. A fixed array removes hashing if worst-case deterministic behavior matters under this bounded domain.
