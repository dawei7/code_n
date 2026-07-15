# Boats to Save People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 881 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/boats-to-save-people/) |

## Problem Description
### Goal
Each entry `people[i]` is one person's weight. There is an unlimited supply of boats, every boat has maximum total weight `limit`, and no boat may carry more than two people at once. Two people can share only when their combined weight is at most the limit.

Find the minimum number of boats required to carry every person. Each person must be assigned to exactly one boat, and every individual weight is guaranteed not to exceed `limit`.

### Function Contract
**Inputs**

- `people`: an array of $n$ weights, where $1 \leq n \leq 5\cdot10^4$ and $1 \leq \texttt{people[i]} \leq \texttt{limit}$.
- `limit`: the capacity of each boat, where $1 \leq \texttt{limit} \leq 3\cdot10^4$.

**Return value**

Return the minimum number of capacity-respecting boats needed when each boat carries at most two people.

### Examples
**Example 1**

- Input: `people = [1,2], limit = 3`
- Output: `1`

Both people fit together.

**Example 2**

- Input: `people = [3,2,2,1], limit = 3`
- Output: `3`

One possible assignment is `(1,2)`, `(2)`, and `(3)`.

**Example 3**

- Input: `people = [3,5,3,4], limit = 5`
- Output: `4`

No two weights can share a boat.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Make the heaviest remaining person the next obligation**

Sort a copy of the weights. Keep `light` at the smallest unassigned person and `heavy` at the largest. The person at `heavy` must occupy the next boat under every possible solution, so assign that boat immediately.

If `people[light] + people[heavy] <= limit`, place the lightest person in the same boat and advance `light`. Otherwise, the heaviest person cannot share with anyone: every other remaining weight is at least the lightest. In either case, move `heavy` left and add one boat.

**The greedy pairing cannot increase the optimum**

When the lightest person fits with the heaviest, consider any optimal assignment. If those two are not together, the heaviest is alone or paired with someone no lighter. Moving the lightest into the heaviest's boat remains feasible, and the displaced partner can take the lightest's former place or remain alone without using more boats. Thus an optimal assignment exists with the greedy pair. If the lightest does not fit, no partner can fit, so sending the heaviest alone is forced. Repeating these safe choices yields a minimum boat count.

#### Complexity detail

Sorting $n$ weights costs $O(n\log n)$ time, and the two pointers each move across the array once in $O(n)$ additional time. Keeping a sorted copy avoids mutating the input and requires $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Repeatedly scan the unsorted people:** Finding the heaviest person and a feasible partner each time is correct but can take $O(n^2)$ time.
- **Pair adjacent sorted weights:** Two heavy adjacent people may exceed the limit even though each can pair with a lighter person.
- **First-fit boat packing:** Generic bin-packing heuristics add unnecessary state; the at-most-two-person rule makes the endpoint greedy exact.
- **Single person:** Exactly one boat is required.
- **Exact capacity:** A pair whose weights sum to `limit` can share.
- **Heaviest cannot pair with lightest:** The heaviest must travel alone.
- **Repeated weights:** The pointer argument depends only on sorted order, not on distinct values.
- **Input preservation:** Sorting a copy keeps the caller's `people` array unchanged; in-place sorting can reduce explicit allocation when mutation is acceptable.

</details>
