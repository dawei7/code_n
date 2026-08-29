### 1. Description

You are given a **0-indexed** string `s`. You are also given a **0-indexed** string `queryCharacters` of length `k` and a **0-indexed** array of integer **indices** `queryIndices` of length `k`, both of which are used to describe `k` queries.

The $i^{\text{th}}$ query updates the character in `s` at index $\text{queryIndices}[i]$ to the character $\text{queryCharacters}[i]$.

Return *an array* `lengths` *of length *`k`* where* $\text{lengths}[i]$ *is the **length** of the **longest substring** of *`s`* consisting of **only one repeating** character **after** the* $i^{\text{th}}$ *query** is performed.*

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).
- `queryCharacters`: Input parameter (`str`).
- `queryIndices`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** `s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]`
- **Output:** `[3,3,4]`
- **Explanation:** 
- 1^st query updates s = "<u>b**b**b</u>acc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2^nd query updates s = "bbb<u>**c**cc</u>".
The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3^rd query updates s = "<u>bbb**b**</u>cc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].

#### Example 2

- **Input:** `s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]`
- **Output:** `[2,3]`
- **Explanation:** 
- 1^st query updates s = "ab**a**<u>zz</u>". The longest substring consisting of one repeating character is "zz" with length 2.
- 2^nd query updates s = "<u>a**a**a</u>zz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.

- $k = \text{queryCharacters.length} = \text{queryIndices.length}$

- $1 \le k \le 10^{5}$

- `queryCharacters` consists of lowercase English letters.

- $0 \le \text{queryIndices}[i] < \text{s.length}$
