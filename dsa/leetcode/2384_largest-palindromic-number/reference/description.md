### 1. Description

You are given a string `num` consisting of digits only.

Return *the **largest palindromic** integer (in the form of a string) that can be formed using digits taken from *`num`. It should not contain **leading zeroes**.

### 2. Function Contract

**Inputs**

- `num`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Note

- You do **not** need to use all the digits of `num`, but you must use **at least** one digit.

- The digits can be reordered.

### 4. Examples

#### Example 1

- **Input:** $num = "444947137"$
- **Output:** `"7449447"`
- **Explanation:** Use the digits "4449477" from "<u>**44494**</u><u>**7**</u>13<u>**7**</u>" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.

#### Example 2

- **Input:** $num = "00009"$
- **Output:** `"9"`
- **Explanation:** It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.

### 5. Constraints

- $1 \le \text{num.length} \le 10^{5}$

- `num` consists of digits.
