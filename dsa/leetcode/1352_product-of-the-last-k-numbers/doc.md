# Product of the Last K Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1352 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Design, Data Stream, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/product-of-the-last-k-numbers/) |

## Problem Description

### Goal

Design a `ProductOfNumbers` data structure for a stream of nonnegative integers. Calling `add(num)` appends `num` to the stream. Calling `getProduct(k)` must return the product of the last `k` appended numbers; every query guarantees that at least `k` numbers have been added.

The operation sequence can contain zeroes. Any queried suffix containing a zero has product zero, while queries confined to numbers added after the most recent zero must return their exact product. Support a long interleaving of additions and queries without recomputing each suffix from scratch.

### Function Contract

**Inputs**

- `add(num)`: append one nonnegative integer to the stream.
- `getProduct(k)`: request the product of the last $k$ appended values.
- The app-local `solve(operations)` adapter receives `[method, arguments]` pairs.
- Let $q$ be the total number of operations.

**Return value**

- `add` returns no value.
- `getProduct(k)` returns the exact integer product of the requested suffix.
- The app-local adapter returns every method result in order, using `null` for additions.

### Examples

**Example 1**

- Operations: add `3, 0, 2, 5, 4`; query the last `2`, `3`, and `4` values; add `8`; query the last `2`.
- Output: `[null, null, null, null, null, 20, 40, 0, null, 32]`

**Example 2**

- Operations: add `1, 2, 3`; query the last `3`.
- Output: `[null, null, null, 6]`

**Example 3**

- Operations: add `0, 9`; query the last `1` and `2`.
- Output: `[null, null, 9, 0]`

### Required Complexity

- **Time:** $O(q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Store prefix products after the latest zero.** Keep a list beginning with the sentinel product `1`. For a nonzero addition, append the previous prefix product multiplied by the new number. If the current zero-free segment has values $x_1,\ldots,x_a$, the list stores $1,x_1,x_1x_2,\ldots,x_1\cdots x_a$.

**Reset at zero.** When zero is added, replace the list with just `[1]`. The list length minus one is therefore exactly the number of consecutive nonzero values after the most recent zero.

For `getProduct(k)`, if $k$ is at least the current list length, the requested suffix crosses the latest zero and its product is zero. Otherwise, divide the full segment prefix by the prefix immediately before the requested suffix: `prefix[-1] // prefix[-1 - k]`. All stored factors are integers and the denominator is an exact factor of the numerator, so this quotient is precisely the suffix product.

#### Complexity detail

Each `add` and `getProduct` performs a constant number of list and arithmetic operations in the standard unit-cost model, so $q$ operations take $O(q)$ time. At most one prefix product is stored per addition after the latest zero, bounded by $O(q)$ space.

#### Alternatives and edge cases

- **Store raw values:** Appending is constant time, but multiplying the last $k$ values makes a query $O(k)$ and repeated growing queries quadratic overall.
- **Keep every historical prefix across zeroes:** Division cannot recover a suffix that crosses a zero, so zero positions still need special handling; resetting makes that boundary explicit.
- **Query crosses a zero:** The prefix-list length detects this immediately and the answer is zero.
- **Consecutive zeroes:** Each zero simply resets the same sentinel state.
- **Product of one value:** Dividing adjacent prefixes returns the latest number.

</details>
