### 1. Description

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return *its corresponding column number*.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
```

### 2. Function Contract

**Inputs**

- `columnTitle`: A valid, non-empty Excel column title made from uppercase English letters.

**Return value**

Return the corresponding positive column number.

### 3. Examples

#### Example 1

- **Input:** $columnTitle = "A"$
- **Output:** `1`
#### Example 2

- **Input:** $columnTitle = "AB"$
- **Output:** `28`
#### Example 3

- **Input:** $columnTitle = "ZY"$
- **Output:** `701`

### 4. Constraints

- $1 \le \text{columnTitle.length} \le 7$

- `columnTitle` consists only of uppercase English letters.

- `columnTitle` is in the range `["A", "FXSHRXW"]`.