# Count Ways to Make Array With Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1735 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-ways-to-make-array-with-product/) |

## Problem Description

### Goal

Each query `[n,k]` asks about ordered arrays of $n$ positive integers. Count how many different arrays have a product exactly equal to $k$. Values may repeat, but every entry must be positive. Placing the same factors in different positions can produce different arrays because their order matters.

Queries are independent and their answers must remain in the original order. Because a count may be large, return each result modulo $10^9+7$.

### Function Contract

**Inputs**

- `queries`: a list of between $1$ and $10^4$ pairs `[n,k]`, with $1 \le n,k \le 10^4$.

Let $Q$ be the number of queries and

$$
K = \max_{[n,k] \in \texttt{queries}} k.
$$

**Return value**

- Return a length-$Q$ integer list whose $i$th value is the answer for `queries[i]` modulo $10^9+7$.

### Examples

**Example 1**

- Input: `queries = [[2,6],[5,1],[73,660]]`
- Output: `[4,1,50734910]`
- Explanation: Product $6$ can be split across two positions as `(1,6)`, `(2,3)`, `(3,2)`, or `(6,1)`; product $1$ forces every entry to be $1$.

**Example 2**

- Input: `queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]`
- Output: `[1,2,3,10,5]`
- Explanation: Every query is counted independently, including prime and prime-power products.

**Example 3**

- Input: `queries = [[4,8],[3,12],[2,36]]`
- Output: `[20,18,9]`
- Explanation: The prime exponents of each product are distributed independently among the requested positions.

### Required Complexity

- **Time:** $O(Q\sqrt{K})$
- **Space:** $O(Q)$

<details>
<summary>Approach</summary>

#### General

**Translate products into prime exponents**

Factor a query's target as

$$
k = \prod_j p_j^{e_j}.
$$

Each array entry contributes a nonnegative exponent of every prime. For a fixed prime $p_j$, the exponents assigned to the $n$ ordered positions must sum to $e_j$; no other constraint couples those assignments.

**Distribute one exponent with stars and bars**

The number of nonnegative $n$-tuples summing to $e_j$ is

$$
\binom{n+e_j-1}{e_j}.
$$

Assignments for distinct primes are independent, so multiply these binomial coefficients. Every resulting collection of exponent assignments determines exactly one positive-integer array, and every valid array yields exactly one such collection, making the product exact rather than an overcount.

**Factor only as far as necessary**

Trial divisors need only continue while their square is at most the remaining value. After removing all copies of a divisor, any remainder greater than $1$ is one final prime with exponent $1$. The target $k=1$ has no prime factors, so the empty product correctly gives one all-ones array.

#### Complexity detail

Trial division takes $O(\sqrt{k})$ time per query in the worst case, while the number of extracted prime exponents is at most logarithmic in $k$. Each exponent is at most $13$ under $k \le 10^4$, so its binomial coefficient is computed in bounded additional work. Across all queries this is $O(Q\sqrt K)$ time. The returned answers use $O(Q)$ space, while factorization uses constant auxiliary state.

#### Alternatives and edge cases

- **Enumerate arrays:** Even for modest $n$ and $k$, trying positive values for every position creates an exponential search space.
- **Test every possible divisor through $k$:** This factors primes correctly but takes $O(QK)$ time instead of stopping at the square root.
- **Dynamic programming over products:** Tracking every achievable product for every position uses substantially more time and memory than distributing prime exponents directly.
- **Product one:** Exactly one array is possible, consisting entirely of ones.
- **Array length one:** The sole entry must equal $k$, so every such query has answer one.
- **Prime target:** Its single exponent can be assigned to any one of the $n$ positions, giving $n$ arrays.
- **Repeated queries:** They remain separate output positions even when their answers coincide.
- **Modulo reduction:** Reduce after each multiplication so large intermediate counts do not affect the required result.

</details>
