## Description

You are given a string `s` and an integer `t`, representing the number of **transformations** to perform. In one **transformation**, every character in `s` is replaced according to the following rules:

- If the character is `'z'`, replace it with the string `"ab"`.

- Otherwise, replace it with the **next** character in the alphabet. For example, `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.

Return the **length** of the resulting string after **exactly** `t` transformations.

Since the answer may be very large, return it **modulo**<!-- notionvc: eb142f2b-b818-4064-8be5-e5a36b07557a --> $10^{9} + 7$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abcyy", t = 2

**Output:** 7

**Explanation:**

- **First Transformation (t = 1)**:

		<li>`'a'` becomes `'b'`

- `'b'` becomes `'c'`

- `'c'` becomes `'d'`

- `'y'` becomes `'z'`

- `'y'` becomes `'z'`

- String after the first transformation: `"bcdzz"`

	</li>
- **Second Transformation (t = 2)**:

		<li>`'b'` becomes `'c'`

- `'c'` becomes `'d'`

- `'d'` becomes `'e'`

- `'z'` becomes `"ab"`

- `'z'` becomes `"ab"`

- String after the second transformation: `"cdeabab"`

	</li>
- **Final Length of the string**: The string is `"cdeabab"`, which has 7 characters.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "azbk", t = 1

**Output:** 5

**Explanation:**

- **First Transformation (t = 1)**:

		<li>`'a'` becomes `'b'`

- `'z'` becomes `"ab"`

- `'b'` becomes `'c'`

- `'k'` becomes `'l'`

- String after the first transformation: `"babcl"`

	</li>
- **Final Length of the string**: The string is `"babcl"`, which has 5 characters.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists only of lowercase English letters.

- $1 \le t \le 10^{5}$