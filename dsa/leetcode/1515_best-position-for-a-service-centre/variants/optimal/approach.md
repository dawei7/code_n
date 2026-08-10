## General

**The objective is the geometric median**

For candidate center `(x, y)`, the objective is

$$
F(x,y)
=
\sum_i \sqrt{(x-x_i)^2+(y-y_i)^2}.
$$

This is a convex function. Unlike squared distance, ordinary Euclidean distance is not minimized simply by taking coordinate averages. The minimizing point is called a geometric median.

The stored solution uses iterative gradient descent with a decaying step size. It begins at the arithmetic mean of all customer x-coordinates and y-coordinates. The centroid is not always the geometric median, but it is a reasonable central starting point.

**Computing the gradient direction**

For a center not exactly equal to customer `i`, that customer's distance contributes gradient

$$
\left(
\frac{x-x_i}{d_i},
\frac{y-y_i}{d_i}
\right),
$$

where $d_i$ is the Euclidean distance.

The source loops over all positions, computes `a = x - x1`, `b = y - y1`, and `c = sqrt(a * a + b * b)`. It adds `a / (c + 1e-8)` and `b / (c + 1e-8)` to the gradient components. It also accumulates `dist += c` as the current objective value.

The small denominator addition regularizes the undefined gradient when the candidate exactly matches a customer. At zero distance, both numerators are zero, so that customer's contribution becomes zero rather than causing division by zero.

**Taking and shrinking steps**

The initial learning rate `alpha` is 0.5. The proposed movement is

`dx = grad_x * alpha` and `dy = grad_y * alpha`.

The source subtracts these quantities from the current coordinates, moving opposite the gradient toward lower objective values.

After every iteration, `alpha *= 0.999`. This exponential decay gradually reduces movement size. The loop returns when both coordinate changes have absolute value at most `1e-6`.

The returned `dist` was computed at the position before that final tiny update. Since the final movement is small, it is intended as an approximation at essentially the converged location.

**Why the direction is sensible**

Each customer contributes a unit vector pointing from that customer toward the candidate. Their sum points in a direction of increasing total distance. Subtracting it pulls the candidate toward the balance point of all customer directions.

At a differentiable optimum, those direction vectors sum to zero. Convexity means any point satisfying the appropriate zero-gradient or subgradient condition is globally optimal rather than merely locally optimal.

The centroid initialization lies within the coordinate-wise customer range, and iterative pulls generally keep the search near the customer cloud.

**What the stopping condition does and does not prove**

Because each normalized component has magnitude at most approximately one, each gradient component is bounded by the number of customers. Since `alpha` decays geometrically toward zero, `dx` and `dy` will eventually become smaller than `eps`, so the loop terminates.

However, a tiny step can occur because the gradient is small or merely because `alpha` became tiny. The stopping test does not explicitly verify that the objective is within $10^{-5}$ of the mathematical minimum. A geometrically decaying schedule has finite total future travel, and the regularized gradient slightly changes behavior at customer locations.

Thus this is a practical numerical heuristic for the convex geometric-median problem, not a formal precision certificate. The documentation should not claim stronger convergence guarantees than the exact source establishes.

**Special geometric cases**

With one customer, the centroid equals that point, every computed difference is zero, and the method returns zero after the first tiny-step check.

With two customers, every point on the segment between them has the same minimum total distance equal to the distance between customers. Their midpoint centroid is already one such minimizer.

Symmetric configurations often place the centroid at the geometric median, giving an immediate near-zero gradient.

## Complexity detail

Let $N$ be the number of customer positions and $T$ the number of iterations until the step-size condition is met. Each iteration scans all $N$ points and uses constant extra state, so exact time is $O(NT)$ and auxiliary space is $O(1)$ beyond the input.

The manifest states $O(nI^2)$ time. The stored source contains one iteration loop and one customer loop, not two nested iteration dimensions. If $I$ denotes its number of gradient steps, the direct bound is $O(nI)$.

Because gradient components are bounded and `alpha` decays by 0.999, termination can be related to the logarithm of the initial scale divided by `eps`. Actual $T$ also depends on when both component steps become small. Numerical arithmetic uses ordinary floating point.

## Alternatives and edge cases

- **Weiszfeld's algorithm:** A specialized geometric-median iteration often converges faster, but it needs careful handling when the iterate lands on a customer point.
- **Nested ternary search:** Convexity can support searches over coordinates with inner and outer iterations, which may explain an $I^2$ style bound but is not the stored method.
- **Hill climbing over directions:** Repeatedly test neighboring positions while shrinking a spatial step. It is intuitive but also approximate.
- **One customer:** The exact minimum sum is zero at that customer's location.
- **Two customers:** Every point on their connecting segment is optimal.
- **Duplicate positions:** The regularizing denominator avoids division by zero and naturally gives that location extra weight through repeated entries.
- **Symmetric positions:** Vector contributions cancel at the center.
- **Centroid is not generally optimal:** It is only the initial guess for ordinary-distance minimization.
- **Tiny alpha:** It guarantees eventual small updates but not independently certified objective accuracy.
- **Returned iteration value:** `dist` corresponds to the pre-update point of the terminating iteration.
- **Required import:** `sqrt` must be available from `math`.
