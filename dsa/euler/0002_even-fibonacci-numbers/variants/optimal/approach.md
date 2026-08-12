# Even Fibonacci Numbers - Optimal Approach

## Algorithm Explanation

The standard Fibonacci sequence is $1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, \dots$.

Notice the parity pattern of terms:
$$\text{odd}, \mathbf{even}, \text{odd}, \text{odd}, \mathbf{even}, \text{odd}, \text{odd}, \mathbf{even}, \dots$$

Every third term is even. By setting $E_n = F_{3n}$, we can derive a direct recurrence relation for only the even terms:
$$E_n = 4 E_{n-1} + E_{n-2}$$

Starting with $E_1 = 2$ and $E_2 = 8$:
- $E_3 = 4(8) + 2 = 34$
- $E_4 = 4(34) + 8 = 144$

This allows us to skip two out of three iterations, computing the sum directly in logarithmic steps.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log(\text{limit}))$ - Grows logarithmically as Fibonacci terms grow exponentially by the golden ratio $\phi^3 \approx 4.236$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
