## General

**Why the answer is the first missing power of two.** Consider a power $2^k$. A bitwise OR can equal this value only if every selected number contains bit $k$ and contains no other bit. Because OR can add bits but never remove them, every selected positive number would therefore have to equal $2^k$ itself. Consequently, $2^k$ is expressible exactly when that value occurs in `nums`.

Now let $2^k$ be the first absent power of two. Every smaller positive integer uses only bit positions below $k$. Since each smaller single-bit value $1, 2, 4, \ldots, 2^{k-1}$ occurs in the array, selecting the values corresponding to the set bits of any such integer forms it by OR. Hence every positive integer below $2^k$ is expressible, while $2^k$ is not, proving it is the minimum impossible value.

**Record powers without a set.** A positive integer is a power of two exactly when `value & (value - 1) == 0`. OR every such input value into one integer `present_powers`; each set bit then records that the corresponding single-bit value appeared. Starting at `answer = 1`, shift left while that bit is present. The first clear bit represents the first missing power of two.

## Complexity detail

Let $n$ be the length of `nums`. The array scan takes $O(n)$ time. At most 30 input bit positions can be marked because each value is at most $10^9$, so the final bit scan is bounded by a constant and the total time is $O(n)$. The bit mask and counters use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Hash set membership:** Storing all values in a set and probing successive powers of two also takes $O(n)$ time, but uses $O(n)$ auxiliary space instead of one bit mask.
- **Sort then search:** Sorting before checking powers is correct but raises the time to $O(n \log n)$ and orders values that do not affect the answer.
- **Non-power values:** A value with several set bits cannot help form an isolated missing bit because OR cannot clear its extra bits.
- **Missing one:** If the array does not contain the exact value `1`, the answer is immediately $1$, even when odd non-power values are present.
- **Duplicates:** Repeated powers set the same mask bit and do not change which values are expressible.
- **Answer above the input bound:** If every legal power through $2^{29}$ appears, the answer is $2^{30}$; the returned value need not itself satisfy the input-element bound.
