## General

**Extend only alternating selections**

Track how many one-building selections end in each type and how many valid alternating two-building selections end in each type. When the current building has type $b$, every existing pair ending in $1-b$ becomes a valid alternating triple, so add that pair count to the answer.

The current building can also finish a new alternating pair after any earlier single building of type $1-b$. Add that single count to the pair count ending in $b$, then count the current building as another single ending in $b$. Updating longer selections before shorter ones prevents the same index from being used twice.

After each character, the stored counts represent every increasing alternating subsequence of lengths one and two within the processed prefix. Extending exactly the opposite-ending pairs counts every valid `010` or `101` triple at its final index, once and only once.

## Complexity detail

Let $n=\lvert s\rvert$. Each character performs a constant number of counter updates, so time is $O(n)$.

The two fixed-size counter arrays and answer use $O(1)$ space.

## Alternatives and edge cases

- **Enumerate triples:** Checking all index triples directly is correct but costs $O(n^3)$ time.
- **Choose each middle building:** Multiplying opposite-type counts to its left and right also yields an $O(n)$ solution, but requires total counts or a reverse pass.
- **General subsequence dynamic programming:** A table for the literal patterns `010` and `101` works but stores more states than necessary.
- **All one type:** No alternating pair exists, so the answer is zero.
- **Exactly three buildings:** The result is one only when the entire string alternates.
- **Repeated equal runs:** Indices remain distinct choices even when their building types are equal.
- **Large result:** The number of triples can exceed 32-bit integer range.
