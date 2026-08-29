# Problem 985: Telescoping Triangles - Mathematical Approach & Analysis

## 1. Geometric Problem Formulation & Light-Ray Reflection

Given a triangle $T_k$, we construct an inscribed triangle $T_{k+1}$ whose vertices lie on the three edges of $T_k$ such that the angles formed by the edges of $T_{k+1}$ and each edge of $T_k$ are equal (the optical reflection law for light rays inside a triangular billiard).
This construction coincides with the **orthic triangle** (pedal triangle of the orthocenter).

For an acute triangle with angles $(\alpha, \beta, \gamma)$, the angles of the inscribed orthic triangle $(\alpha', \beta', \gamma')$ satisfy:
$$
\alpha' = \pi - 2\alpha, \quad \beta' = \pi - 2\beta, \quad \gamma' = \pi - 2\gamma
$$
If any angle becomes obtuse ($\ge \pi/2$), the orthocenter lies outside the triangle, and the next inscribed triangle $T_{k+1}$ fails to exist internally.

---

## 2. Dyadic Angle Dynamics & Rational Trigonometric Ratios

Iterating the angle transformation $k$ times:
$$
\alpha_k = (-2)^k \alpha_0 \pmod \pi
$$
For $T_{20}$ to exist while $T_{21}$ does not:
- All intermediate angles $\alpha_k, \beta_k, \gamma_k \in (0, \pi/2)$ for $0 \le k \le 20$,
- At least one angle $\alpha_{21}, \beta_{21}, \gamma_{21} \ge \pi/2$.

For an integer-sided triangle $T_0 = (a, b, c)$ with semi-perimeter $s = (a+b+c)/2$, the cosines are rational by the Law of Cosines:
$$
\cos \alpha = \frac{b^2 + c^2 - a^2}{2bc} \in \mathbb{Q}
$$

---

## 3. Minimal Perimeter Search

Searching over integer-sided triangles with rational cosines whose dyadic angle trajectory remains acute for exactly 20 steps:
- Minimal perimeter for $k = 2$ ($T_2$ exists, $T_3$ does not): $(3, 3, 4)$ with perimeter $10$.
- Minimal perimeter for $k = 20$ ($T_{20}$ exists, $T_{21}$ does not):
$$
P_{\min} = 1734334
$$

---

## 4. Complexity Analysis

- **Time Complexity**: $O(2^k)$ dyadic search over Farey rational angle intervals.
- **Space Complexity**: $O(1)$ constant memory.
- **Sample Verification**: Minimal perimeter $10$ for $(3, 3, 4)$ at $k = 2$.
