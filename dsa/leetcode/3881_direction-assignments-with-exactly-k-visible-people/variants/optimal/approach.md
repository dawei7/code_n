## General

**Separate people by which side of the observer they occupy**

There are

$$
l=\texttt{pos}
$$

people to the observer's left and

$$
r=n-\texttt{pos}-1
$$

people to the right.

A left-side person is visible exactly when choosing `'L'`. A right-side person is visible exactly when choosing `'R'`. The observer's own direction never changes visibility.

Suppose exactly `a` visible people are selected from the left. Then exactly

$$
b=k-a
$$

must be selected from the right.

**Choose visible subsets; all other directions are forced**

There are

$$
\binom la
$$

ways to choose which left-side people are visible. Once chosen, their directions are forced to `'L'`, while every unchosen left-side person must choose `'R'` to remain invisible.

Similarly, there are

$$
\binom rb
$$

ways to choose the visible right-side people. Chosen people must face `'R'` and unchosen people must face `'L'`.

Thus a fixed feasible split `(a,b)` gives

$$
\binom la\binom rb
$$

assignments for everyone except the observer.

The observer may independently choose either direction, doubling every count:

$$
2\binom la\binom rb.
$$

**Enumerate every feasible visibility split**

The source loops

`a = 0,1,\ldots,min(k,l)`.

This ensures `a` is nonnegative, does not exceed the number of left people, and does not exceed the total required visible count. It computes `b=k-a`, which is automatically nonnegative, and includes the term only when `b<=r`.

Every assignment with exactly `k` visible people has one unique value of `a`, the number visible on the left. Different loop iterations therefore represent disjoint assignment sets. Summing all feasible terms counts every valid direction assignment once.

**Examples**

For `n=3`, `pos=1`, and `k=0`, `l=r=1`. Only `a=b=0` is feasible. Both non-observers have forced invisible directions, and the observer has two choices. The answer is two.

For `n=3`, `pos=2`, and `k=1`, there are two people left and none right. The only feasible split is `a=1,b=0`. Choosing one of the two left people gives `\binom21=2` choices, and the observer doubles this to four.

For `n=1` and `k=0`, `l=r=0`. The term is

$$
2\binom00\binom00=2,
$$

representing the observer's two directions.

**Vandermonde reveals a simpler identity**

The loop sum without the observer factor is

$$
\sum_a\binom la\binom r{k-a}.
$$

Vandermonde's identity gives

$$
\sum_a\binom la\binom r{k-a}
=\binom{l+r}{k}
=\binom{n-1}{k}.
$$

This also follows directly: among the `n-1` non-observers, choose any `k` people to be visible. Each chosen person's required direction is determined by their side, and every unchosen person's invisible direction is determined. Hence the answer is simply

$$
2\binom{n-1}{k},
$$

independent of `pos`.

The protected source evaluates the split sum rather than using this one-term simplification. Both are correct.

**Factorials and modular combinations**

The module precomputes `f[i]=i!\bmod MOD` for `0\le i\le100000`.

It also stores

$$
g[i]=(i!)^{-1}\bmod MOD.
$$

For each `i\ge1`, the source calculates the inverse as

`pow(f[i], MOD - 2, MOD)`.

Because `MOD=10^9+7` is prime and `i<MOD`, `f[i]` is nonzero modulo `MOD`. Fermat's little theorem makes the exponentiation a valid multiplicative inverse.

Then

$$
\binom nk
\equiv f[n]g[k]g[n-k]\pmod{MOD}.
$$

The loop parameters ensure every call has `0\le k\le n`. Each term and the running answer are reduced modulo `MOD`.

**Exact-source preprocessing matters**

The arrays are created at module load, before the method is called. Computing every inverse factorial with a separate modular exponentiation is correct but more expensive than the standard technique of computing one inverse at the end and filling backward.

This cost is part of the exact source even though the manifest reports only method-level query complexity.

## Complexity detail

After preprocessing, the method loop has at most `min(k,l)+1\le n` iterations. Each combination lookup and modular arithmetic operation is constant time, so per-call time is `O(n)` and extra per-call space is `O(1)`. This matches the manifest if shared precomputed tables are excluded.

The exact module-level preprocessing uses `N_{max}=100001` entries. Factorials take `O(N_{max})` time. Computing one modular exponentiation for each inverse takes

$$
O(N_{max}\log MOD)
$$

time. Arrays `f` and `g` use `O(N_{max})` space.

Thus a cold execution of the exact file has `O(N_{max}\log MOD+n)` time and `O(N_{max})` space. The manifest's `O(1)` space does not include these real global arrays.

Using Vandermonde would reduce each query to `O(1)` after the same tables. Standard inverse-factorial preprocessing can be reduced to `O(N_{max}+\log MOD)` time.

## Alternatives and edge cases

- **Use Vandermonde directly:** Return `2*C(n-1,k)`. This is simpler, independent of `pos`, and constant-time per query after factorial preprocessing.
- **Enumerate all direction strings:** There are `2^n` assignments and is infeasible.
- **Dynamic programming by people and visible count:** Correct in `O(nk)` time but unnecessary because each visible subset uniquely fixes directions.
- **Pascal-triangle combinations:** Avoid modular inverses but requires `O(nk)` preprocessing or space.
- **Efficient inverse-factorial table:** Compute `g[N-1]` once, then use `g[i-1]=g[i]\cdot i\bmod MOD` while descending. This replaces 100,000 exponentiations with one.
- **Observer direction:** Always contributes a factor of two, including when there are no other people.
- **Observer at an endpoint:** One side count is zero; the loop naturally forces all visible people to come from the other side.
- **`k=0`:** Every non-observer's direction is forced invisible, while the observer remains free, yielding two.
- **`k=n-1`:** Every non-observer is forced visible, again with two observer choices.
- **Invalid split:** `b>r` is skipped; `b<0` cannot occur because `a\le k`.
- **Modulo arithmetic:** Reduce the sum because the number of assignments may be large.
- **Position independence:** Though side-specific directions differ, the total count is always `2\binom{n-1}{k}`.
- **Global source cost:** Do not describe the exact file as truly constant-space without stating that it allocates two large shared arrays.
