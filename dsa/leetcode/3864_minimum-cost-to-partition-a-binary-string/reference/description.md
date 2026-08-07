## Description

You are given a binary string `s` and two integers `encCost` and `flatCost`.

For each index `i`, $s[i] = '1'$ indicates that the $$i^{\text{th}}$$element is sensitive, and$s[i] = '0'$ indicates that it is not.

The string must be partitioned into **segments**. Initially, the entire string forms a single segment.

For a segment of length `L` containing `X` sensitive elements:

- If $X = 0$, the cost is `flatCost`.

- If `X > 0`, the cost is $L * X * encCost$.

If a segment has **even length**, you may split it into **two contiguous segments** of **equal** length and the cost of this split is the **sum** of **costs** of the resulting segments.

Return an integer denoting the **minimum possible total cost** over all valid partitions.
### Function Contract

**Inputs**

- `s`: A nonempty binary string in which `"1"` denotes a sensitive element.
- `encCost`: The positive multiplier used by any segment containing at least
  one sensitive element.
- `flatCost`: The cost of a segment containing no sensitive elements.

Let $N = \lvert\texttt{s}\rvert$. For a current segment with length $L$ and
$X$ occurrences of `"1"`, keeping it intact costs

$$
\begin{cases}
\texttt{flatCost}, & X = 0, \\
L X \cdot \texttt{encCost}, & X > 0.
\end{cases}
$$

A segment may remain intact. When $L$ is even, it may instead be replaced by
its left and right contiguous halves, each of length $L/2$, and those halves
follow the same rule independently. An odd-length segment cannot be split.

**Return value**

Return the minimum possible sum of final-segment costs over every valid
recursive equal-halving partition.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "1010", encCost = 2, flatCost = 1

**Output:** 6

**Explanation:**

- The entire string `s = "1010"` has length 4 and contains 2 sensitive elements, giving a cost of $4 * 2 * 2 = 16$.

- Since the length is even, it can be split into `"10"` and `"10"`. Each segment has length 2 and contains 1 sensitive element, so each costs $2 * 1 * 2 = 4$, giving a total of 8.

- Splitting both segments into four single-character segments yields the segments `"1"`, `"0"`, `"1"`, and `"0"`. A segment containing `"1"` has length 1 and exactly one sensitive element, giving a cost of $1 * 1 * 2 = 2$, while a segment containing `"0"` has no sensitive elements and therefore costs $flatCost = 1$.

- ​​​​​​​The total cost is thus $2 + 1 + 2 + 1 = 6$, which is the minimum possible total cost.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "1010", encCost = 3, flatCost = 10

**Output:** 12

**Explanation:**

- The entire string `s = "1010"` has length 4 and contains 2 sensitive elements, giving a cost of $4 * 2 * 3 = 24$.

- Since the length is even, it can be split into two segments `"10"` and `"10"`.

- Each segment has length 2 and contains one sensitive element, so each costs $2 * 1 * 3 = 6$, giving a total of 12, which is the minimum possible total cost.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "00", encCost = 1, flatCost = 2

**Output:** 2

**Explanation:**

The string `s = "00"` has length 2 and contains no sensitive elements, so storing it as a single segment costs $flatCost = 2$, which is the minimum possible total cost.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists only of `'0'` and `'1'`.

- $1 \le encCost, flatCost \le 10^{5}$