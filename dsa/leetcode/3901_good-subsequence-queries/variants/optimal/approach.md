## General

A subsequence can have GCD exactly $p$ only if every selected element is divisible by $p$. The source therefore ignores non-divisible values in its GCD structure, maintains the GCD of all divisible values under point updates, and then handles the “strictly shorter than the whole array” condition separately.

The most surprising branch is `n > 6`. It is not an arbitrary shortcut: the value bound implies that whenever more than six divisible elements have normalized GCD 1, at least one element can be removed without changing that GCD. The source uses this bounded witness theorem to avoid expensive deletion checks for large arrays.

**Discarding values that can never belong to a good subsequence**

If a subsequence has GCD $p$, then $p$ divides every selected element. Any array value not divisible by $p$ is unusable.

The segment tree stores:

$$
v_i=
\begin{cases}
\texttt{nums}[i],&p\mid\texttt{nums}[i],\\
0,&p\nmid\texttt{nums}[i].
\end{cases}
$$

Zero is a convenient empty value because

$$
\gcd(0,x)=x.
$$

Thus non-divisible positions do not affect the tree's aggregate GCD. The variable `cnt` records how many positions are currently divisible by $p$.

**What the root GCD tells us**

Let $D$ be the set of current divisible elements, and let

$$
g=\gcd(D),
$$

with $g=0$ when $D$ is empty. The root `tree.tr[1].g` stores this value.

If $g\ne p$, no selected subset can have GCD $p$. Every element of $D$ is a multiple of $p$, so when $D$ is nonempty, $g$ is also a multiple of $p$. Removing elements from a GCD can only leave the GCD unchanged or increase it to a multiple of the old GCD. Therefore:

- when $g>p$, every subset GCD is a multiple of $g$ and cannot equal $p$;
- when $g=0$, no divisible element exists, so no nonempty candidate exists.

If $g=p$, the complete set $D$ itself has the required GCD. The only remaining question is whether it is a proper subsequence.

**The easy proper-subsequence case**

When `cnt < n`, at least one array position is not divisible by $p$. Select every element in $D$ and omit all non-divisible positions. This subsequence is nonempty because its GCD is $p$, has GCD exactly $p$ by the root test, and has length strictly less than $n$.

That proves the query is successful immediately. No information about which particular non-divisible positions exist is needed.

The difficult case is `cnt == n`: every array element is divisible by $p$, and selecting all divisible elements would select the forbidden full array.

**Normalizing the all-divisible case**

Write

$$
a_i=\frac{\texttt{nums}[i]}p.
$$

Because every element is divisible by $p$,

$$
\gcd(\texttt{nums}[0],\ldots,\texttt{nums}[n-1])=p
$$

is equivalent to

$$
\gcd(a_0,\ldots,a_{n-1})=1.
$$

A proper subsequence with GCD $p$ is equivalent to a proper subset of the normalized values with GCD 1.

If any smaller subset has GCD 1, it can be enlarged to a subset of exactly $n-1$ elements while preserving that GCD. Adding another positive integer to a set whose GCD is already 1 keeps the GCD at 1. Therefore it is enough to ask whether deleting one index leaves GCD 1—or, before normalization, GCD $p$.

**Why more than six elements guarantee a removable one**

Assume for contradiction that $n\ge7$, the normalized GCD of all $n$ values is 1, but removing any one value makes the remaining GCD greater than 1.

For every index $i$, choose a prime $r_i$ dividing the GCD of all normalized values except $a_i$. Then:

- $r_i$ divides every $a_j$ with $j\ne i$;
- $r_i$ cannot divide $a_i$, because otherwise it would divide every value and the total GCD would not be 1.

The witness primes $r_i$ must be distinct. If $r_i=r_j$ for $i\ne j$, then the rule for $r_i$ says that prime divides $a_j$, while the rule for $r_j$ says it does not divide $a_j$, a contradiction.

Choose the index whose witness prime is smallest. Its value $a_i$ must be divisible by the other $n-1$ distinct witness primes. With at least seven elements, that means at least six distinct primes larger than the smallest witness. The smallest possible product of such six primes is

$$
3\cdot5\cdot7\cdot11\cdot13\cdot17
=255255.
$$

Hence $a_i\ge255255$. But updates and initial values are at most 50000, and normalization can only make a value smaller:

$$
a_i=\frac{\texttt{nums}[i]}p\le50000.
$$

This contradiction proves that for $n>6$, some element is redundant: deleting it keeps normalized GCD 1 and original GCD $p$. Therefore, once the root equals $p$ and all values are divisible, the source may answer yes immediately when `n > 6`.

**Checking every deletion when \(n\le6\)**

