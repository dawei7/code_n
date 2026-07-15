# Find the Shortest Superstring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 943 |
| Difficulty | Hard |
| Topics | Array, String, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-shortest-superstring/) |

## Problem Description

### Goal

Given an array `words` of unique lowercase English strings, construct the shortest string that contains every member of `words` as a substring. A word may begin at any position in the result, and overlapping suffixes and prefixes may share the same characters rather than being repeated.

No input word is a substring of another input word. If several strings have the minimum possible length while containing all the words, any one of those shortest superstrings may be returned.

### Function Contract

Let $m$ be the number of strings and let $\ell$ be the maximum string length. Define

$$
T = m^2 2^m + m^2 \ell^2,
\qquad
S = m2^m + m^2.
$$

**Inputs**

- `words`: a list of $m$ unique lowercase English strings, where $1 \le m \le 12$ and each string has length from $1$ through $20$.
- No string in `words` is a substring of another string in `words`.

**Return value**

Return any minimum-length string that contains every string in `words` as a substring.

### Examples

**Example 1**

- Input: `words = ["alex", "loves", "leetcode"]`
- Output: `"alexlovesleetcode"`

There are no useful overlaps here, so concatenating the three words in any order has minimum length and is acceptable.

**Example 2**

- Input: `words = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]`
- Output: `"gctaagttcatgcatc"`

### Required Complexity

- **Time:** $O(T)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Turn shared characters into edge weights.** For each ordered pair of distinct words, compute the largest length for which a suffix of the first word equals a prefix of the second. Appending the second word after the first then adds only the unmatched suffix. Because no input word is contained in another, a shortest superstring can be represented by some ordering of all words with each adjacent pair merged at its maximum suffix-prefix overlap. Minimizing the final length is therefore equivalent to maximizing the sum of those adjacent overlap lengths.

**Remember only the used set and final word.** Represent a subset of words by a bitmask. Let `dp[mask][last]` be the greatest total overlap saved by an ordering that uses exactly the words in `mask` and ends at `words[last]`. A one-word state saves zero characters. For a larger state, remove `last` from the mask and try every possible preceding word `previous`; the candidate saving is `dp[previous_mask][previous] + overlap[previous][last]`. Keep the largest candidate and record which preceding word produced it.

Every ordering contributing to a state has one well-defined final edge, so removing that edge produces one of the predecessor states considered by the transition. Conversely, extending any predecessor ordering by `last` produces a valid ordering for the current state. Induction over the number of set bits therefore shows that each state stores the maximum possible saving.

**Reconstruct instead of storing partial strings.** Select the final word with the greatest saving for the full mask, follow the recorded parents backward, and reverse that index sequence. Start with its first word, then append only `words[next][overlap[current][next]:]` for every adjacent pair. This realizes exactly the overlap total optimized by the dynamic program, so the resulting superstring has minimum length and contains every word.

#### Complexity detail

Computing one suffix-prefix overlap by checking lengths up to $\ell$ costs $O(\ell^2)$ with ordinary string slicing and comparison, so all ordered pairs cost $O(m^2\ell^2)$. The dynamic program has $m2^m$ states and tries up to $m$ predecessors per state, costing $O(m^2 2^m)$. Together these are $O(T)$ time.

The score and parent tables hold $m2^m$ entries, and the overlap table holds $m^2$ entries, for $O(S)$ space. The final returned string is additional output storage.

#### Alternatives and edge cases

- **Store a string in every DP state:** The same subset recurrence can keep the best partial superstring itself. It remains correct, but repeated concatenation and comparison copy strings throughout the state transitions and add a substantial factor to runtime and memory.
- **Enumerate all word orders:** Evaluate every permutation and merge adjacent words greedily by maximum overlap. This is correct but takes factorial time, which is impractical at $m=12$.
- **Greedily merge the currently best overlap:** Repeatedly combining the pair with the largest immediate overlap is fast, but a locally large overlap can prevent a better global ordering and does not guarantee minimum length.
- **One word:** The only input word is already the shortest superstring.
- **No positive overlaps:** Every ordering has length equal to the sum of all word lengths, so any concatenation is optimal.
- **Multiple optimal orders:** Parent tie-breaking may choose any of them; the returned text need not match a particular sample.
- **Directed overlap:** The overlap from one word to another need not equal the reverse overlap, so both ordered pairs must be computed separately.

</details>
