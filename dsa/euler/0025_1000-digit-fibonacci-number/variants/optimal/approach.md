# 1000-digit Fibonacci Number - Optimal Approach

## Algorithm Explanation

By Binet's formula, the $n^{\text{th}}$ Fibonacci number is:
$$F_n = \frac{\phi^n - \psi^n}{\sqrt{5}} \approx \frac{\phi^n}{\sqrt{5}}$$
where $\phi = \frac{1 + \sqrt{5}}{2}$ is the golden ratio.

A number $X$ has $D$ digits if $\log_{10}(X) \ge D - 1$:
$$\log_{10}(F_n) \approx n \log_{10}(\phi) - \frac{1}{2} \log_{10}(5) \ge D - 1$$

Solving for $n$:
$$n \ge \frac{(D - 1) + \frac{1}{2} \log_{10}(5)}{\log_{10}(\phi)}$$

Taking the ceiling $\lceil n \rceil$ for $D = 1000$ computes the exact index in $\mathcal{O}(1)$ time.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - Single logarithmic formula evaluation.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
