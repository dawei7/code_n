# Largest Rectangle in Histogram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 84 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

## Problem Description
### Goal
The array `heights` describes adjacent histogram bars, each with unit width and a nonnegative height. Choose one contiguous span of bars and place an axis-aligned rectangle on the common baseline entirely beneath that span.

The rectangle's width is the number of selected bars, and its height cannot exceed the shortest selected bar. Return the greatest possible area over every span and allowable height. Zero-height bars may split useful regions, and a rectangle may consist of a single bar.

### Function Contract
**Inputs**

- `heights`: a nonempty list of nonnegative bar heights

**Return value**

The maximum rectangular area as an integer.

### Examples
**Example 1**

- Input: `heights = [2,1,5,6,2,3]`
- Output: `10`

**Example 2**

- Input: `heights = [2,4]`
- Output: `4`

**Example 3**

- Input: `heights = [0]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**A stack entry remembers height and its earliest legal start**

Store pairs `(start, height)` in a monotonic nondecreasing stack. For an entry, every bar from `start` through the current processed suffix is at least `height`, so `start` is the earliest index where a rectangle of that height can begin.

Increasing heights remain unresolved because a future bar may let them extend farther. A shorter current bar is the event that proves which taller candidates can no longer continue.

**Pop exactly when a right boundary becomes known**

Set `start` to the current index. While the stack top height exceeds the current height, pop `(previous_start, previous_height)` and compute area `previous_height * (index - previous_start)`. The current bar is the first shorter bar on the right, so this width is final.

Assign `start = previous_start` after each pop. The current shorter height can extend across every bar that supported the popped taller rectangle, so it inherits the earliest popped start before being pushed. A final zero-height sentinel supplies a shorter right boundary for every remaining positive candidate.

**Nondecreasing heights encode unresolved left boundaries**

Stack heights are nondecreasing, and each pair's start is the earliest position since which all bars are at least that height. Entries below a popped item are shorter and remain valid across more positions. A popped height cannot cross the current shorter bar, while its stored start proves it cannot extend farther left, so its computed span is maximal for that limiting height.

**Trace several pops at one right boundary**

For `[2,1,5,6,2,3]`, height 1 pops 2 and inherits start 0. Later height 2 pops 6 and 5; height 5 spans indices 2 and 3, producing area 10. The sentinel finalizes remaining spans.

**A popped height has just discovered its widest span**

A stack entry stores a height and the earliest index from which every bar has been at least that tall. The height remains pending while later bars can extend its rectangle. The first strictly shorter bar ends that possibility, so popping evaluates the exact widest span using that height as the limiting bar.

Every maximal histogram rectangle has some limiting height and is finalized at its first shorter boundary or the sentinel. Conversely, each popped span contains only bars at least as tall as its stored height. Thus every candidate area is valid and every optimum is considered.

#### Complexity detail

Each bar is pushed once and popped once, yielding $O(n)$ time. The stack holds at most `n` pairs, using $O(n)$ space.

#### Alternatives and edge cases

- **Expand left and right from every bar:** can take $O(n^2)$ time.
- **Test every interval minimum:** takes at least quadratic time without additional range structures.
- **Divide and conquer:** can be efficient with range-minimum support but is more complex than the direct monotonic stack.
- Zero-height bars naturally flush positive candidates and contribute zero area. Equal heights may remain as separate nondecreasing entries or be coalesced if earliest starts are preserved.
- The sentinel is conceptual and should not alter the caller's input unless mutation is explicitly intended.

</details>
