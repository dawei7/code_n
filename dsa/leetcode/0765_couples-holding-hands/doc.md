# Couples Holding Hands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 765 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Greedy, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/couples-holding-hands/) |

## Problem Description

### Goal

There are `n` couples seated in a row of `2n` seats, with seats grouped as adjacent pairs `(0, 1)`, `(2, 3)`, and so on. People `0` and `1` are a couple, people `2` and `3` are the next couple, following the same numbering rule.

In one move, swap the people in any two seats. Return the minimum number of swaps needed so that every couple occupies one adjacent seat pair. Couples may appear in any order after rearrangement; only sitting together matters.

### Function Contract

**Inputs**

- `row`: an even-length permutation of the people numbered from `0` through `len(row) - 1`.

**Return value**

- The minimum number of arbitrary two-person swaps that makes every adjacent seat pair a couple.

### Examples

**Example 1**

- Input: `row = [0,2,1,3]`
- Output: `1`
- Explanation: Swap people `2` and `1` so both seat pairs contain couples.

**Example 2**

- Input: `row = [3,2,0,1]`
- Output: `0`
- Explanation: Both couples already sit together, regardless of order within a pair.

**Example 3**

- Input: `row = [0,2,4,1,3,5]`
- Output: `2`
- Explanation: The three couples form one misplacement cycle, which requires two swaps.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Locate every partner in constant time**

Couple numbering makes the partner of person `x` equal to $x \oplus 1$: the operation changes only the final bit. Build a table from each person to their current seat, then inspect seat pairs from left to right.

**Repair a mismatched seat pair immediately**

For seats `first` and `first + 1`, let `person` occupy `first`. If the neighbor is not `person ^ 1`, find that partner through the position table and swap the partner into `first + 1`. Update both affected positions in the table and count one move. Never touch this completed seat pair again.

Any valid final seating must change a mismatched pair because its first person currently lacks their partner, so at least one future swap is unavoidable. The greedy swap uses exactly one move to finish that pair and exchanges only seats in the unprocessed suffix, leaving all earlier couples intact. It therefore meets the lower bound for the current pair without reducing the best achievable result for the suffix. Repeating this argument proves the total is minimum.

#### Complexity detail

Let `n` be the number of people. Building the position table and processing $n / 2$ seat pairs take $O(n)$ time. The copied seating and position table use $O(n)$ space.

#### Alternatives and edge cases

- **Union-find over couples:** Connect the two couple IDs present in each seat pair; a component of `k` couples needs $k - 1$ swaps, giving the same answer in near-linear time.
- **Graph cycle counting:** Seat pairs create a degree-two multigraph of couples, and each component contributes its vertices minus one.
- **Linear partner search after every mismatch:** The same greedy choice remains correct, but repeatedly scanning the suffix costs $O(n^2)$ time.
- **Couple already adjacent:** No swap is made, even if the higher-numbered partner sits first.
- **Single couple:** The answer is always zero.
- **One long misplacement cycle:** A component containing `k` couples requires exactly $k - 1$ swaps.
- **Input preservation:** Working on a copy avoids changing the caller's row while computing the count.

</details>
