### 1. Description

You are given a string array `words`, consisting of **distinct** 4-letter strings, each containing lowercase English letters.

A **word square** consists of 4 **distinct** words: `top`, `left`, `right` and `bottom`, arranged as follows:

- `top` forms the **top row**.

- `bottom` forms the **bottom row**.

- `left` forms the **left column** (top to bottom).

- `right` forms the **right column** (top to bottom).

It must satisfy:

- $\text{top}[0] = \text{left}[0]$, $\text{top}[3] = \text{right}[0]$

- $\text{bottom}[0] = \text{left}[3]$, $\text{bottom}[3] = \text{right}[3]$

Return all valid **distinct** word squares, sorted in **ascending lexicographic** order by the 4-tuple `(top, left, right, bottom)`.

### 2. Function Contract

**Inputs**

- `words`: An array of distinct lowercase strings, each with length four.

Each returned square must use four different entries from `words`; a word cannot fill more than one side of the same square.

**Return value**

Return a list of all valid four-word arrays in the role order `[top, left, right, bottom]`. Order that outer list lexicographically by those four positions. Return an empty list when no valid square exists.

### 3. Examples

#### Example 1

- **Input:** words = ["able","area","echo","also"]

- **Output:** [["able","area","echo","also"],["area","able","also","echo"]]

- **Explanation:** There are exactly two valid 4-word squares that satisfy all corner constraints:

- `"able"` (top), `"area"` (left), `"echo"` (right), `"also"` (bottom)

		- $\text{top}[0] = \text{left}[0] = 'a'$

- $\text{top}[3] = \text{right}[0] = 'e'$

- $\text{bottom}[0] = \text{left}[3] = 'a'$

- $\text{bottom}[3] = \text{right}[3] = 'o'$

- `"area"` (top), `"able"` (left), `"also"` (right), `"echo"` (bottom)

		- All corner constraints are satisfied.

Thus, the answer is `[["able","area","echo","also"],["area","able","also","echo"]]`.

#### Example 2

- **Input:** words = ["code","cafe","eden","edge"]

- **Output:** []

- **Explanation:** No combination of four words satisfies all four corner constraints. Thus, the answer is empty array `[]`.

### 4. Constraints

- $4 \le \text{words.length} \le 15$

- $\text{words}[i].length = 4$

- $\text{words}[i]$ consists of only lowercase English letters.

- All $\text{words}[i]$ are **distinct**.
