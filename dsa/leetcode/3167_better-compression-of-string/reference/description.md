## Description

You are given a string `compressed` representing a compressed version of a string. The format is a character followed by its frequency. For example, `"a3b1a1c2"` is a compressed version of the string `"aaabacc"`.

We seek a **better compression** with the following conditions:

- Each character should appear **only once** in the compressed version.

- The characters should be in **alphabetical order**.

Return the *better compression* of `compressed`.

**Note:** In the better version of compression, the order of letters may change, which is acceptable.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** compressed = "a3c9b2c1"

**Output:** "a3b2c10"

**Explanation:**

Characters "a" and "b" appear only once in the input, but "c" appears twice, once with a size of 9 and once with a size of 1.

Hence, in the resulting string, it should have a size of 10.

</div>
#### Example 2

<div class="example-block">
**Input:** compressed = "c2b3a1"

**Output:** "a1b3c2"

</div>
#### Example 3

<div class="example-block">
**Input:** compressed = "a2b4c1"

**Output:** "a2b4c1"

</div>
### Constraints

- $1 \le \text{compressed.length} \le 6 * 10^{4}$

- `compressed` consists only of lowercase English letters and digits.

- `compressed` is a valid compression, i.e., each character is followed by its frequency.

- Frequencies are in the range $[1, 10^{4}]$ and have no leading zeroes.