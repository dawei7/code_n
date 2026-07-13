# Burst Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 312 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/burst-balloons/) |

## Problem Description
### Goal
Given a row of balloons with nonnegative values, burst every balloon in an order of your choice. When balloon `i` is burst, it awards the product of its own value and the values of its nearest still-unburst neighbors at that moment.

Treat a missing neighbor beyond either end as a virtual balloon of value `1`; virtual balloons cannot be burst. After a real balloon disappears, its surviving neighbors become adjacent for later rewards. Return the maximum total coins obtainable after all balloons are removed. The original adjacent values alone do not determine every reward because the chosen burst order changes future neighborhoods.

### Function Contract
**Inputs**

- `nums`: a nonempty list of nonnegative balloon values

**Return value**

The maximum total coins obtainable after every balloon is burst. Missing neighbors beyond either array edge have value one.

### Examples
**Example 1**

- Input: `nums = [3,1,5,8]`
- Output: `167`

**Example 2**

- Input: `nums = [7,1]`
- Output: `14`

**Example 3**

- Input: `nums = [10,2]`
- Output: `30`

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Choose the last balloon, not the first**

Choosing the first balloon in an interval changes which values become adjacent, so the two resulting sides remain coupled. Choosing the balloon burst last has the opposite property: at that final moment, every balloon inside the interval except that one is already gone, and its neighbors are the interval's fixed boundary balloons.

Pad the values with a virtual one at each end. Let `dp[left][right]` be the best coins obtainable by bursting every balloon strictly between boundary indices `left` and `right`. If `last` is the final balloon in that open interval, its final contribution is
`values[left] * values[last] * values[right]`.

**The last choice separates two independent intervals**

Before `last` is burst, all balloons between `left` and `last` and all balloons between `last` and `right` must already be gone. Their optimal rewards are `dp[left][last]` and `dp[last][right]`, and the boundaries ensure those subproblems do not affect each other.

Therefore:
`dp[left][right] = max(dp[left][last] + boundary_product + dp[last][right])`
over every interior `last`. Fill intervals from short to long so both smaller subintervals are ready.

For `[3,1,5,8]`, bursting value `1` first earns $3 \cdot 1 \cdot 5 = 15$, then value `5` earns $3 \cdot 5 \cdot 8 = 120$, value `3` earns $1 \cdot 3 \cdot 8 = 24$, and the final value `8` earns `8`, totaling `167`. The fixed-boundary recurrence accounts for exactly these changing neighbors.

**Every burst order has one unique final split**

Any complete order for an interval has exactly one last balloon. Removing that final action partitions all earlier actions into the left and right open intervals. Since actions on opposite sides never cross the retained last balloon, replacing either side by its optimal suborder cannot reduce the total. Thus the recurrence considers an option at least as good as every possible order.

Conversely, combining optimal left and right suborders followed by the selected last burst is a legal order whose reward equals the recurrence candidate. Maximizing these exact constructions proves every DP entry, including the full padded interval, optimal.

#### Complexity detail

There are $O(n^2)$ open intervals and each tries $O(n)$ possible final balloons, giving $O(n^3)$ time. The interval table contains $O(n^2)$ values. Padding and loop variables are lower-order space.

#### Alternatives and edge cases

- **Enumerate every burst order:** explores up to $n!$ permutations.
- **Greedily burst the largest immediate product:** ignores how the burst changes future adjacency and is not reliable.
- A single balloon earns its value because both virtual neighbors are one. Zero-valued balloons contribute no coins directly but can still change adjacency until removed.

</details>
