### 1. Description

Given two **version strings**, `version1` and `version2`, compare them. A version string consists of **revisions** separated by dots `'.'`. The **value of the revision** is its **integer conversion** ignoring leading zeros.

To compare version strings, compare their revision values in **left-to-right order**. If one of the version strings has fewer revisions, treat the missing revision values as `0`.

Return the following:

- If `version1 < version2`, return -1.

- If `version1 > version2`, return 1.

- Otherwise, return 0.

### 2. Function Contract

**Inputs**

- `version1`: The first valid dot-separated version string.
- `version2`: The second valid dot-separated version string.

**Return value**

Return `-1` when the first version is smaller, `1` when it is larger, and `0` when their revision values are equal.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** version1 = "1.2", version2 = "1.10"

**Output:** -1

**Explanation:**

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

</div>
#### Example 2

<div class="example-block">
**Input:** version1 = "1.01", version2 = "1.001"

**Output:** 0

**Explanation:**

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

</div>
#### Example 3

<div class="example-block">
**Input:** version1 = "1.0", version2 = "1.0.0.0"

**Output:** 0

**Explanation:**

version1 has less revisions, which means every missing revision are treated as "0".

</div>

### 4. Constraints

- $1 \le \text{version1.length}, \text{version2.length} \le 500$

- `version1` and `version2` only contain digits and `'.'`.

- `version1` and `version2` **are valid version numbers**.

- All the given revisions in `version1` and `version2` can be stored in a **32-bit integer**.