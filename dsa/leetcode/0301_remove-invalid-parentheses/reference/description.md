### 1. Description

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return *a list of **unique strings** that are valid with the minimum number of removals*. You may return the answer in **any order**.

### 2. Function Contract

**Inputs**

- `s`: A string made from lowercase English letters and parentheses.

**Return value**

Return all distinct valid strings that use the minimum possible number of parenthesis deletions, in any order.

### 3. Examples

#### Example 1

- **Input:** `s = "()())()"`
- **Output:** `["(())()","()()()"]`

#### Example 2

- **Input:** `s = "(a)())()"`
- **Output:** `["(a())()","(a)()()"]`

#### Example 3

- **Input:** `s = ")("`
- **Output:** `[""]`

### 4. Constraints

- $1 \le \text{s.length} \le 25$

- `s` consists of lowercase English letters and parentheses `'('` and `')'`.

- There will be at most `20` parentheses in `s`.
