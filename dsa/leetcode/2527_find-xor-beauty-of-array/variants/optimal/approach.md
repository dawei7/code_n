## General

**The enormous triplet XOR collapses bit by bit**

There are $n^3$ ordered triplets, so direct enumeration is impossible for $n=10^5$.

Bitwise OR, AND, and XOR act independently at every bit position. Analyze one bit and determine whether it appears an odd number of times among all effective values. XOR sets that result bit exactly when the count is odd.

The analysis will show that this parity is the same as the parity of that bit among the input numbers. That means the complete answer is simply the XOR of all elements.

**Count input ones at one bit**

Fix a bit position. Let:

- $c$ be the number of array elements whose bit is one;
- $z=n-c$ be the number whose bit is zero.

For effective value

$$
(\texttt{nums}[i]\mathbin{|}\texttt{nums}[j])
\mathbin{\&}\texttt{nums}[k],
$$

the chosen bit is one under two requirements:

1. `nums[k]` has the bit, giving $c$ choices for `k`;
2. at least one of `nums[i]` or `nums[j]` has the bit.

**Count ordered `(i,j)` pairs whose OR bit is one**

There are $n^2$ ordered pairs in total. Their OR bit is zero only when both selected elements have zero at that bit, giving $z^2$ pairs.

Thus the number whose OR bit is one is

$$
n^2-z^2
=(n-z)(n+z)
=c(2n-c).
$$

Multiplying by the $c$ valid choices of `k`, the result bit appears in

$$
c^2(2n-c)
$$

effective values.

**Reduce that count modulo two**

Only parity matters to XOR. Since $2n$ is even,

$$
(2n-c)\bmod2=c\bmod2.
$$

Also $c^2$ has the same parity as $c$. Therefore,

$$
c^2(2n-c)\bmod2
=
c\bmod2.
$$

The effective-values XOR sets this bit exactly when $c$ is odd.

But the XOR of the original input values also sets a bit exactly when an odd number of elements have that bit. The two results agree at every bit position.

**Conclude the identity**

Because all bits agree independently,

$$
\bigoplus_{0\le i,j,k<n}
\left((\texttt{nums}[i]\mathbin{|}\texttt{nums}[j])
\mathbin{\&}\texttt{nums}[k]\right)
=
\bigoplus_{x\in\texttt{nums}}x.
$$

The source implements the right side with:

`reduce(xor,nums)`.

**Trace `[1,4]`**

Binary 1 has bit zero, and binary 4 has bit two. Each of those bits appears in exactly one input value, an odd count, so both survive the input XOR:

$$
1\mathbin{\mathtt{\char94}}4=5.
$$

Every other bit appears zero times and remains unset. The $2^3=8$ triplet effective values listed in the example XOR to the same result five.

**Why ordered and repeated indices are covered**

The counting used $n^2$ ordered choices for `(i,j)` and $n$ independent choices for `k`. It allows `i=j`, `j=k`, or all three indices equal, exactly as the range definition permits.

Changing the problem to distinct or unordered indices would change the count and invalidate the reduction. The proof matches the exact triplet domain.

**Why `reduce` is safe**

`reduce(xor,nums)` XORs elements from left to right. XOR is associative, so grouping does not affect the result.

The array is guaranteed non-empty, so `reduce` has an initial element and does not need an explicit initializer.

**No numeric sign complication**

All inputs are positive and at most $10^9$. Their ordinary nonnegative binary representations make the per-bit count direct. The result fits within the union of their set bits.


For every bit, combinatorial parity proves that the triplet XOR sets it if and only if the input contains an odd number of that bit. The linear XOR reduction has exactly the same criterion. Equality at all bit positions proves the returned integer is the xor-beauty.

This is an equality of complete integers, not merely an equality of one statistic: every nonnegative integer is uniquely determined by which binary positions are set.

## Complexity detail

`reduce` visits all $n$ values once and performs one constant-time XOR per additional element. Time is $O(n)$.

Only the running reduction value is needed, so auxiliary space is $O(1)$.

The mathematical proof avoids constructing any of the $n^3$ triplets or storing per-bit counts.

## Alternatives and edge cases

- **Enumerate triplets:** It costs $O(n^3)$ and is infeasible.
- **Explicit per-bit counting:** Count ones at each bit and apply the parity proof; it costs $O(nB)$ for bit width $B$ but is unnecessary once the identity is known.
- **Single element:** The sole effective triplet reduces to that element, matching its XOR.
- **Duplicate values:** XOR parity naturally cancels even multiplicities.
- **Repeated triplet indices:** They are included in the $n^3$ ordered domain.
- **All values equal with even `n`:** Their input XOR is zero, so xor-beauty is zero.
- **All values equal with odd `n`:** One copy remains under XOR.
- **Non-empty guarantee:** It makes `reduce` valid without an initializer.
- **Bit independence:** OR, AND, and XOR can be analyzed separately at every position.
- **Positive inputs:** No sign-extension behavior needs consideration.
