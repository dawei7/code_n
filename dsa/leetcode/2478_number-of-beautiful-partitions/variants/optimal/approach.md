## General

**Valid boundaries determine valid parts**

Every part must start with a prime digit from `"2357"` and end with a non-prime digit. Therefore:

- The full string must start prime.
- The full string must end non-prime.
- Every internal cut must occur after a non-prime digit and before a prime digit.

The early check returns zero when the global start or end condition fails.

**Define exact-prefix states**

`f[i][j]` is the number of ways to partition the first `i` characters into exactly `j` beautiful parts, with a valid boundary at `i`.

`f[0][0]=1` represents the empty prefix with zero parts. It is a construction seed, not a real substring.

The table `g` stores prefix sums:

$$
g[i][j]=\sum_{p=0}^{i}f[p][j]\pmod M.
$$

This lets one transition combine all eligible prior cut positions in constant time.

Both tables include row zero so the first real part can begin at the start of the string. They include columns zero through `k` so transitions from zero completed parts into the first part use the same indexing as every later transition.

**Recognize a valid ending boundary**

The loop enumerates characters with one-based prefix length `i` and current character `c=s[i-1]`. Prefix `i` may end a part when:

- `i>=minLength`;
- `c` is non-prime, so the part ends correctly;
- either `i==n` or `s[i]` is prime, so the next part would start correctly.

Only at such a boundary can `f[i][j]` be nonzero.

**Enforce minimum length with a prefix sum**

If the current part ends at prefix `i` and has length at least `minLength`, its previous boundary `p` must satisfy

$$
p\le i-\texttt{minLength}.
$$

Every valid `f[p][j-1]` in that range can precede the current part. Their sum is exactly

`g[i-minLength][j-1]`.

Thus the assignment

`f[i][j]=g[i-minLength][j-1]`

replaces a loop over all previous boundaries with one lookup.

Invalid prior boundary positions contribute zero to `f`, so including them in `g` causes no false partitions.

**Update the prefix-sum table**

After calculating any `f[i][j]` values, the code sets

`g[i][j]=(g[i-1][j]+f[i][j])%mod`.

This preserves the prefix-sum definition for use by later endpoints.

The final answer `f[n][k]` counts partitions that consume the whole string into exactly `k` parts. The global end check ensures `n` is an eligible terminal boundary.

Applying the modulus while updating `g` is sufficient because every later `f` value is copied from a modular prefix sum. Addition modulo $M$ is compatible with counting, so reducing intermediate totals never changes the final remainder.

**Trace the recurrence conceptually**

For a possible third part ending at `i`, `g[i-minLength][2]` contains every way to finish two valid parts early enough that at least `minLength` characters remain for the third. Boundary validity also guarantees the character after the previous cut begins prime, because `f` exists only at recognized cuts.

Each sequence of $k-1$ internal cut positions maps to one partition, and the recurrence adds it exactly when processing its final endpoint.


Every beautiful partition has valid boundaries and minimum gaps. Removing its last part leaves a beautiful partition counted by some eligible `f[p][j-1]` with `p<=i-minLength`, so the transition includes it.

Conversely, every counted prior prefix plus the current valid boundary creates a part of sufficient length that begins prime and ends non-prime. Repeating the argument reconstructs a valid complete partition. No cut sequence is counted twice because its final prior boundary and part count are unique.

**Exact space differs from the manifest**

The manifest claims $O(n)$ space, suggesting rolling arrays across part counts. The protected source allocates both `f` and `g` as $(n+1)\times(k+1)$ tables, so its actual auxiliary space is $O(nk)$.

## Complexity detail

The outer position loop runs $n$ times. At every position, updating `g` loops through $k+1$ counts; valid endpoints also fill up to $k$ `f` states. Total time is $O(nk)$.

Two full tables of $O(nk)$ integers dominate memory, so exact space is $O(nk)$, not the manifest's $O(n)$.

All additions are reduced modulo $10^9+7$. State values remain bounded, though Python integer and nested-list overhead can still be substantial at $n=k=1000$.

## Alternatives and edge cases

- **Roll by part count:** Compute one-dimensional endpoint and prefix arrays for each number of parts, reducing storage toward the manifest's $O(n)$.
- **Enumerate previous cuts:** A direct DP transition scans $O(n)$ prior boundaries per state and costs $O(kn^2)$ time.
- **Invalid first digit:** No partition can repair the first part's start, so zero is immediate.
- **Invalid last digit:** No final part can end correctly, so zero is immediate.
- **Insufficient total length:** When `k*minLength>n`, no transition reaches `f[n][k]` and the result is zero.
- **Internal cut:** It must lie between a non-prime digit and a prime digit.
- **`minLength=1`:** Boundary character rules remain the only spacing restriction.
- **Exactly one part:** The whole string qualifies when its endpoints satisfy the rules and length is sufficient.
- **Modulo arithmetic:** Prefix sums and final counts remain equivalent after reduction.
- **Metadata mismatch:** The exact code uses two $O(nk)$ tables rather than rolled $O(n)$ storage.
