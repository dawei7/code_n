# Minimum Moves to Pick K Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3086 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-moves-to-pick-k-ones](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/) |

## Problem Description

### Goal

You are given a binary array `nums` of length $n$, a positive integer `k`, and a non-negative integer `maxChanges`. Alice chooses one fixed index `aliceIndex` and remains there for the entire game. If `nums[aliceIndex]` is initially `1`, she picks up that one immediately, changes the entry to `0`, and spends no move.

Alice may then make either kind of move any number of times. She may choose an index `j` different from `aliceIndex` whose value is `0` and change it to `1`; across the game, this action may be used at most `maxChanges` times. Alternatively, she may swap adjacent entries `nums[x] = 1` and `nums[y] = 0`. When the destination `y` is `aliceIndex`, Alice picks up the arriving one and the value at her position becomes `0` again.

Determine the minimum number of moves needed for Alice to pick up exactly `k` ones. The guarantee `maxChanges + sum(nums) >= k` ensures that this is possible.

### Function Contract

**Inputs**

- `nums`: A binary list of length $n$, where $2 \le n \le 10^5$.
- `k`: The exact number of ones Alice must pick up, where $1 \le k \le 10^5$.
- `maxChanges`: The maximum number of allowed zero-to-one actions, where $0 \le \texttt{maxChanges} \le 10^5$.

The input satisfies `maxChanges + sum(nums) >= k`. Alice's chosen position is not an input; the algorithm may optimize over every possible `aliceIndex`.

**Return value**

- The minimum number of moves required to pick up exactly `k` ones.

### Examples

#### Example 1

- **Input:** `nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1`
- **Output:** `3`
- **Explanation:** Alice can stand at index `1` and take its one for free. She creates a one at index `2` and swaps it left, then swaps the original one at index `0` right. The creation and two swaps use three moves.

#### Example 2

- **Input:** `nums = [0,0,0,0], k = 2, maxChanges = 3`
- **Output:** `4`
- **Explanation:** Alice can repeatedly create a one next to her position and swap it onto her position. Each pickup requires one creation and one swap, so two pickups cost four moves.
