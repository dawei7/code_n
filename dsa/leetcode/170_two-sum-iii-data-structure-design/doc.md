# Two Sum III - Data structure design

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 170 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Design, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-iii-data-structure-design/) |

## Problem Description
### Goal
Design a stateful `TwoSum` structure that accumulates integer occurrences through `add(number)`. Repeated additions are retained as separate occurrences rather than collapsed into one set entry, and values remain available for every later query.

For `find(value)`, return whether two distinct stored occurrences can sum to the requested value. A number may pair with itself only when it has been added at least twice; otherwise the two addends may be different values in either order. Process construction, additions, and queries sequentially, returning `None` for mutations and a boolean for each query without removing or consuming any stored occurrence.

### Function Contract
**Inputs**

- `operations`: method names beginning with `TwoSum`, followed by `add` and `find`
- `arguments`: one integer argument for each add or find operation

**Return value**

A result list aligned with operations: `None` for construction and add, and a boolean for each find query.

### Examples
**Example 1**

- Input: add `1`, `3`, `5`; find `4`; find `7`
- Output: `[null,null,null,null,true,false]`

**Example 2**

- Input: add `3` twice; find `6`
- Output: `True`

**Example 3**

- Input: add `-2` and `5`; find `3`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

The design choice is where to pay for the work: during `add` or during `find`. Favoring a fast stream update, store a frequency map from each value to the number of times it has been added. Each `add(number)` increments one counter in expected constant time.

For `find(value)`, scan the distinct stored numbers. For each `x`, its only possible partner is `y = value - x`. The frequency map answers whether `y` exists, but multiplicity matters:

- If $x \ne y$, one occurrence of each is sufficient.
- If $x = y$, the same stored occurrence cannot be used twice, so `count[x]` must be at least two.

For example, after adding one `3`, `find(6)` must be false. After adding a second `3`, the same query becomes true. A set would lose precisely the information needed to distinguish those states.

The map always represents the complete multiset of values added so far. A query examines every possible distinct first value and its unique complement, so it cannot overlook a valid pair.

If the query returns true, the map contains the complement and the multiplicity check proves that two distinct stored occurrences are available, so a valid pair exists. Conversely, suppose a valid stored pair `(a, b)` sums to the query value. When the scan reaches `a`, it computes complement `b`. If the values differ, both are present; if they are equal, the valid pair guarantees at least two occurrences. The corresponding condition succeeds, so every valid pair is detected.

#### Complexity detail

`add` takes expected $O(1)$ time. If `u` distinct values have been stored, `find` takes $O(u)$ time, bounded by $O(n)$ additions. The frequency map uses $O(u)$ space.

#### Alternatives and edge cases

- Precomputing every attainable pair sum can make `find` constant time, but each `add` must combine with all earlier values and the sum set can grow quadratically.
- Keeping values sorted enables a two-pointer query, but inserting into an array costs $O(n)$ unless a more complex ordered structure is used.
- A plain set is insufficient because it cannot represent two equal occurrences.
- Negative values and zero work with the same complement calculation.
- The best trade-off can depend on workload: this design suits frequent additions with linear-time queries.

</details>
