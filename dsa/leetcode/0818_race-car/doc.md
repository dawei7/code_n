# Race Car

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 818 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/race-car/) |

## Problem Description

### Goal

A car moves along an unbounded number line. It begins at position `0` with speed `1` and accepts a sequence made from two instructions. `A` accelerates: the car first moves by its current signed speed, then doubles that speed. `R` reverses without changing position: a positive speed becomes `-1`, and a negative speed becomes `1`.

Given a positive target position, determine the minimum number of instructions required to land on it exactly. The car may pass the target, travel through negative positions, and reverse more than once; only the final position and instruction count matter.

### Function Contract

**Inputs**

- `target`: a positive destination position.

**Return value**

- The minimum number of accelerate/reverse instructions needed to reach `target` exactly.

### Examples

**Example 1**

- Input: `target = 3`
- Output: `2`
- Explanation: Two accelerations visit positions `1` and `3`.

**Example 2**

- Input: `target = 6`
- Output: `5`
- Explanation: `AAARA` reaches `7`, reverses, then accelerates back to `6`.

**Example 3**

- Input: `target = 4`
- Output: `5`
- Explanation: `AARRA` reaches `3`, turns twice to face forward again, and advances to `4`.

### Required Complexity

- **Time:** $O(T \log T)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Use distances because reversal restores a unit speed**

Let `dp[t]` be the minimum instructions needed to cover positive distance `t` starting from speed `1`. Reversing after a block of accelerations resets the speed magnitude to `1`, so the unresolved gap is another instance of the same distance problem, possibly viewed in the opposite direction.

After `n` consecutive accelerations, the car travels $2^{n} - 1$. For a distance `t`, choose $n = \operatorname{bit\_length}(t)$, making $2^{(n-1)} - 1 < t \le 2^{n} - 1$.

**Handle an exact power-of-two-minus-one destination**

If $t = 2^{n} - 1$, exactly `n` accelerations reach it. No shorter program can travel that far because fewer accelerations have total forward reach below `t`, so `dp[t] = n`.

**Compare overshooting with turning short of the target**

One choice is to accelerate `n` times past the target, reverse once, and solve the gap $2^{n} - 1 - t$. Its cost is

`n + 1 + dp[2 ** n - 1 - t]`.

The other choice accelerates $n - 1$ times to $2^{(n-1)} - 1$, reverses, accelerates backward `m` times for any $0 \le m < n - 1$, then reverses again. The backward block travels $2^{m} - 1$, leaving positive distance

$t - (2^{(n-1)} - 1) + (2^{m} - 1)$.

That candidate costs

`(n - 1) + 1 + m + 1 + dp[remaining]`.

Every remaining distance in these transitions is smaller than `t`, so compute `dp` from `1` upward. An optimal program's first useful turn either follows the first acceleration block that reaches/passes `t`, giving the overshoot case, or occurs at the last full acceleration position below `t`; before turning forward again, it may make any shorter backward acceleration block, giving one of the undershoot cases. Taking the minimum therefore covers an optimal first maneuver, and the already optimal `dp` value completes its remaining gap.

#### Complexity detail

For each distance through `T = target`, the algorithm considers at most $O(\log T)$ backward acceleration counts. This gives $O(T \log T)$ time. The table stores $T + 1$ integers, using $O(T)$ space.

#### Alternatives and edge cases

- **Top-down memoization:** The same recurrence can evaluate only requested subdistances; it has comparable bounds but uses recursion and a hash-backed cache.
- **Breadth-first search over position and speed:** BFS directly finds the shortest instruction count, but bounding positions and speeds safely is less transparent and can maintain many more states.
- **Unmemoized recurrence:** Recomputing the same remaining distances is correct but grows exponentially across nested overshoot and undershoot choices.
- **Target `1`:** One acceleration reaches it.
- **Target $2^{k} - 1$:** The answer is exactly `k`, with no reversal.
- **Overshoot can be optimal:** For target `6`, reaching `7` and coming back beats stopping short and maneuvering forward.
- **Two reversals may be optimal:** Reversing early, backing up, and reversing again can create a shorter final forward gap.

</details>
