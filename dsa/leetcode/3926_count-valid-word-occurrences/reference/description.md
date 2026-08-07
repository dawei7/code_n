## Description

You are given an array of strings `chunks`. Concatenate all strings in `chunks` in order to form a string `s`.

You are also given an array of strings `queries`.

A **joiner hyphen** is a hyphen character `'-'` in `s` whose previous and next characters both exist and are lowercase English letters.

A **word** is a **maximal** substring of `s` consisting only of lowercase English letters and **joiner hyphens**.

All other characters, including spaces and hyphens that are not **joiner hyphens**, are treated as separators.

Return an integer array `ans`, where $\text{ans}[i]$ is the number of times $\text{queries}[i]$ appears as a word in `s`.
### Function Contract

**Inputs**

- `chunks`: The ordered string pieces that are concatenated directly to form `s`.
- `queries`: Valid word strings whose complete-word occurrence counts are requested.

Let

$$
C = \sum_{x \in \texttt{chunks}} \lvert x \rvert
\quad\text{and}\quad
Q = \sum_{q \in \texttt{queries}} \lvert q \rvert.
$$

Hyphen classification uses neighboring characters in the fully concatenated `s`, including neighbors that originated in different chunks.

**Return value**

Return an integer array `ans` with `ans[i]` equal to the number of maximal words in `s` that exactly equal `queries[i]`.

### Examples
#### Example 1

<div class="example-block">
**Input:** chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]

**Output:** [2,1,0]

**Explanation:**

- After concatenating all strings in `chunks`, `s = "hello world hello"`.

- The words are `"hello"`, `"world"`, and `"hello"`.

- The substring `"wor"` appears inside `"world"`, but it is not a full word.

</div>
#### Example 2

<div class="example-block">
**Input:** chunks = ["a-b a--b ","a-","b"], queries = ["a-b","a","b"]

**Output:** [2,1,1]

**Explanation:**

- After concatenating all strings in `chunks`, `s = "a-b a--b a-b"`.

- In `"a-b"`, the hyphen is a joiner hyphen because it is between two lowercase English letters, so `"a-b"` is one word.

- In `"a--b"`, neither hyphen is a joiner hyphen, so it is split into the words `"a"` and `"b"`.

- Therefore, the words are `"a-b"`, `"a"`, `"b"`, and `"a-b"`.

</div>
#### Example 3

<div class="example-block">
**Input:** chunks = ["-cat dog- mouse"], queries = ["cat","dog","mouse","cat-dog"]

**Output:** [1,1,1,0]

**Explanation:**

- After concatenating all strings in `chunks`, `s = "-cat dog- mouse"`.

- The leading hyphen before `"cat"` and the trailing hyphen after `"dog"` are not joiner hyphens, so they are separators.

- The words are `"cat"`, `"dog"`, and `"mouse"`.

</div>
### Constraints

- $1 \le \text{chunks.length} \le 10^{5}$

- $1 \le \text{chunks}[i].length \le 10^{5}$

- The total length of all strings in `chunks` does not exceed $10^{5}$.

- $\text{chunks}[i]$ consists only of lowercase English letters, spaces, and `'-'`.

- $1 \le \text{queries.length} \le 10^{5}$

- $1 \le \text{queries}[i].length \le 10^{5}$

- The total length of all strings in `queries` does not exceed $10^{5}$.

- $\text{queries}[i]$ consists only of lowercase English letters and `'-'`.

- $\text{queries}[i]$ is a valid word: it does not start or end with `'-'`, and it does not contain two consecutive hyphens.