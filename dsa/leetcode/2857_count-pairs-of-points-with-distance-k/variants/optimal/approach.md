## General

**Turn the distance equation into a lookup.** For two points $(x_1,y_1)$ and $(x_2,y_2)$, define

$$
a=x_1\mathbin{\mathrm{XOR}}x_2
\quad\text{and}\quad
b=y_1\mathbin{\mathrm{XOR}}y_2.
$$

Both quantities are non-negative integers, and the required distance condition is simply $a+b=k$. Because `k` is at most `100`, every possible split can be enumerated: choose $a$ from `0` through `k`, and then $b$ must be `k - a`. There are only `k + 1` splits.

The key property of XOR is that it is its own inverse. From

$$
x_1\mathbin{\mathrm{XOR}}x_2=a,
$$

XOR both sides with $x_2$ to obtain

$$
x_1=a\mathbin{\mathrm{XOR}}x_2.
$$

The same reasoning gives $y_1=b\mathbin{\mathrm{XOR}}y_2$. Therefore, after fixing the current point $(x_2,y_2)$ and a split $(a,b)$, there is exactly one coordinate pair that could be its partner: `x1 = a ^ x2` and `y1 = b ^ y2`.

This changes the task from “compare the current point with every older point” into “ask how many times this one required partner has appeared.”

**Why the frequency map contains only earlier points.** The solution processes `coordinates` from left to right. Before handling the point at current index $j$, `cnt[(x, y)]` is the number of occurrences of that coordinate among indices strictly smaller than $j$. For each distance split, the solution adds the count of the required coordinate to `ans`. Only after all splits have been queried does it execute `cnt[(x2, y2)] += 1`.

That order automatically enforces $i<j$. A point cannot pair with itself because it is absent from the map during its own queries. A pair is not counted again in reverse order because when the later endpoint is processed, only the earlier endpoint is eligible; the algorithm never goes backward and recounts the same index pair.

**Why enumerating the splits is complete.** Consider any valid pair ending at the current point. Its two XOR contributions have definite values $a$ and $b$. Since the pair's distance is `k`, they satisfy $a+b=k$, so the loop eventually reaches exactly that `a`, sets `b = k - a`, reconstructs precisely the earlier point, and counts it. Thus every valid pair is included.

Conversely, whenever the map contributes a count, the reconstructed coordinate satisfies `x1 ^ x2 == a` and `y1 ^ y2 == b`. Its distance is therefore $a+b=k$, so every counted pair is valid. Completeness and soundness together prove the accumulated answer is exact.

Different split values cannot accidentally count the same coordinate occurrence twice for one current point. If two values $a_1$ and $a_2$ reconstructed the same $x_1$, then `a1 ^ x2 == a2 ^ x2`; XORing both sides with `x2` implies $a_1=a_2$. Once $a$ is fixed, $b=k-a$ is also fixed. Each candidate coordinate therefore belongs to only one split.

**Example of the lookup process.** Suppose the current point is `(4, 2)` and `k = 5`. For `a = 5` and `b = 0`, the required earlier point is `(5 ^ 4, 0 ^ 2) = (1, 2)`. If `(1, 2)` has appeared twice, both earlier indices form valid pairs, so the counter contributes `2`. The algorithm correctly counts index pairs, not merely distinct coordinate values.

For `k = 0`, the loop has only $a=b=0$. XOR distance zero requires both coordinates to be identical, so each occurrence adds the number of identical earlier occurrences. Five copies contribute `0 + 1 + 2 + 3 + 4 = 10`, matching the number of unordered index pairs.

## Complexity detail

Let $n$ be the number of points. The outer loop runs $n$ times and the inner loop runs exactly $k+1$ times. Each iteration performs constant-many integer XOR operations and one expected constant-time hash-table lookup. The expected running time is therefore $O(n(k+1))$, conventionally written $O(nk)$ when emphasizing the parameter `k`. Because `k <= 100`, this is effectively linear in the input size under the stated constraints, but retaining `k` in the bound explains the algorithm's mechanism.

The counter stores at most one entry per distinct coordinate seen. If $u$ is the number of distinct points, auxiliary space is $O(u)$ and is $O(n)$ in the worst case. Python's `Counter` lookup for a missing key returns zero, which is exactly what the accumulation needs. Hash-table bounds are expected or amortized; pathological collision behavior is not the standard model used for this solution.

The maximum answer is $\binom{n}{2}$, which may exceed a 32-bit signed integer for `n = 50000`; Python handles that automatically. Implementations in fixed-width languages should use a 64-bit result.

## Alternatives and edge cases

- **Brute-force pairs:** Test all $\binom n2$ pairs directly in $O(n^2)$ time and $O(1)$ extra space. It is simple but far too slow for `50000` points.
- **Why not enumerate coordinate bits:** The small quantity is `k`, not the coordinate range. Splitting `k` into $a+b$ gives only at most `101` cases even though coordinates reach $10^6$.
- **Duplicate coordinates:** The counter stores multiplicity, so separate earlier indices at the same coordinate are all counted. This is essential for `k = 0`.
- **Zero target distance:** Only identical points qualify, and the single split `(0, 0)` handles the case without special branching.
- **Repeated candidate concern:** XOR is bijective when one operand is fixed, so distinct `a` values yield distinct required `x1` values and cannot double-count one earlier point.
- **Ordering requirement:** Inserting the current point after querying is crucial. Inserting first would incorrectly permit pairing a point with itself when `k = 0`.
- **Large answer:** Use a wide integer type outside Python because the count of pairs can be about $1.25\times10^9$.
