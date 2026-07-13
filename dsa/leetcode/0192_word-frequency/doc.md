# Word Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 192 |
| Difficulty | Medium |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/word-frequency/) |

## Problem Description
### Goal
The file `words.txt` contains lowercase words separated by spaces or line breaks. Treat every whitespace-delimited token as one word and count how many times each distinct word occurs across the complete file, regardless of which line contains it.

Write one line to standard output for each distinct word in the form `word count`, using one space between the token and its decimal frequency. Sort the lines in descending order by frequency, and do not emit headers, punctuation, or duplicate summary rows. An empty file produces no output. Preserve shell-style file input and stdout behavior rather than reframing the task as a function call.

### Function Contract
**Inputs**

- `words.txt`: lowercase words separated by spaces or line breaks

**Return value**

Write one `word count` pair per line to stdout, ordered by decreasing count.

### Examples
**Example 1**

- File: `the day is sunny the the the sunny is is`
- Output starts with: `the 4`, then `is 3`, then `sunny 2`, then `day 1`

**Example 2**

- File: `code`
- Output: `code 1`

**Example 3**

- File contains words across multiple lines
- Output: counts combine all lines

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

The input uses both spaces and newlines as separators, while Unix counting tools work most naturally with one record per line. A pipeline can transform and aggregate the file without loading it into shell variables:

1. `tr -s '[:space:]' '\n'` turns every whitespace-delimited word into one line and squeezes repeated separators.
2. Remove any empty record defensively.
3. Lexicographically `sort` the words so all occurrences of the same word are contiguous.
4. `uniq -c` replaces each contiguous run with its exact count and word.
5. Sort those counted rows numerically by count in descending order, then use `awk` to print `word count` rather than `count word`.

The first sort is not for presentation; it is what makes `uniq -c` a correct global frequency counter. Without it, only adjacent repeated words would be combined. The second sort establishes the requested frequency order. The reference pipeline adds a deterministic word tie-breaker, although the problem constrains only descending count.

Quoting and locale deserve attention in shell solutions. Use the character class `[:space:]` rather than assuming only literal spaces, and specify numeric sorting for counts so `10` is ordered above `2`. The input filename should be redirected or quoted rather than interpolated from untrusted text.

Whitespace normalization emits exactly one line for every word occurrence and no line for a separator. Lexicographic sorting makes all equal words form one maximal contiguous run, so `uniq -c` emits one row whose count equals that word's total frequency. The final numeric descending sort changes only row order, not counts, and `awk` changes only field presentation. Therefore stdout contains every distinct word exactly once with its correct count, ordered by decreasing frequency.

#### Complexity detail

For `n` word occurrences, the sorting phases dominate at $O(n \log n)$ time in the comparison model and can use $O(n)$ temporary/external storage. Tokenization, run counting, and formatting are streaming linear passes. Actual Unix `sort` may spill to disk for large inputs.

#### Alternatives and edge cases

- An associative-array `awk` program counts in one pass, but the resulting keys still need an ordering phase by frequency.
- Repeatedly invoking `grep` for each distinct word rescans the file and can become quadratic.
- `uniq -c` without the first sort counts only adjacent runs and is incorrect for separated repetitions.
- A single word prints with count one; repeated spaces, tabs, and line breaks do not create empty words.
- Counts combine occurrences across all lines. Empty input produces no output rows.

</details>
