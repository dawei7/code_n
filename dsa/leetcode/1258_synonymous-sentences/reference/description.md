### 1. Description

You are given a list of equivalent string pairs `synonyms` where $\text{synonyms}[i] = [s_{i}, t_{i}]$ indicates that $s_{i}$ and $t_{i}$ are equivalent strings. You are also given a sentence `text`.

Return *all possible synonymous sentences **sorted lexicographically***.

### 2. Function Contract

### Inputs

- `synonyms`: A list of unique two-string pairs $[s_{i}, t_{i}]$, each declaring its distinct strings equivalent.
- `text`: A sentence containing at most ten words, separated by single spaces.

For the complexity discussion, let $P$ be the number of synonym pairs, $V$ the number of distinct strings appearing in those pairs, $W$ the number of words in `text`, and $K$ the number of returned sentences.

### Return value

Return every possible synonymous sentence in lexicographically ascending order. Each output preserves the number and order of word positions from `text`.

### 3. Examples

#### Example 1

- **Input:** $synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"$
- **Output:** `["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]`

#### Example 2

- **Input:** $synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"$
- **Output:** `["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]`

### 4. Constraints

- $0 \le \text{synonyms.length} \le 10$

- $\text{synonyms}[i].length = 2$

- $1 \le s_{i}.length,_ t_{i}.length \le 10$

- $s_{i} \neq t_{i}$

- `text` consists of at most `10` words.

- All the pairs of `synonyms` are **unique**.

- The words of `text` are separated by single spaces.
