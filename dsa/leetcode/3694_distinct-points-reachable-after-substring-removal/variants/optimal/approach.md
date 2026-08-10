## General

Executing a movement string adds one displacement vector per character. Because vector addition is associative and commutative, the final coordinate after removing a substring equals:

$$
\text{displacement of all moves}
-
\text{displacement of the removed moves}.
$$

The retained prefix and suffix still execute in their original order, but order does not affect their final vector sum. Therefore, the algorithm never has to rebuild and simulate each remaining string. It computes every removable substring's displacement in constant time using prefix coordinates.

**Prefix coordinates**

The source creates two arrays of length $n+1$:

- `f[i]` is the horizontal coordinate after executing the first $i$ moves;
- `g[i]` is the vertical coordinate after executing the first $i$ moves.

Both index-zero entries remain zero, representing the starting point before any move.

The running variables `x` and `y` are updated for each character:

- `U` increments `y`;
- `D` decrements `y`;
- `L` decrements `x`;
- `R` reaches the final `else` branch and increments `x`.

After processing character number `i` in one-based enumeration, the source stores the new coordinate in `f[i]` and `g[i]`.

At the end:

$$
(f[n],g[n])
$$

is the endpoint of the complete, unmodified movement string.

**Displacement of one removed window**

The second loop uses `i` as the exclusive prefix length at the window's right boundary. The removed substring contains the $k$ characters whose zero-based indices are:

$$
i-k,\ldots,i-1.
$$

The coordinate after the prefix ending just before this window is `(f[i-k], g[i-k])`. The coordinate after also executing the window is `(f[i], g[i])`. Subtracting gives the window's displacement:

$$
\left(f[i]-f[i-k],\ g[i]-g[i-k]\right).
$$

This calculation works even though the path may turn and revisit coordinates. Only the net displacement of the removed moves affects the final endpoint.

**Subtracting the removed contribution**

If the full string's displacement is $(X,Y)$ and the window's displacement is $(d_x,d_y)$, the remaining moves end at:

$$
(X-d_x,\ Y-d_y).
$$

The source computes:

`a = f[n] - (f[i] - f[i - k])`

`b = g[n] - (g[i] - g[i - k])`

and inserts tuple `(a, b)` into `st`.

The set is necessary because different removed substrings may lead to the same endpoint. The problem asks for distinct coordinates, not the number of removal positions.

**Covering every legal removal exactly once**

A length-$k$ substring can end after prefix lengths:

$$
k,k+1,\ldots,n.
$$

The loop:

`for i in range(k, n + 1):`

visits exactly these $n-k+1$ possibilities. The first iteration removes characters zero through $k-1$; the last removes characters $n-k$ through $n-1$.

No shorter or longer substring is considered, so the “exactly one substring of length $k$” requirement is respected.

**Why endpoint order can be reduced to vector arithmetic**

Let the original string be prefix $P$, removed block $B$, and suffix $S$. Its total displacement is:

$$
\Delta(P)+\Delta(B)+\Delta(S).
$$

After removal, the executed string is $PS$, whose displacement is:

$$
\Delta(P)+\Delta(S)
=\Delta(P)+\Delta(B)+\Delta(S)-\Delta(B).
$$

This is exactly the formula used by the source. Every set entry corresponds to one legal removal, and every legal removal contributes its endpoint to the set. The set's final size is therefore the number of distinct reachable points.

**Tracing the first example**

For `s = "LUL"`:

- prefix coordinates are $(0,0)$, $(-1,0)$, $(-1,1)$, and $(-2,1)$;
- the full displacement is $(-2,1)$.

With `k = 1`:

- removing the first `L` subtracts $(-1,0)$, producing $(-1,1)$;
- removing `U` subtracts $(0,1)$, producing $(-2,0)$;
- removing the last `L` again produces $(-1,1)$.

Three removals create two distinct tuples, so the method returns two.

## Complexity detail

Let $n$ be `len(s)`.

Building the prefix-coordinate arrays visits every movement once and takes $O(n)$ time. The removal loop has $n-k+1\le n$ iterations, each performing constant arithmetic and an expected $O(1)$ set insertion. Total expected time is $O(n)$.

The two prefix arrays contain $2(n+1)$ integers. The endpoint set can contain up to $n-k+1$ tuples. Worst-case auxiliary space is $O(n)$.

Hash-set operations provide expected constant time; this is the standard model behind the manifest's linear bound.

## Alternatives and edge cases

- **Rebuild every remaining string:** Removing each window and simulating its $n-k$ moves costs $O(n^2)$ total time.
- **Prefix and suffix endpoint arrays:** One can combine a prefix displacement before the window with a suffix displacement after it. The total-minus-window formula needs only the two ordinary prefix arrays.
- **Rolling window displacement:** The removed block's vector can be updated by removing its outgoing move and adding its incoming move, reducing prefix-array workspace. The endpoint set can still require $O(n)$ space.
- **`k = n`:** There is one legal removal, the remaining string is empty, and the computed endpoint is $(0,0)$.
- **`k = 1`:** Every single movement is considered as the removed block.
- **Different removals with one endpoint:** The set intentionally collapses them, as in `"UU"` with `k = 1`.
- **Path revisits:** Prefix coordinates need not be unique. Subtracting two prefix vectors still gives the exact net displacement of their intervening substring.
- **Order of retained moves:** The prefix remains before the suffix, but final coordinates depend only on the sum of move vectors; no reordering is actually performed.
- **Infinite grid:** Coordinates may become negative, and tuple hashing handles signed integers directly.
- **Mandatory removal:** The loop never inserts the full-string endpoint unless some legal removal happens to have zero displacement. It does not include a “remove nothing” option.
