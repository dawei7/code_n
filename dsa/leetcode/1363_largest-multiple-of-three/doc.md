# Largest Multiple of Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1363 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/largest-multiple-of-three/) |

## Problem Description

### Goal

Given an array of decimal digits, select any nonempty subset of their occurrences and arrange the selected digits in any order. Each input occurrence may be used at most once.

Return the numerically largest arrangement that is divisible by $3$, represented as a string. The representation must not contain leading zeroes unless its value is exactly zero; if no nonempty selection can form a multiple of three, return the empty string. When the selected digits are all zero, return `"0"` rather than several zeroes.

### Function Contract

**Inputs**

- `digits`: an array of $n$ integers, each from $0$ through $9$.

**Return value**

- The largest decimal string obtainable from some input occurrences whose integer value is divisible by $3$, or `""` when no such nonempty selection exists.

### Examples

**Example 1**

- Input: `digits = [8,1,9]`
- Output: `"981"`

**Example 2**

- Input: `digits = [8,6,7,1,0]`
- Output: `"8760"`

**Example 3**

- Input: `digits = [1]`
- Output: `""`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use the digit-sum divisibility rule.** A decimal integer is divisible by $3$ exactly when its digit sum is divisible by $3$. Count the occurrences of all ten digits and compute the total sum. The order of selected digits does not affect divisibility.

**Discard as little value as possible.** If the sum has remainder one, either remove the smallest available digit with remainder one or, when none exists, remove the two smallest digits with remainder two. For remainder two, apply the symmetric choice. Removing one digit is always preferable to removing two because it leaves a longer decimal representation; within the same removal count, discarding the smallest digits preserves the greatest remaining multiset.

**Arrange the retained multiset maximally.** Emit remaining digits from `9` down through `0`. Descending order is the largest permutation of a fixed multiset. If nothing remains, no answer exists. If the first emitted digit is zero, every retained digit is zero, so normalize the result to `"0"`.

The remainder repair produces a divisible multiset while maximizing first its length and then its descending lexicographic order. Those criteria exactly maximize a nonnegative decimal integer, proving the returned string is optimal.

#### Complexity detail

Counting and summing the $n$ input digits takes $O(n)$ time. Repairing the remainder and traversing ten counters take constant time; producing the output takes at most $O(n)$ time. The ten counters use $O(1)$ auxiliary space, excluding the required output string.

#### Alternatives and edge cases

- **Sort then repair:** Sort all digits, remove the smallest remainder-compatible occurrence or pair, and reverse the remainder. This is correct but costs $O(n\log n)$ time.
- **Subset dynamic programming:** Track the best string for each remainder while processing digits. It works but repeatedly compares or copies long strings and is unnecessary for a ten-symbol alphabet.
- **Enumerate subsets:** Test every selected multiset and permutation, which is exponential and infeasible.
- **Two-digit repair:** When no digit has the total remainder, two smallest digits from the opposite nonzero remainder class must be removed.
- **All zeroes:** Any number of zeroes represents the same value, so return exactly `"0"`.
- **Only unusable digits:** If remainder repair removes every digit, return the empty string.
- **Duplicate occurrences:** Counts preserve multiplicity, and each occurrence is removed or emitted at most once.

</details>
