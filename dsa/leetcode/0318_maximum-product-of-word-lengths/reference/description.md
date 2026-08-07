## Description

Given a string array `words`, return *the maximum value of* $length(\text{word}[i]) * length(\text{word}[j])$ *where the two words do not share common letters*. If no such two words exist, return `0`.
### Function Contract

**Inputs**

- `words`: An array of lowercase English words.

**Return value**

Return the largest product of lengths over two words with disjoint letter sets, or `0` if every pair shares a letter.

### Examples

#### Example 1

- **Input:** $words = ["abcw","baz","foo","bar","xtfn","abcdef"]$
- **Output:** `16`
- **Explanation:** The two words can be "abcw", "xtfn".
#### Example 2

- **Input:** $words = ["a","ab","abc","d","cd","bcd","abcd"]$
- **Output:** `4`
- **Explanation:** The two words can be "ab", "cd".
#### Example 3

- **Input:** $words = ["a","aa","aaa","aaaa"]$
- **Output:** `0`
- **Explanation:** No such pair of words.
### Constraints

- $2 \le \text{words.length} \le 1000$

- $1 \le \text{words}[i].length \le 1000$

- $\text{words}[i]$ consists only of lowercase English letters.