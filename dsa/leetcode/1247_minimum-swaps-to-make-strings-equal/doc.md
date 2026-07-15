# Minimum Swaps to Make Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1247 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/) |

## Problem Description

### Goal

You are given two strings `s1` and `s2` of equal length. Every character in both strings is either `"x"` or `"y"`. In one operation, choose an index `i` in `s1` and an index `j` in `s2`, then swap `s1[i]` with `s2[j]`. The two chosen indices do not need to be the same.

Return the minimum number of such swaps needed to make the two strings equal. If no sequence of cross-string swaps can make them equal, return `-1`.

### Function Contract

**Inputs**

- `s1`: a string containing only `"x"` and `"y"`.
- `s2`: a string of the same length as `s1`, also containing only `"x"` and `"y"`.
- The common length $n$ satisfies $1 \le n \le 1000$.

**Return value**

- Return the minimum number of swaps between one character of `s1` and one character of `s2` that makes the strings equal, or `-1` when this is impossible.

### Examples

**Example 1**

- Input: `s1 = "xx"`, `s2 = "yy"`
- Output: `1`
- Explanation: Swapping `s1[0]` with `s2[1]` makes both strings `"yx"`.

**Example 2**

- Input: `s1 = "xy"`, `s2 = "yx"`
- Output: `2`
- Explanation: The two mismatches have opposite orientations, so one swap cannot repair both of them.

**Example 3**

- Input: `s1 = "xx"`, `s2 = "xy"`
- Output: `-1`
- Explanation: There is an odd number of mismatched positions, so the strings cannot be made equal.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Positions where the strings already agree never need to participate in a minimum solution. Every remaining position has exactly one of two orientations: `s1` has `"x"` while `s2` has `"y"`, or `s1` has `"y"` while `s2` has `"x"`. Let their counts be $a$ and $b$, respectively.

**Why pairs of the same orientation cost one swap**

Consider two `x/y` mismatches. Swapping the `"x"` from one position in `s1` with the `"y"` at the other position in `s2` fixes both positions at once. Therefore every pair contributes one swap, giving $\lfloor a/2 \rfloor$ swaps for the first orientation and $\lfloor b/2 \rfloor$ for the second.

**Why the remaining parities decide feasibility**

A cross-string swap preserves the total number of each character across both strings. Equality requires mismatches to be eliminated in pairs, so an odd value of $a+b$ is impossible. After same-orientation pairs are removed, the only possible residue is one mismatch of each orientation. Those two cannot be fixed by one cross-string swap: the first swap changes them into two mismatches of the same orientation, and a second swap repairs that pair. Thus this residue costs exactly two swaps.

A single pass counts $a$ and $b$. If $a+b$ is odd, return `-1`; otherwise return $\lfloor a/2 \rfloor + \lfloor b/2 \rfloor + 2(a \bmod 2)$.

#### Complexity detail

The scan examines each of the $n$ aligned character pairs once, so it takes $O(n)$ time. Only the two mismatch counters are retained, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Explicit mismatch lists:** Recording the indices of both mismatch orientations leads to the same greedy pairing, but uses $O(n)$ extra space without helping compute the answer.
- **Breadth-first search over swaps:** Exploring string configurations can find a minimum for tiny inputs, but the state space grows exponentially and is unnecessary once mismatch orientations are counted.
- **Already equal strings:** Both mismatch counts are zero, so the minimum is `0`.
- **One unmatched position:** An odd total mismatch count cannot be repaired and must return `-1`.
- **One mismatch of each orientation:** This is the parity residue that requires exactly two swaps, not one.

</details>
