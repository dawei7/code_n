# Jump Game VII

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/jump-game-vii/) |
| Frontend ID | 1871 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You begin at index `0` of a zero-indexed binary string `s`; this starting character is guaranteed to be `"0"`. From a reachable index `i`, a forward jump may land at index `j` only when the jump length is between `minJump` and `maxJump`, inclusive, and `s[j]` is also `"0"`.

Determine whether some sequence of valid jumps reaches the final index. Jumps cannot move backward or land on a `"1"`. It is not necessary to use either boundary length on every move: each jump may independently choose any integer distance in the permitted interval.

### Function Contract

**Inputs**

- `s`: a binary string of length $N$, where $2 \le N \le 10^5$ and `s[0] == "0"`.
- `minJump`: the minimum permitted jump length.
- `maxJump`: the maximum permitted jump length, with $1 \le \texttt{minJump} \le \texttt{maxJump} < N$.

**Return value**

- Return `true` if index $N-1$ is reachable from index `0` using only valid forward jumps to zero characters.
- Otherwise return `false`.

### Examples

#### Example 1

- **Input:** `s = "011010", minJump = 2, maxJump = 3`
- **Output:** `true`

Jump from index `0` to `3`, then from `3` to `5`.

#### Example 2

- **Input:** `s = "01101110", minJump = 2, maxJump = 3`
- **Output:** `false`

The zero positions do not form a valid chain to the final index.

#### Example 3

- **Input:** `s = "0000", minJump = 1, maxJump = 2`
- **Output:** `true`

Several paths exist, including `0 -> 1 -> 3`.
