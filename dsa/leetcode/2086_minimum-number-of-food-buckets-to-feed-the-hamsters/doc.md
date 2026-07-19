# Minimum Number of Food Buckets to Feed the Hamsters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2086 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/) |

## Problem Description

### Goal

A zero-indexed street is represented by `hamsters`. Each `"H"` marks a hamster, while each `"."` marks an empty position where a food bucket may be placed. A hamster at index $i$ is fed when a bucket occupies at least one adjacent position, $i-1$ or $i+1$; buckets cannot be placed on hamster positions.

Choose empty positions so that every hamster is fed, and return the minimum number of buckets used. One bucket between two hamsters may feed both of them. If no placement can feed every hamster, return `-1`.

### Function Contract

**Input**

- `hamsters`: a string of length $n$, where $1 \le n \le 10^5$ and every character is either `"H"` or `"."`.

**Return value**

Return the minimum number of buckets needed to feed all hamsters, or `-1` when a valid placement does not exist.

### Examples

**Example 1**

- Input: `hamsters = "H..H"`
- Output: `2`
- Explanation: Buckets at indices `1` and `2` feed the two endpoint hamsters.

**Example 2**

- Input: `hamsters = ".H.H."`
- Output: `1`
- Explanation: A bucket at index `2` is adjacent to both hamsters.

**Example 3**

- Input: `hamsters = ".HHH."`
- Output: `-1`
- Explanation: The middle hamster has no adjacent empty position.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Resolving hamsters from left to right**

When the scan reaches a hamster, any bucket on its left has already been chosen. If that bucket exists, the hamster is fed and no new action is needed. Otherwise a bucket must be placed in one of the hamster's currently available adjacent empty positions.

**Why the right position has priority**

If the position to the right is empty, place the bucket there. This feeds the current hamster and may also feed the next hamster two positions later. Placing on the left cannot help any future hamster, so exchanging such a left placement for the available right placement never increases the bucket count or invalidates an already processed hamster.

Only when the right position is unavailable should the algorithm use an empty position on the left. If neither side can hold a bucket and no previously placed left bucket feeds the hamster, the instance is impossible. Remembering the index of the latest bucket is enough to distinguish an original `"."` from a position already selected for food.

**Why the count is minimum**

Every new bucket is forced because the current hamster is not yet fed. The right-first choice preserves at least as much usefulness for the unprocessed suffix as any other feasible choice. Applying this exchange argument at each hamster transforms an optimal placement into the greedy choices without adding buckets, so the greedy count is optimal.

#### Complexity detail

The scan examines each of the $n$ positions once and performs constant work per position, giving $O(n)$ time. It stores only the latest bucket index and the running count, so the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Dynamic programming over local states:** A DP can record whether the previous position contains a hamster or bucket, but the one-directional greedy exchange removes the need for a state table.
- **Backtracking over empty positions:** Trying bucket subsets eventually finds the optimum but has exponential worst-case growth.
- **Mutable street copy:** Marking bucket positions in a character array is still linear-time and clear, but uses $O(n)$ auxiliary space.
- A street with no hamsters needs zero buckets.
- A lone hamster with no adjacent empty position makes the answer `-1`.
- A pattern `"H.H"` needs one shared bucket, while `".HH."` needs two outer buckets.
- Three consecutive hamsters are impossible because the middle hamster has no empty neighbor.

</details>
