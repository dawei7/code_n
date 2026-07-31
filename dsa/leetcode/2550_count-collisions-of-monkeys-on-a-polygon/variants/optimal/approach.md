## General

Every monkey independently chooses clockwise or counterclockwise, so there are $2^n$ total direction assignments. Count the complement: a movement has no collision only when every monkey chooses the same direction. All-clockwise rotates the entire configuration by one vertex, and all-counterclockwise rotates it the other way, giving exactly two collision-free assignments.

**Why every mixed assignment collides**

In a circular sequence containing both directions, some adjacent pair must form a boundary between the two choices. At one of the two boundary orientations, those neighboring monkeys travel toward one another on their shared edge and intersect. Equivalently, avoiding every opposing edge forces each monkey's direction to equal the next monkey's direction around the whole cycle, so all directions must be uniform.

The desired count is therefore $2^n-2$. Compute the power by binary modular exponentiation because $n$ may reach $10^9$, then normalize the subtraction modulo $10^9+7$.

## Complexity detail

Binary modular exponentiation processes the bits of `n`, taking $O(\log n)$ time. Its iterative state contains only the current base, exponent, and accumulated result, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate direction assignments:** Considering all $2^n$ choices is exponential and impossible for large `n`.
- **Multiply by two `n` times:** Repeated modular multiplication is correct but takes $O(n)$ time instead of $O(\log n)$.
- **Compute the full power before reducing:** The integer $2^n$ is unnecessarily enormous; reduce during exponentiation.
- **Subtract before modular normalization:** In languages where `%` may preserve a negative sign, add the modulus or otherwise normalize after subtracting 2.
- **Minimum polygon:** At `n = 3`, the formula gives 6, matching the first example.
- **Two safe assignments only:** Clockwise and counterclockwise uniform motion are distinct even though both preserve the one-monkey-per-vertex arrangement.
