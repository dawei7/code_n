# Fair Candy Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 888 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/fair-candy-swap/) |

## Problem Description
### Goal
Alice and Bob each own boxes of candy, and the integer at each position of `aliceSizes` or `bobSizes` is the number of candies in that box. Their current total numbers of candies are different.

They will exchange exactly one box each. Return `[x, y]`, where Alice gives a box containing `x` candies and Bob gives a box containing `y` candies, so their totals are equal after the exchange. At least one valid swap is guaranteed; when several swaps work, return any one of them.

### Function Contract
Let $p=\lvert\texttt{aliceSizes}\rvert$ and $q=\lvert\texttt{bobSizes}\rvert$.

**Inputs**

- `aliceSizes`: Alice's box sizes, where $1 \leq p \leq 10^4$ and every size is between $1$ and $10^5$.
- `bobSizes`: Bob's box sizes, where $1 \leq q \leq 10^4$ and every size is between $1$ and $10^5$.

Alice's and Bob's initial totals differ, and the input guarantees at least one balancing exchange.

**Return value**

Return `[x, y]` for any valid exchange of Alice's `x`-candy box and Bob's `y`-candy box.

### Examples
**Example 1**

- Input: `aliceSizes = [1,1], bobSizes = [2,2]`
- Output: `[1,2]`

**Example 2**

- Input: `aliceSizes = [1,2], bobSizes = [2,3]`
- Output: `[1,2]`

**Example 3**

- Input: `aliceSizes = [2], bobSizes = [1,3]`
- Output: `[2,3]`

### Required Complexity
- **Time:** $O(p+q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Derive the required difference between the two boxes**

Let $A$ and $B$ be Alice's and Bob's current candy totals. If Alice gives size $x$ and receives size $y$, equality after the swap requires

$$
A-x+y=B-y+x,
$$

so $x-y=(A-B)/2$. The existence guarantee implies that the total difference is even. For each candidate `x`, the only Bob box that can pair with it is therefore `y = x - difference`, where `difference` stores `(A - B) // 2`.

**Find the required Bob box in constant expected time**

Place all sizes from `bobSizes` in a hash set. Scan Alice's boxes and compute the corresponding `y`; as soon as `y` belongs to Bob's set, return `[x, y]`.

Membership proves that both selected box sizes actually exist. The derived equation then makes the post-swap totals equal. Conversely, every valid swap must satisfy the same equation, so scanning every Alice size and testing its unique required partner cannot miss all valid answers.

#### Complexity detail

Summing both arrays, building Bob's set, and scanning Alice's boxes take $O(p+q)$ expected time. The set stores at most $q$ distinct sizes, giving $O(q)$ auxiliary space.

#### Alternatives and edge cases

- **Try every pair of boxes:** Directly checking all exchanges is correct but costs $O(pq)$ time.
- **Sort and use two pointers:** Comparing pair differences after sorting works in $O(p\log p+q\log q)$ time and can avoid a hash set when in-place sorting is allowed.
- **Hash Alice's sizes instead:** Rearranging the same equation permits storing either person's values; storing the smaller side can reduce practical memory use.
- **Duplicate box sizes:** A set may collapse duplicates because the answer needs only one box of each required size.
- **Multiple valid exchanges:** Any pair satisfying the membership and equal-total conditions is acceptable.
- **Alice has the larger total:** Then `difference` is positive, so Alice must give a box larger than the one she receives by exactly that amount.
- **Bob has the larger total:** A negative `difference` correctly makes the required Bob box larger than Alice's candidate.

</details>
