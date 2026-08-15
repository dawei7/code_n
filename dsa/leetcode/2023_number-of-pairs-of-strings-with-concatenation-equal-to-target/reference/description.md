### 1. Description

Given an array of **digit** strings `nums` and a **digit** string `target`, return *the number of pairs of indices *`(i, j)`* (where *$i \neq j$*) such that the **concatenation** of *$\text{nums}[i] + \text{nums}[j]$* equals *`target`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[str]`).
- `target`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = ["777","7","77","77"], target = "7777"`
- **Output:** `4`
- **Explanation:** Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

#### Example 2

- **Input:** `nums = ["123","4","12","34"], target = "1234"`
- **Output:** `2`
- **Explanation:** Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"

#### Example 3

- **Input:** `nums = ["1","1","1"], target = "11"`
- **Output:** `6`
- **Explanation:** Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"

### 4. Constraints

- $2 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i].length \le 100$

- $2 \le \text{target.length} \le 100$

- $\text{nums}[i]$ and `target` consist of digits.

- $\text{nums}[i]$ and `target` do not have leading zeros.
