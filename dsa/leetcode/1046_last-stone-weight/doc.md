# Last Stone Weight

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1046 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/last-stone-weight/) |

## Problem Description

### Goal

The array `stones` gives the weight of every stone in a game. On each turn, choose the two heaviest stones. Let their weights be $x$ and $y$, with $x \le y$, and smash them together.

If $x=y$, both stones are destroyed. If $x\ne y$, the stone weighing $x$ is destroyed and the other stone's weight becomes `y - x`. Continue until at most one stone remains. Return its weight, or return `0` when every stone has been destroyed.

### Function Contract

**Inputs**

- `stones`: the $N$ positive stone weights, where $1 \le N \le 30$ and $1 \le \texttt{stones[i]} \le 1000$.

**Return value**

- The weight of the only remaining stone after repeatedly smashing the two heaviest, or `0` if no stone remains.

### Examples

**Example 1**

- Input: `stones = [2,7,4,1,8,1]`
- Output: `1`
- Explanation: The successive heaviest pairs produce differences `1`, `2`, and `1`; an equal pair is then destroyed, leaving weight `1`.

**Example 2**

- Input: `stones = [1]`
- Output: `1`

### Required Complexity

- **Time:** $O(N \log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Represent a max-heap with negated weights:** Python's standard heap removes the smallest value. Insert every weight as its negative, so removing the smallest stored number retrieves the heaviest real stone. Heap construction takes linear time.

**Process exactly the required pair:** While at least two stones remain, pop twice. The heap property guarantees these are the current two heaviest weights. If they are equal, insert nothing because both are destroyed. Otherwise insert the negative of their positive difference, which represents the changed heavier stone.

**Preserve the game state:** Before each turn, the heap contains precisely one entry for every surviving stone. Popping removes the required pair, and the conditional insertion matches the two possible smash outcomes exactly, so the invariant holds after the turn. Each turn reduces the number of stones by at least one and must terminate. The remaining heap root is therefore the requested weight; an empty heap means the answer is zero.

#### Complexity detail

Heap construction costs $O(N)$. There are at most $N-1$ turns, each using a constant number of $O(\log N)$ heap operations, for $O(N \log N)$ time. The heap stores at most $N$ entries, so space is $O(N)$.

#### Alternatives and edge cases

- **Repeated linear maximum searches:** Scan a list to locate and remove the two heaviest stones on every turn. It is correct but takes $O(N^2)$ time.
- **Sort after every smash:** Reordering all survivors each turn is also correct but costs $O(N^2 \log N)$ in the straightforward implementation.
- **Balanced ordered multiset:** Removing maxima and inserting differences gives $O(N \log N)$ time, but Python has no built-in ordered multiset.
- **Single stone:** No turn is played, so its original weight is returned.
- **Equal heaviest stones:** Both disappear and no zero-weight stone is inserted.
- **All stones destroyed:** An empty heap produces `0`.
- **Repeated weights:** Duplicate heap entries represent distinct stones and must be preserved until selected.

</details>
