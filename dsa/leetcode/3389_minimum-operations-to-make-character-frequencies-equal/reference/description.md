### 1. Description

You are given a string `s`.

A string `t` is called **good** if all characters of `t` occur the same number of times.

You can perform the following operations **any number of times**:

- Delete a character from `s`.

- Insert a character in `s`.

- Change a character in `s` to its next letter in the alphabet.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that you cannot change `'z'` to `'a'` using the third operation.

Return* *the **minimum** number of operations required to make `s` **good**.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** s = "acab"

**Output:** 1

**Explanation:**

We can make `s` good by deleting one occurrence of character `'a'`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "wddw"

**Output:** 0

**Explanation:**

We do not need to perform any operations since `s` is initially good.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aaabc"

**Output:** 2

**Explanation:**

We can make `s` good by applying these operations:

- Change one occurrence of `'a'` to `'b'`

- Insert one occurrence of `'c'` into `s`

</div>

### 5. Constraints

- $3 \le \text{s.length} \le 2 * 10^{4}$

- `s` contains only lowercase English letters.