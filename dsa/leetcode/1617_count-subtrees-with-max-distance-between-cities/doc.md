# Count Subtrees With Max Distance Between Cities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1617 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Bit Manipulation, Tree, Dynamic Programming, Bitmask, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) |

## Problem Description
### Goal
There are `n` cities numbered from 1 through `n`, joined by `n - 1` bidirectional edges. A unique path exists between every pair of cities, so the complete infrastructure is a tree. A subtree is determined by a subset of cities whose induced paths remain entirely inside that subset; equivalently, the selected cities form a connected induced subgraph. Two subtrees differ when their selected city sets differ.

For every distance $d$ from 1 through $n-1$, count the subtrees whose maximum distance between any two selected cities is exactly $d$. Distance is measured by the number of edges on the unique path. Return the $n-1$ counts in increasing distance order. Single-city subsets have diameter zero and therefore do not contribute to the returned array.

### Function Contract
**Inputs**

- `n`: the number of cities, where $2 \le n \le 15$.
- `edges`: exactly $n-1$ distinct pairs `[u, v]` describing a tree on cities 1 through `n`.

**Return value**

Return an array `answer` of length $n-1$, where `answer[d - 1]` is the number of connected city subsets with diameter exactly $d$.

### Examples
**Example 1**

- Input: `n = 4, edges = [[1,2],[2,3],[2,4]]`
- Output: `[3,4,0]`

**Example 2**

- Input: `n = 2, edges = [[1,2]]`
- Output: `[1]`

**Example 3**

- Input: `n = 3, edges = [[1,2],[2,3]]`
- Output: `[2,1]`

### Required Complexity
- **Time:** $O(2^n n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Represent each city subset as a bitmask.** With $n \le 15$, all $2^n$ subsets can be examined directly. Skip masks containing fewer than two cities because their diameter is zero. For every other mask, select its least-significant city bit as a traversal start.

**Use one restricted traversal to prove connectivity.** Traverse only neighbors whose bits belong to the current mask. Because the original graph is a tree, the traversal never needs a general visited set: carrying the parent prevents returning along the only edge just used. Count the reached cities. If that count differs from `mask.bit_count()`, the selected cities do not form a connected subtree and the mask contributes nothing.

**Find the diameter with a second tree traversal.** During the connectivity traversal, retain a farthest reached city. In any tree, a farthest vertex from an arbitrary start is an endpoint of a diameter. Traverse the same induced subtree again from that endpoint; the greatest distance reached is the subtree diameter. Increment the result bucket for that distance.

Every accepted mask is connected by the reached-count test, and every connected city subset appears as exactly one mask. The two-traversal tree property supplies its exact maximum pairwise distance. Therefore each qualifying subtree increments exactly one correct distance bucket, and no disconnected or single-city subset is counted.

#### Complexity detail

There are $2^n$ masks. Each restricted traversal examines at most $n$ cities and their incident tree edges, and a connected mask needs two such traversals. The total time is $O(2^n n)$. The adjacency lists, traversal stack, and result array each use $O(n)$ space; the masks are processed one at a time.

#### Alternatives and edge cases

- **All-pairs distances per connected mask:** Precompute tree distances, then inspect every selected city pair to obtain each diameter. This is correct but takes $O(2^n n^2)$ time when many subsets are connected.
- **Edge-count connectivity test:** In a subset of a tree, having exactly one fewer internal edge than vertices proves connectivity, but finding the diameter still needs either pair scanning or a traversal.
- **Enumerate endpoint pairs:** Dynamic programming can count subtrees for each proposed diameter endpoint pair, but avoiding duplicate counts requires more intricate tie-breaking.
- Single-city masks are connected but have diameter zero, which has no output bucket.
- The smallest tree has one two-city subtree and returns `[1]`.
- A path of $n$ cities has exactly $n-d$ connected intervals of diameter $d$.
- A star has many diameter-two subtrees, because every selection containing the center and at least two leaves is connected.
- City labels are 1-based in `edges` but are normalized before bit operations.

</details>
