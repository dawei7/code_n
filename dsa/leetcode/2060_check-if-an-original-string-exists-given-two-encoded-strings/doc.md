# Check if an Original String Exists Given Two Encoded Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2060 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/) |

## Problem Description

### Goal

To encode a lowercase original string, split it into nonempty substrings, optionally replace any chosen substring by the decimal representation of its length, and concatenate all resulting pieces. A run of digits in the encoding may therefore represent one length or several adjacent lengths; for example, `"123"` can arise from lengths $123$, $1+23$, $12+3$, or $1+2+3$.

Given two such encoded strings, determine whether at least one lowercase original string could produce both. Each input contains letters and digits `1` through `9`, has length at most $40$, and contains no digit run longer than three characters.

### Function Contract

**Inputs**

- `s1`, `s2`: nonempty encoded strings of lengths $n_1$ and $n_2$, each at most $40$, containing lowercase letters and digits `1` through `9`; consecutive digit runs have length at most three.

Let $B$ be the number of distinct unmatched-length balances reachable for one pair of input positions.

**Return value**

- Return `true` when some lowercase string can be encoded as both `s1` and `s2`; otherwise return `false`.

### Examples

**Example 1**

- Input: `s1 = "internationalization", s2 = "i18n"`
- Output: `true`
- Explanation: The middle eighteen letters may be replaced by their length.

**Example 2**

- Input: `s1 = "l123e", s2 = "44"`
- Output: `true`
- Explanation: Both may encode `"leetcode"` using different substring partitions.

**Example 3**

- Input: `s1 = "a5b", s2 = "c5b"`
- Output: `false`
- Explanation: Their first required literal letters disagree.

### Required Complexity

- **Time:** $O(n_1n_2B)$
- **Space:** $O(n_1n_2B)$

<details>
<summary>Approach</summary>

#### General

**A balance represents unmatched wildcard characters**

Use a state `(first, second, balance)`, where the positions identify the unconsumed suffixes and `balance` is the wildcard length produced by `s1` minus that produced by `s2`. Parse one, two, or three digits from the current run of either string. A number from `s1` increases the balance; one from `s2` decreases it. Trying every numeric prefix naturally covers every partition of adjacent numeric substrings.

**Consuming literals only on the shorter expansion**

When `balance > 0`, `s1` has unmatched wildcard characters, so the next literal from `s2` can consume one and reduce the balance. When `balance < 0`, a literal from `s1` consumes one unit in the opposite direction. At balance zero, two literal characters must match and advance together. Success requires both encodings exhausted with balance zero.

Memoize states because different digit partitions repeatedly reach the same positions and balance. Each transition preserves the set of possible expanded prefixes represented by its state, and the three cases exhaust all ways the next original character can be accounted for. Therefore reaching the terminal zero-balance state is equivalent to a common original string existing.

#### Complexity detail

There are at most $n_1n_2B$ reachable position-and-balance states. Each state tries at most three numeric prefixes per input or one literal transition, so time and memo space are $O(n_1n_2B)$. The constraints bound all three quantities, but retaining $B$ makes the dependence on numeric ambiguity explicit.

#### Alternatives and edge cases

- **Uncached depth-first search:** It follows the same transitions but revisits states exponentially often as digit partitions accumulate.
- **Linear memo lookup:** Storing memoized states in a list preserves correctness but can add a linear state-search factor compared with hashing.
- A consecutive digit run is not necessarily one number; every partition into one- to three-digit lengths must be considered.
- Literal letters compare directly only when the unmatched wildcard balance is zero.
- Both inputs must be exhausted and the final balance must be zero; equal encoded lengths alone are insufficient.

</details>