For a small array, the bounded-value theorem does not guarantee redundancy. The source tests each possible omitted index $i$.

It queries the GCD of positions before $i$ and positions after $i$:

$$
g_{\text{left}}=\gcd(1,\ldots,i-1),
$$

$$
g_{\text{right}}=\gcd(i+1,\ldots,n),
$$

using one-based tree positions. Empty ranges return 0. The GCD after deleting $i$ is

$$
\gcd(g_{\text{left}},g_{\text{right}}).
$$

If this equals $p$ for any index, all elements except that one form a valid nonempty proper subsequence. If no deletion works, no smaller subset can work either, because any smaller GCD-$p$ subset could have been enlarged to some $n-1$ element subset while retaining GCD $p$.

**How each query updates the maintained state**

For update `[idx, val]`:

1. If the old `nums[idx]` is divisible by $p$, the source writes zero at that tree position and decrements `cnt`.
2. If the new `val` is divisible by $p$, it writes that value into the same position and increments `cnt`.
3. It stores `val` in `nums[idx]` so later queries see the updated value.
4. It applies the root-GCD and proper-subsequence tests.

A segment-tree leaf stores one filtered value. Every internal node stores the GCD of its two children, so changing one leaf and recomputing nodes on the path to the root restores the aggregate invariant.

The method increments `ans` once for each query state in which a good subsequence exists and finally returns that count.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$, $Q=\lvert\texttt{queries}\rvert$, and $V$ be the maximum value.

Building the zero-initialized segment-tree node structure costs $O(N)$ time and $O(N)$ space. The source then inserts every initially divisible value with a separate point modification. There can be $N$ such modifications, each taking $O(\log N)$ tree levels, so initialization costs

$$
O(N\log N)
$$

time as written.

Each update performs at most two point modifications, costing $O(\log N)$. The root test and `cnt` checks are constant time. Deletion range queries occur only when $N\le6$; at most six indices each make two $O(\log N)$ range queries. Since this branch is restricted to a fixed maximum of six elements, it does not change the overall per-query asymptotic bound.

Under the usual word-RAM convention where GCD on bounded machine integers is treated as constant-time, total source time is

$$
O((N+Q)\log N).
$$

If Euclid's arithmetic cost is made explicit, each GCD can cost $O(\log V)$, giving a conservative bit-operation bound of $O((N+Q)\log N\log V)$.

The tree array is allocated with $4N$ slots and contains $O(N)$ nodes. Recursive tree operations use $O(\log N)$ call-stack depth. Total auxiliary space is

$$
O(N).
$$

This differs materially from the Optimal manifest. The source does not build a sieve, factor values, or maintain prime evidence, so it has no $O(M\log\log M)$ preprocessing and no $O(M)$ prime table. Its actual mechanism is a GCD segment tree plus the six-element number-theoretic bound.

The method mutates `nums` in place as it applies queries, which is consistent with cumulative updates but visible to the caller.

## Alternatives and edge cases

- **Prime-evidence maintenance:** One can characterize indispensable normalized values through prime factors, matching the manifest summary, but the checked-in source instead uses direct range GCDs and the bounded witness theorem.
- **Prefix and suffix GCD per query:** Rebuilding arrays after every update would cost $O(NQ)$ and is too slow; the segment tree supports changing GCD data logarithmically.
- **No divisible values:** The root remains zero rather than $p$, so no nonempty good subsequence exists.
- **Root GCD larger than \(p\):** Removing elements cannot lower a GCD to $p$; it can only preserve or increase the common divisor.
- **Some values not divisible by \(p\):** When the divisible-value GCD is $p$, those divisible values themselves form a proper subsequence, regardless of the unusable values.
- **All values divisible and \(N>6\):** The value ceiling forces at least one redundant normalized element, so a proper GCD-$p$ subsequence exists.
- **All values divisible and \(N\le6\):** The source must test deletion GCDs because a small set can be minimally necessary to reach GCD $p$.
- **Two-element array:** A good proper subsequence has one element, so one of the values must itself equal $p$; the deletion checks capture this exactly.
- **Empty range identity:** Returning zero for an empty segment is correct because $\gcd(0,x)=x$.
- **Update remains divisible:** The source removes the old value and inserts the new one, leaving `cnt` unchanged overall while correctly changing the GCD.
- **Update changes divisibility:** `cnt` and the leaf's zero/nonzero status change together, preserving both maintained facts.
- **Repeated query index:** Updating `nums[idx]` ensures the next query removes the most recent value, not the original one.
- **Input mutation:** The final contents of `nums` reflect all queries; callers needing the original array must pass a copy.
- **Required library name:** Standalone execution needs `gcd` from Python's `math` module.
