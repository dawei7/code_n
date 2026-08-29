### 1. Description

You are given a list of strings of the **same length** `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

- `target` should be formed from left to right.

- To form the $i^{\text{th}}$ character (**0-indexed**) of `target`, you can choose the $k^{\text{th}}$ character of the $j^{\text{th}}$ string in `words` if $\text{target}[i] = \text{words}[j][k]$.

- Once you use the $k^{\text{th}}$ character of the $j^{\text{th}}$ string of `words`, you **can no longer** use the $x^{\text{th}}$ character of any string in `words` where $x \le k$. In other words, all characters to the left of or at index `k` become unusuable for every string.

- Repeat the process until you form the string `target`.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `target`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Notice

that you can use **multiple characters** from the **same string** in `words` provided the conditions above are met.

Return *the number of ways to form `target` from `words`*. Since the answer may be too large, return it **modulo** $10^{9} + 7$.

### 4. Examples

#### Example 1

- **Input:** $words = ["acca","bbbb","caca"], target = "aba"$
- **Output:** `6`
- **Explanation:** There are 6 ways to form target.
"aba" -> index 0 ("<u>a</u>cca"), index 1 ("b<u>b</u>bb"), index 3 ("cac<u>a</u>")
"aba" -> index 0 ("<u>a</u>cca"), index 2 ("bb<u>b</u>b"), index 3 ("cac<u>a</u>")
"aba" -> index 0 ("<u>a</u>cca"), index 1 ("b<u>b</u>bb"), index 3 ("acc<u>a</u>")
"aba" -> index 0 ("<u>a</u>cca"), index 2 ("bb<u>b</u>b"), index 3 ("acc<u>a</u>")
"aba" -> index 1 ("c<u>a</u>ca"), index 2 ("bb<u>b</u>b"), index 3 ("acc<u>a</u>")
"aba" -> index 1 ("c<u>a</u>ca"), index 2 ("bb<u>b</u>b"), index 3 ("cac<u>a</u>")

#### Example 2

- **Input:** $words = ["abba","baab"], target = "bab"$
- **Output:** `4`
- **Explanation:** There are 4 ways to form target.
"bab" -> index 0 ("<u>b</u>aab"), index 1 ("b<u>a</u>ab"), index 2 ("ab<u>b</u>a")
"bab" -> index 0 ("<u>b</u>aab"), index 1 ("b<u>a</u>ab"), index 3 ("baa<u>b</u>")
"bab" -> index 0 ("<u>b</u>aab"), index 2 ("ba<u>a</u>b"), index 3 ("baa<u>b</u>")
"bab" -> index 1 ("a<u>b</u>ba"), index 2 ("ba<u>a</u>b"), index 3 ("baa<u>b</u>")

### 5. Constraints

- $1 \le \text{words.length} \le 1000$

- $1 \le \text{words}[i].length \le 1000$

- All strings in `words` have the same length.

- $1 \le \text{target.length} \le 1000$

- $\text{words}[i]$ and `target` contain only lowercase English letters.
