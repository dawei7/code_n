# Estimating Pi via Monte Carlo

| | |
|---|---|
| **ID** | `randomized_06` |
| **Category** | randomized |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 1/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) |

## Problem statement

Given an integer `N` representing the number of iterations, estimate the mathematical constant \pi (Pi) using purely randomized geometry.

**Input:** An integer `N` (e.g. 1,000,000).
**Output:** A floating point number estimating \pi.

## When to use it

- The absolute "Hello World" of Monte Carlo simulations.
- Used to teach how probabilistic sampling can approximate complex mathematical integrals that are too difficult to solve analytically.

## Approach

Imagine a square with side lengths of 2, centered at the origin `(0, 0)`.
The area of this square is 2 x 2 = 4.
Now, draw a circle with radius 1, also centered at `(0, 0)`. This circle perfectly touches the edges of the square.
The area of this circle is \pi \cdot r^2 = \pi \cdot 1^2 = \pi.

The ratio of the Area of the Circle to the Area of the Square is exactly \frac{\pi}{4}.

**The Monte Carlo Method:**
If we generate millions of completely random points uniformly distributed inside the square, a certain percentage of them will land inside the circle.
Statistically, the ratio of (Points inside Circle) / (Total Points) will converge to exactly the ratio of their areas!

\frac{\text{Points Inside}}{\text{Total Points}} ~= \frac{\text{Area Circle}}{\text{Area Square}} = \frac{\pi}{4}

Therefore:
\pi ~= 4 x \frac{\text{Points Inside}}{\text{Total Points}}

**How to check if a point is inside the circle?**
Using the Pythagorean theorem, a point `(x, y)` is inside the unit circle if its distance from the origin `(0, 0)` is less than or equal to the radius `1`.
x^2 + y^2 \le 1^2

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_06: Estimating Pi via Monte Carlo.

Estimate the value of pi using the Monte Carlo
"""


def solve(n, seed_value):
    """Estimate pi via Monte Carlo: count points (x, y) in
    [0, 1]^2 with x^2 + y^2 <= 1, return 4 * (count / n)."""
    import random
    rng = random.Random(seed_value)
    inside = 0
    for _ in range(n):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / n
```

</details>

## Walk-through

`iterations = 4`

1. Random point: `(0.5, 0.5)`. 0.5^2 + 0.5^2 = 0.25 + 0.25 = 0.5. `0.5 <= 1`. Inside! `points = 1`.
2. Random point: `(0.9, 0.9)`. 0.9^2 + 0.9^2 = 0.81 + 0.81 = 1.62. `1.62 > 1`. Outside. `points = 1`.
3. Random point: `(-0.1, 0.2)`. 0.01 + 0.04 = 0.05. Inside! `points = 2`.
4. Random point: `(0.8, -0.8)`. 0.64 + 0.64 = 1.28. Outside. `points = 2`.

Estimate = 4 x (2 / 4) = 2.0.
*(Extremely inaccurate because N=4, but with N=10^6, it rapidly approaches 3.14159).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The loop runs exactly N times performing $O(1)$ arithmetic. Time complexity is $O(N)$.
Only integer counters are maintained. Space complexity is $O(1)$.

## Variants & optimizations

- **First Quadrant Optimization:** Because a circle is perfectly symmetrical, you only need to simulate the top-right quadrant. Generate `x` and `y` between `0.0` and `1.0`. The math and ratios remain identical, but generating positive floats might be marginally faster in some languages.
- **Ray Tracing:** Monte Carlo path tracing in modern video games uses this exact probabilistic logic to simulate light bouncing around a scene. Instead of calculating the infinite complexity of billions of photons, it sends a few hundred random rays per pixel and averages their colors!

## Real-world applications

- **Financial Risk Modeling:** Pricing exotic derivatives (like Asian Options) where the payout depends on the entire history of the stock price, which is impossible to calculate analytically but easy to simulate stochastically via Monte Carlo.

## Related algorithms in cOde(n)

- **[randomized_05 - Karger's Min-Cut](randomized_05_karger-s-min-cut-monte-carlo.md)** — Another application of the Monte Carlo paradigm, applied to graphs instead of geometry.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
