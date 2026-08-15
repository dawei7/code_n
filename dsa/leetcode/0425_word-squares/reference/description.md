### 1. Description

Given an array of **unique** strings `words`, return *all the ***<a href="https://en.wikipedia.org/wiki/Word_square" target="_blank">word squares</a>*** you can build from *`words`. The same word from `words` can be used **multiple times**. You can return the answer in **any order**.

A sequence of strings forms a valid **word square** if the $$k^{\text{th}}$$ row and column read the same string, where $0 \le k < max(numRows, numColumns)$.

- For example, the word sequence `["ball","area","lead","lady"]` forms a word square because each word reads the same both horizontally and vertically.

### 2. Function Contract

**Inputs**

- `words`: An array of unique lowercase-English words that all have the same length.

**Return value**

Return every word square constructible from `words`. The same input word may occupy multiple rows, and the outer
list may use any order.

### 3. Examples

#### Example 1

- **Input:** $words = ["area","lead","wall","lady","ball"]$
- **Output:** `[["ball","area","lead","lady"],["wall","area","lead","lady"]]`
- **Explanation:** The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

#### Example 2

- **Input:** $words = ["abat","baba","atan","atal"]$
- **Output:** `[["baba","abat","baba","atal"],["baba","abat","baba","atan"]]`
- **Explanation:** The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

### 4. Constraints

- $1 \le \text{words.length} \le 1000$

- $1 \le \text{words}[i].length \le 4$

- All $\text{words}[i]$ have the same length.

- $\text{words}[i]$ consists of only lowercase English letters.

- All $\text{words}[i]$ are **unique**.
