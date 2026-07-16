# Check If String Is Transformable With Substring Sort Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1585 |
| Difficulty | Hard |
| Topics | String, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/) |

## Problem Description
### Goal

Given digit strings `s` and `t` of equal length, decide whether `s` can be changed into `t` by repeating the following operation any number of times: choose a non-empty substring of the current string and sort that substring in ascending order in place.

Each operation may move a smaller digit left across larger digits, but ascending sorting cannot move a larger digit left across a smaller digit. Operations may overlap, and choosing no operations is allowed.

Return whether some sequence of these substring sorts produces exactly `t`. A substring is a contiguous part of the string.

### Function Contract
**Inputs**

- `s`: A string of $N$ decimal digits, where $1 \le N \le 10^5$.
- `t`: A string of the same length as `s`, also containing only decimal digits.

**Return value**

Return `true` if ascending sorts of non-empty substrings can transform `s` into `t`; otherwise, return `false`.

### Examples
**Example 1**

- Input: `s = "84532", t = "34852"`
- Output: `true`

**Example 2**

- Input: `s = "34521", t = "23415"`
- Output: `true`

**Example 3**

- Input: `s = "12345", t = "12435"`
- Output: `false`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Track the unused occurrences of every digit**

Record, in increasing order, every index at which each digit `0` through `9` occurs in `s`. While reading `t` from left to right, use the earliest still-unused occurrence of the required digit. Equal digits are interchangeable, so choosing a later occurrence could never make a transformation easier.

If no unused occurrence exists, the strings do not even have the same digit counts and the answer is false.

**Recognize which digits may move left**

Suppose the next required digit is `d` and its earliest unused occurrence was at `source_index`. It may move left across unused digits larger than `d`: an ascending substring sort can place `d` before them. It may not cross an unused smaller digit that originally occurs before `source_index`, because every ascending sort preserves the smaller digit before `d` whenever both participate.

Therefore, before consuming `d`, inspect every smaller digit. If any smaller digit's earliest unused position is before `source_index`, producing this prefix of `t` is impossible. Otherwise consume the selected occurrence and continue.

This condition is also sufficient. When no smaller unused digit blocks `d`, the digit can be brought to the next output position by sorting across only larger intervening digits. Repeating that argument constructs the target prefix from left to right, so passing every check proves that `t` is reachable.

#### Complexity detail

Building the ten position lists takes $O(N)$ time and space. Each target character checks at most ten digit classes, which is a fixed constant, so processing all characters takes $O(N)$ time. The position lists and their consumption counters use $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Ordered queues of indices:** store each digit's positions in a queue and compare queue fronts. This expresses the same greedy rule but incurs queue-object overhead.
- **Repeatedly edit the remaining string:** find the next target digit, verify that no smaller digit precedes it, and remove it. This is correct but repeated scans and removals take $O(N^2)$ time.
- **Compare only digit counts:** matching multisets are necessary but insufficient; for example, `"12"` cannot become `"21"` because `2` cannot cross the smaller `1`.
- **Already equal strings:** zero operations are permitted, so the result is true.
- **One character:** transformation is possible exactly when the two digits match.
- **Repeated digits:** occurrences of the same value retain no meaningful identity, so consuming them from left to right is safe.
- **Globally descending source:** sorting the whole string can produce its globally ascending arrangement.
- **Missing or extra digit:** the required occurrence list becomes exhausted and the result is false.

</details>
