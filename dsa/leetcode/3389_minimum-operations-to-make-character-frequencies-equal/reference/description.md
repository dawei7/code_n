### 1. Description

You are given a string `s`.

A string `t` is called **good** if all characters of `t` occur the same number of times.

You can perform the following operations **any number of times**:

- Delete a character from `s`.

- Insert a character in `s`.

- Change a character in `s` to its next letter in the alphabet.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Note

that you cannot change `'z'` to `'a'` using the third operation.

Return* *the **minimum** number of operations required to make `s` **good**.

### 4. Examples

#### Example 1

- **Input:** s = "acab"

- **Output:** 1

- **Explanation:** We can make `s` good by deleting one occurrence of character `'a'`.

#### Example 2

- **Input:** s = "wddw"

- **Output:** 0

- **Explanation:** We do not need to perform any operations since `s` is initially good.

#### Example 3

- **Input:** s = "aaabc"

- **Output:** 2

- **Explanation:** We can make `s` good by applying these operations:

- Change one occurrence of `'a'` to `'b'`

- Insert one occurrence of `'c'` into `s`

### 5. Constraints

- $3 \le \text{s.length} \le 2 * 10^{4}$

- `s` contains only lowercase English letters.
