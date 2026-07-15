# Print Words Vertically

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1324 |
| Difficulty | Medium |
| Topics | Array, String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/print-words-vertically/) |

## Problem Description
### Goal
Given a sentence `s`, place its words into columns in their original order and read the resulting character grid row by row. Each input word occupies exactly one column and appears from top to bottom.

When a word is shorter than a requested row, its column contributes a space so later words remain aligned. Remove spaces only from the end of each returned row; spaces before or between visible characters must be preserved.

Return all vertical rows from the first character position through the longest word's final position. The sentence contains uppercase English words separated by single spaces.

### Function Contract
**Inputs**

- `s`: a sentence of uppercase English words with one space between adjacent words and total length at most 200.

Let $w$ be the number of words, $L$ the maximum word length, and $P=wL$ the number of cells in the padded word rectangle.

**Return value**

A list of $L$ strings representing the rectangle's rows after trailing spaces are removed from each row.

### Examples
**Example 1**

- Input: `s = "HOW ARE YOU"`
- Output: `["HAY", "ORO", "WEU"]`

**Example 2**

- Input: `s = "TO BE OR NOT TO BE"`
- Output: `["TBONTB", "OEROOE", "   T"]`
- Explanation: The third row keeps its leading alignment spaces but has no trailing spaces.

**Example 3**

- Input: `s = "CONTEST IS COMING"`
- Output: `["CIC", "OSO", "N M", "T I", "E N", "S G", "T"]`

### Required Complexity
- **Time:** $O(P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Transpose the padded words**

Split `s` into its words and find $L$. For each character position `row` from 0 through `L - 1`, visit the words from left to right. Append `word[row]` when that position exists; otherwise append a space as a placeholder for the shorter column.

After the row is assembled, remove only its trailing spaces and append it to the answer. Padding during construction preserves the exact columns of any later visible characters, while `rstrip` enforces the output rule. Iterating every possible character position of the longest word produces exactly the required number and order of rows.

#### Complexity detail

The nested loops inspect all $P=wL$ cells. Splitting the sentence and finding $L$ are bounded by the input length and do not exceed this work. The temporary row buffers and returned strings contain at most $P$ characters, so auxiliary output construction space is $O(P)$.

#### Alternatives and edge cases

- **Pad then transpose:** Explicitly right-pad every word to length $L$ before transposing is simple but materializes another full $P$-character rectangle.
- **Repeated string concatenation:** Extending immutable row strings one character at a time can repeatedly copy prefixes; a character list plus one join avoids that overhead.
- **One word:** Return its characters as one-character strings.
- **Equal-length words:** No padding or trimming is needed.
- **Short middle word:** Its spaces inside a row must remain when a later column has a character.
- **Trailing short words:** Their absent characters become trailing spaces and must be removed.

</details>
