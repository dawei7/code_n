## General

**Use XOR to undo the encoding one position at a time**

The encoding rule gives

$$
\texttt{encoded}[i]
=
\texttt{arr}[i]\mathbin{\mathrm{XOR}}\texttt{arr}[i+1].
$$

At first this appears to combine two unknown values. However, when `arr[i]` is known, XOR can isolate the next value because applying the same operand twice cancels it.

For any integers $a$ and $b$,

$$
(a\mathbin{\mathrm{XOR}}b)\mathbin{\mathrm{XOR}}a
=
b.
$$

This follows from associativity and commutativity together with $a\mathbin{\mathrm{XOR}}a=0$ and $0\mathbin{\mathrm{XOR}}b=b$.

Therefore,

$$
\texttt{arr}[i+1]
=
\texttt{arr}[i]\mathbin{\mathrm{XOR}}\texttt{encoded}[i].
$$

That recurrence is the entire decoding mechanism.

**Seed the reconstruction with the supplied first value**

The source initializes `ans = [first]`. This is not a guess: the contract explicitly gives `first = arr[0]`.

Once the first element is present, the first encoded value determines the second original value. That reconstructed value and the next encoded value determine the third, and so on. The dependency is a chain, so no search or branching is required.

**Read the most recently reconstructed value**

For each `x` in `encoded`, the source appends

`ans[-1] ^ x`.

`ans[-1]` is the latest decoded original value. If the loop is currently handling `encoded[i]`, then `ans[-1]` is `arr[i]` and `x` is `arr[i] XOR arr[i+1]`. Their XOR is exactly `arr[i+1]`.

Appending rather than overwriting preserves every previously reconstructed value and makes the new one available to the next iteration.

**Trace the first example**

Start with `first = 1`, so `ans = [1]`.

- The first encoded value is one. `1 XOR 1 = 0`, so append zero.
- The next encoded value is two. `0 XOR 2 = 2`, so append two.
- The last encoded value is three. `2 XOR 3 = 1`, so append one.

The result is `[1,0,2,1]`. Re-encoding adjacent pairs gives one, two, and three, confirming the reconstruction.

For `encoded = [6,2,7,3]` and `first = 4`, the successive values are `4 XOR 6 = 2`, `2 XOR 2 = 0`, `0 XOR 7 = 7`, and `7 XOR 3 = 4`.

**Why XOR works bit by bit**

XOR compares each binary bit independently. A result bit is one exactly when the two input bits differ. If one original bit and the corresponding encoded-difference bit are known, the next original bit is uniquely determined.

The integer recurrence simply performs this recovery across every bit position at once. There are no carries between bits, unlike addition, so decoding one pair cannot depend on any neighboring bit.

**Why the answer is unique**

The first value is fixed. The first encoding equation then has exactly one possible second value because XOR with a fixed integer is a one-to-one operation. Repeating that argument fixes every later value.

Formally, assume `ans` correctly contains `arr[0]` through `arr[i]` before an iteration. The appended value is

$$
\texttt{arr}[i]\mathbin{\mathrm{XOR}}
(\texttt{arr}[i]\mathbin{\mathrm{XOR}}\texttt{arr}[i+1])
=\texttt{arr}[i+1].
$$

Thus the invariant extends by one. It holds initially for `arr[0]`, so induction proves the complete returned list equals the hidden array.

No other array can share both the supplied first value and all encoded adjacent XORs, because its first differing reconstructed position would be forced by the same preceding value and encoding.

**Why output length is correct**

If `encoded` has length $n-1$, `ans` begins with one element and appends one for each encoded entry. Its final length is

$$
1+(n-1)=n,
$$

exactly the hidden array length.

The method also preserves nonnegative integer values naturally. XOR may produce values with any bit pattern implied by the valid input, and the promise guarantees they form the intended array.

## Complexity detail

Let $n$ be the length of the decoded array, so `encoded` has $n-1$ elements. The loop performs one XOR and one append per encoded value, taking $O(n)$ time.

The returned list contains $n$ integers and therefore uses $O(n)$ space, matching the manifest. Excluding required output storage, the algorithm uses only the loop variable and access to the list's last element, so additional working state is $O(1)$.

Python list append is amortized constant time. XOR cost is treated as constant for values within the stated bounded integer range.

## Alternatives and edge cases

- **Preallocate the result:** Allocate `len(encoded)+1` entries, set the first, and fill by index. It has the same complexity and avoids amortized list growth.
- **Recursive decoding:** Apply the same recurrence recursively, but it adds $O(n)$ call-stack space and risks recursion depth for long input.
- **Brute-force candidates:** Trying possible next values is unnecessary because XOR inversion gives one unique result directly.
- **First value zero:** The next value is simply `encoded[0]` because zero XOR changes nothing.
- **Encoded value zero:** Adjacent original values are equal, since `a XOR a = 0`.
- **Repeated original values:** They are reconstructed normally; uniqueness concerns the whole array, not distinct elements.
- **Minimum encoded length:** With hidden length two, one iteration appends the second value.
- **Large bit patterns:** XOR operates independently on all bits without carries.
- **Input preservation:** `encoded` and `first` are read but never modified.
- **Result verification:** XORing each adjacent returned pair reproduces the corresponding encoded entry by construction.
- **Order dependence:** Each step needs the immediately previous decoded value, so encoded entries must be processed left to right.
