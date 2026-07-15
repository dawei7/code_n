# Dice Roll Simulation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1223 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/dice-roll-simulation/) |

## Problem Description

### Goal

A die simulator produces a sequence of `n` rolls, each with a value from `1` through `6`. The six-element array `rollMax` limits consecutive repetitions: face $i+1$ may appear at most `rollMax[i]` times in a row.

Return the number of distinct roll sequences that satisfy every face's consecutive-occurrence limit. Because the count can be large, return it modulo $M=10^9+7$.

### Function Contract

**Inputs**

- `n`: The number of rolls in a sequence, where $1\le n\le5000$.
- `roll_max`: Six consecutive-run limits corresponding to faces `1` through `6`; each value lies from `1` through `15`. This is the app-local form of LeetCode's `rollMax` parameter.

Define the total number of run-length states as

$$
R=\sum_{f=0}^{5}\texttt{roll\_max[f]}.
$$

**Return value**

- The number of valid length-`n` roll sequences, reduced modulo $M$.

### Examples

**Example 1**

- Input: `n = 2`, `roll_max = [1,1,2,2,2,3]`
- Output: `34`

Of the `36` two-roll sequences, `11` and `22` violate their limits.

**Example 2**

- Input: `n = 2`, `roll_max = [1,1,1,1,1,1]`
- Output: `30`

The second roll must differ from the first, giving `6 * 5` choices.

**Example 3**

- Input: `n = 3`, `roll_max = [1,1,1,2,2,3]`
- Output: `181`

### Required Complexity

- **Time:** $O(nR)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Retain both the final face and its run length.** A partial sequence's legal next rolls depend only on which face appears last and how many consecutive times it currently appears. Store a count for every permitted `(face, run_length)` state. At length one, each face has one sequence with run length one.

**Separate face changes from run extensions.** For each new roll position, first total the states ending in every face and the total across all faces. A new run of face `f` with length one can follow any sequence not ending in `f`, so its count is the all-face total minus face `f`'s total. Existing runs of `f` shift from length `r` to `r + 1` only while `r` is below `roll_max[f]`.

**Why the transitions form a partition.** Every valid longer sequence either changes face on its final roll, uniquely placing it in a new length-one state, or repeats its final face, uniquely extending the previous run by one. The limit check rejects exactly the forbidden extensions. Conversely, every constructed state respects its face's bound and inherits validity from its prefix. Induction over sequence length therefore makes the final sum count every valid sequence exactly once.

#### Complexity detail

Each roll position totals and advances the $R$ states once, giving $O(nR)$ time. Only the current and next collections of $R$ states are retained, so auxiliary space is $O(R)$. All additions and subtractions are reduced modulo $M$.

#### Alternatives and edge cases

- **Enumerate complete roll sequences:** Recursive generation is direct but explores exponentially many valid prefixes.
- **Recompute every prefix length independently:** It produces correct counts but repeats all earlier transitions and takes $O(n^2R)$ time.
- **Three-dimensional table by length, face, and run:** This mirrors the recurrence but stores $O(nR)$ values when only the preceding length is needed.
- **One roll:** Every face is legal regardless of its positive limit, so the answer is `6`.
- **All limits equal one:** Adjacent rolls must differ, yielding $6\cdot5^{n-1}$ sequences before modular reduction.
- **Large limits:** When every limit is at least `n`, all $6^n$ sequences are valid.
- **Simultaneous layer update:** New states must not feed other transitions at the same sequence length.

</details>
