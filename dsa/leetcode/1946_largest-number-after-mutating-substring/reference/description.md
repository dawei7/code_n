### 1. Description

You are given a string `num`, which represents a large integer. You are also given a **0-indexed** integer array `change` of length `10` that maps each digit `0-9` to another digit. More formally, digit `d` maps to digit $\text{change}[d]$.

You may **choose** to **mutate a single substring** of `num`. To mutate a substring, replace each digit $\text{num}[i]$ with the digit it maps to in `change` (i.e. replace $\text{num}[i]$ with $change[\text{num}[i]]$).

Return *a string representing the **largest** possible integer after **mutating** (or choosing not to) a **single substring** of *`num`.

A **substring** is a contiguous sequence of characters within the string.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $num = "<u>1</u>32", change = [9,8,5,0,3,6,4,2,6,8]$
- **Output:** `"<u>8</u>32"`
- **Explanation:** Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, "<u>1</u>32" becomes "<u>8</u>32".
"832" is the largest number that can be created, so return it.
#### Example 2

- **Input:** $num = "<u>021</u>", change = [9,4,3,5,7,2,1,9,0,6]$
- **Output:** `"<u>934</u>"`
- **Explanation:** Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, "<u>021</u>" becomes "<u>934</u>".
"934" is the largest number that can be created, so return it.
#### Example 3

- **Input:** $num = "5", change = [1,4,7,5,3,2,5,6,9,4]$
- **Output:** `"5"`
- **Explanation:** "5" is already the largest number that can be created, so return it.

### 4. Constraints

- $1 \le \text{num.length} \le 10^{5}$

- `num` consists of only digits `0-9`.

- $\text{change.length} = 10$

- $0 \le \text{change}[d] \le 9$