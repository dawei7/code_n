# Count Ways to Distribute Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1692 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-ways-to-distribute-candies/) |

## Problem Description
### Goal

There are $n$ distinct candies, identified from 1 through $n$, and $k$ bags. Distribute every candy so that each bag receives at least one. The order of candies within a bag is irrelevant, and the bags themselves have no labels: rearranging the bags does not create a different distribution.

Two distributions differ when some pair of candies appears together in one distribution but belongs to separate bags in the other. Equivalently, count the partitions of the $n$ distinct candies into exactly $k$ nonempty groups. Return the number of such distributions modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of distinct candies
- `k`: the exact number of nonempty, unlabeled bags, with $1 \le k \le n \le 1000$

**Return value**

The number of distinct valid distributions, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 3, k = 2`
- Output: `3`

The three partitions are one singleton paired with the complementary two-candy group.

**Example 2**

- Input: `n = 4, k = 2`
- Output: `7`

There are four singleton-plus-triple partitions and three partitions into two pairs.

**Example 3**

- Input: `n = 20, k = 5`
- Output: `206085257`

The exact count is 1,881,780,996, whose remainder modulo $10^9+7$ is 206,085,257.

### Required Complexity

- **Time:** $O(nk)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Classify the role of the newest candy**

Let the count for $i$ candies and $j$ nonempty unlabeled bags be the corresponding Stirling number of the second kind. Consider candy $i$. It has exactly two mutually exclusive roles in a final partition.

It may occupy a new singleton bag. Removing that singleton leaves a valid partition of the first $i-1$ candies into $j-1$ bags. Alternatively, it may join one of the $j$ existing bags of a partition of the first $i-1$ candies into $j$ bags. Those bags are distinguishable by their current contents even though they have no external labels, so the second case contributes $j$ choices per earlier partition. Thus

$$
S(i,j)=S(i-1,j-1)+jS(i-1,j).
$$

The two cases cover every partition exactly once according to whether candy $i$ is alone in its group, which both proves the recurrence and avoids accidentally treating bag order as significant. The base value is $S(0,0)=1$; all impossible states with a positive number of candies and zero bags are zero.

**Roll one row in descending bag order**

Maintain `ways[j] = S(i - 1, j)` before processing candy `i`. Update `j` from `min(i, k)` down to 1. The old `ways[j]` supplies the join-an-existing-bag term, while `ways[j - 1]` has not yet been overwritten and supplies the new-singleton term. Reduce each update modulo $10^9+7$.

Descending order is essential: an ascending pass would read the current row from `ways[j - 1]` and count invalid mixtures of different candy totals. After all $n$ candies, `ways[k]` is exactly the requested partition count.

#### Complexity detail

For candy count $i$, only bag counts through $\min(i,k)$ are reachable. Across all rows there are at most $nk$ constant-time transitions, so the running time is $O(nk)$. The rolling array contains $k+1$ modular counts and uses $O(k)$ auxiliary space.

#### Alternatives and edge cases

- **Full two-dimensional table:** storing every $S(i,j)$ follows the same recurrence in $O(nk)$ time but consumes $O(nk)$ space.
- **Labeled-bag assignments:** counting onto functions into $k$ named bags overcounts each valid result by $k!$ because this problem ignores bag order.
- **Stars and bars:** that method applies to identical candies placed in labeled containers, whereas these candies are distinct and the bags are unlabeled.
- **Repeated addition for multiplication:** adding `ways[j]` exactly $j$ times computes the recurrence correctly but takes $O(nk^2)$ time as $k$ grows.
- **One bag:** all candies must form one group, so the count is one.
- **One bag per candy:** every candy is a singleton, also giving exactly one distribution.
- **Modulo timing:** applying the modulus after every transition preserves the result and prevents intermediate counts from growing unnecessarily.

</details>
