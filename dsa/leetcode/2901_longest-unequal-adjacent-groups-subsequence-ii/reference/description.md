### 1. Description

You are given a string array `words`, and an array `groups`, both arrays having length `n`.

The **hamming distance** between two strings of equal length is the number of positions at which the corresponding characters are **different**.

You need to select the **longest** subsequence from an array of indices `[0, 1, ..., n - 1]`, such that for the subsequence denoted as $[i_{0}, i_{1}, ..., i_{k}-1]$ having length `k`, the following holds:

- For **adjacent** indices in the subsequence, their corresponding groups are **unequal**, i.e., $groups[i_{j}] \neq groups[i_{j}+1]$, for each `j` where $0 < j + 1 < k$.

- $words[i_{j}]$ and $words[i_{j}+1]$ are **equal** in length, and the **hamming distance** between them is `1`, where $0 < j + 1 < k$, for all indices in the subsequence.

Return *a string array containing the words corresponding to the indices **(in order)** in the selected subsequence*. If there are multiple answers, return *any of them*.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `groups`: Input parameter (`List[int]`).

**Return value**

- Returns `List[str]`.

### 3. Note

strings in `words` may be **unequal** in length.

### 4. Examples

#### Example 1

- **Input:** words = ["bab","dab","cab"], groups = [1,2,2]

- **Output:** ["bab","cab"]

- **Explanation:** A subsequence that can be selected is `[0,2]`.

- $\text{groups}[0] \neq \text{groups}[2]$

- $\text{words}[0].length = \text{words}[2].length$, and the hamming distance between them is 1.

So, a valid answer is `[words[0],words[2]] = ["bab","cab"]`.

Another subsequence that can be selected is `[0,1]`.

- $\text{groups}[0] \neq \text{groups}[1]$

- $\text{words}[0].length = \text{words}[1].length$, and the hamming distance between them is `1`.

So, another valid answer is `[words[0],words[1]] = ["bab","dab"]`.

It can be shown that the length of the longest subsequence of indices that satisfies the conditions is `2`.

#### Example 2

- **Input:** words = ["a","b","c","d"], groups = [1,2,3,4]

- **Output:** ["a","b","c","d"]

- **Explanation:** We can select the subsequence `[0,1,2,3]`.

It satisfies both conditions.

Hence, the answer is `[words[0],words[1],words[2],words[3]] = ["a","b","c","d"]`.

It has the longest length among all subsequences of indices that satisfy the conditions.

Hence, it is the only answer.

### 5. Constraints

- $1 \le n = \text{words.length} = \text{groups.length} \le 1000$

- $1 \le \text{words}[i].length \le 10$

- $1 \le \text{groups}[i] \le n$

- `words` consists of **distinct** strings.

- $\text{words}[i]$ consists of lowercase English letters.
