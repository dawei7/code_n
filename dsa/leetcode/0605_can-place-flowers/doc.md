# Can Place Flowers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 605 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/can-place-flowers/) |

## Problem Description
### Goal
You have a long flowerbed represented by a binary array `flowerbed`, where `1` means a plot already contains a flower and `0` means it is empty. Flowers cannot be planted in adjacent plots, and the initial flowerbed already obeys this no-adjacent-flowers rule.

Given an integer `n`, return `True` if at least `n` new flowers can be planted without violating the rule, and `False` otherwise. Existing flowers cannot be moved, and a newly planted flower must have no occupied plot immediately to its left or right; positions beyond either end of the array count as empty boundaries.

### Function Contract
**Inputs**

- `flowerbed: list[int]`: plots where `1` is occupied and `0` is empty; existing flowers are nonadjacent
- `n: int`: number of new flowers required

**Return value**

- `True` when a legal placement of at least `n` flowers exists; otherwise `False`

### Examples
**Example 1**

- Input: `flowerbed = [1,0,0,0,1], n = 1`
- Output: `True`

**Example 2**

- Input: `flowerbed = [1,0,0,0,1], n = 2`
- Output: `False`

**Example 3**

- Input: `flowerbed = [0], n = 1`
- Output: `True`

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Plant at the earliest legal plot**

Scan from left to right. An empty plot is usable when its existing left neighbor, if any, is zero and its right neighbor, if any, is zero. Boundary plots simply omit the missing-neighbor check.

**Skip the newly blocked neighbor**

After planting at index `i`, index $i + 1$ cannot be used, so advance by two. This avoids mutating the input while still remembering the placement's only effect on future decisions.

**Stop once the target is reached**

Count each greedy placement and return immediately when the count reaches `n`. A zero target is always feasible.

**Why the earliest choice is safe**

Consider the first plot where the greedy scan plants. Any feasible placement for the remaining flowerbed either already plants there or leaves it empty. If it instead plants at the next possible plot to the right within the same empty region, move that flower to the greedy plot: no left conflict exists by the legality test, and moving left cannot create a new right conflict. Thus an optimal placement can always include the greedy choice. Repeating the exchange after each placement proves the scan achieves maximum capacity.

#### Complexity detail

For `m` plots, the index only moves forward and examines each plot a constant number of times, taking $O(m)$ time. The algorithm stores only an index and placement count, so extra space is $O(1)$.

#### Alternatives and edge cases

- **Count zero runs:** derive each empty segment's capacity with special formulas for boundaries; this is also $O(m)$ but has more cases.
- **Mutate a copied bed:** writing each greedy flower makes neighbor checks straightforward but uses $O(m)$ copy space.
- **Revalidate the whole bed after each tentative flower:** is correct but repeats scans and can take $O(m^2)$ time.
- **Backtracking all placements:** is exponential and unnecessary because the earliest legal choice is safe.
- **$n = 0$:** always returns true.
- **Single empty plot:** can hold one flower.
- **Single occupied plot:** cannot hold another flower.
- **Empty boundary plot:** has only one real neighbor.
- **Long zero run:** alternating placements maximize capacity.
- **Existing flowers:** are guaranteed legal but still block their adjacent plots.

</details>
