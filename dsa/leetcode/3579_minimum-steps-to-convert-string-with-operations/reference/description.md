## Description

You are given two strings, `word1` and `word2`, of equal length. You need to transform `word1` into `word2`.

For this, divide `word1` into one or more **contiguous substrings**. For each substring `substr` you can perform the following operations:

- **Replace:** Replace the character at any one index of `substr` with another lowercase English letter.

- **Swap:** Swap any two characters in `substr`.

- **Reverse Substring:** Reverse `substr`.

Each of these counts as **one** operation and each character of each substring can be used in each type of operation at most once (i.e. no single index may be involved in more than one replace, one swap, or one reverse).

Return the **minimum number of operations** required to transform `word1` into `word2`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** word1 = "abcdf", word2 = "dacbe"

**Output:** 4

**Explanation:**

Divide `word1` into `"ab"`, `"c"`, and `"df"`. The operations are:

- For the substring `"ab"`,

		<li>Perform operation of type 3 on `"ab" -> "ba"`.

- Perform operation of type 1 on `"ba" -> "da"`.

	</li>
- For the substring `"c"` do no operations.

- For the substring `"df"`,

		<li>Perform operation of type 1 on `"df" -> "bf"`.

- Perform operation of type 1 on `"bf" -> "be"`.

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** word1 = "abceded", word2 = "baecfef"

**Output:** 4

**Explanation:**

Divide `word1` into `"ab"`, `"ce"`, and `"ded"`. The operations are:

- For the substring `"ab"`,

		<li>Perform operation of type 2 on `"ab" -> "ba"`.

	</li>
- For the substring `"ce"`,

		<li>Perform operation of type 2 on `"ce" -> "ec"`.

	</li>
- For the substring `"ded"`,

		<li>Perform operation of type 1 on `"ded" -> "fed"`.

- Perform operation of type 1 on `"fed" -> "fef"`.

	</li>

</div>
#### Example 3

<div class="example-block">
**Input:** word1 = "abcdef", word2 = "fedabc"

**Output:** 2

**Explanation:**

Divide `word1` into `"abcdef"`. The operations are:

- For the substring `"abcdef"`,

		<li>Perform operation of type 3 on `"abcdef" -> "fedcba"`.

- Perform operation of type 2 on `"fedcba" -> "fedabc"`.

	</li>

</div>
### Constraints

- $1 \le \text{word1.length} = \text{word2.length} \le 100$

- `word1` and `word2` consist only of lowercase English letters.