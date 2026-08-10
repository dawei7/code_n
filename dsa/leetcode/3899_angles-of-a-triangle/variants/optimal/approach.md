## General

The source first sorts the three side lengths, decides whether they form a positive-area triangle, and then applies the law of cosines. Sorting serves two purposes at once:

1. it reduces triangle validation to one inequality involving the largest side; and
2. it makes the angles computed opposite those sides already appear in non-decreasing order.

Let the sorted side lengths be

$$
a\le b\le c.
$$

The source names the opposite angles $A$, $B$, and $C$ respectively.

**Why one triangle inequality is enough after sorting**

Three positive lengths form a non-degenerate triangle exactly when every side is strictly less than the sum of the other two:

$$
a+b>c,\qquad a+c>b,\qquad b+c>a.
$$

Since $a$ and $b$ are positive and $c$ is the largest:

- $a+c>b$ holds automatically because $c\ge b$ and $a>0$;
- $b+c>a$ also holds automatically because both $b$ and $c$ are positive and at least as large as $a$ where relevant.

Only

$$
a+b>c
$$

can fail. The source rejects when `a + b <= c`.

Equality is correctly rejected. If $a+b=c$, the three segments lie on one straight line and enclose zero area. The problem asks for a triangle with positive area, so this degenerate case must return an empty array just like the case $a+b<c$.

**Recovering the first two angles with the law of cosines**

For a triangle with side $a$ opposite angle $A$, the law of cosines states

$$
a^2=b^2+c^2-2bc\cos A.
$$

Rearranging gives

$$
\cos A=\frac{b^2+c^2-a^2}{2bc}.
$$

Applying inverse cosine yields $A$ in radians, and `degrees` converts it to degrees:

$$
A=
\operatorname{degrees}\!\left(
\arccos\!\frac{b^2+c^2-a^2}{2bc}
\right).
$$

The source uses the analogous formula for the angle opposite side $b$:

$$
B=
\operatorname{degrees}\!\left(
\arccos\!\frac{a^2+c^2-b^2}{2ac}
\right).
$$

All denominators are nonzero because the input sides are positive.

**Why the third angle is obtained by subtraction**

The interior angles of every Euclidean triangle sum to $180^\circ$. Once $A$ and $B$ are known, the source sets

$$
C=180-A-B.
$$

This avoids a third inverse-cosine call. It also enforces the angle-sum identity in the returned floating-point values, apart from the ordinary rounding already present in $A$ and $B$.

For sides 3, 4, and 5:

$$
A=\arccos\!\left(\frac{4^2+5^2-3^2}{2\cdot4\cdot5}\right)
\approx36.86990^\circ,
$$

$$
B=\arccos\!\left(\frac{3^2+5^2-4^2}{2\cdot3\cdot5}\right)
\approx53.13010^\circ,
$$

and

$$
C=180^\circ-A-B=90^\circ.
$$

**Why the returned angle order is already sorted**

In a triangle, larger sides lie opposite larger angles. Therefore

$$
a\le b\le c
\quad\Longrightarrow\quad
A\le B\le C.
$$

One way to see this is through the law of cosines. With the other geometric conditions fixed, the cosine expression for an opposite angle decreases as its opposing side grows, while $\arccos$ is decreasing on $[-1,1]$; the resulting angle grows with its opposing side. The standard side-angle ordering theorem gives the same conclusion directly.

Because the source sorts the sides before assigning $A$, $B$, and $C$, returning `[A, B, C]` satisfies the non-decreasing requirement without a separate angle sort.

Equal sides produce equal opposite angles. For example, $a=b$ makes the two cosine formulas symmetric, so $A=B$.

**Why the formulas describe the unique requested triangle**

Once three positive sides satisfy the strict triangle inequality, the side-side-side condition determines a triangle uniquely up to rotation and reflection. Those transformations do not change internal angles. The law of cosines therefore computes the only possible angle triple.

If validation fails, no positive-area triangle exists, so `[]` is the only correct response. If validation succeeds, each inverse-cosine argument corresponds to a real triangle angle, the third angle completes the $180^\circ$ total, and the side ordering supplies the required result ordering.

## Complexity detail

The input always contains exactly three values. Sorting three elements takes constant time and constant auxiliary space. The validation performs one addition and comparison, and the angle calculation performs a fixed number of arithmetic and mathematical-library operations.

The time complexity is

$$
O(1).
$$

The method stores only three side variables and three angle variables. The returned list always has either zero or three entries, so the auxiliary and output space are both

$$
O(1).
$$

The source calls `sides.sort()`, which mutates the caller-provided list into non-decreasing order. This side effect does not affect the mathematical result, but it is observable by the caller.

Floating-point arithmetic introduces small rounding error, which is why the problem accepts answers within $10^{-5}$. With the documented positive integer bounds, the valid cosine ratios are within the mathematical domain $[-1,1]$.

## Alternatives and edge cases

- **Compute all three cosine angles:** This is symmetric and direct, but performs one extra inverse-cosine call; the source uses the exact $180^\circ$ sum for the third angle.
- **Heron's formula plus trigonometry:** Area can help recover angles, but it adds more operations and can be less numerically direct than the law of cosines.
- **Avoid input mutation:** Using `a, b, c = sorted(sides)` would preserve the caller's list while keeping the same algorithm and bounds.
- **Degenerate equality:** Sides such as `[2,2,4]` satisfy $a+b=c$ and must return `[]` because their area is zero.
- **Clearly impossible triangle:** If $a+b<c$, the longest side cannot be connected by the shorter two, so the method returns `[]`.
- **Equilateral triangle:** Equal sides produce three angles of approximately $60^\circ$ in already sorted order.
- **Isosceles triangle:** Equal sides produce equal opposite angles; non-decreasing order permits equality.
- **Right triangle:** For a Pythagorean triple, the largest angle $C$ is approximately $90^\circ$.
- **Very narrow valid triangle:** A side triple just satisfying $a+b>c$ has one angle close to $180^\circ$, but still represents positive area and must not be rejected.
- **Positive-side guarantee:** Zero-length sides would make a cosine denominator invalid, but the constraints exclude them.
- **Floating-point tolerance:** Results should be compared approximately, not by exact decimal equality.
- **Required library names:** Standalone execution needs `acos` and `degrees` from Python's `math` module.
