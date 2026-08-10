## General

**Compress twelve row colorings into two pattern types**

Each row has three cells. Horizontal neighbors must have different colors, so the first cell has three choices, the second has two choices different from the first, and the third has two choices different from the second. There are $3 \cdot 2 \cdot 2 = 12$ legal colorings for one row.

Those twelve colorings fall into only two structural types:

- In an ABA pattern, the first and third cells use the same color while the middle uses another, such as red-yellow-red.
- In an ABC pattern, all three cells use different colors, such as red-yellow-green.

There are six colorings of each type. For ABA, choose the repeated color in three ways and the middle color in two ways. For ABC, choose a permutation of all three colors in $3! = 6$ ways.

The exact color names do not affect how many next rows are compatible. Only whether the row is ABA or ABC matters. This symmetry is what lets the dynamic program store two numbers instead of all twelve row states.

In the code, `f0` is the number of valid grids ending in an ABA row, and `f1` is the number ending in an ABC row. For the first row:

```python
f0 = f1 = 6
```

Their sum is 12, matching the complete set of legal one-row grids.

**Count transitions from an ABA row**

Fix one ABA row, and name its colors `A B A`. A next row must differ vertically in every column and horizontally between adjacent cells.

There are three compatible next rows of ABA type and two compatible next rows of ABC type. This count is the same no matter which actual colors `A` and `B` represent. Therefore, every grid currently counted by `f0` contributes:

- $3$ possibilities to the next ABA count.
- $2$ possibilities to the next ABC count.

These contributions explain `3 * f0` in `g0` and `2 * f0` in `g1`.

**Count transitions from an ABC row**

Now fix a row whose three colors are all different, `A B C`. Applying the same horizontal and vertical restrictions gives two compatible ABA next rows and two compatible ABC next rows.

Thus every grid counted by `f1` contributes:

- $2$ possibilities to the next ABA count.
- $2$ possibilities to the next ABC count.

Combining both source types produces the recurrence:

$$
\begin{aligned}
g_0 &= 3f_0 + 2f_1,\\
g_1 &= 2f_0 + 2f_1.
\end{aligned}
$$

The code applies the modulus immediately:

```python
g0 = (3 * f0 + 2 * f1) % mod
g1 = (2 * f0 + 2 * f1) % mod
```

Here `g0` and `g1` describe grids with one additional row. After both have been computed from the old state, the simultaneous assignment `f0, f1 = g0, g1` advances the DP.

Computing both new values before overwriting either old one is essential. If `f0` were updated first and then used in the formula for `f1`, the second formula would mix counts from two different row lengths.

**Why the loop runs `n - 1` times**

The initialization already represents a grid with one painted row. Each loop iteration adds exactly one more row. Therefore, reaching $n$ rows requires $n-1$ transitions:

```python
for _ in range(n - 1):
```

For `n = 1`, the range is empty. The algorithm correctly returns `6 + 6 = 12` without applying any transition.

The underscore signals that the loop number itself is irrelevant. Only the repeated state transformation matters.

**A small numerical trace**

For two rows, starting from `f0 = 6` and `f1 = 6`:

$$
g_0 = 3 \cdot 6 + 2 \cdot 6 = 30,
$$

and

$$
g_1 = 2 \cdot 6 + 2 \cdot 6 = 24.
$$

There are $30 + 24 = 54$ valid two-row grids.

For a third row, the state becomes:

$$
g_0 = 3 \cdot 30 + 2 \cdot 24 = 138,
$$

and

$$
g_1 = 2 \cdot 30 + 2 \cdot 24 = 108.
$$

The total is $138 + 108 = 246$. The two counters retain enough information for the next transition while discarding irrelevant exact color labels.

**Why multiplication counts complete grids correctly**

Suppose there are `f0` valid partial grids ending in an ABA row. Each such complete partial grid has exactly three compatible ABA choices for its next row. Pairing every partial grid with each compatible next row yields `3 * f0` distinct extended grids. The same product rule applies to all four transition categories.

The ABA and ABC destination sets do not overlap because a row cannot both have equal outer colors and have all three colors distinct. Contributions from the two previous types are also disjoint because their prefixes are different completed grids. Adding the products therefore neither misses nor double-counts an extension.

By induction, `f0` and `f1` count all valid grids of the current height by final-row type. The base counts are correct for height one, and the transition considers every row compatible with every valid prefix. After $n-1$ transitions, every valid $n$-row grid ends in exactly one of the two types, so `f0 + f1` is the required total.

**Why modular reduction is safe**

The answer can grow exponentially with $n$, but the problem requests only the remainder modulo $10^9+7$. Addition and multiplication respect congruence, so reducing `g0` and `g1` after each recurrence produces the same final remainder as computing enormous exact counts and reducing once at the end.

The return statement applies the modulus once more to the sum:

```python
return (f0 + f1) % mod
```

This ensures the returned value is in the required range even though each individual counter is already reduced.

## Complexity detail

The loop performs exactly $n-1$ iterations. Each iteration uses a fixed number of additions, multiplications by small constants, remainder operations, and assignments. The running time is $O(n)$.

Only `mod`, `f0`, `f1`, `g0`, and `g1` are stored, regardless of the number of rows. The auxiliary space is therefore $O(1)$. No grid, list of row patterns, or DP array proportional to $n$ is constructed.

Modulo reduction also keeps the stored integers below the modulus after every iteration, so arithmetic values do not grow with the exponential number of mathematical colorings.

## Alternatives and edge cases

- **Twelve-state row DP:** Track every legal exact row coloring and test vertical compatibility with every next coloring. This is correct and still $O(n)$ because twelve is constant, but the two-type symmetry produces a smaller and clearer state.
- **Depth-first enumeration:** Recursively choosing a color for every cell explores an exponential number of grids and is infeasible for $n$ up to 5000.
- **Transfer matrix:** The recurrence can be written as a two-by-two matrix applied $n-1$ times. Fast exponentiation reduces time to $O(\log n)$, though the linear loop is already simple and adequate for the constraint.
- **DP array by row:** Storing both counts for every height uses $O(n)$ space. Only the immediately previous pair is needed, so the rolling variables avoid that extra storage.
- **Treating all rows as one state:** Knowing only the total number of prefixes is insufficient because ABA and ABC rows have different numbers of compatible ABA successors.
- **One row:** Initialization already counts all twelve legal rows, and the empty transition loop returns 12.
- **Horizontal adjacency:** Patterns such as AAA or AAB are never states because adjacent equal colors violate the rules within one row.
- **Vertical adjacency:** The transition coefficients count only next rows whose color differs from the prior row in each of the three columns.
- **Color symmetry:** Renaming red, yellow, and green does not change compatibility counts, which justifies grouping exact rows by pattern type.
- **Simultaneous update:** Both `g0` and `g1` must use the old `f0` and `f1`. In-place sequential updates would corrupt the recurrence.
- **Large `n`:** Applying `% mod` every iteration prevents huge counts and returns the required remainder for `n = 5000`.
