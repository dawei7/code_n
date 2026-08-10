## General

**Write all circular XOR equations together**

For a candidate binary array `original`, the derived values are:

$$
\begin{aligned}
d_0 &= o_0\oplus o_1,\\
d_1 &= o_1\oplus o_2,\\
&\ \vdots\\
d_{n-1} &= o_{n-1}\oplus o_0.
\end{aligned}
$$

The last equation closes the circle. That closure creates one global consistency condition that is enough to answer whether a solution exists.

**XOR every equation**

XOR is associative and commutative, so all right-hand sides can be rearranged.

Every original bit appears exactly twice:

- once paired with its next neighbor;
- once paired with its previous neighbor.

Because `a ^ a = 0`, each pair cancels. Therefore any valid derived array must satisfy:

$$
d_0\oplus d_1\oplus\cdots\oplus d_{n-1}=0.
$$

This proves that total XOR zero is necessary.

**Why the condition is also sufficient**

A necessary condition alone would not justify returning true. We must show that total XOR zero lets us construct an original array.

Choose `o_0 = 0`. For each non-final relation, define the next bit by:

$$
o_{i+1}=o_i\oplus d_i.
$$

Because both inputs are binary, every constructed value remains either zero or one. These definitions automatically satisfy the first $n-1$ adjacent equations.

After applying all $n$ derived values around the cycle, the value that should return to the starting position is:

$$
o_0\oplus d_0\oplus d_1\oplus\cdots\oplus d_{n-1}.
$$

When total derived XOR is zero, this equals `o_0`. The circular endpoint is consistent, so all equations, including the last one, are satisfied.

Thus total XOR zero is sufficient as well as necessary.

**What `reduce(xor, derived)` computes**

`reduce` combines the array from left to right using the imported XOR operator:

`(((derived[0] ^ derived[1]) ^ derived[2]) ...)`.

Associativity means the parenthesization does not affect the result. The final value is exactly the cumulative XOR used in the proof.

The constraint guarantees at least one element, so calling `reduce` without an explicit initializer is safe.

**Trace a valid example**

For `derived = [1, 1, 0]`:

$$
1\oplus1\oplus0=0.
$$

The code returns true.

To witness sufficiency, begin with `original[0] = 0`:

- the first derived bit gives `original[1] = 0 ^ 1 = 1`;
- the second gives `original[2] = 1 ^ 1 = 0`;
- the last requires `original[2] ^ original[0] = 0 ^ 0 = 0`, matching the last derived bit.

The constructed array is `[0, 1, 0]`.

**Trace an invalid example**

For `derived = [1, 0]`, cumulative XOR is one, so the code returns false.

Assume the first original bit is zero. The first equation forces the second bit to one, but the circular equation would then produce `1 ^ 0 = 1` rather than the required zero.

Starting with one merely flips both reconstructed bits and leaves the same inconsistency. The global XOR condition captures this unavoidable contradiction.

**Both starting choices behave consistently**

Choosing `original[0] = 1` instead of zero flips every reconstructed bit.

XOR of two flipped adjacent bits is unchanged:

$$
(a\oplus1)\oplus(b\oplus1)=a\oplus b.
$$

Therefore a zero total XOR actually permits both complementary original arrays, while a nonzero total permits neither. The algorithm only needs to decide existence, so it never has to build either one.

**Single-element behavior**

For $n=1$, the only derived equation is:

$$
d_0=o_0\oplus o_0=0.
$$

The reduction returns the sole value. It accepts `[0]` and rejects `[1]`, exactly matching the circular definition.

**Why counting ones is equivalent**

For binary values, cumulative XOR is zero precisely when the number of ones is even.

The exact solution uses XOR because it follows directly from the equations and would generalize to wider integer XOR values. A parity-of-sum check is another way to express the same condition for binary input.


If an original array exists, XORing all defining equations cancels every original bit twice, so the solution's reduction must equal zero and the algorithm returns true.

Conversely, if the reduction equals zero, choosing an initial binary bit and successively applying the derived relations reconstructs binary neighbors and returns consistently to the chosen start. This constructs a valid original array.

The returned Boolean is therefore true exactly when the requested array exists.

**Why this is optimal**

Every derived bit can affect the cumulative parity. An algorithm cannot generally skip an unread position because changing only that bit can switch a valid input to invalid.

One pass with one accumulator matches the $\Omega(n)$ information-reading requirement.

## Complexity detail

`reduce` processes all $n$ elements once and performs one constant-time XOR per combination. Total time is $O(n)$.

Reduction keeps only its accumulator and current element, so auxiliary space is $O(1)$. No original array is constructed, and `derived` is not modified.

## Alternatives and edge cases

- **Reconstruct from initial zero:** Correct in $O(n)$ time but stores an array unnecessarily unless only the current bit is retained.
- **Try both initial bits:** Redundant because the two reconstructions are complements and pass or fail together.
- **Count ones and test even parity:** Equivalent for binary input, using `sum(derived) % 2 == 0`.
- **Nested equation solving:** Adds complexity without improving the one global consistency check.
- **Single zero:** Valid because a bit XOR itself is zero.
- **Single one:** Invalid because no bit XOR itself can be one.
- **All zeros:** Valid; a constant all-zero or all-one original works.
- **Odd number of ones:** Total XOR is one, so no original exists.
- **Even number of ones:** Total XOR is zero, so a construction exists.
- **Nonempty constraint:** Makes `reduce` without an initializer safe.
- **Binary constraint:** Ensures the constructive recurrence always produces binary values.
- **Input preservation:** Reduction only reads the array.
