### 1. Description

Given a string `text` and an array of strings `words`, return *an array of all index pairs *`[i, j]`* so that the substring *`text[i...j]`* is in `words`*.

Return the pairs `[i, j]` in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).

### 2. Function Contract

**Inputs**

- `text`: a non-empty lowercase English string to search.
- `words`: a non-empty array of distinct, non-empty lowercase English strings.

Let $N = \lvert\texttt{text}\rvert$, let $W = \lvert\texttt{words}\rvert$, and let

$L = \max_{w \in \texttt{words}} \lvert w \rvert.$

Each returned pair `[i, j]` uses inclusive zero-based boundaries and therefore represents $text[i:j + 1]$.

**Return value**

- Every pair `[i, j]` whose represented substring is a member of `words`, sorted first by `i` and then by `j`.

### 3. Examples

#### Example 1

- **Input:** $text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]$
- **Output:** `[[3,7],[9,13],[10,17]]`
#### Example 2

- **Input:** $text = "ababa", words = ["aba","ab"]$
- **Output:** `[[0,1],[0,2],[2,3],[2,4]]`
- **Explanation:** Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

### 4. Constraints

- $1 \le \text{text.length} \le 100$

- $1 \le \text{words.length} \le 20$

- $1 \le \text{words}[i].length \le 50$

- `text` and $\text{words}[i]$ consist of lowercase English letters.

- All the strings of `words` are **unique**.