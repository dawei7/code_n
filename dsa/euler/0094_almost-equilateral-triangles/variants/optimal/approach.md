# Almost Equilateral Triangles - Optimal Approach

## Algorithm Explanation

Find the sum of perimeters of all almost equilateral triangles with integer sides $(a, a, b)$ ($b = a \pm 1$) and integer area, whose perimeter $P \le 1,000,000,000$.

### Pell Recurrence Derivation:
An isosceles triangle with sides $(a, a, b)$ has area $A = \frac{b}{4} \sqrt{4a^2 - b^2}$.

- **Case 1: $b = a + 1$** (Perimeter $P = 3a + 1$):
  The area condition leads to the Pell-type recurrence:
  $$a_{k} = 14 a_{k-1} - a_{k-2} - 4$$
  Starting with $a_0 = 1, a_1 = 5$.

- **Case 2: $b = a - 1$** (Perimeter $P = 3a - 1$):
  The area condition leads to the Pell-type recurrence:
  $$a_{k} = 14 a_{k-1} - a_{k-2} + 4$$
  Starting with $a_0 = 1, a_1 = 17$.

### Strategy:
Iterate both linear recurrences, accumulating $P = 3a \pm 1$ while $P \le 10^9$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log L)$ logarithmic iterations where $L = 10^9$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
