### 1. Description

You are given a string `s` consisting only of the characters `'1'` and `'2'`.

You may delete any number of characters from `s` without changing the order of the remaining characters.

Return the **largest possible resultant string** that represents an **even** integer. If there is no such string, return the empty string `""`.

### 2. Function Contract

**Inputs**

- `s`: A nonempty decimal string whose characters are all `'1'` or `'2'`.

The result must be a subsequence of `s`: characters may be deleted, but retained characters cannot be reordered. Every nonempty candidate has no leading zero because zero never occurs in the input.

**Return value**

Return the string representation of the largest attainable even integer. Return `""` when no such nonempty subsequence exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "1112"

**Output:** "1112"

**Explanation:**

The string already represents the largest possible even number, so no deletions are needed.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "221"

**Output:** "22"

**Explanation:**

Deleting `'1'` results in the largest possible even number which is equal to 22.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "1"

**Output:** ""

**Explanation:**

There is no way to get an even number.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists only of the characters `'1'` and `'2'`.