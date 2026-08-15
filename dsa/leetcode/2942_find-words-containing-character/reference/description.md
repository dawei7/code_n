### 1. Description

You are given a **0-indexed** array of strings `words` and a character `x`.

Return *an **array of indices** representing the words that contain the character *`x`.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `x`: Input parameter (`str`).

**Return value**

- Returns `List[int]`.

### 3. Note

that the returned array may be in **any** order.

### 4. Examples

#### Example 1

- **Input:** $words = ["leet","code"], x = "e"$
- **Output:** `[0,1]`
- **Explanation:** "e" occurs in both words: "l**<u>ee</u>**t", and "cod<u>**e**</u>". Hence, we return indices 0 and 1.

#### Example 2

- **Input:** $words = ["abc","bcd","aaaa","cbc"], x = "a"$
- **Output:** `[0,2]`
- **Explanation:** "a" occurs in "**<u>a</u>**bc", and "<u>**aaaa**</u>". Hence, we return indices 0 and 2.

#### Example 3

- **Input:** $words = ["abc","bcd","aaaa","cbc"], x = "z"$
- **Output:** `[]`
- **Explanation:** "z" does not occur in any of the words. Hence, we return an empty array.

### 5. Constraints

- $1 \le \text{words.length} \le 50$

- $1 \le \text{words}[i].length \le 50$

- `x` is a lowercase English letter.

- $\text{words}[i]$ consists only of lowercase English letters.
