## General

**Reduce rearrangement to character multiplicities.** A string can be
rearranged to contain `"leet"` exactly when it contains at least one `l`, at
least two `e` characters, and at least one `t`. Once those four characters are
available, place them consecutively as `"leet"` and arrange every remaining
character arbitrarily around them.

**Count the complement with three bad events.** Among all $26^n$ lowercase
strings, let $A$ mean no `l`, $B$ mean no `t`, and $C$ mean fewer than two `e`
characters. Their individual counts are

$$
\lvert A\rvert=\lvert B\rvert=25^n,
\qquad
\lvert C\rvert=25^n+n25^{n-1}.
$$

The two terms for $C$ count zero `e` characters and exactly one `e`, whose
position has $n$ choices. Thus the sum of single-event counts is
$3\cdot25^n+n25^{n-1}$.

**Account for intersections without losing the repeated `e`.** Strings in
$A\cap B$ use 24 letters. For $A\cap C$, excluding `l` leaves 24 non-`e`
letters when there is no `e`, or one chosen `e` position plus 24 choices at
every other position; $B\cap C$ is symmetric. The pairwise total is therefore

$$
3\cdot24^n+2n24^{n-1}.
$$

Finally, $A\cap B\cap C$ has size $23^n+n23^{n-1}$. Inclusion-exclusion gives

$$
26^n-3\cdot25^n-n25^{n-1}
+3\cdot24^n+2n24^{n-1}
-23^n-n23^{n-1}.
$$

Every string missing a required multiplicity cancels, while every good string
remains once. Evaluate each power modulo $10^9+7$ and normalize the final
expression modulo the same value.

## Complexity detail

There are a constant number of modular exponentiations, each taking
$O(\log n)$ time by repeated squaring. All other arithmetic is constant, so
total time is $O(\log n)$ and auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Capped-state dynamic programming:** Track whether `l` and `t` have appeared and cap the `e` count at two; eight states give $O(n)$ time and $O(1)$ space.
- **Enumerate character counts:** Summing multinomial counts over all valid multiplicities introduces unnecessary nested ranges.
- **Lengths below four:** No string can supply all four characters of `"leet"`, and the formula evaluates to zero modulo $10^9+7$.
- **Exactly four characters:** The only valid multiset is `{l, e, e, t}`, producing $4!/2!=12$ strings.
- **Repeated `e`:** Counting only the presence of `e` is insufficient; two copies are required.
- **Modulo subtraction:** Intermediate inclusion-exclusion terms may be negative, so the final result must be normalized modulo $10^9+7$.
