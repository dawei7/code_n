## General

Let $n$ be the number of hours.

**Define states by the drink consumed now**

Let $A_i$ be the greatest energy total among schedules that consume drink A in hour $i$, and define $B_i$ symmetrically. To consume A now, either continue from A in the immediately previous hour or switch from B consumed two hours earlier, leaving hour $i-1$ as the required cleansing hour. Therefore

$$
A_i=\texttt{energyDrinkA[i]}+\max(A_{i-1},B_{i-2}),
$$

and similarly

$$
B_i=\texttt{energyDrinkB[i]}+\max(B_{i-1},A_{i-2}).
$$

For hour zero, the two state values are the corresponding energy entries. Because all energy boosts are positive, an optimal schedule ending on a drink in hour one consumes that same drink in both initial hours, which initializes $A_1$ and $B_1$ as their two-entry sums.

**Roll the two preceding layers**

Each recurrence needs only its own drink's previous-hour state and the other drink's state from two hours back. Retain those four totals, compute both current values before overwriting anything, then shift the state window. The larger final drink state is the answer.

Every schedule ending on A at hour $i$ falls into exactly the continue or switch case represented by the recurrence, and both predecessor schedules obey the rules. Taking their maximum plus the current boost therefore gives the optimal A-ending schedule; the same holds for B. The base states are exact, so induction proves every layer and the final maximum.

## Complexity detail

The algorithm performs two constant-time transitions per hour, for $O(n)$ time. Four rolling totals and two new totals provide all DP state, so auxiliary space is $O(1)$. The answer can reach $10^{10}$ and requires a wide integer type outside Python.

## Alternatives and edge cases

- **Enumerate switching schedules:** Recursively choosing continue or switch revisits equivalent hour-and-drink states and can grow exponentially.
- **Memoized recursion:** Caching those states gives $O(n)$ work but uses $O(n)$ memory and risks deep recursion.
- **Choose the larger value each hour:** A locally attractive switch sacrifices the entire intervening hour and can reduce the final total.
- **Switch without a skipped hour:** This violates the cleansing rule and overestimates achievable energy.
- Starting on either drink is allowed and requires no initial cleansing.
- Multiple switches are legal when each has its own skipped hour.
- Positive boosts make consecutive consumption of the same drink beneficial whenever no switch occurs.
- A skipped hour contributes zero, not either array's value.
- Large inputs can produce totals above 32-bit range.
