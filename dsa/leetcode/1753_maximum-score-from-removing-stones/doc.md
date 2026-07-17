# Maximum Score From Removing Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1753 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-from-removing-stones/) |

## Problem Description

### Goal

You are playing a solitaire game with exactly three nonempty piles containing `a`, `b`, and `c` stones. On each turn, choose two different piles that are both nonempty, remove one stone from each chosen pile, and increase the score by one.

The game ends when fewer than two piles remain nonempty, because no legal pair can then be chosen. Decide how to choose the piles on every turn so that the final score is as large as possible, and return that maximum score.

### Function Contract

**Inputs**

- `a`, `b`, and `c`: the three initial pile sizes, each satisfying $1 \le a,b,c \le 10^5$.

Let $S=a+b+c$ and $M=\max(a,b,c)$.

**Return value**

- Return the maximum number of turns, equivalently the maximum score, obtainable before fewer than two piles are nonempty.

### Examples

**Example 1**

- Input: `a = 2, b = 4, c = 6`
- Output: `6`
- Explanation: All twelve stones can be consumed in six cross-pile pairs.

**Example 2**

- Input: `a = 4, b = 4, c = 6`
- Output: `7`
- Explanation: The fourteen stones can be paired completely across seven turns.

**Example 3**

- Input: `a = 1, b = 8, c = 8`
- Output: `8`
- Explanation: Pair the two size-eight piles until both are empty; the remaining single stone cannot form another move.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Bound the score by total stone supply**

Every point consumes exactly two stones, so $S$ stones can support at most $\lfloor S/2\rfloor$ moves. This limit is decisive when the piles are balanced enough to keep forming cross-pile pairs until at most one stone remains.

**Bound the score by stones outside the largest pile**

No move can take two stones from the same pile. Consequently, every move that consumes a stone from the largest pile needs a partner outside it, and moves between the two smaller piles consume that outside supply even faster. The score can never exceed $S-M$, the total number of stones outside the largest pile.

**Take the smaller bound**

If $M>S-M$, pair every outside stone with the largest pile and attain exactly $S-M$ moves before only the largest pile remains. Otherwise, the largest pile does not dominate the combined remainder; repeatedly pairing two currently nonempty piles can consume all stones except possibly one and attain $\lfloor S/2\rfloor$. Both upper bounds are therefore tight, so the answer is

$$
\min\left(\left\lfloor\frac{S}{2}\right\rfloor,\ S-M\right).
$$

#### Complexity detail

Computing one sum, one maximum, and the minimum of two arithmetic bounds takes $O(1)$ time. Only a fixed number of integer values is stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Max-heap simulation:** Repeatedly remove from the two largest nonempty piles. This greedy process is correct, but takes time proportional to the returned score instead of constant time.
- **Case analysis after sorting:** Sorting three values and comparing the largest with the other two derives the same formula; sorting a fixed three-element collection is still $O(1)$.
- **Dominant pile:** When one pile exceeds the sum of the other two, unused stones necessarily remain in that pile.
- **Balanced piles:** If the largest pile is no larger than the combined remainder, all but at most one stone can be consumed.
- **Odd total:** The total-stone bound rounds down because each move consumes two stones.
- **Equal piles:** The result is determined by $\lfloor S/2\rfloor$.
- **Permutation symmetry:** Reordering `a`, `b`, and `c` cannot change the answer.
- **Maximum pile value:** Arithmetic must comfortably represent totals up to $3\cdot10^5$.

</details>
