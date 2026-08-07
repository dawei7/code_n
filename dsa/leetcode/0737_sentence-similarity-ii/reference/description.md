## Description

We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`.

Given two sentences `sentence1` and `sentence2` each represented as a string array and given an array of string pairs `similarPairs` where $\text{similarPairs}[i] = [x_{i}, y_{i}]$ indicates that the two words $x_{i}$ and $y_{i}$ are similar.

Return `true`* if `sentence1` and `sentence2` are similar, or *`false`* if they are not similar*.

Two sentences are similar if:

- They have **the same length** (i.e., the same number of words)

- $\text{sentence1}[i]$ and $\text{sentence2}[i]$ are similar.

Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words `a` and `b` are similar, and the words `b` and `c` are similar, then `a` and `c` are **similar**.
### Function Contract

$solve(sentence1: \text{list}[str], sentence2: \text{list}[str], similarPairs: list[\text{list}[str]]) -> bool$

Let $n$ be the common sentence length when the two lengths match, let $p = \lvert\texttt{similarPairs}\rvert$, and let $w$ be the number of distinct words appearing in those pairs.

**Inputs**

- `sentence1`: the first nonempty ordered array of words.
- `sentence2`: the second nonempty ordered array of words.
- `similarPairs`: two-word relationships whose undirected, transitive connections form similarity groups.

**Return value**

Return `True` exactly when the sentences have the same length and every pair of words at a matching position is either identical or belongs to the same similarity group. Otherwise, return `False`.

### Examples

#### Example 1

- **Input:** $sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]$
- **Output:** `true`
- **Explanation:** The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
#### Example 2

- **Input:** $sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]$
- **Output:** `true`
- **Explanation:** "leetcode" --> "platform" --> "anime" --> "manga" --> "onepiece".
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.
#### Example 3

- **Input:** $sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]$
- **Output:** `false`
- **Explanation:** "leetcode" is not similar to "onepiece".
### Constraints

- $1 \le \text{sentence1.length}, \text{sentence2.length} \le 1000$

- $1 \le \text{sentence1}[i].length, \text{sentence2}[i].length \le 20$

- $\text{sentence1}[i]$ and $\text{sentence2}[i]$ consist of lower-case and upper-case English letters.

- $0 \le \text{similarPairs.length} \le 2000$

- $\text{similarPairs}[i].length = 2$

- $1 \le x_{i}.length, y_{i}.length \le 20$

- $x_{i}$ and $y_{i}$ consist of English letters.