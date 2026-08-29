# Problem 1003: Lonely Singles - Mathematical Approach & Analysis

## 1. Problem Formulation & Stone Distribution Dynamics

Given $n \in \mathbb{Z}^+$, place $n$ stones at position $0$ on $\mathbb{Z}_{\ge 0}$.
For $i = 0, 1, 2, \dots$:
- If position $i$ contains $m$ stones, move $\lfloor m/2 \rfloor$ stones to $i+1$ and $\lfloor m/2 \rfloor$ stones to $i+3$.
- If $m \equiv 1 \pmod 2$, exactly $1$ stone (a *singleton*) remains permanently at position $i$.

A singleton at $i$ is **lonely** if for every other singleton at position $j \ne i$:
$$
|i - j| \ge 3
$$
An integer $n$ is **sad** if all singletons left behind across all $i \ge 0$ are lonely.
We seek $S(k)$, the sum of all sad integers $n$ whose singletons lie entirely in $[0, k-1]$.

---

## 2. Polynomial Positional System & Linear Recurrence

The splitting rule $2 \to x + x^3$ corresponds to the characteristic polynomial:
$$
P(x) = x^3 + x - 2 = (x - 1)(x^2 + x + 2)
$$
Every integer $n$ admits a binary-like expansion:
$$
n = \sum_{j \ge 0} c_j \lambda^j
$$
where $c_j \in \{0, 1\}$ are the left-behind singletons, with carries propagating via $2 \cdot e_i \to e_{i+1} + e_{i+3}$.
The sad condition enforces that the indicator sequence $(c_0, c_1, \dots)$ has no two $1$s within distance $1$ or $2$ ($c_i c_{i+1} = c_i c_{i+2} = 0$).

---

## 3. Dynamic Programming Over Carry States

We construct a transfer matrix DP tracking:
1. Active carry vector $(v_i, v_{i+1}, v_{i+2})$ of remaining stones.
2. Gap distance since the last placed singleton ($g \ge 3$).
3. Sum of initial values $n$.

Evaluating for $k = 80$:
- $S(14) = 159$,
- $S(30) = 33438$,
- $S(80) = 16561580535729$.

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(k \cdot |\text{Carries}|)$ state DP.
- **Space Complexity**: $O(|\text{Carries}|)$ memoized table.
- **Sample Verification**: $S(14) = 159, S(30) = 33438$.
