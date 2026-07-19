# Find the Kth Largest Integer in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1985 |
| Difficulty | Medium |
| Topics | Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/) |

## Problem Description
### Goal
The array `nums` contains non-negative integers represented as decimal strings.
Each representation contains only digits and has no leading zero, except that
the integer zero itself is written as `"0"`. Values may contain far more digits
than ordinary fixed-width integer types can store.

Order all entries by their numeric values from largest to smallest and return
the string occupying one-based rank `k`. Equal numeric strings remain separate
entries: if the maximum occurs twice, those copies occupy ranks one and two
rather than being deduplicated.

### Function Contract
**Inputs**

- `nums`: a list of $N$ valid decimal integer strings, where
  $1 \le N \le 10^4$ and every string has length from $1$ through $100$.
- `k`: the requested one-based descending rank, where $1 \le k \le N$.
- Let $L$ be the maximum string length in `nums`.

**Return value**

- The original string representing the `k`th largest numeric value, counting
  duplicate entries separately.

### Examples
**Example 1**

- Input: `nums = ["3", "6", "7", "10"], k = 4`
- Output: `"3"`

**Example 2**

- Input: `nums = ["2", "21", "12", "1"], k = 3`
- Output: `"2"`

**Example 3**

- Input: `nums = ["0", "0"], k = 2`
- Output: `"0"`

Both zero entries occupy their own rank.

### Required Complexity
- **Time:** $O(N\log N \cdot L)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Compare magnitude before digits**

For canonical non-negative decimal strings without leading zeros, a value with
more digits is always numerically larger. When two strings have equal length,
their ordinary lexicographic order is also their numeric order because the
first differing digit determines both comparisons.

Use the pair `(len(value), value)` as each entry's sorting key. This compares
arbitrarily long values directly as strings and avoids relying on language
support for integers wider than the stated 100 digits.

**Select the descending rank**

Sort the entries in non-decreasing numeric order under that key. The largest
entry is last, the second largest is immediately before it, and the `k`th
largest is therefore at index `-k`. Sorting preserves duplicate copies as
separate list positions, exactly matching the ranking rule.

The returned object is one of the supplied canonical strings, so no formatting
or conversion back to decimal is necessary.

#### Complexity detail

Sorting $N$ entries performs $O(N\log N)$ key comparisons. Comparing
equal-length strings may inspect up to $L$ digits, giving the conservative time
bound $O(N\log N \cdot L)$. The ordered list and its keys require $O(N)$
references or key records; the input strings themselves are not duplicated.

#### Alternatives and edge cases

- **Convert to arbitrary-precision integers:** Sorting by parsed integer values
  is concise in languages with suitable support, but direct string ordering is
  portable and avoids conversion.
- **Min-heap of size `k`:** Retain the `k` largest numeric strings while
  scanning. This uses $O(k)$ heap space and $O(N\log k \cdot L)$ time.
- **Quickselect:** Partitioning can achieve expected $O(NL)$ time, but requires
  careful custom comparison and has a quadratic worst case without stronger
  pivot guarantees.
- Repeated values must not be collapsed into a set because every occurrence
  consumes a rank.
- `"0"` is the only representation beginning with zero; length comparison
  therefore remains valid without stripping digits.
- A 100-digit value outranks every shorter value regardless of its individual
  digits.
- For `k = 1`, return a maximum; for `k = N`, return a minimum.

</details>
