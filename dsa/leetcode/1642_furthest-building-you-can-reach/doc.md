# Furthest Building You Can Reach

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1642 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/furthest-building-you-can-reach/) |

## Problem Description
### Goal
An array `heights` gives the heights of consecutive buildings. Starting at building 0, move from each building `i` to `i + 1` while using a limited supply of bricks and ladders.

Moving to an equal or lower building costs nothing. For a positive climb of `heights[i + 1] - heights[i]`, either spend exactly that many bricks or use one ladder. Return the largest 0-indexed building position reachable when the resources are assigned optimally.

### Function Contract
**Inputs**

- `heights`: an integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{heights[i]} \le 10^6$.
- `bricks`: the available brick count, where $0 \le \texttt{bricks} \le 10^9$.
- `ladders`: the available ladder count, where $0 \le \texttt{ladders} \le n$.

**Return value**

Return the furthest building index reachable by moving only to the next building and assigning bricks or ladders to every positive climb.

### Examples
**Example 1**

- Input: `heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1`
- Output: `4`

Spending five bricks on the climb from 2 to 7 and the ladder on the climb from 6 to 9 reaches building 4, but the later climb cannot be paid.

**Example 2**

- Input: `heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2`
- Output: `7`

**Example 3**

- Input: `heights = [14,3,19,3], bricks = 17, ladders = 0`
- Output: `3`

The only positive climb costs 16 bricks.

### Required Complexity
- **Time:** $O(n\log(\ell+1))$
- **Space:** $O(\ell)$

<details>
<summary>Approach</summary>

#### General

**Reserve ladders for the most expensive climbs seen so far.** While scanning left to right, place every positive climb into a min-heap. Interpret the heap as the climbs currently assigned ladders. If its size exceeds the available ladder count $\ell$, remove the smallest climb and pay that one with bricks instead.

**Exchange smaller ladder assignments for larger climbs.** Suppose a ladder covers climb $x$ while bricks cover a larger climb $y$. Swapping the resources saves $y-x\ge0$ bricks without using another ladder, so among any traversed prefix there is always an optimal assignment in which ladders cover its largest positive climbs. The min-heap maintains exactly that assignment online: a newly encountered large climb displaces the cheapest ladder-covered climb, while a small climb is immediately popped and paid with bricks.

After each required brick payment, a negative brick balance means the transition at the current index cannot be crossed. The maintained assignment already minimizes bricks over the entire prefix, so no different past choice can succeed; return the current building index. If every transition is processed, return the final index.

#### Complexity detail

Each of the at most $n-1$ climbs is pushed once and at most one climb is popped per transition. The heap retains at most $\ell$ ladder-covered climbs; using $\log(\ell+1)$ keeps the zero-ladder case well defined. Total time is $O(n\log(\ell+1))$, and the heap uses $O(\ell)$ space.

#### Alternatives and edge cases

- **Spend bricks first, then replace the largest paid climb:** A max-heap of brick-paid climbs can restore bricks whenever a ladder is needed. It is also greedy but may retain more than $\ell$ entries unless managed carefully.
- **Binary search the answer:** Test whether a prefix is reachable by sorting its positive climbs and assigning ladders to the largest. This repeats work and typically takes $O(n\log^2 n)$ time.
- **Sorted ladder list:** Maintaining ladder climbs in a Python list gives the same choices, but insertion shifts can make the implementation quadratic when $ell$ grows with $n$.
- A single building is always reachable at index 0.
- Equal-height and downward transitions consume no resource and must not enter the heap.
- With zero ladders, every positive climb is paid immediately with bricks.
- With enough ladders for all positive climbs, bricks are irrelevant.
- A climb costing exactly the remaining bricks is affordable; failure occurs only after the balance becomes negative.

</details>
