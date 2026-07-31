## General

**Reduce each index to the factors relevant to `k`**

For an index $i$, only $\gcd(i,k)$ matters to whether $ij$ is divisible by
$k$. Write $g_i=\gcd(i,k)$. Every prime-power factor of $k$ contributed by
$i$ is present in $g_i$, so

$$
k\mid ij \quad\Longleftrightarrow\quad k\mid g_i g_j.
$$

This also handles index zero: $\gcd(0,k)=k$, making it compatible with every
other index.

**Keep counts separate by value**

Process indices from left to right. For each array value, store how many
earlier indices produced each gcd class. At index $j$, inspect only the classes
belonging to `nums[j]`; add a class count when its gcd multiplied by
$\gcd(j,k)$ is divisible by `k`. Then record the current index for later
pairs.

Every counted entry is earlier and has the same value. The gcd compatibility
test is equivalent to the original product condition, so all and only valid
pairs ending at $j$ are added exactly once.

## Complexity detail

The possible gcd classes are divisors of $k$, and $k$ has at most
$O(\sqrt{k})$ divisors. For $n$ elements, scanning the stored classes therefore
takes $O(n\sqrt{k})$ time. At most one count entry is created per processed
index before classes merge, so the storage bound is $O(n)$.

## Alternatives and edge cases

- **Enumerate every pair:** Test equality and `(i * j) % k == 0` directly. It
  is simple and correct but takes $O(n^2)$ time.
- **Store raw earlier indices:** Grouping by value avoids unrelated pairs, but
  rescanning every prior index in a frequent-value group remains quadratic.
- Index `0` has a product of zero with every later index, and zero is divisible
  by every positive `k`.
- When `k = 1`, divisibility is automatic and only value equality matters.
- Equal values do not qualify unless the index-product condition also holds.
- Factors may be split between the two indices; neither index must itself be
  divisible by `k`.
