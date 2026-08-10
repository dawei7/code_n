## General

**Reducing the requested average to three statistics**

An arithmetic mean is the sum of the included values divided by how many values are included. The input has $N$ salaries. Exactly one is the minimum and exactly one is the maximum because all salaries are unique. After excluding those two employees, $N-2$ salaries remain.

Instead of constructing a filtered list, the stored solution computes the sum of all salaries and subtracts the two excluded values:

$$
S_{\text{middle}}
=
\left(\sum_{i=0}^{N-1} salary[i]\right)
- \min(salary)
- \max(salary).
$$

The line `s = sum(salary) - min(salary) - max(salary)` implements this identity. The return statement divides `s` by `len(salary) - 2`, the number of remaining employees.

This is an algebraic filtering technique. Every salary initially contributes once to the total. Subtracting the minimum removes its one contribution, and subtracting the maximum removes its one contribution. Every other salary remains exactly once.

**Following the exact Python behavior**

`sum(salary)` iterates through the list and adds every integer. `min(salary)` makes another traversal to find the least value, and `max(salary)` makes a third traversal to find the greatest value. The expression then performs two integer subtractions and assigns the middle-salary total to `s`.

`len(salary)` is constant time for a Python list because the list stores its current length. The denominator is at least one under the constraint $N \ge 3$, so division by zero cannot occur.

Python's slash operator performs true division. Even when both operands are integers, `s / (len(salary) - 2)` returns a floating-point value. No manual cast is needed, unlike languages in which integer divided by integer truncates the fractional part.

The function does not sort, overwrite, or otherwise mutate `salary`. The three built-ins inspect it and the remaining operations use scalar values.

**Why uniqueness matters**

Uniqueness makes the phrase “the minimum and maximum salary” correspond to two distinct employees and two distinct values. Subtracting each extreme once removes exactly those employees.

Even if duplicate extreme values were allowed, the formula would still subtract one occurrence of each numeric extreme, but that might not match a different contract that intended to exclude every employee tied for minimum or maximum. The given uniqueness guarantee removes that ambiguity. It also ensures the minimum and maximum cannot be the same because there are at least three distinct values.

**Why sorting is unnecessary**

Sorting would place the minimum first and maximum last, making the desired elements easy to slice. However, ordering all values solves a stronger problem than needed. The answer depends only on total sum, least value, greatest value, and count. These statistics can be obtained with linear scans, so no relative ordering among middle salaries is required.

For `[4000, 3000, 1000, 2000]`, the total is `10000`, the minimum is `1000`, and the maximum is `4000`. The middle total is therefore `5000`. Two employees remain, so the returned average is `2500.0`. Their positions in the original list do not matter.

**Why the formula is correct**

Let the salary values be a set of $N$ unique integers, with minimum $m$ and maximum $M$. Split the full sum into the excluded values and all remaining values:

$$
\sum salary[i] = m + M + S_{\text{middle}}.
$$

Rearranging gives

$$
S_{\text{middle}} = \sum salary[i] - m - M,
$$

which is exactly how `s` is calculated. Removing two of $N$ employees leaves $N-2$. Dividing the remaining sum by that count is the definition of their arithmetic mean. Therefore, the returned value is the requested average.

The accepted tolerance of $10^{-5}$ means normal floating-point representation is sufficient for these bounded integers. The mathematical average may not have a finite binary representation, but Python returns its closest ordinary floating-point approximation, and the comparison tolerance accommodates that.

## Complexity detail

Let $N$ be the number of salaries. `sum` scans $N$ elements, `min` scans $N$ elements, and `max` scans $N$ elements. Three linear passes take $3N$ element visits, which simplifies to $O(N)$ time. The exact implementation is therefore linear even though it is not literally a single-pass loop.

The method stores only `s` and temporary scalar results produced while evaluating the expression. It creates no list, set, or sorted copy whose size depends on $N$. Its auxiliary space is $O(1)$.

Python integers can grow beyond fixed machine width, so a bit-level analysis could include the cost of large-integer addition. Under the stated salary and length bounds, the total is comfortably small, and the standard unit-cost $O(N)$ analysis applies.

A hand-written one-pass version could update sum, minimum, and maximum together. It would still be $O(N)$ time and $O(1)$ space; it merely reduces the constant number of traversals. The built-in version is concise and delegates its loops to optimized runtime code.

## Alternatives and edge cases

- **Single explicit pass:** Maintain running total, minimum, and maximum together, then apply the same formula. It has identical asymptotic bounds and one traversal, but more source code and initialization details.
- **Sorting:** Sort salaries and average the middle slice. This is easy to visualize but takes $O(N \log N)$ time and may mutate the input or allocate a copy.
- **Filtering by value:** Find both extremes, then sum values unequal to them. It is correct under uniqueness but requires additional passes and can become semantically wrong if a future contract allows tied extremes but excludes only one employee at each end.
- **Smallest valid length:** With three salaries, one middle employee remains. The denominator is one, so the result is exactly that employee's salary as a float.
- **Fractional average:** Python true division retains a fractional result instead of truncating it.
- **Unique extremes:** The guarantees ensure that subtracting minimum and maximum removes two different list elements.
- **Input order:** Salaries may appear in any order; sum, minimum, and maximum are order-independent.
- **No mutation:** The source leaves the caller's list unchanged, unlike an in-place sorting solution.
- **Floating-point tolerance:** A repeating or non-binary-exact average is acceptable within the stated tolerance; rounding the result to an integer would not be acceptable.
- **Hypothetical fewer than three values:** The denominator could be zero or negative, but those inputs are excluded by the contract.
- **Large numeric total:** The bounded data is safe, and Python integer summation does not overflow fixed-width storage.
