# Happy Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 202 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/happy-number/) |

## Problem Description
### Goal
Starting with a positive integer `n`, repeatedly replace the current value by the sum of the squares of its decimal digits. For example, each occurrence of a digit contributes independently, and the process continues using the digits of the newly produced value.

Return `True` if this sequence eventually reaches `1`, after which it remains there. Return `False` if the process instead repeats a previous non-one value and enters a cycle that can never reach `1`. The task asks only for this classification, not for the sequence itself or the number of transformations performed.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

`True` when the sequence reaches one; otherwise `False` when it enters a non-one cycle.

### Examples
**Example 1**

- Input: `19`
- Output: `True`

**Example 2**

- Input: `2`
- Output: `False`

**Example 3**

- Input: `1`
- Output: `True`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Define `next(x)` as the sum of the squares of `x`'s decimal digits. Repeatedly applying this deterministic function creates a sequence. The sequence either reaches `1`, which maps to itself forever, or enters a different cycle and can never reach one afterward.

Why must a cycle eventually occur? A number with `d` digits maps to at most `81d`. For sufficiently large numbers this is much smaller than the original value, so repeated transitions enter a bounded finite set. A deterministic sequence inside a finite set must revisit a value.

Use Floyd's cycle detection without storing the visited values. Move `slow` through one `next` transition per iteration and `fast` through two. Once both pointers enter the eventual cycle, the faster pointer gains one cycle position per iteration and must meet the slower pointer.

For `19`, the sequence is `19 -> 82 -> 68 -> 100 -> 1`, so both pointers ultimately meet at the self-loop `1`. For an unhappy number such as `2`, the pointers meet in the non-one cycle containing `4`; the exact meeting point need not be the first cycle value.

The digit-square sequence is eventually cyclic because it becomes bounded. Floyd's algorithm therefore terminates at some value in that eventual cycle. If the sequence is happy, its eventual cycle is the self-loop at `1`, so the meeting value is one. If the meeting value is one, the original sequence reaches one and is happy. Any meeting at another value proves the sequence is trapped in a non-one cycle and is unhappy. Thus testing the meeting value classifies the input exactly.

#### Complexity detail

Computing the first transition examines $O(\log n)$ decimal digits. Subsequent values are bounded by `81` times the digit count and quickly enter a small finite state space; under the standard fixed-width integer model, total time is $O(\log n)$ and the two pointers use $O(1)$ space.

#### Alternatives and edge cases

- A visited set is simpler to explain and detects the first repeated value, but uses additional storage.
- An arbitrary iteration limit has no correctness guarantee unless derived from the bounded state space.
- Recursive evaluation still needs a cycle detector and can consume unbounded call stack without one.
- `1` is immediately happy. Powers of ten transition directly to one.
- Values entering the well-known non-one cycle containing `4` are unhappy.

</details>
