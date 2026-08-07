### 1. Description

You are given a **0-indexed** string `word`.

In one operation, you can pick any index `i` of `word` and change $\text{word}[i]$ to any lowercase English letter.

Return *the **minimum** number of operations needed to remove all adjacent **almost-equal** characters from* `word`.

Two characters `a` and `b` are **almost-equal** if $a = b$ or `a` and `b` are adjacent in the alphabet.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $word = "aaaaa"$
- **Output:** `2`
- **Explanation:** We can change word into "a**<u>c</u>**a<u>**c**</u>a" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
#### Example 2

- **Input:** $word = "abddez"$
- **Output:** `2`
- **Explanation:** We can change word into "**<u>y</u>**bd<u>**o**</u>ez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
#### Example 3

- **Input:** $word = "zyxyxyz"$
- **Output:** `3`
- **Explanation:** We can change word into "z<u>**a**</u>x<u>**a**</u>x**<u>a</u>**z" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.

### 4. Constraints

- $1 \le \text{word.length} \le 100$

- `word` consists only of lowercase English letters.