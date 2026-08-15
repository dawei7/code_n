### 1. Description

Given a `rows x cols` screen and a `sentence` represented as a list of strings, return *the number of times the given sentence can be fitted on the screen*.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

### 2. Function Contract

**Inputs**

- `sentence`: The non-empty ordered list of lowercase words to repeat.
- `rows`: The number of rows on the screen.
- `cols`: The number of character columns in each row.

**Return value**

Return the number of complete repetitions of `sentence` that fit while filling the screen from left to right and
top to bottom under the word and spacing rules.

### 3. Examples

#### Example 1

- **Input:** $sentence = ["hello","world"], rows = 2, cols = 8$
- **Output:** `1`
- **Explanation:** hello---
world---
The character '-' signifies an empty space on the screen.

#### Example 2

- **Input:** $sentence = ["a", "bcd", "e"], rows = 3, cols = 6$
- **Output:** `2`
- **Explanation:** a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.

#### Example 3

- **Input:** $sentence = ["i","had","apple","pie"], rows = 4, cols = 5$
- **Output:** `1`
- **Explanation:** i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.

### 4. Constraints

- $1 \le \text{sentence.length} \le 100$

- $1 \le \text{sentence}[i].length \le 10$

- $\text{sentence}[i]$ consists of lowercase English letters.

- $1 \le rows, cols \le 2 * 10^{4}$
