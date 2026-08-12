# Special Pythagorean Triplet - Optimal Approach

## Algorithm Explanation

Given $a + b + c = S = 1000$ and $a^2 + b^2 = c^2$:

Substitute $c = S - a - b$ into the Pythagorean theorem:
$$a^2 + b^2 = (S - a - b)^2$$
$$a^2 + b^2 = S^2 + a^2 + b^2 - 2Sa - 2Sb + 2ab$$
$$2Sa + 2Sb - 2ab = S^2$$
$$b(2S - 2a) = S^2 - 2Sa$$
$$b = \frac{S^2 / 2 - Sa}{S - a}$$

Iterate $a$ from $1$ to $\lfloor \frac{S}{3} \rfloor$. Whenever $b$ evaluates to an exact integer, calculate $c = S - a - b$ and return $a \cdot b \cdot c$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(S)$ - Single loop up to $\frac{S}{3} = 333$ iterations.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
