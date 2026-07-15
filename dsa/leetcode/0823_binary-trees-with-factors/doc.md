# Binary Trees With Factors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 823 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-trees-with-factors/) |

## Problem Description

### Goal

You are given an array `arr` of unique integers, each strictly greater than `1`. Construct binary trees whose node values are chosen from `arr`. A value may be used for any number of nodes and in any number of different trees; using it once does not remove it from the available choices. A single node is a valid tree.

Every non-leaf node must have two children, and its value must equal the product of its left child's value and its right child's value. Left and right positions are distinct, so exchanging two unequal children produces a different tree. Return the total number of valid binary trees, reduced modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `arr`: an array of $n$ unique integers in arbitrary order, where $1 \le n \le 1000$ and $2 \le \texttt{arr}[i] \le 10^9$

**Return value**

- The number of valid binary trees whose node values come from `arr`, modulo $10^9 + 7$

### Examples

**Example 1**

- Input: `arr = [2, 4]`
- Output: `3`
- Explanation: The single-node trees rooted at `2` and `4` are valid, as is the tree with root `4` and two children valued `2`.

**Example 2**

- Input: `arr = [2, 4, 5, 10]`
- Output: `7`
- Explanation: Besides the four single-node trees and the tree rooted at `4`, root `10` can have ordered children `(2, 5)` or `(5, 2)`.

**Example 3**

- Input: `arr = [2, 4, 8]`
- Output: `8`
- Explanation: There is one tree rooted at `2`, two rooted at `4`, and five rooted at `8`.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count trees by their root value**

Sort the values in ascending order and let $D(x)$ be the number of valid trees rooted at value $x$. Every value contributes one single-node tree, so initialize $D(x) = 1$. Because every allowed value is greater than `1`, both factors of a composite root $x$ are strictly smaller than $x$. Sorting therefore ensures that every child count needed for $D(x)$ has already been computed.

**Extend a root through each ordered factorization**

For each earlier value $a$, test whether it divides the current root value $x$. If it does, let $b = x/a$ and check whether $b$ is also an earlier array value. Choosing any tree counted by $D(a)$ for the left child and any tree counted by $D(b)$ for the right child creates $D(a)D(b)$ trees rooted at $x$.

The loop considers every possible left-child value. Thus, when $a \ne b$, the iterations for $a$ and for $b$ count the two child orientations separately. When $a=b$, that factor appears only once and contributes $D(a)^2$, which already counts every ordered choice of the two subtrees without duplicating the factor pair.

**Why the dynamic program counts every tree exactly once**

A valid tree is either the single-node tree or has a unique root value together with a unique ordered pair of child-root values. The base contribution counts the first case. The factor transition counts the second case under exactly the iteration matching its left-child value, and the two child subtrees are counted recursively by their completed dynamic-programming values. No valid decomposition is omitted, and no ordered tree is assigned to two transitions.

Store each completed count in a hash map keyed by its root value, reduce additions modulo $10^9+7$, and sum $D(x)$ over every possible root $x$.

#### Complexity detail

Let $n$ be the number of values. Sorting costs $O(n \log n)$. For each sorted value, the algorithm examines every smaller value once and performs constant-time expected hash lookups, for $O(n^2)$ dynamic-programming time overall; this dominates sorting. The sorted array and the map of $n$ root counts use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Top-down memoized recursion:** Recursively count trees for each root and cache completed values. It has the same $O(n^2)$ worst-case time and $O(n)$ stored state, but recursion adds call-stack and cycle-avoidance concerns that the sorted bottom-up order avoids.
- **Accumulate by factor pairs:** Iterate over pairs of known roots, multiply their values, and add their subtree combinations when the product exists in `arr`. This can also run in $O(n^2)$ time, but the root-indexed transition more directly exposes dependency order.
- **Unmemoized recursive enumeration:** Building every tree explicitly repeats the same rooted subproblems and can take exponential time even though only one count per root is needed.
- **Unsorted input:** Array order carries no meaning; sorting is what makes all factor dependencies available before their product.
- **Reusable values:** Repetition is allowed across nodes, so factors are not consumed and the same value may appear in both child subtrees.
- **Unequal factors:** `(a, b)` and `(b, a)` are different ordered child arrangements and must both be counted.
- **Equal factors:** A square root factorization contributes $D(a)^2$ once, not twice.
- **No factorization in the array:** The value contributes only its single-node tree.
- **Large counts:** Apply the modulus during the dynamic program so every stored count and the final sum use the required residue.

</details>
