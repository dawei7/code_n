## General

Only the number of available values matters. Subtracting `l` from every entry preserves equality and comparison direction, so replace `[l, r]` by ranks from `0` through $m-1$, where $m=\texttt{r}-\texttt{l}+1$.

Because adjacent values cannot be equal, each adjacent comparison is either upward or downward. The ban on three strictly monotone consecutive values says precisely that two neighboring comparisons cannot have the same direction. Thus every valid array alternates between upward and downward steps.

**Count one small alphabet with directional states**

For an alphabet of size $q$, let `up[v]` count arrays of the current length that end at rank `v` with an upward last step, and let `down[v]` count those with a downward last step. At length two,

$$
\texttt{up[v]}=v
\qquad\text{and}\qquad
\texttt{down[v]}=q-1-v,
$$

because an upward pair may start at any smaller rank, while a downward pair may start at any larger rank.

An upward step must follow a downward one and must come from a smaller last value. A downward step has the symmetric rule:

$$
\begin{aligned}
\texttt{next\_up[v]} &= \sum_{u<v}\texttt{down[u]},\\
\texttt{next\_down[v]} &= \sum_{u>v}\texttt{up[u]}.
\end{aligned}
$$

A left-to-right prefix sum and a right-to-left suffix sum compute every transition in $O(q)$ time. After reaching length `n`, summing both directional arrays counts all valid arrays: their first step is either upward or downward, and the two sets are disjoint.

**Why a few alphabet sizes determine the huge one**

Let $F(m)$ be the answer before the modulus is applied. Group valid arrays by their equality and relative-order pattern. A pattern using exactly $k$ distinct ranks can be instantiated by choosing those ranks from the $m$ available values, contributing a fixed multiple of $\binom{m}{k}$. Since $k\le n$, $F(m)$ is a polynomial in $m$ of degree at most $n$.

Compute $F(q)$ modulo $10^9+7$ for every $q$ from $0$ through $n$. These $n+1$ values uniquely determine that polynomial. For the actual $m$, evaluate it with Lagrange interpolation at the consecutive points:

$$
F(m)=\sum_{i=0}^{n}F(i)
\frac{\prod_{0\le j\le n,\ j\ne i}(m-j)}{i!\,(-1)^{n-i}(n-i)!}.
$$

Prefix and suffix products provide each numerator with all factors except `m - i` in constant time. Factorials and inverse factorials provide the denominators. The modulus is prime, and every factorial index is at most `200`, so all required inverses exist. If $m\le n$, return the already computed sample directly.

The directional recurrence counts exactly every legal comparison sequence for each sampled alphabet. The polynomial argument then proves that interpolation gives the same count at the actual, possibly enormous interval size.

## Complexity detail

For a sampled alphabet size $q$, the directional DP uses $O(nq)$ time. Summing this over $q=1,2,\ldots,n$ takes $O(n^3)$ time. Consecutive-point interpolation adds $O(n)$ time. The current and next directional arrays, samples, factorials, and product arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **DP over the actual interval:** The same prefix/suffix transitions take $O(nm)$ time and $O(m)$ space, but $m$ may be $10^9$, so the real alphabet cannot be materialized.
- **Direct predecessor scans for every sample:** Replacing prefix and suffix sums with a scan over all smaller or larger ranks remains correct but raises the total time to $O(n^4)$.
- **Order-polynomial coefficient methods:** One can derive the fence-poset counting polynomial in another basis, but the recurrence and consecutive-point interpolation are simpler to audit at `n <= 200`.
- **Two available values:** Once the first value is chosen, every later value is forced, so exactly two arrays are valid for every legal `n`.
- **Strict comparisons:** Equal adjacent values belong to neither directional state; using inclusive prefix or suffix ranges would count invalid arrays.
- **Both starting directions:** Length-two initialization records upward and downward starts separately. Omitting either half loses its mirror-image arrays.
- **Modular signs:** The Lagrange denominator contributes $(-1)^{n-i}$, so negative terms must be normalized modulo $10^9+7$.
