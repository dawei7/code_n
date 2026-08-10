## General

XOR is useful whenever equal values occur in pairs because it has three key properties:

$$
x\oplus x=0,
$$

$$
x\oplus0=x,
$$

and XOR is associative and commutative. Therefore, values may be conceptually rearranged without changing the result, and every duplicated number cancels with its identical copy.

If the two singleton values are called $p$ and $q$, XORing the complete array leaves

$$
\text{xs}=p\oplus q.
$$

The exact source computes this with `reduce(xor, nums)`. This is not yet enough to recover either number directly, but it identifies every bit position where $p$ and $q$ differ.

**Why `xs` must contain a set bit**

The two singletons are distinct; otherwise one value would occur twice rather than two values occurring once. XOR is zero only when its operands are equal, so $p\oplus q\ne0$. At least one bit of `xs` is therefore `1`.

At any such bit, exactly one singleton has a `1` and the other has a `0`. That bit can partition the array so the singletons enter different groups.

**Isolate one differing bit**

The expression

```text
lb = xs & -xs
```

isolates the least significant set bit of `xs`. In two's-complement arithmetic, negation flips bits above and including the rightmost `1` in a way that leaves only that position common under bitwise AND. The result `lb` is a power of two: it has exactly one set bit.

The algorithm does not depend on choosing the least significant differing bit specifically. Any set bit of `xs` would separate the singletons. The low-bit formula is simply a constant-time way to select one.

**XOR only one partition**

The second pass considers values satisfying `x & lb`, meaning their bit at the selected position is `1`. It XORs those values into `a`.

Every ordinary duplicated value sends both copies to the same partition because identical bit patterns make the same test result. If its selected bit is `1`, both copies enter `a` and cancel; if the bit is `0`, neither enters. The duplicate pairs cannot contaminate the result.

Exactly one of $p$ and $q$ has the selected bit set, so exactly one enters this partition. After all paired values cancel, `a` equals that singleton.

The other singleton is recovered from the total singleton XOR:

$$
b=\text{xs}\oplus a.
$$

If `a = p`, then `(p ^ q) ^ p = q` because the two copies of `p` cancel. The source returns `[a, b]`. Which singleton appears first depends on the selected bit, and the contract permits either order.

**Trace through the first example**

For `nums = [1, 2, 1, 3, 2, 5]`, the paired `1` values cancel and the paired `2` values cancel. Thus

$$
\text{xs}=3\oplus5=6.
$$

In binary, `6` is `110`, so `lb = 010`, the value `2`. Values having that bit set are `2`, `3`, and the second `2`. Their XOR is

$$
2\oplus3\oplus2=3,
$$

so `a = 3`. Finally, `b = 6 ^ 3 = 5`, and the function returns `[3, 5]`.

Notice that it was unnecessary to form the zero-bit partition explicitly. Once one singleton is known, the combined XOR reveals the other.

**Why negative values still work in Python**

Python models bitwise operations on negative integers as though they had an unbounded two's-complement representation. The identity `x & -x` still isolates the least significant set bit for nonzero `x`, and XOR cancellation remains valid.

For `[-1, 0]`, the combined XOR is `-1`. Its isolated low bit is `1`, so `-1` enters the selected partition and becomes `a`; `0` does not. Then `b = -1 ^ -1 = 0`. No conversion to a fixed-width unsigned representation is required by this implementation.

**Why the result is exact**

The first pass proves that `xs` contains only the XOR of the two singletons. The isolated bit is set in exactly one of them. The second pass groups identical copies together, so all duplicate values cancel within whichever side they occupy, while exactly one singleton remains as `a`. XORing `a` out of `xs` leaves the other singleton as `b`. Thus both and only the required values are returned.

## Complexity detail

Let $n$ be the number of array elements. `reduce(xor, nums)` reads all $n$ values once. The partition loop reads all $n$ values again. Every visit performs a constant number of fixed-width bit operations under the problem's 32-bit integer model, so total time is $O(n)$.

The algorithm stores only `xs`, `lb`, `a`, `b`, and the current loop value. Their number is independent of $n$, so auxiliary space is $O(1)$. The input is not modified, and no frequency table or partition arrays are created.

## Alternatives and edge cases

- **Frequency hash map:** Count every value and return the two with count one. It is straightforward and $O(n)$ expected time, but requires $O(n)$ extra space in the worst case.
- **Sort the array:** Paired values become adjacent and singletons can be found by scanning. Sorting takes $O(n\log n)$ time and may mutate the input or require a copy.
- **Build both XOR partitions:** Maintain one accumulator for the selected-bit group and another for the zero-bit group. It directly yields both singletons but is unnecessary because `xs ^ a` recovers the second.
- **Singleton value zero:** Zero participates normally: it changes no XOR accumulator, but after the other singleton is recovered, `xs ^ other` correctly yields zero.
- **Negative values:** Python's bitwise semantics preserve the low-bit and cancellation identities, including the minimum 32-bit value.
- **The two singletons differ only in a high bit:** `xs & -xs` finds their lowest differing bit, whether low or high; at least one difference always exists.
- **Duplicate values with the selected bit set:** Both copies enter `a` and cancel. Copies with the bit clear both stay out, so either case is harmless.
- **Input length two:** There are no duplicate pairs. The differing bit separates the two values immediately.
- **Nonempty-input assumption:** `reduce` is called without an initializer, but the constraints guarantee at least two elements. An empty list outside the contract would raise an error.
- **More or fewer singleton values:** The proof relies on exactly two. With a different occurrence pattern, `xs` would not necessarily encode a separable pair and this method would need redesign.
- **Return order:** The selected bit determines which singleton becomes `a`; the problem explicitly accepts either ordering.
