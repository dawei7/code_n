## General

**Solve one data center independently**

Money cannot move between data centers, so choices for one center do not affect any other. The four arrays can be zipped and each tuple solved with the same algebra.

For one center, let:

- $C$ be the initial server count;
- $U$ be the cost to upgrade one server;
- $S$ be the income from selling one server;
- $M$ be initial money.

Suppose we want to upgrade exactly $x$ servers. The other $C-x$ servers may be sold, producing available money

$$
M+(C-x)S.
$$

Upgrading $x$ servers costs $xU$. The choice is feasible exactly when

$$
xU\le M+(C-x)S.
$$

**Rearrange the budget inequality**

Move the term $xS$ to the left:

$$
xU+xS\le CS+M.
$$

Factor $x$:

$$
x(U+S)\le CS+M.
$$

The largest integer satisfying this money constraint is

$$
\left\lfloor\frac{CS+M}{U+S}\right\rfloor.
$$

However, we cannot upgrade more than the $C$ servers that exist. Therefore, the answer is

$$
\min\left(C,\left\lfloor\frac{CS+M}{U+S}\right\rfloor\right).
$$

The exact append expression implements this formula with `cnt`, `cost`, `income`, and `cash`.

**Why “sell then upgrade” is captured correctly**

The formula assumes every server not upgraded is sold. Could keeping an unupgraded, unsold server help? No. It provides no benefit toward maximizing the number upgraded and gives up nonnegative sale income. Selling every non-upgraded server weakly increases the available budget, so some optimal plan has this form.

There is no ordering problem. Conceptually selling produces money before upgrades, but the final feasibility inequality is all that matters. The operations are independent per server.


If formula returns $x$, then $x\le C$ and floor division guarantees

$$
x(U+S)\le CS+M.
$$

Reversing the algebra gives $xU\le M+(C-x)S$. Sell $C-x$ servers and use the resulting money to upgrade the other $x$; this is an achievable plan.

Now consider $x+1$ when $x<C$. Since $x$ is the floor of the budget quotient,

$$
(x+1)(U+S)>CS+M,
$$

so the corresponding upgrade cost exceeds initial plus sale money. Upgrading $x+1$ is impossible. If the cap returned $C$, no larger count exists physically. Thus the returned value is maximal.

**Example**

For $C=4$, $U=3$, $S=4$, and $M=8$:

$$
\left\lfloor\frac{4\cdot4+8}{3+4}\right\rfloor
=\left\lfloor\frac{24}{7}\right\rfloor=3.
$$

Selling one server yields $8+4=12$, exactly enough to upgrade three servers for 9, so 3 is feasible. Four upgrades would cost 12 but leave no servers to sell, and initial money 8 is insufficient.

For one server with upgrade cost 2, sale income 1, and cash 1, the quotient is $\lfloor2/3\rfloor=0$. Selling the only server leaves nothing to upgrade, while keeping it leaves insufficient upgrade money, so zero is correct.

**Why the centers stay independent in code**

`zip(count, upgrade, sell, money)` aligns values at the same index. Each computed integer is appended immediately to `ans`. No aggregate cash or server pool is created, faithfully preserving the prohibition on cross-center transfers.

The arrays are guaranteed equal length, so `zip` does not silently omit a center under valid input.

## Complexity detail

Let $n$ be the number of data centers.

The loop processes each center once with constant-time multiplication, addition, floor division, and minimum, so time is $O(n)$ under the bounded-integer model.

Apart from the required output list of length $n$, the method stores a fixed number of scalar values. Auxiliary space excluding output is $O(1)$; including output it is $O(n)$.

Python arbitrary-precision integers prevent overflow in `cnt * income + cash`. With the given bounds, even fixed 64-bit arithmetic would be sufficient, but relying on a too-small 32-bit type could overflow.

No input array is modified.

## Alternatives and edge cases

- **Binary search number upgraded:** Feasibility is monotone in $x$, so binary search works in $O(\log C)$ per center, but algebra gives the boundary directly.
- **Try every sale count:** It takes $O(C)$ per center and obscures the simple inequality.
- **Upgrade greedily while selling:** Simulation reaches the same result but performs unnecessary repeated operations.
- **Enough initial cash for all:** The quotient may exceed $C$, and `min` correctly caps the answer at all servers.
- **No affordable upgrade:** The floor quotient can be zero even though selling produces money, as in the one-server example.
- **Sell income larger than upgrade cost:** The denominator still includes both $U$ and $S$ because choosing one more upgrade both costs $U$ and forgoes sale income $S$.
- **Exactly enough money:** The non-strict inequality and floor division include the feasible boundary.
- **One server:** The formula chooses between upgrading it with initial cash or upgrading none; selling it cannot fund upgrading itself.
- **Independent centers:** Excess money from one result cannot raise another result.
- **All values positive:** The denominator `U + S` is nonzero, and selling an unused server never hurts.
- **Physical count cap:** Budget alone might suggest more upgrades than servers; `min(cnt, ...)` is mandatory.
- **Equal array lengths:** This contract makes `zip` cover every data center exactly once.
