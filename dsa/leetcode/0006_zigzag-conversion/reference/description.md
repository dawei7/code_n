## Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`
Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```
### Function Contract

**Inputs**

- `s`: The string whose characters will be arranged.
- `numRows`: The positive number of zigzag rows.

**Return value**

Return the concatenation of the completed zigzag's rows from top to bottom.

### Examples
#### Example 1
```
- **Input:** `s = "PAYPALISHIRING", numRows = 3`
- **Output:** `"PAHNAPLSIIGYIR"`
#### Example 2

- **Input:** `s = "PAYPALISHIRING", numRows = 4`
- **Output:** `"PINALSIGYAHRPI"`
- **Explanation:**
P     I    N
A   L S  I G
Y A   H R
P     I
#### Example 3

- **Input:** `s = "A", numRows = 1`
- **Output:** `"A"`
### Constraints

- $1 \le \text{s.length} \le 1000$

- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.

- $1 \le numRows \le 1000$