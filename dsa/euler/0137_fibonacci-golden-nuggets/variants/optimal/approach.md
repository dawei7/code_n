# Fibonacci Golden Nuggets - Optimal Approach

## Algorithm Explanation

Find the $15^{\text{th}}$ "golden nugget" $n_{15}$, which is a positive integer value of the Fibonacci generating series $A_F(x) = \frac{x}{1 - x - x^2}$ for which $x$ is rational.

### Generating Function Discriminant Reduction:
Setting $A_F(x) = n$:
$$n x^2 + (n + 1)x - n = 0$$

For $x$ to be rational, the quadratic discriminant must be a perfect square $y^2$:
$$D = (n + 1)^2 + 4n^2 = 5n^2 + 2n + 1 = y^2$$

### Closed-Form Fibonacci Identity:
Solving the Pell-like Diophantine equation $5n^2 + 2n + 1 = y^2$ reveals that integer solutions $n_k$ correspond to products of consecutive Fibonacci numbers:
$$n_k = F_{2k} \times F_{2k+1}$$

For $k = 15$:
$$n_{15} = F_{30} \times F_{31}$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(k)$ where $k = 15$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant memory.
