# Minimized Maximum of Products Distributed to Any Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2064 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) |

## Problem Description

### Goal

There are $n$ specialty stores and $m$ product types. The array `quantities` gives the available count of every type, and all products must be distributed. One product type may be split among several stores, but each store may receive products of at most one type. Stores are also allowed to receive nothing.

For a completed distribution, let $x$ be the largest number of products assigned to any one store. Return the smallest value of $x$ achievable while obeying the rules.

### Function Contract

**Inputs**

- `n`: the number of stores, where $1 \le n \le 10^5$.
- `quantities`: an array of $m$ positive product counts, where $1 \le m \le n$ and each count is at most $10^5$.

Let $Q=\max(\texttt{quantities})$.

**Return value**

- Return the minimum possible maximum number of products held by any store after distributing every product.

### Examples

**Example 1**

- Input: `n = 6, quantities = [11,6]`
- Output: `3`
- Explanation: Split the first type among four stores as `2,3,3,3` and the second among two stores as `3,3`.

**Example 2**

- Input: `n = 7, quantities = [15,10,10]`
- Output: `5`
- Explanation: The three types can use three, two, and two stores, each holding five products.

**Example 3**

- Input: `n = 1, quantities = [100000]`
- Output: `100000`
- Explanation: The only store must receive the complete quantity.

### Required Complexity

- **Time:** $O(m\log Q)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn a proposed maximum into a feasibility test**

Suppose no store may receive more than a positive limit $x$. A product type with quantity $q$ then needs exactly $\lceil q/x\rceil$ stores: fewer cannot hold all its units, and that many suffice by splitting the type. The limit is feasible precisely when the sum of these requirements over all types is at most $n$.

**Exploit the monotone boundary**

If a limit is feasible, every larger limit is also feasible; if it is infeasible, every smaller one is infeasible. Binary-search the first feasible integer between $1$ and $Q$. For a midpoint, compute each ceiling as `(quantity + limit - 1) // limit`. Move the upper boundary to the midpoint when the required-store sum fits, and otherwise discard the midpoint and everything below it.

The feasibility calculation is both necessary and sufficient because stores assigned to different types never need to mix their products. Binary search preserves the first feasible value inside its interval, so when the boundaries meet, that value is exactly the minimum achievable maximum.

#### Complexity detail

Each feasibility test scans all $m$ quantities in $O(m)$ time, and binary search performs $O(\log Q)$ tests. The total time is $O(m\log Q)$. Apart from the search boundaries and running store count, the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Test limits in increasing order:** The same feasibility test is correct, but trying every value through $Q$ can take $O(mQ)$ time.
- **Priority-queue splitting:** Repeatedly give another store to the type with the largest current share can model the choices, but it needs more bookkeeping and can be slower when many spare stores exist.
- When $m=n$, every type must fit in one store, so the answer is $Q$.
- A type may occupy several stores, but no store may combine even small leftovers from two types.
- Unused stores are allowed; feasibility requires at most $n$ stores rather than exactly $n$.
- Ceiling division is essential when a quantity is not divisible by the tested limit.

</details>
