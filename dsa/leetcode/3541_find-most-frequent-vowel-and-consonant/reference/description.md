## Description

You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`).

Your task is to:

- Find the vowel (one of `'a'`, `'e'`, `'i'`, `'o'`, or `'u'`) with the **maximum** frequency.

- Find the consonant (all other letters excluding vowels) with the **maximum** frequency.

Return the sum of the two frequencies.

**Note**: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The **frequency** of a letter `x` is the number of times it occurs in the string.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "successes"

**Output:** 6

**Explanation:**

- The vowels are: `'u'` (frequency 1), `'e'` (frequency 2). The maximum frequency is 2.

- The consonants are: `'s'` (frequency 4), `'c'` (frequency 2). The maximum frequency is 4.

- The output is $2 + 4 = 6$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aeiaeia"

**Output:** 3

**Explanation:**

- The vowels are: `'a'` (frequency 3), `'e'` ( frequency 2), `'i'` (frequency 2). The maximum frequency is 3.

- There are no consonants in `s`. Hence, maximum consonant frequency = 0.

- The output is $3 + 0 = 3$.

</div>
### Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists of lowercase English letters only.