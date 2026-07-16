# Most Visited Sector in a Circular Track

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1560 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/) |

## Problem Description
### Goal

A circular track contains `n` sectors labeled from `1` through `n`. Movement follows increasing labels, wrapping from sector `n` back to sector `1`. A marathon consists of $m$ rounds: round $i$ starts at `rounds[i - 1]` and finishes at `rounds[i]`.

Count a sector whenever the runner visits it, including the initial sector and every round endpoint. Return all sectors tied for the greatest visit count, sorted in ascending numeric order.

### Function Contract
**Inputs**

- `n`: The number of sectors, where $2 \le n \le 100$.
- `rounds`: A list of $m+1$ checkpoints, where $1 \le m \le 100$ and every checkpoint lies in $[1,n]$.
- Consecutive checkpoints are distinct, and travel between them always follows increasing sector labels with wraparound.

**Return value**

Return the most frequently visited sector labels in strictly increasing order.

### Examples
**Example 1**

- Input: `n = 4, rounds = [1,3,1,2]`
- Output: `[1,2]`

**Example 2**

- Input: `n = 2, rounds = [2,1,2,1,2,1,2,1,2]`
- Output: `[2]`

**Example 3**

- Input: `n = 7, rounds = [1,3,5,7]`
- Output: `[1,2,3,4,5,6,7]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Cancel complete laps**

Concatenate all rounds into one continuous clockwise walk beginning at `rounds[0]` and ending at `rounds[-1]`. Every complete lap visits each sector exactly once, so complete laps add the same amount to every visit count and cannot affect which sectors are maximal.

After removing those equal contributions, only the final partial lap remains. Its sectors form the inclusive clockwise arc from the starting checkpoint to the final checkpoint. Every sector on this arc has exactly one more visit than every sector outside it, so this arc is precisely the answer. Intermediate round endpoints merely divide the same walk into rounds; they do not change the resulting comparison.

**Emit the arc in numeric order**

If the start label is at most the end label, the arc is the ordinary interval `start..end`. If the walk wraps, the arc consists of `start..n` and `1..end`; because the answer must be sorted, emit `1..end` first and then `start..n`.

The case `start == end` can occur after multiple rounds even though adjacent checkpoints differ. Then the walk contains an integer number of complete laps, and the initially visited start sector has the sole extra visit, so the formula correctly returns only that sector.

#### Complexity detail

The algorithm reads the first and last checkpoints and creates at most $n$ output labels, taking $O(n)$ time in the worst case. Apart from the returned list, it uses only the two endpoint values, so auxiliary space is $O(1)$.

The benchmark scales legal sector and round counts together. Descending checkpoints make direct visit-by-visit simulation traverse almost a complete lap per round, exposing its quadratic work while the endpoint method remains output-bounded.

#### Alternatives and edge cases

- **Direct simulation:** increment a counter for every visited sector across every round, then select the maximum. It is straightforward but can perform $O(mn)$ work.
- **Difference-array counting:** encode each clockwise round as one or two circular ranges and prefix-sum the counts. This improves simulation to $O(m+n)$ but is still more machinery than the endpoint invariant requires.
- **Wraparound arc:** when `start > end`, numeric output order differs from travel order, so sectors `1..end` must appear before `start..n`.
- **No wraparound:** when `start < end`, every label in the closed interval is tied for most visited.
- **Same overall endpoint:** equal first and last checkpoints return one sector, despite the intervening completed laps.
- **All sectors tied:** an arc from `1` to `n` returns every sector.
- **Intermediate checkpoints:** changing them without changing the first and last checkpoint cannot change the answer.

</details>
