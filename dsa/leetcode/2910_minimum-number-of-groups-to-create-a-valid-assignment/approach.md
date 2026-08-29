## General

Every occurrence of the same number must be assigned to the same kind of group: a group cannot mix different values. At the same time, the sizes of any two groups may differ by at most one. Those two rules mean that, after choosing the smaller allowed group size $k$, every group in the entire assignment must have size either $k$ or $k+1$.

The actual values in `nums` are therefore less important than their frequencies. The solution begins with `Counter(nums)`. If a value occurs $v$ times, the question becomes:

> Can $v$ items be split into groups of size $k$ and $k+1$, and if so, how many groups are required?

The algorithm searches possible $k$ values from largest to smallest. For each one, it tests every frequency. The first $k$ that works for all values produces the minimum total number of groups.

**Why the search begins at the minimum frequency**

Let $f_{\min}$ be the smallest frequency in the counter. The smaller allowed group size cannot exceed $f_{\min}$. If $k>f_{\min}$, the least frequent value does not contain enough occurrences to fill even one group of size $k$, and it cannot be combined with another value. Therefore all larger choices are impossible.

The loop consequently tries

$$
k=f_{\min}, f_{\min}-1,\ldots,1.
$$

The case $k=1$ always works: every frequency can be divided into groups of size $1$ or $2$. Hence the function is guaranteed to return from the loop even though there is no separate return statement afterward.

**Derive the feasibility test for one frequency**

For a fixed $k$, divide a frequency $v$ by $k$:

$$
v=ak+b,
\qquad
a=\left\lfloor\frac{v}{k}\right\rfloor,
\qquad
0\le b<k.
$$

Imagine starting with $a$ groups of size $k$. These groups account for $ak$ items, leaving $b$ items. A leftover item can be placed into a different group, increasing that group's size from $k$ to $k+1$. Thus all leftovers can be absorbed exactly when there are at least $b$ groups available:

$$
a\ge b.
$$

The code expresses the failure of this condition as

`v // k < v % k`.

If it is true for even one frequency, this $k$ cannot describe a globally valid assignment. The code sets `ans` back to zero, breaks out of the frequency loop, and continues with the next smaller $k$.

The same argument gives a concrete construction when $a\ge b$: make $b$ of the groups size $k+1$, and leave the remaining $a-b$ groups at size $k$. Their total number is still $a$, and their item count is

$$
b(k+1)+(a-b)k=ak+b=v.
$$

So the quotient/remainder condition is not merely necessary; it is sufficient.

**Count the fewest groups for a feasible frequency**

Although the quotient argument above begins with groups of size $k$, the smallest possible number of groups is obtained by using as many size-$(k+1)$ groups as possible. Each group can contain at most $k+1$ items, so at least

$$
\left\lceil\frac{v}{k+1}\right\rceil
$$

groups are necessary. When the feasibility condition holds, that lower bound can be achieved with sizes $k$ and $k+1$. The implementation computes it with integer arithmetic:

`(v + k) // (k + 1)`.

To see why it is achievable, let $q=\lceil v/(k+1)\rceil$. Starting with $q$ groups of maximum size $k+1$ gives capacity $q(k+1)$. Reducing some groups by one can reach $v$ provided the total reduction is at most $q$, which is equivalent to $v\ge qk$. This is another form of the same representability condition checked by the quotient and remainder.

The algorithm adds this group count for every distinct value. If all frequencies are feasible, `ans` is positive and is returned.

**Why the first feasible smaller size is optimal**

The search proceeds downward, so the first feasible $k$ gives the largest possible pair of group sizes, $k$ and $k+1$. Increasing permitted group capacity cannot require more groups for any fixed frequency: the minimum is `ceil(v / (k + 1))`, which is nonincreasing as $k$ grows.

Suppose a later, smaller feasible value $k'$ were used. Its largest group has size $k'+1\le k+1$, so each frequency would need at least as many groups as it needed under the first feasible $k$. Summing across all distinct values cannot improve the answer. Therefore it is safe to return immediately upon finding the largest globally feasible $k$.

Consider frequencies $3$ and $5$. The minimum frequency is $3$. For $k=3$, frequency $5$ has quotient $1$ and remainder $2$, so one initial group cannot absorb two leftovers; this choice fails. For $k=2$, $3$ can be one group of $3$, while $5$ can be groups of $2$ and $3$. The total is three groups, and there is no need to test $k=1$.

## Complexity detail

Let $n$ be the length of `nums`, let $u$ be the number of distinct values, and let $f_{\min}$ be the smallest frequency.

Building the counter takes $O(n)$ expected time and $O(u)$ space. The nested search performs at most $f_{\min}\cdot u$ frequency checks. This product is at most $n$, because every one of the $u$ distinct values occurs at least $f_{\min}$ times:

$$
u f_{\min}\le \sum_{x}\operatorname{freq}(x)=n.
$$

Thus even though the code contains nested loops, their total worst-case number of iterations is $O(n)$, not $O(n^2)$. Together with counter construction, the overall expected time is $O(n)$. The “expected” qualification comes from Python hash-table operations in `Counter`.

The counter stores one entry per distinct value and uses $O(u)$ space. The loop variables and accumulator use $O(1)$ additional space. No representation of the actual groups is built because only their minimum count is requested.

## Alternatives and edge cases

- **Construct groups directly:** Repeatedly assigning occurrences to concrete lists adds unnecessary bookkeeping. Frequency arithmetic decides feasibility and count without materializing any group.
- **Try all partitions of each frequency:** Enumerating combinations of $k$- and $(k+1)$-sized groups is exponential or pseudo-polynomial. Quotient and remainder reduce the decision to one constant-time inequality.
- **Search group count rather than size:** It is possible to test candidate numbers of groups for each frequency, but coordinating a common global size pair is less direct. Searching the shared smaller size exposes the validity rule cleanly.
- **All values are unique:** Every frequency is $1$, so $k=1$ is immediately feasible and each occurrence forms one group.
- **Only one distinct value:** The largest trial is its full frequency. One group containing all occurrences is valid, so the answer is $1$.
- **A remainder larger than the quotient:** For example, $v=5,k=3$ gives quotient $1$ and remainder $2$. One size-$3$ group cannot absorb two separate extra items, which is exactly why the implementation rejects `a < b`.
- **Do not use only divisibility:** A frequency need not be divisible by $k$ or by $k+1$. Mixed sizes are allowed; $5=2+3$ is valid for $k=2$.
- **Global consistency matters:** A $k$ that works for one frequency is insufficient. Every value's occurrences must be partitionable using the same two sizes, which is why the inner loop must finish successfully.
- **Why `ans == 0` signals failure safely:** Every successful frequency contributes at least one group. Therefore a completely feasible pass always leaves a positive sum, while zero can unambiguously mean that a frequency caused the pass to break.
