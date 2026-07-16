# Best Position for a Service Centre

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1515 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/best-position-for-a-service-centre/) |

## Problem Description
### Goal

A delivery company knows the Cartesian coordinates of all customers in a city. It may place one service centre at any real-valued point in the plane, not only at an existing customer position or an integer coordinate.

Choose the centre so that the sum of its Euclidean distances to every customer is as small as possible, and return that minimum total. An answer within $10^{-5}$ of the true value is accepted.

### Function Contract
**Inputs**

Let $n$ be the number of customer positions and $I$ the fixed number of ternary-search iterations used per coordinate.

- `positions`: A list of $n$ coordinate pairs `[x_i, y_i]`, where $1 \leq n \leq 50$.
- Each coordinate is an integer in the inclusive range from 0 through 100.
- The service centre may use arbitrary real coordinates.

**Return value**

Return the minimum possible value of

$$
\sum_{i=1}^{n}\sqrt{(x-x_i)^2+(y-y_i)^2}
$$

over all real centre positions $(x,y)$.

### Examples
**Example 1**

- Input: `positions = [[0, 1], [1, 0], [1, 2], [2, 1]]`
- Output: `4.0`
- Explanation: Placing the centre at `(1, 1)` gives distance 1 to each customer.

**Example 2**

- Input: `positions = [[1, 1], [3, 3]]`
- Output: `2.82843`
- Explanation: Every point on the segment between the two customers has the same minimum total, equal to their separation.

**Example 3**

- Input: `positions = [[1, 1]]`
- Output: `0.0`

### Required Complexity

- **Time:** $O(nI^2)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use convexity of the geometric-median objective**

For any fixed centre, summing its distances to the customers defines a convex function over the plane. Its restriction to any horizontal or vertical line is therefore convex and unimodal: moving along that line reaches one minimum region and cannot create separated local minima.

The optimum lies inside the axis-aligned bounding box of the customer points. Outside that box, moving toward it decreases every coordinatewise separation and cannot worsen the total distance. These finite coordinate bounds make tolerance-controlled search possible.

**Minimize one coordinate inside the other**

For a fixed $x$, ternary-search $y$ between the minimum and maximum customer $y$ coordinates. Compare the objective at the two trisection points and discard the third that cannot contain the minimum. After $I$ iterations, evaluate the midpoint of the narrow remaining interval; call this minimized value $g(x)$.

Partial minimization preserves convexity, so $g(x)=\min_y f(x,y)$ is convex in $x$. Apply the same ternary search to $x$, calling the inner $y$ search for each comparison. The verified native artifact uses seventy iterations per dimension, while the traced app-local adapter uses forty-five. Even forty-five shrinks an initial width of at most 100 to roughly $10^{-6}$, below the required $10^{-5}$ output tolerance.

**Why the returned value is globally minimal**

Each inner search converges to the global minimum on its vertical line because that restriction is convex. The outer search then minimizes the convex function formed by those exact line minima. As both retained intervals shrink geometrically, the final point approaches the two-dimensional geometric median and its objective approaches the global minimum.

The objective value, rather than the centre coordinates, is returned. This matters when the minimizer is not unique, such as two customers: every point on their connecting segment gives the same optimal total.

#### Complexity detail

One objective evaluation scans all $n$ positions in $O(n)$ time. An inner search performs $O(I)$ evaluations, and the outer search invokes two inner searches in each of $O(I)$ iterations. Total time is $O(nI^2)$.

The coordinate bounds, trisection points, and running totals occupy constant auxiliary state. The input positions are read directly, so extra space is $O(1)$.

#### Alternatives and edge cases

- **Weiszfeld's algorithm:** iteratively computes a weighted average using inverse distances and often converges quickly. A robust implementation must handle an iterate that lands exactly on a customer.
- **Shrinking-step hill climbing:** move toward improving neighboring points and reduce the step when none improves. Convexity makes it practical, but direction choice and stopping tolerance require care.
- **Gradient descent:** the objective is convex but nondifferentiable at customer positions, so a naive gradient formula can divide by zero or oscillate.
- **Integer grid search:** restricting the centre to integer coordinates is incorrect because the geometric median may have fractional coordinates.
- **Single customer:** placing the centre at that customer yields zero.
- **Two customers:** the minimum equals their Euclidean separation and is attained along the entire connecting segment.
- **Repeated positions:** duplicates increase that location's weight and may pull the optimum onto the repeated point.
- **Collinear customers:** the problem reduces to a one-dimensional median along their line.
- **Symmetric configuration:** symmetry often identifies the centre, but the algorithm does not rely on it.
- **Nonsmooth optimum:** ternary comparisons use objective values only and do not require derivatives.

</details>
