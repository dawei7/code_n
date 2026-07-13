# Similar RGB Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 800 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/similar-rgb-color/) |

## Problem Description

### Goal

Given a lowercase RGB color `#RRGGBB`, find the most similar color that can be written in three-digit shorthand. A shorthand color `#RGB` expands to `#RRGGBB`, so each red, green, and blue byte must consist of one repeated hexadecimal digit.

Similarity is the negative sum of the squared numerical differences between corresponding RGB channels. Return the shorthand-expressible color with maximum similarity in lowercase six-digit form. Optimize the three channels together under that definition; an exact shorthand channel remains unchanged.

### Function Contract

**Inputs**

- `color`: a lowercase string in the form `#RRGGBB`.

**Return value**

- The lowercase `#RRGGBB` form of the shorthand-expressible color with maximum similarity to `color`.

### Examples

**Example 1**

- Input: `color = "#09f166"`
- Output: `"#11ee66"`
- Explanation: The closest repeated-digit values to hexadecimal `09`, `f1`, and `66` are `11`, `ee`, and `66`.

**Example 2**

- Input: `color = "#4e3fe1"`
- Output: `"#5544dd"`
- Explanation: Each RGB channel is independently rounded to its nearest shorthand value.

**Example 3**

- Input: `color = "#abcdef"`
- Output: `"#aaccee"`
- Explanation: The nearest repeated-digit values are `aa`, `cc`, and `ee`.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Recognize the shorthand channel values**

Repeating one hexadecimal digit `d` forms the byte `0xDD`, whose decimal value is $17 \cdot d$. Thus each channel of a shorthand color must be one of the 16 multiples of 17 from 0 through 255.

**Optimize each channel independently**

Color similarity is the negative sum of the squared differences in red, green, and blue. Because no term mixes two channels, maximizing the total is equivalent to choosing the nearest multiple of 17 for each channel separately.

For a channel value `v`, `(v + 8) // 17` gives the nearest shorthand digit index. Adjacent candidates are $17$ apart, so an integer value can never lie exactly halfway between them; adding $8$ selects the unique nearest multiple. Convert the index to one hexadecimal digit and repeat it twice. Independent nearest choices minimize every squared term, so their combined color uniquely maximizes similarity.

#### Complexity detail

The input always contains exactly three channels. Parsing, rounding, and formatting each one takes constant time and uses only a fixed amount of temporary storage, so both time and auxiliary space are $O(1)$.

#### Alternatives and edge cases

- **Scan 16 channel candidates:** Testing every shorthand value independently for each channel is correct and bounded, but arithmetic rounding avoids the repeated comparisons.
- **Enumerate all 4096 colors:** Comparing every three-digit shorthand color is also constant under the fixed format but performs unnecessary Cartesian-product work.
- **Round the packed RGB integer:** Treating all six digits as one number is incorrect because carries mix channels and do not minimize the three squared differences independently.
- **Exact shorthand channel:** A multiple of 17 remains unchanged.
- **Near zero or 255:** Rounding stays within digit indices `0` through `15`.
- **Apparent midpoint:** Since the gap is odd, no integer byte is equally distant from adjacent shorthand values.
- **Formatting:** Preserve the leading `#`, emit lowercase hexadecimal, and repeat each chosen digit.

</details>
