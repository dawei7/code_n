## General

For a horizon of $T$ hours and a recharge interval $q$, exactly $T-\lfloor T/q\rfloor$ hours are usable. The first horizon providing $x$ usable hours has a direct form:

$$
\operatorname{need}(x,q)=x+\left\lfloor\frac{x-1}{q-1}\right\rfloor.
$$

Every complete group of $q-1$ usable hours forces one recharge hour; using $x-1$ in the numerator correctly avoids adding a recharge after the final required usable hour.

Three capacities constrain the schedule. Drone 1 needs enough hours outside multiples of `r[0]`; drone 2 needs enough outside multiples of `r[1]`; and both quotas together need enough hours outside multiples of $\operatorname{lcm}(r_1,r_2)$, the hours when both drones recharge. With two drones, these individual and combined conditions are also sufficient: reserve hours available to only one drone first, then distribute shared hours.

The earliest feasible horizon is therefore the maximum of the three exact requirements:

$$
\max\!\left(
\operatorname{need}(d_1,r_1),
\operatorname{need}(d_2,r_2),
\operatorname{need}(d_1+d_2,\operatorname{lcm}(r_1,r_2))
\right).
$$

## Complexity detail

The input always contains exactly two delivery counts and two recharge intervals. A fixed number of arithmetic operations and one greatest-common-divisor computation are performed, so time is $O(1)$ under fixed-width integer arithmetic and auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Binary search:** Testing the same three capacity inequalities is correct in $O(\log A)$ time, but the inequalities can be inverted exactly.
- **Simulate every hour:** This takes $O(A)$ time and is impractical for billion-delivery quotas.
- **Check only total deliveries:** The combined capacity alone misses cases where one drone cannot meet its own quota.
- **Check only individual capacities:** Separate checks can assign the same shared hour twice.
- **Simultaneous recharge:** Multiples of the least common multiple are unavailable to both drones.
- **Exact group boundary:** The numerator `deliveries - 1` prevents charging an unnecessary recharge hour after the final delivery.
- **Large quotas:** Use 64-bit arithmetic for the answer and least common multiple.
