### 1. Description

Given an integer `columnNumber`, return *its corresponding column title as it appears in an Excel sheet*.

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

- `columnNumber`: A positive integer column number.

**Return value**

Return its Excel-style uppercase column title.

### 3. Examples

#### Example 1

- **Input:** $columnNumber = 1$
- **Output:** `"A"`

#### Example 2

- **Input:** $columnNumber = 28$
- **Output:** `"AB"`

#### Example 3

- **Input:** $columnNumber = 701$
- **Output:** `"ZY"`

### 4. Constraints

- $1 \le columnNumber \le 2^{31} - 1$
