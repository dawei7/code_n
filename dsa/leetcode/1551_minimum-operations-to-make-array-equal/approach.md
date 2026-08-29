## General

**Determine the only possible final value**

The array contains the first $n$ positive odd numbers:

$$
1,3,5,\ldots,2n-1.
$$

Every operation transfers one unit from one element to another, so the total sum never changes. The sum of the first $n$ odd numbers is $n^2$, making the average and only possible common final value equal to $n$.

The goal is therefore to move surplus units from values above $n$ into deficits below $n$.

**Count deficit rather than simulate transfers**

One operation increases one deficient element by one and decreases one surplus element by one. It repairs exactly one unit of total deficit.

Because total surplus equals total deficit, the minimum number of operations is the sum of deficits among all original elements below $n$. No operation can repair more than one deficit unit, and pairing each deficit unit with any surplus unit achieves that lower bound.

The values below $n$ occur at the first $\lfloor n/2\rfloor$ indices. For index `i`, the original value is `2*i + 1`, so its deficit is:

$$
n-(2i+1).
$$

The source sums exactly these terms.

**Decode the bit operations**

`n >> 1` is integer division by two for positive `n`, so `range(n >> 1)` visits indices zero through $\lfloor n/2\rfloor-1$.

Inside the generator, `i << 1` equals `2*i`. Bitwise OR with one makes the low bit one:

`(i << 1) | 1`.

Since `2*i` is even, this value is exactly `2*i + 1`, the array element at index `i`.

The generated term `n - (i << 1 | 1)` is therefore the deficit of that below-average element. Python precedence evaluates the shift before the bitwise OR, and the source's parentheses contain the complete odd-number expression.

**Even-length derivation**

Let $n=2q$. There are $q$ below-average values. Their deficits are:

$$
2q-1,\ 2q-3,\ldots,1.
$$

These are the first $q$ odd numbers in reverse order, whose sum is $q^2$. Therefore the answer is:

$$
\frac{n^2}{4}.
$$

For `n = 6`, the deficits from values one, three, and five to target six are five, three, and one. Their sum is nine, matching the example.

**Odd-length derivation**

Let $n=2q+1$. The middle array value is already $n$ and needs no change. The $q$ values below it have deficits:

$$
2q,\ 2q-2,\ldots,2.
$$

Their sum is $2(1+2+\cdots+q)=q(q+1)$, equivalent to:

$$
\frac{n^2-1}{4}.
$$

For `n = 3`, only original value one lies below target three, with deficit two. Two transfers from value five make all values three.

**Why summing only the lower half is sufficient**

The upper half contains precisely the same total amount above $n$ by symmetry. Pair the smallest value with the largest: their distances below and above $n$ are equal. Continue inward.

The generator need not inspect or construct the surplus side because conservation of the fixed total guarantees enough units to fill every computed deficit.

**Why the operation count is minimum**

Let $D$ be the summed deficit. Every legal operation can increase at most one below-target position by one, so at least $D$ operations are necessary.

The array has exactly $D$ surplus units above target. Transfer one such unit to a deficient position in each operation. After $D$ operations all deficits and surpluses are zero, so every value equals $n$.

This constructive upper bound equals the lower bound, proving the sum returned by the source is minimum.

**Exact source versus the closed form**

Although the mathematical answer has a constant-time formula, the stored solution evaluates a generator with $\lfloor n/2\rfloor$ terms and passes it to `sum`.

It computes the same formula correctly, but it does not execute in $O(1)$ time. This distinction matters when explaining the exact implementation rather than only the mathematical approach.

## Complexity detail

The generator visits $\lfloor N/2\rfloor$ indices and performs constant work for each. The exact stored source therefore runs in $O(N)$ time, not the manifest's stated $O(1)$.

The manifest bound corresponds to directly returning `n*n // 4`, which covers both parity cases through integer floor division.

The generator is lazy and `sum` consumes one term at a time. It does not materialize a list, so auxiliary space is $O(1)$, matching the manifest's space bound.

## Alternatives and edge cases

- **Closed-form floor:** Return $\lfloor n^2/4\rfloor$ to realize true $O(1)$ time and $O(1)$ space.
- **Explicit array simulation:** Building values and transferring units is unnecessary and can use extra time and space.
- **Sum upper-half surplus:** It equals lower-half deficit and gives the same answer.
- **Pair symmetric elements:** Each pair reveals how many unit transfers it needs; this is equivalent to the deficit sum.
- **n equals one:** The generator is empty, `sum` returns zero, and the sole value is already equal.
- **Even n:** No element initially equals the average, but symmetric deficits and surpluses balance.
- **Odd n:** The central value equals `n` and contributes no operation.
- **Generator laziness:** It preserves constant auxiliary space despite linear iteration.
- **Bitwise odd construction:** `(i << 1) | 1` is exactly `2*i + 1` for nonnegative `i`.
- **Conservation of sum:** It forces the final value to be `n` and guarantees total deficit equals total surplus.
- **Operation endpoints:** The two selected indices may be chosen to transfer any needed surplus unit directly to any deficit.
- **Manifest mismatch:** The declared constant-time bound describes the closed-form alternative, not this exact summation loop.
- **Integer arithmetic:** All formulas are integral for both parity cases, and Python avoids overflow.
