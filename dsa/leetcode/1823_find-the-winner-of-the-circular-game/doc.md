# Find the Winner of the Circular Game

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) |
| Frontend ID | 1823 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Recursion, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

There are `n` friends numbered from 1 through `n` clockwise around a circle. Moving clockwise after friend `n` returns to friend 1. The game begins at friend 1.

Count `k` friends clockwise, including the friend where the count starts; wrapping may visit friends more than once when `k` exceeds the current circle size. The `k`th counted friend leaves. If multiple friends remain, resume counting at the friend immediately clockwise of the one removed. Repeat until one friend remains, and return that winner's label.

### Function Contract

**Inputs**

- `n`: the number of friends, with $1 \le n \le 500$.
- `k`: the number counted in every round, with $1 \le k \le n$.

**Return value**

- Return the surviving friend's 1-based label.

### Examples

**Example 1**

- Input: `n = 5, k = 2`
- Output: `3`

Friends leave in the order 2, 4, 1, and 5, leaving friend 3.

**Example 2**

- Input: `n = 6, k = 5`
- Output: `1`

The elimination order is 5, 4, 6, 2, and 3.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Express the smaller game in zero-based positions**

With one friend, the survivor occupies position 0. Suppose `winner` is the zero-based survivor position for a circle of size `size - 1` after one removal. In the preceding `size`-friend circle, counting removes position `(k - 1) % size`, and the next position becomes the smaller circle's position 0.

**Undo one elimination**

Mapping a smaller-circle position back to the preceding circle shifts it forward by `k` positions modulo `size`. Therefore update `winner = (winner + k) % size` for sizes 2 through `n`. After rebuilding the full circle, add 1 to convert the zero-based position to the friends' labels.

**Why the recurrence preserves the winner**

After each elimination, relabeling the next friend as zero produces exactly the same game rules on one fewer friend. The recurrence reverses that relabeling: shifting by `k` skips the removed position and restores every surviving position to its location before the round. Starting from the certain one-person survivor and undoing all rounds consequently identifies the original winner.

#### Complexity detail

The loop performs one constant-time modular update for each size from 2 through $n$, so time is $O(n)$. Only `winner` and the loop size are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Queue rotation:** Rotating `k - 1` friends and removing the front directly models the rules, but counting each step can take $O(nk)$ time and the queue uses $O(n)$ space.
- **List deletion:** Computing each removal index avoids individual rotations, but deletion shifts later elements and can take $O(n^2)$ time.
- **Recursive Josephus formula:** It matches the same recurrence, but the iterative form avoids $O(n)$ call-stack space.
- **One friend:** No round occurs, so the zero-based survivor 0 converts to label 1.
- **`k = 1`:** The current starting friend leaves each round, so friend `n` wins.
- **`k` equal to `n`:** Later rounds still use the same fixed `k`, with modulo handling repeated wraps.
- **One-based labels:** Apply the `+1` conversion only after all zero-based recurrence steps.

</details>
