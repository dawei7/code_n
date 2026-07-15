# Largest Component Size by Common Factor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 952 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Union-Find, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [largest-component-size-by-common-factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) |

## Problem Description

### Goal

Given an array `nums` of unique positive integers, form an undirected graph with one node for every array value. Two different values have an edge exactly when they share a common factor greater than 1.

Connectivity is transitive: values belong to the same connected component even when they do not share a factor directly, provided a path of qualifying edges joins them. Return the number of nodes in the largest connected component of this graph.

### Function Contract

Let $N$ be the length of `nums`, let $M = \max(\texttt{nums})$, and let $\alpha$ denote the inverse Ackermann function.

**Inputs**

- `nums`: a list of $N$ unique positive integers, where $1 \le N \le 2\cdot 10^4$ and `1 <= nums[i] <= 100000`.

**Return value**

Return the size of the largest component under the common-factor edge rule.

### Examples

**Example 1**

- Input: `nums = [4,6,15,35]`
- Output: `4`

**Example 2**

- Input: `nums = [20,50,9,63]`
- Output: `2`

**Example 3**

- Input: `nums = [2,3,6,7,4,12,21,39]`
- Output: `8`

### Required Complexity

- **Time:** $O(N\sqrt{M}\,\alpha(N))$
- **Space:** $O(N+M)$

<details>
<summary>Approach</summary>

#### General

**Represent components with disjoint sets.** Create one disjoint-set node for each array index. Path compression and union by component size make repeated connectivity updates nearly constant amortized time.

**Connect through prime-factor representatives.** Factor each value into its distinct prime factors. Keep a map from every factor already encountered to one index containing it. The first value with factor `p` becomes that factor's representative; every later value divisible by `p` is unioned with the stored index. Repeated powers such as $2^3$ contribute factor 2 only once, because they do not create additional graph relationships.

**Why factor representatives reproduce every graph edge.** If two input values share any common factor greater than 1, they share at least one prime factor. Both indices are therefore unioned through that prime's representative, possibly indirectly. Conversely, every union is performed only between values divisible by the same prime, so it corresponds to a valid common-factor edge. The disjoint-set components are consequently identical to the graph's connected components.

After processing all values, find the root of each index, count how many indices have each root, and return the largest count. The value 1 contributes no prime factor and correctly remains isolated.

#### Complexity detail

Trial division examines at most $O(\sqrt{M})$ candidate factors per number. Each discovered factor causes at most one union, whose amortized cost is $O(\alpha(N))$, so the stated upper bound is $O(N\sqrt{M}\,\alpha(N))$. The disjoint-set arrays use $O(N)$ space and the factor-owner map has at most $O(M)$ possible keys.

#### Alternatives and edge cases

- **Pairwise greatest common divisors:** Test every pair with Euclid's algorithm and union pairs whose gcd exceeds 1. This constructs the graph directly but costs $O(N^2\log M)$ time.
- **Smallest-prime-factor sieve:** Precompute a factor table through $M$ and factor each number from it. This improves repeated factorization at the cost of an explicit $O(M)$ table.
- **Explicit adjacency graph:** Materializing every qualifying edge can require quadratic space; factor representatives avoid storing those redundant edges.
- **Value one:** Since 1 has no factor greater than 1, it is always an isolated one-node component.
- **Prime values:** A prime connects only to values containing that same prime factor.
- **Indirect connection:** Values with no pairwise factor may still share a component through intermediate values, so counting only direct neighbors is insufficient.

</details>
