# Word Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 916 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/word-subsets/) |

## Problem Description
### Goal

You are given two arrays of lowercase English strings, `words1` and `words2`. A string `b` is a subset of a string `a` when every letter occurring in `b` also occurs in `a` at least as many times. Multiplicity matters: for example, `"wrr"` is a subset of `"warrior"`, but not of `"world"`.

A word `a` from `words1` is universal when every string `b` in `words2` is a subset of `a`. Return all universal strings from `words1`. The answer may be returned in any order.

### Function Contract
**Inputs**

- `words1`: an array of unique lowercase English strings.
- `words2`: an array of lowercase English strings.
- Each array contains between $1$ and $10^4$ strings, and each string has length from $1$ through $10$.

Let the total number of input characters be

$$
S = \sum_{w \in \texttt{words1}} \lvert w \rvert
  + \sum_{w \in \texttt{words2}} \lvert w \rvert.
$$

**Return value**

A list containing exactly the strings in `words1` whose letter multiplicities satisfy every string in `words2`. Any output order is valid.

### Examples
**Example 1**

- Input: `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]`
- Output: `["facebook","google","leetcode"]`

**Example 2**

- Input: `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]`
- Output: `["leetcode"]`

**Example 3**

- Input: `words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]`
- Output: `["cccbb"]`

### Required Complexity
- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Replace many subset tests with one requirement profile**

For one candidate word, satisfying every word in `words2` means meeting the largest requested multiplicity of each letter. If one requirement contains two `e` characters and another contains three, a universal word needs three `e` characters—not five—because each subset condition is tested against the same candidate independently.

Build a 26-entry array `required`. Count the letters of each word in `words2`, then update each entry with the componentwise maximum. This single profile is equivalent to the entire second array: a candidate satisfies every original word exactly when its count for every letter is at least the corresponding maximum.

**Filter each candidate once**

For every word in `words1`, build its 26-letter frequency profile and compare it with `required`. Append the original word if all 26 counts meet the thresholds. If any count is too small, reject the candidate immediately.

The componentwise construction proves both directions. Every requirement count is bounded by the stored maximum, so meeting the profile satisfies every word in `words2`. Conversely, any universal word must satisfy the particular requirement that supplied each maximum, so it must meet every entry of the profile.

#### Complexity detail

The algorithm reads each input character a constant number of times, giving $O(S)$ time. Both frequency profiles contain exactly 26 integers, so auxiliary space is $O(1)$ because the alphabet is fixed. The returned list is output storage and is not included in the auxiliary-space bound.

#### Alternatives and edge cases

- **Test every pair of words:** Checking each candidate against every string in `words2` directly is correct but can take quadratic time in the numbers of strings.
- **Merge requirements by summing counts:** Adding multiplicities across `words2` is incorrect; simultaneous subset conditions require the maximum count per letter, not the sum.
- **Repeated requirement words:** Duplicates in `words2` do not change the componentwise maximum.
- **Multiplicity:** Presence alone is insufficient; a candidate with one copy of a letter cannot satisfy a requirement containing two copies.
- **No universal candidates:** Return an empty list when every word in `words1` misses at least one required letter.
- **Unconstrained letters:** A letter absent from all of `words2` has required count zero and never disqualifies a candidate.

</details>
