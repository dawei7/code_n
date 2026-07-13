# Shopping Offers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 638 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/shopping-offers/) |

## Problem Description
### Goal
In a store with `n` item types, `price[i]` is the individual price of item `i`, and `needs[i]` is the exact number of pieces you want. Each row in `special` gives quantities of all `n` items followed by the bundle's sale price.

Return the lowest total price needed to satisfy all quantities exactly. You may buy items individually and may use any special offer multiple times, but you are not allowed to buy more of any item than `needs` requests, even when an overfilled bundle would cost less. Offers may be combined in any order.

### Function Contract
**Inputs**

- `price`: the individual price of each of `M` item types
- `special`: bundle rows containing `M` item quantities followed by that bundle's price
- `needs`: the exact required quantity of each item type

**Return value**

- The minimum total cost that satisfies all needs exactly

### Examples
**Example 1**

- Input: `price = [2,5]`, `special = [[3,0,5],[1,2,10]]`, `needs = [3,2]`
- Output: `14`

**Example 2**

- Input: `price = [2,3,4]`, `special = [[1,1,0,4],[2,2,1,9]]`, `needs = [1,2,1]`
- Output: `11`

**Example 3**

- Input: `price = [2,3]`, `special = []`, `needs = [2,1]`
- Output: `7`

### Required Complexity

- **Time:** $O(SM \cdot \prod(needs_i + 1))$
- **Space:** $O(M \cdot \prod(needs_i + 1))$

<details>
<summary>Approach</summary>

#### General

**Use remaining needs as the complete state**

After any sequence of bundle purchases, future choices depend only on the quantities still required, not on the order used to reach them. Represent that state as an immutable tuple so equivalent subproblems share one memoized result.

**Keep individual purchases as a universal fallback**

For each state, buying every remaining item individually is always legal and gives an initial upper bound. Then try each bundle whose quantities do not exceed the remaining needs, subtract it componentwise, and combine its price with the optimal cost of the smaller state.

**Discard bundles that cannot improve a solution**

Ignore a bundle containing no items, which would not advance recursion. A bundle priced at least as high as its items bought individually is also unnecessary: replacing it with those individual purchases never costs more and preserves exact quantities.

**Why the recurrence finds the global minimum**

Any optimal plan either uses no further bundle, in which case the individual fallback matches it, or has a first bundle. That first bundle must fit the current needs, and the remainder of the plan is an optimal solution to the reduced state; otherwise it could be replaced by a cheaper remainder. Evaluating every legal first bundle and memoizing the minimum therefore covers and optimizes every valid plan.

#### Complexity detail

There are at most $Π(\mathit{needs}_{i} + 1)$ remaining-quantity states. Each state checks `S` bundles across `M` item types, giving $O(SM \cdot \prod(needs_i + 1))$ time. Memo keys and recursion frames store `M` quantities per reachable state, using $O(M \cdot \prod(needs_i + 1))$ space.

#### Alternatives and edge cases

- **Backtracking without memoization:** explores the same legal bundle sequences but recomputes equivalent remaining states exponentially many times.
- **Bottom-up multidimensional dynamic programming:** has the same state bound but is awkward to index when the number of item types varies.
- **Enumerate bundle usage counts:** bounding each offer independently creates a large Cartesian product and still needs exact-quantity checks.
- A bundle that exceeds any remaining quantity is illegal even when its price is attractive.
- Bundles may be reused as long as every application fits the remaining needs.
- Zero needs cost zero regardless of available offers.
- Non-discounted bundles may be ignored because individual purchases remain available.
- The modulus is not involved; return the exact minimum integer cost.

</details>
