# Number of Burgers with No Waste of Ingredients

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1276 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/) |

## Problem Description

### Goal

Two burger sizes consume ingredients differently. Each jumbo burger requires four tomato slices and one cheese slice, while each small burger requires two tomato slices and one cheese slice.

Given the available numbers of tomato and cheese slices, determine nonnegative counts of jumbo and small burgers that use every slice of both ingredients, leaving no waste. Return the counts with jumbo burgers first. If no such combination exists, return an empty list.

### Function Contract

**Inputs**

- `tomato_slices`: the available tomato-slice count, where $0 \le \texttt{tomato_slices} \le 10^7$.
- `cheese_slices`: the available cheese-slice count, where $0 \le \texttt{cheese_slices} \le 10^7$.

**Return value**

- Return `[jumbo, small]` when nonnegative integers satisfy both $4\,\textit{jumbo}+2\,\textit{small}=\texttt{tomato_slices}$ and $\textit{jumbo}+\textit{small}=\texttt{cheese_slices}$. Return `[]` if no such counts exist.

### Examples

**Example 1**

- Input: `tomato_slices = 16, cheese_slices = 7`
- Output: `[1,6]`

**Example 2**

- Input: `tomato_slices = 17, cheese_slices = 4`
- Output: `[]`

**Example 3**

- Input: `tomato_slices = 4, cheese_slices = 17`
- Output: `[]`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Let $j$ be the number of jumbo burgers and $s$ the number of small burgers. Cheese gives $j+s=\texttt{cheese_slices}$. If every cheese slice were initially assigned to a small burger, that would consume twice as many tomato slices as cheese slices. Changing one of those burgers from small to jumbo consumes two additional tomato slices, so

$$
j = \frac{\texttt{tomato_slices}-2\,\texttt{cheese_slices}}{2},
\qquad
s = \texttt{cheese_slices}-j.
$$

These equations determine at most one answer. It is valid only when the numerator for $j$ is even and both computed counts are nonnegative. Those checks also cover having too few tomatoes to make every burger small or too many tomatoes even if every burger is jumbo. When all conditions hold, substituting the two values back into the equations accounts for every tomato and cheese slice exactly.

#### Complexity detail

The method performs a fixed number of integer arithmetic operations and comparisons, independent of the ingredient counts, for $O(1)$ time and $O(1)$ auxiliary space. The benchmark uses the total burger count as its scaling size and contrasts this direct calculation with enumerating possible jumbo counts.

#### Alternatives and edge cases

- **Enumerate jumbo counts:** Trying every value from zero through `cheese_slices` finds the same unique answer but requires $O(\texttt{cheese_slices})$ time.
- **Solve with floating-point arithmetic:** It risks unnecessary representation and equality problems; the equations and divisibility conditions are entirely integral.
- **Odd tomato count:** Every burger consumes an even number of tomato slices, so no solution exists.
- **No ingredients:** `[0,0]` is valid because it uses both zero totals without waste.
- **All one size:** Either computed count may be zero and remains a valid answer.
- **Insufficient or excess tomatoes:** Counts outside the range from twice to four times the cheese count make one computed burger count negative.

</details>
