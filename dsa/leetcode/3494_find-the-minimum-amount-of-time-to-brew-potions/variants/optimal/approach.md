## General

For one potion with mana $x$, define `prefix[i]` as the sum of the first $i$ wizard skills. If that potion starts at time $s$, it reaches wizard $i$ at `s + x * prefix[i]` and leaves that wizard at `s + x * prefix[i + 1]`. The no-wait rule fixes all of these times once $s$ is chosen.

Suppose the previous potion started at time $p$ and had mana $y$. The new potion may not reach wizard $i$ before that wizard finishes the previous potion. Thus its start must satisfy

$$
s+x\,\texttt{prefix}[i]\ge p+y\,\texttt{prefix}[i+1]
$$

for every wizard $i$. Rearranging gives one lower bound on $s$ per wizard. The maximum of those $n$ bounds is both feasible and minimal: it prevents every overlap, while decreasing it would violate the wizard that supplied the maximum.

Process the potions in order. Only the preceding potion matters because potion order makes each wizard's completion times non-decreasing; if the new potion starts after the preceding one clears every wizard, it also clears all earlier potions. After finding the last potion's start, add its total processing duration to obtain the final completion time.

## Complexity detail

Let $n$ be the number of wizards and $m$ the number of potions. Building the skill prefix sums takes $O(n)$ time. Each of the remaining $m-1$ potions evaluates exactly one constant-time bound per wizard, so total time is $O(nm)$. The prefix array uses $O(n)$ auxiliary space.

The benchmark sets both list lengths to a common dimension $q$ and records `size = q`. The optimal method performs $\Theta(q^2)$ bound evaluations. The calibrated slower implementation recomputes each prefix sum from the original skill list for every wizard and potion, performing $\Theta(q^3)$ work while producing the same schedule.

## Alternatives and edge cases

- **Forward completion times plus a reverse synchronization pass:** This equivalent $O(nm)$ simulation stores every wizard's latest completion time and moves backward after each potion to restore its no-wait arrival times.
- **Recompute prefix sums inside every constraint:** Correct, but repeated summation raises the running time to $O(mn^2)$.
- **Ordinary flow-shop dynamic programming:** Allowing a potion to wait between wizards solves a different problem and can return an infeasible result here.
- **One wizard:** Potions cannot overlap, so the answer is that wizard's skill multiplied by the sum of all mana values.
- **One potion:** It starts at time zero and takes its mana times the sum of all wizard skills.
- **Changing mana values:** A smaller potion may still need a large start delay because it reaches downstream wizards quickly; every wizard's bound remains necessary.
- **Large products:** The final time can exceed 32-bit range, so fixed-width implementations need 64-bit arithmetic.
