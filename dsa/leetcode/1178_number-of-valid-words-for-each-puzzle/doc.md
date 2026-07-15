# Number of Valid Words for Each Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1178 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) |

## Problem Description

### Goal

You are given a list of lowercase `words` and a list of seven-letter `puzzles`. A word is valid for a puzzle only when it satisfies both rules: the word contains the puzzle's first letter, and every letter occurring in the word also occurs somewhere in the puzzle. Repeated occurrences of a letter do not require separate puzzle entries.

For each puzzle independently, count how many entries in `words` are valid for it. Return the counts in the same order as `puzzles`; repeated word entries, if present, contribute separately.

### Function Contract

**Inputs**

- `words`: Between $1$ and $10^5$ lowercase English strings, each with length from $4$ through $50$.
- `puzzles`: Between $1$ and $10^4$ lowercase English strings. Every puzzle has exactly seven distinct letters, and its character at index `0` is the required letter.
- Define

$$
W=\sum_{w\in\texttt{words}} \lvert w\rvert.
$$

- Let $p=\lvert\texttt{puzzles}\rvert$ and let $u$ be the number of distinct word-letter masks containing at most seven letters.

**Return value**

- A length-$p$ integer array where entry $i$ is the number of words whose letters are all contained in `puzzles[i]` and that contain `puzzles[i][0]`.

### Examples

**Example 1**

- Input: `words = ["aaaa","asas","able","ability","actt","actor","access"]`, `puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]`
- Output: `[1,1,3,2,4,0]`

For `"actresz"`, the valid words are `"aaaa"`, `"actt"`, `"actor"`, and `"access"`.

**Example 2**

- Input: `words = ["apple","pleas","please"]`, `puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]`
- Output: `[0,1,3,2,0]`

**Example 3**

- Input: `words = ["aaaa","bbbb","abab"]`, `puzzles = ["abcdefg","bcdefgh"]`
- Output: `[2,1]`

### Required Complexity

- **Time:** $O(W+p)$
- **Space:** $O(u)$

<details>
<summary>Approach</summary>

#### General

**Collapse each word to its distinct-letter mask.** Assign one bit to every lowercase letter and OR together the bits appearing in a word. Multiplicity does not affect either validity rule, so anagrams and repeated-letter variants with the same set share one mask. Count how many word entries produce each mask. Discard masks with more than seven set bits because no seven-letter puzzle can contain them.

**Generate only masks a puzzle can accept.** A valid word mask must include the puzzle's first-letter bit and may include any subset of the other six puzzle bits. There are only $2^6=64$ such possibilities. Build the mask for the six optional letters, enumerate all of its submasks with `submask = (submask - 1) & optional`, OR each with the required bit, and add its stored word frequency.

**Preserve multiplicity and order.** The frequency table makes all word entries with the same mask contribute together, while processing puzzles from left to right produces answers in their original order. Every counted mask contains the required first letter by construction and no bit outside the puzzle, so it satisfies both validity rules. Conversely, every valid word's optional letters form one enumerated submask, so none are missed.

#### Complexity detail

Constructing word masks examines $W$ characters. Each puzzle has seven characters and exactly 64 relevant submasks, both fixed constants, so all puzzle work is $O(p)$. Total time is $O(W+p)$. The frequency map stores $u$ retained masks, using $O(u)$ auxiliary space; the answer array is output storage.

#### Alternatives and edge cases

- **Check every word against every puzzle:** Set containment is direct and correct, but the cross product takes $O(\lvert\texttt{words}\rvert p)$ comparisons.
- **Trie over sorted distinct letters:** A trie can prune branches not present in a puzzle, but mask counting and 64 submasks are simpler for the fixed alphabet and puzzle length.
- **Word with more than seven distinct letters:** It can never fit any puzzle and should be omitted from the frequency map.
- **Repeated letters in a word:** They set one bit and do not need multiple puzzle occurrences.
- **Required first letter absent:** A subset of the other six letters alone never counts because the required bit is ORed into every lookup.
- **Duplicate word masks:** Each original word entry counts, so the map stores a frequency rather than a Boolean.
- **Required letter only:** A word consisting solely of repeated copies of the first puzzle letter corresponds to the zero optional submask.

</details>
