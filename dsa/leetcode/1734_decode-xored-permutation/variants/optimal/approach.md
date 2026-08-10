## General

**The adjacent XOR rule can decode once one endpoint is known**

The encoding gives

$$
\texttt{encoded}[i]
=
\texttt{perm}[i]\mathbin{\mathrm{XOR}}\texttt{perm}[i+1].
$$

If either adjacent permutation value is known, the other is recovered by XORing the encoding again, because $x\mathbin{\mathrm{XOR}}x=0$.

Unlike the simpler decode problem, this method is not given the first value. It derives the last value from the facts that `perm` contains every integer from one through odd $n$ exactly once.

The hidden length itself is not separately supplied. Because adjacent encoding produces one fewer entry than the original sequence, `n = len(encoded) + 1` recovers it exactly and determines both the numeric permutation range and the output allocation size.

**XOR all values in the hidden permutation**

`b` begins at zero. The loop from one through `n` computes

$$
b=1\mathbin{\mathrm{XOR}}2\mathbin{\mathrm{XOR}}\cdots
\mathbin{\mathrm{XOR}}n.
$$

Since `perm` is a permutation of those integers, $b$ is also the XOR of every hidden permutation element, regardless of order.

**Use even encoded positions to cover every element except the last**

Because $n$ is odd, `encoded` has even length $n-1$. The source XORs encoded indices zero, two, four, and so on:

`for i in range(0, n - 1, 2): a ^= encoded[i]`.

These entries expand to

$$
(\texttt{perm}[0]\mathbin{\mathrm{XOR}}\texttt{perm}[1])
\mathbin{\mathrm{XOR}}
(\texttt{perm}[2]\mathbin{\mathrm{XOR}}\texttt{perm}[3])
\mathbin{\mathrm{XOR}}\cdots.
$$

The pairs are disjoint and cover indices zero through `n-2`. The only hidden value not included is `perm[n-1]`.

Thus `a` is the XOR of every permutation element except the last.

**Cancel the shared values to isolate the last**

`b` contains all values, while `a` contains all but the last. XORing them cancels each shared value in pairs:

$$
a\mathbin{\mathrm{XOR}}b=\texttt{perm}[n-1].
$$

The source stores this as `perm[-1] = a ^ b`.

This is where the odd-length guarantee matters. With even $n$, taking alternating encoded entries would not partition the first $n-1$ permutation positions into complete adjacent pairs in the same way.

**Reconstruct backward**

After allocating `perm = [0] * n` and setting its last value, the source visits encoded indices from `n-2` down to zero:

`perm[i] = encoded[i] ^ perm[i + 1]`.

If `perm[i+1]` is known, then

$$
\texttt{encoded}[i]\mathbin{\mathrm{XOR}}\texttt{perm}[i+1]
=
\texttt{perm}[i].
$$

Each iteration establishes the preceding value, so the known suffix grows leftward until the entire permutation is filled.

**Trace the length-three example**

For `encoded=[3,1]`, $n=3$.

Even encoded positions contribute only index zero, so `a=3`. The XOR of one, two, and three is zero, so `b=0`. The last permutation value is `3 XOR 0 = 3`.

Moving backward, `perm[1] = 1 XOR 3 = 2` and `perm[0] = 3 XOR 2 = 1`. The result is `[1,2,3]`.

**Why the result is guaranteed to be the permutation**

The derivation proves the last value equals the hidden last value using only properties guaranteed by the input. Backward recurrence then uniquely recovers every earlier hidden value.

At each step, the recovered pair re-encodes to the supplied entry. Since the problem promises a valid unique answer, no additional range or duplicate validation is needed.

**Why XOR order does not matter**

XOR is associative and commutative. The loop over one through $n$ need not know the hidden permutation order, and cancellation between `a` and `b` works even though one XOR was assembled from numeric order and the other from adjacent permutation order.

## Complexity detail

Let $n$ be the permutation length. XORing alternating encoded entries takes $O(n)$ time, XORing one through $n$ takes $O(n)$, and backward reconstruction takes $O(n)$. Their sum is $O(n)$.

The returned `perm` list uses $O(n)$ space, matching the manifest. Excluding required output, only `a`, `b`, `n`, and loop indices are stored, so extra working state is $O(1)$.

The input `encoded` is not modified.

## Alternatives and edge cases

- **Derive the first value instead:** XOR all permutation values with encoded entries at odd indices, then reconstruct forward. It is the symmetric common formulation.
- **Try every possible first value:** Validate each reconstruction as a permutation, but this adds unnecessary quadratic work.
- **Odd length:** It is essential for alternating encoded pairs to cover all but one permutation element.
- **Minimum `n=3`:** One even-indexed encoding pair covers the first two hidden values.
- **Last value equals an earlier numeric XOR result:** Cancellation still works bitwise; values themselves remain distinct by the permutation promise.
- **Encoded zero:** Adjacent permutation values would be equal, which cannot occur in a valid permutation, so valid inputs will not create that contradiction.
- **Backward direction:** The source derives the last value, so it must reconstruct from right to left.
- **Zero initialization:** Placeholder zeros are overwritten before return and are not permutation candidates.
- **Order independence:** XORing one through $n$ equals XORing the permuted sequence.
- **Input validity promise:** No explicit duplicate or range check is performed.
- **Output length:** It is exactly `len(encoded)+1`.
