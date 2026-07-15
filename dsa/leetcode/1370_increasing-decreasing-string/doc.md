# Increasing Decreasing String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1370 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/increasing-decreasing-string/) |

## Problem Description

### Goal

Rearrange a string of lowercase English letters through repeated increasing and decreasing selections. First choose the smallest remaining character and then repeatedly choose the smallest remaining character strictly greater than the one just appended. When no greater character remains, choose the largest remaining character and repeatedly choose the largest remaining character strictly smaller than the last appended character.

Remove each chosen occurrence from the remaining multiset. Alternate these increasing and decreasing phases until every original occurrence has been appended, then return the resulting string.

### Function Contract

**Inputs**

- `s`: a string of length $n$ containing lowercase English letters.
- Let $A=26$ be the alphabet size and $F$ the maximum frequency of any character.

**Return value**

- The permutation of `s` produced by the prescribed alternating increasing and decreasing selection process.

### Examples

**Example 1**

- Input: `s = "aaaabbbbcccc"`
- Output: `"abccbaabccba"`

**Example 2**

- Input: `s = "rat"`
- Output: `"art"`

**Example 3**

- Input: `s = "leetcode"`
- Output: `"cdelotee"`

### Required Complexity

- **Time:** $O(n+AF)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Represent the remaining multiset with frequencies.** Count the occurrences of each of the 26 letters. This avoids repeatedly sorting or deleting from the string.

**Translate each phase into an alphabet sweep.** Scan indices from `0` through `25`; whenever a count is positive, emit that letter once and decrement its count. The emitted letters are exactly the smallest available character followed by successive strictly greater choices. Then scan from `25` down through `0` to implement the symmetric decreasing phase.

Repeat the two sweeps while unconsumed characters remain. During an increasing sweep, every available distinct letter is selected exactly once in the mandated order; the decreasing sweep has the same property in reverse. Frequencies preserve all unused duplicate occurrences, so repeated rounds emit every input occurrence exactly once and in precisely the specified sequence.

#### Complexity detail

Counting and emitting all output characters takes $O(n)$ time. There are at most $F$ sweep rounds, each examining $A$ counters in both directions, for $O(AF)$ additional work. Total time is $O(n+AF)$; because $A=26$, this is linear in $n$. The counter array uses $O(A)$ auxiliary space.

#### Alternatives and edge cases

- **Mutable sorted multiset:** Rebuild the distinct remaining characters for each phase and remove occurrences from a list. It follows the rules directly but can cost $O(n^2)$ time.
- **Sort once into buckets:** A sorted input can be partitioned into frequency runs, which ultimately recreates the same counter representation with extra sorting cost.
- **One distinct character:** Increasing and decreasing phases repeatedly emit the same character until its count is exhausted.
- **All distinct:** One increasing sweep emits the entire string in ascending order; no decreasing output remains.
- **Unequal frequencies:** A letter participates in exactly as many sweeps as its frequency permits.
- **Strict comparisons:** A phase selects at most one occurrence of each character; duplicates wait for later sweeps.
- **Final half-round:** Stop as soon as all $n$ occurrences have been emitted, even if that happens after the increasing phase.

</details>
