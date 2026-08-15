### 1. Description

You are given a string `s`.

Your task is to remove **all** digits by doing this operation repeatedly:

- Delete the *first* digit and the **closest** **non-digit** character to its *left*.

Return the resulting string after removing all digits.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Note

that the operation *cannot* be performed on a digit that does not have any non-digit character to its left.

### 4. Examples

#### Example 1

- **Input:** s = "abc"

- **Output:** "abc"

- **Explanation:** There is no digit in the string.<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde -->

#### Example 2

- **Input:** s = "cb34"

- **Output:** ""

- **Explanation:** First, we apply the operation on $s[2]$, and `s` becomes `"c4"`.

Then we apply the operation on $s[1]$, and `s` becomes `""`.

### 5. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters and digits.

- The input is generated such that it is possible to delete all digits.
