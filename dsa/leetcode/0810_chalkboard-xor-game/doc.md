# Chalkboard XOR Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 810 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/chalkboard-xor-game/) |

## Problem Description

### Goal

Integers are written on a chalkboard. Alice and Bob alternate erasing exactly one number, with Alice moving first. If a player begins a turn when the XOR of all remaining numbers is `0`, that player wins immediately.

Otherwise the player must erase one number, but loses if that erasure makes the XOR of the remaining numbers equal to `0`. The XOR of an empty board is `0`. Return `True` exactly when Alice can win assuming both players choose moves optimally, and `False` otherwise.

### Function Contract

**Inputs**

- `nums`: a nonempty list of nonnegative integers initially written on the chalkboard.

**Return value**

- `True` if Alice has a winning strategy under optimal play; otherwise, `False`.

### Examples

**Example 1**

- Input: `nums = [1,1,2]`
- Output: `False`
- Explanation: The XOR is nonzero and the list length is odd, so every move gives Bob a winning position.

**Example 2**

- Input: `nums = [0,1]`
- Output: `True`
- Explanation: The XOR is nonzero, but an even number of entries guarantees Alice a safe move.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `True`
- Explanation: The initial XOR is zero, so Alice wins before removing anything.
