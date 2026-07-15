# Stamping The Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 936 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Stack, Greedy, Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [stamping-the-sequence](https://leetcode.com/problems/stamping-the-sequence/) |

## Problem Description

### Goal

Given strings `stamp` and `target`, begin with a string `s` of length `target.length` containing only `?` characters. In one turn, place the entire `stamp` within the boundaries of `s` and overwrite the covered positions with the corresponding stamp characters. Later stamps may overwrite characters written by earlier turns.

Transform `s` into `target` using at most `10 * target.length` turns. Return the starting index of the stamp's leftmost character for every turn in execution order. Any sequence satisfying the limit and producing `target` is valid. If no such sequence exists, return an empty list.

### Function Contract

**Inputs**

- `stamp`: a non-empty lowercase string of length $m$.
- `target`: a lowercase string of length $n$, where $m \le n \le 1000$.

**Return value**

Return any list of at most $10n$ valid stamp starting indices that constructs `target` from `"?" * n`, or `[]` when construction is impossible.

### Examples

**Example 1**

- Input: `stamp = "abc", target = "ababc"`
- Output: `[0,2]`
- Explanation: `[1,0,2]` is another valid answer.

**Example 2**

- Input: `stamp = "abca", target = "aabcaca"`
- Output: `[3,0,1]`

### Required Complexity

- **Time:** $O(nm)$
- **Space:** $O(nm)$

<details>
<summary>Approach</summary>

#### General

**Solve the construction backward.** Forward stamping can overwrite useful characters, making local choices difficult. Instead, imagine erasing `target` back to question marks. A window can be erased once every character that still matters in it agrees with `stamp`; already erased positions impose no restriction. Reversing the successful erase indices gives a valid forward order.

**Represent each window's blockers.** For every start, separate covered target positions into `made`, where the target matches the corresponding stamp character, and `todo`, where it differs. A window with empty `todo` can be erased immediately. Mark each newly erased position once and place it in a queue.

**Propagate newly erased positions.** When position `p` leaves the queue, inspect only windows covering `p` and remove it from their `todo` sets. When a set becomes empty, record that window and enqueue its not-yet-erased `made` positions. Each window-position dependency is processed once. If all $n$ positions become erased, reverse the recorded windows; otherwise return `[]`. Every reverse erase was compatible when chosen, so the reversed forward sequence reconstructs the target.

#### Complexity detail

There are $n-m+1$ windows with $m$ covered positions each. Building and processing dependencies takes $O(nm)$ time and stores $O(nm)$ total memberships. The queue and erased markers add $O(n)$ space.

#### Alternatives and edge cases

- **Repeated full-window scans:** Repeatedly search every window for one that can be erased. This is correct but can take $O(n^2m)$ time when only one window becomes available per pass.
- **Forward backtracking:** Try and undo placements from the question-mark string; the branching factor is exponential.
- **Stamp equals target:** One move at index `0` suffices.
- **Overlapping stamps:** Overlap is permitted and often necessary.
- **Move limit:** Each window is recorded at most once, so the result has at most $n-m+1 \le 10n$ moves.

</details>
