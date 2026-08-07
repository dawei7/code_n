## Description

You are given a string `s` consisting of lowercase English letters.

A **run** in `s` is a **substring** of **equal** letters that cannot be extended further. For example, the runs in `"hello"` are `"h"`, `"e"`, `"ll"`, and `"o"`.

You can **select** runs that have the **same** length in `s`.

Return an integer denoting the **maximum** number of runs you can select in `s`.
### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string whose maximal equal-character runs are examined.

Every position belongs to exactly one run. Run identity depends on maximal boundaries and its character, but selection compatibility depends only on run length.

**Return value**

Return the highest frequency of any run length in `s`. Runs may contain different letters; they need only have the same number of characters.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "hello"

**Output:** 3

**Explanation:**

The runs in `s` are `"h"`, `"e"`, `"ll"`, and `"o"`. You can select `"h"`, `"e"`, and `"o"` because they have the same length 1.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aaabaaa"

**Output:** 2

**Explanation:**

The runs in `s` are `"aaa"`, `"b"`, and `"aaa"`. You can select `"aaa"` and `"aaa"` because they have the same length 3.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters only.