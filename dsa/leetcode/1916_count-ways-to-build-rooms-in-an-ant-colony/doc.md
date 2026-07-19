# Count Ways to Build Rooms in an Ant Colony

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/) |
| Frontend ID | 1916 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Tree, Depth-First Search, Graph Theory, Topological Sort, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An ant colony plans $N$ rooms numbered from `0` through `N - 1`. For each room `i`, `prevRoom[i]` identifies the room that must be built immediately before room `i` becomes accessible through a direct connection. Room `0` is the root and has parent `-1`; every other room is eventually reachable from it, so these connections form a rooted tree.

Only one room can be built at a time. Any unbuilt room may be chosen once its parent has already been built. Count all distinct orders that build every room while respecting those parent-before-child dependencies, and return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `prevRoom`: a length-$N$ parent array describing a rooted tree at room `0`.
- `prevRoom[0] = -1`; for each other room, `prevRoom[i]` is a valid room index.
- $2 \le N \le 10^5$.

**Return value**

- Return the number of valid complete construction orders modulo $1\,000\,000\,007$.

### Examples

**Example 1**

- Input: `prevRoom = [-1,0,1]`
- Output: `1`

The chain forces the order `0, 1, 2`.

**Example 2**

- Input: `prevRoom = [-1,0,0,1,2]`
- Output: `6`

The two child chains may be interleaved in six parent-respecting ways after room `0`.

**Example 3**

- Input: `prevRoom = [-1,0,0]`
- Output: `2`

After room `0`, its two children may be built in either order.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**View valid orders as tree linear extensions**

For every node $v$, let $s_v$ be the number of rooms in its subtree, including $v$. A classic hook-length identity for rooted trees gives the number of parent-before-child orders:

$$
\frac{N!}{\prod_v s_v}.
$$

To see why, consider a node whose child subtrees have sizes $s_1,\ldots,s_t$. The node itself must come first within its subtree. The valid orders inside the child subtrees can then be interleaved in

$$
\frac{(s_1+\cdots+s_t)!}{s_1!\cdots s_t!}
$$

ways while preserving each child's internal order. Multiplying this recurrence down the tree cancels the child factorials and leaves the hook-length formula.

**Compute subtree sizes without recursion**

Build child lists from `prevRoom`. Starting at room `0`, produce a parent-before-child traversal order iteratively. Process every non-root room in reverse order, adding its accumulated size to its parent. This remains safe for a chain of $10^5$ rooms, where recursive DFS could exceed Python's call-stack limit, and it does not assume parent indices are numerically smaller than child indices.

**Divide modulo the prime**

Compute $N!$ and the product of all subtree sizes modulo $M=10^9+7$. Every subtree size is positive and smaller than $M$, so the product is invertible. Fermat's little theorem gives its inverse as `pow(product, M - 2, M)`. Multiplying the factorial by this inverse yields the required residue.

#### Complexity detail

Building the tree, producing the traversal order, accumulating subtree sizes, and multiplying the factors each take $O(N)$ time. Modular exponentiation costs $O(\log M)$, which is constant with respect to $N$, so total time is $O(N)$. Child lists, order, and subtree sizes use $O(N)$ space.

#### Alternatives and edge cases

- **Merge child counts with binomial coefficients:** A postorder DFS can multiply child answers and interleaving combinations directly; it is also $O(N)$ with precomputed factorials but needs recursion safeguards or an explicit stack.
- **Enumerate topological orders:** Backtracking over currently available rooms is exact only for tiny trees and grows exponentially.
- **Recompute every subtree:** Running a traversal from each node is correct but takes $O(N^2)$ time on a chain.
- **Chain:** Every room has only one possible successor, so the answer is one.
- **Star:** Once the root is built, its $N-1$ children may appear in any order, giving $(N-1)!$.
- **Arbitrary labels:** A parent may have a larger numeric ID than its child; traversal order, not numeric order, controls accumulation.

</details>
