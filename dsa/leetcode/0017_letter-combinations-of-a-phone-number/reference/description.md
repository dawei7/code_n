## Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](images/1200px-telephone-keypad2svg.png)
### Function Contract

**Inputs**

- `digits`: A non-empty string of telephone digits from `2` through `9`.

**Return value**

Return all strings formed by selecting one mapped letter for each digit, in any order.

### Examples

#### Example 1

- **Input:** $digits = "23"$
- **Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
#### Example 2

- **Input:** $digits = "2"$
- **Output:** `["a","b","c"]`
### Constraints

- $1 \le \text{digits.length} \le 4$

- $\text{digits}[i]$ is a digit in the range `['2', '9']`.