## General

**Reserve the mandatory dollar first**

Every child must receive at least one dollar. Giving one to each consumes `children` dollars. If `money < children`, even this baseline is impossible, so the function returns $-1$.

After the baseline, turning one child from one dollar into exactly eight requires seven additional dollars. Ignoring special restrictions for a moment, the largest possible number of eight-dollar children is

$$
\left\lfloor\frac{\texttt{money}-\texttt{children}}7\right\rfloor.
$$

The final return uses this formula, but two boundary configurations need repair.

**Case one: more than eight dollars per child on average**

If `money > 8 * children`, it is impossible for all children to receive exactly eight because all money must be distributed. At least one child must absorb the excess and therefore stop being an eight-dollar child.

The maximum is at most `children - 1`. It is achievable: give eight dollars to that many children and give all remaining money to the final child. The final amount is greater than eight, so it is positive and not equal to four.

That proves the first repair branch:

`return children - 1`.

When money equals exactly `8 * children`, this branch does not apply; giving every child eight is valid, and the baseline formula returns `children`.

**Case two: the forbidden four-dollar leftover**

Suppose `money == 8 * children - 4`. The baseline formula suggests `children - 1` eight-dollar children.

After giving those children eight, the one remaining child receives

$$
(8c-4)-8(c-1)=4.
$$

That distribution is forbidden, and there is only one non-eight child available to absorb or share the amount. Therefore `children - 1` is impossible.

Reducing the count to `children - 2` leaves two non-eight children with a combined amount of $12$. They can receive, for example, $6$ and $6$, satisfying positivity and avoiding four. Hence the maximum in this case is exactly `children - 2`.

**Why no other leftover needs a special branch**

Let

$$
x=\left\lfloor\frac{\texttt{money}-\texttt{children}}7\right\rfloor
$$

and begin by giving $x$ children eight and every other child one. Let $r$ be the money still undistributed. Division by seven guarantees $0\le r<7$.

If $r\ne3$, add all leftover money to one non-eight child. That child receives `1 + r`, which is not four, and the $x$ eight-dollar children remain unchanged.

If $r=3$ and at least two non-eight children remain, split the extra as one and two dollars. Their final amounts become two and three, neither forbidden.

The only failure is $r=3$ with exactly one non-eight child. That is precisely $x=children-1$ and

$$
\texttt{money}
=
\texttt{children}+7(\texttt{children}-1)+3
=
8\cdot\texttt{children}-4.
$$

The special branch covers exactly this configuration.

**Why the baseline count is an upper bound**

Every child receiving eight consumes seven dollars beyond the mandatory one-dollar baseline. If $x$ children receive eight, the total must be at least

$$
\texttt{children}+7x.
$$

Rearranging gives

$$
x\le
\left\lfloor\frac{\texttt{money}-\texttt{children}}7\right\rfloor.
$$

Thus the formula is not only constructive; no distribution can exceed it unless the surplus-above-eight case caps the count at `children - 1`.

**Trace `money = 20` and `children = 3`**

The baseline consumes three dollars, leaving seventeen. Two seven-dollar upgrades appear possible by division, but `money = 8*3 - 4 = 20` is the forbidden special case.

Giving two children eight leaves four for the third. Reducing to one eight-dollar child allows a valid distribution such as $8,9,3$. The function returns one.

For `money=16` and two children, money equals `8*children`. Neither repair branch triggers, and the formula gives $(16-2)//7=2$, representing $8,8$.

**Order of the checks**

Impossibility from insufficient money must be handled before subtraction. Excess money is checked before the special four-dollar pattern. These cases are disjoint under the given positive constraints, and the final formula handles every remaining distribution.

No actual list of child amounts is constructed because the proof supplies a valid distribution for every returned count.

## Complexity detail

The function performs a fixed number of comparisons, multiplications, a subtraction, and integer division. Time is $O(1)$ and auxiliary space is $O(1)$.

Values are small under the constraints, though fixed-width implementations should still evaluate `8 * children` in a sufficiently wide integer type in broader variants.

## Alternatives and edge cases

- **Try every count downward:** Testing candidate numbers of eight-dollar children is simple but unnecessary once the two exceptional formulas are derived.
- **Dynamic programming over children and money:** The small constraints permit it, but it obscures the constant-time arithmetic structure.
- **Insufficient money:** Fewer dollars than children makes the mandatory minimum impossible, yielding $-1$.
- **Exact all-eight total:** When `money == 8 * children`, every child can count.
- **Excess above all-eight total:** One child must absorb all excess, so at most `children - 1` count.
- **Forbidden four remainder:** `8 * children - 4` forces the candidate sole leftover child to receive four.
- **Three-dollar remainder with two spare children:** Split the extra to make amounts two and three rather than four and one.
- **All money distributed:** Constructions explicitly assign every leftover dollar; unused money is never allowed.
- **No upper amount per child:** The excess case can safely place arbitrarily many remaining dollars on one non-eight child.
