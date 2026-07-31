## General

**Greedily choose the smallest safe values**

To minimize the sum, consider positive integers in increasing order. Choosing a value $x<\texttt{target}$ excludes its complement $\texttt{target}-x$. For every pair whose two different values add to `target`, the smaller member contributes less to the sum, so an optimal construction always keeps that member and skips the larger one.

The positive integers below half the target therefore form the first safe block. Let

$$
a=\min\!\left(n,\left\lfloor\frac{\texttt{target}}{2}\right\rfloor\right).
$$

The construction takes $1,2,\ldots,a$. When `target` is even, the final value in that range may be `target // 2`. Using it once is legal: the condition concerns two distinct indices, and pairwise distinctness prevents a second copy.

**Jump over every excluded complement**

If $a<n$, the selected low values exclude all integers from `target - a` through `target - 1`. With the full low block selected, every integer strictly between `target // 2` and `target` is either an excluded complement or no smaller than one. The next available value is therefore `target`, followed by consecutive integers `target + 1`, `target + 2`, and so on. None of these values can form the forbidden sum with a positive integer because each is already at least `target`.

Let $b=n-a$. The selected values are exactly

$$
1,2,\ldots,a
$$

and, when $b>0$,

$$
\texttt{target},\texttt{target}+1,\ldots,\texttt{target}+b-1.
$$

This is the increasing greedy construction: at every position it uses the smallest value that can extend the already chosen set. Replacing any selected value by a smaller unselected positive integer is impossible without either duplicating a chosen value or introducing a forbidden complement. Thus no valid array can have a smaller sorted sequence, and consequently none can have a smaller sum.

**Sum both blocks without constructing them**

The first block sums to

$$
\frac{a(a+1)}{2},
$$

while the $b$-term arithmetic progression beginning at `target` sums to

$$
\frac{b(2\,\texttt{target}+b-1)}{2}.
$$

Add these expressions using exact integer arithmetic and apply the modulus only to the final result.

## Complexity detail

The algorithm evaluates a fixed number of integer operations, independent of `n` and `target`, so it takes $O(1)$ time and uses $O(1)$ auxiliary space.

The benchmark uses `n` as `size` and fixes `target = 2`, making every expected sum a directly checkable arithmetic series. A correct calibration implementation performs a doubling traversal up to `n` before evaluating the same formula. It completes every ordinary and benchmark case, but its $O(\log n)$ work fails the constant-time scaling verdict. An explicit set-based constructor is slower still.

## Alternatives and edge cases

- **Explicit greedy set:** Test positive integers in increasing order and keep a value when its complement is absent from a set. This directly mirrors the reasoning and is correct, but it takes $O(n)$ time and $O(n)$ space, which cannot support $n=10^9$.
- **Doubling traversal before the formula:** Walking through powers of two up to `n` and then evaluating the formulas remains correct, but introduces unnecessary $O(\log n)$ work. The benchmark uses this as a completing slower-class calibration.
- **Pair-by-pair selection:** View each pair $(x,\texttt{target}-x)$ below `target` and retain its smaller member. This reaches the same two arithmetic progressions but is still linear if the pairs are enumerated.
- **Even target midpoint:** `target // 2` is safe once because two distinct indices would require two copies, which pairwise distinctness forbids.
- **Enough low values:** If $n \le \lfloor\texttt{target}/2\rfloor$, the answer is simply the sum from $1$ through $n$.
- **Target one:** No two positive integers sum to $1$, so the minimum array is $[1,2,\ldots,n]$.
- **Modulo timing:** Reducing only after computing the exact formulas avoids changing the greedy choice and is safe in Python; fixed-width languages must use a sufficiently wide integer type for intermediate products.
