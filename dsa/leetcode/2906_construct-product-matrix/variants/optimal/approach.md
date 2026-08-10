## General

**Flatten the matrix conceptually.** Row-major order lists cells as `grid[0][0]`, `grid[0][1]`, and so on through the final row. For any current cell, all other elements split into two groups: those before it in this order and those after it.

If `prefix` is the product before the cell and `suffix` is the product after it, the required answer is

$$
\texttt{prefix}\cdot\texttt{suffix}\pmod{12345}.
$$

The algorithm computes these two contributions without physically flattening the matrix.

**Why division is not safe.** A tempting method multiplies every grid value and divides by the current one. Modular division requires a multiplicative inverse, and not every value has an inverse modulo 12345 because the modulus is composite. Values divisible by three, five, or 823 can share factors with it; a value equal to 12345 becomes zero modulo the modulus. Prefix and suffix products avoid division completely.

**Reverse pass stores each suffix in the output.** `suf` starts at one, the multiplicative identity. The loops move from the bottom-right cell backward in row-major order. Before incorporating current `grid[i][j]`, `suf` is exactly the product of all cells after it. The source stores that value in `p[i][j]`.

Then it updates:

`suf = suf * grid[i][j] % mod`.

That makes `suf` correct for the next cell to the left. Taking the modulus after each multiplication is valid because

$$
(ab)\bmod M
=
((a\bmod M)(b\bmod M))\bmod M.
$$

It also prevents intermediate products from growing unnecessarily.

**Forward pass multiplies each stored suffix by its prefix.** `pre` also starts at one. The loops now move top-left to bottom-right. Before current cell is incorporated, `pre` is the product of every earlier cell. The assignment

`p[i][j] = p[i][j] * pre % mod`

combines “everything after” already stored in `p` with “everything before” held in `pre`. Current cell appears in neither factor, so it is excluded exactly once.

After writing the answer, `pre = pre * grid[i][j] % mod` includes current cell for the next position.

**Order within each cell is essential.** In the reverse pass, store `suf` before multiplying by current value; otherwise the cell would be included in its own answer. In the forward pass, combine with `pre` before updating `pre` for the same reason.
During reverse traversal, before processing flattened position $q$, `suf` equals the product of positions greater than $q$ modulo 12345. Initialization is correct beyond the final cell because the empty product is one. The store and update preserve the invariant backward.

During forward traversal, before position $q$, `pre` equals the product of positions smaller than $q$. Reverse invariant already placed the greater-position product in `p[q]`. Their product is therefore every grid value except current one. Forward update preserves the prefix invariant. This proves every output cell.

**Trace `[[1,2],[3,4]]`.** At the top-left cell, the stored suffix is `2*3*4=24` and prefix is one, yielding 24. At the top-right, suffix is `3*4=12` and prefix is one, yielding 12. Later cells similarly combine opposite sides to produce eight and six.

**Why values equivalent to zero modulo 12345 are handled.** A total-product division method would struggle when one or more factors are zero modulo the modulus. Prefix/suffix multiplication simply carries those zeros through whichever answers include them. For `[[12345],[2],[1]]`, excluding 12345 leaves product two, while answers excluding either other value still include 12345 and become zero.

The output matrix `p` doubles as suffix storage, so no separate prefix or suffix matrix is allocated.

## Complexity detail

Let $N=nm$ be the total number of cells. Two complete traversals perform constant work per cell, giving $O(N)$ time. Output matrix `p` contains $N$ values and uses $O(N)$ space.

Excluding required output storage, the algorithm uses only `pre`, `suf`, dimensions, and loop indices, so auxiliary space is $O(1)$. The manifest reports $O(N)$ space including the output, whereas the editorial uses the common convention of calling auxiliary space $O(1)$.

## Alternatives and edge cases

- **Total product plus division:** Invalid under a composite modulus when current values lack modular inverses.
- **Separate prefix and suffix matrices:** Correct but wastes another $O(N)$ storage; the source stores suffixes in the output.
- **Single row or column:** Row-major traversal still acts like the standard one-dimensional except-self algorithm.
- **Factor equal to 12345:** It becomes zero modulo the modulus and is handled naturally.
- **Multiple modular zeros:** Any answer including one becomes zero; excluding one may still include another.
- **Minimum two cells:** Each output is simply the other value modulo 12345.
- **Large raw values:** Reducing after every multiplication keeps stored residues bounded.
- **Output-space convention:** Distinguish $O(N)$ returned storage from $O(1)$ extra working state.
- **Traversal order is part of the proof:** The reverse pass writes the product strictly after each cell, and the forward pass multiplies by the product strictly before it. Including the current factor in either update too early would violate the except-self requirement.
