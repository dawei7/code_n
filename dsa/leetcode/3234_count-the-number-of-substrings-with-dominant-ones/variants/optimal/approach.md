## General

**Separate substrings by their exact zero count.** A substring with $z$ zeroes needs at least $z^2$ ones, so its length must be at least $z^2+z$. Consequently no qualifying substring can have $z^2+z>n$, leaving only $O(\sqrt n)$ positive zero counts to consider.

Count the $z=0$ case directly. Each maximal run of $q$ ones contributes $q(q+1)/2$ all-one substrings.

**Represent positive-zero substrings by consecutive zero positions.** Store every zero index with sentinels at $-1$ and $n$. Fix $z\geq1$ and a consecutive block of $z$ stored zeroes. Any substring containing exactly this block chooses:

- its left endpoint after the preceding zero and at or before the first selected zero;
- its right endpoint at or after the last selected zero and before the following zero.

If these ranges have sizes $L$ and $R$, every pair of endpoint choices contains exactly the selected zero block. Let $C$ be the distance from the first selected zero through the last, and let $x$ and $y$ be the extra characters included on the left and right. The dominance condition is

$$
C+x+y\geq z^2+z.
$$

There are $LR$ endpoint pairs in total. Count and subtract the pairs with $x+y<z^2+z-C$. The invalid pairs form a clipped arithmetic triangle in the $L$-by-$R$ choice grid: some initial rows may be completely invalid, followed by rows whose invalid lengths decrease by one. Their sum is computed in constant time.

Every substring with positive zero count has one unique consecutive block of stored zeroes, so it is considered once. The endpoint inequality is equivalent to the original ones-versus-zeroes condition, proving that exactly the dominant choices are added.

## Complexity detail

For each of $O(\sqrt n)$ feasible positive zero counts, at most $O(n)$ consecutive zero blocks are inspected. The time complexity is $O(n\sqrt n)$. Storing zero positions uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every substring:** Updating zero and one counts incrementally is correct but takes $O(n^2)$ time.
- **Use one ordinary sliding window:** The validity threshold changes quadratically with the zero count and is not monotone under both endpoint movements in the way a single window requires.
- All-one substrings always qualify because $0^2=0$.
- All-zero substrings never qualify because they contain no ones.
- Equality qualifies: one zero and one one satisfy $1\geq1^2$.
- A substring with $z$ zeroes is impossible once $z^2+z>n$.
- Sentinel zero positions make leading and trailing endpoint choices use the same formula as interior blocks.
- The answer can be quadratic in $n$, so implementations should use a sufficiently wide integer type.
