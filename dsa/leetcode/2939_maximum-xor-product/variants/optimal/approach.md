## General

**Separate fixed and controllable bits.** Let
`first = a XOR x` and `second = b XOR x`. Because $x<2^n$, all bits at
positions $n$ and above are fixed in both results. Initialize each partial
factor with those fixed high bits, then decide the lower positions from most
significant to least significant.

**Equal input bits should become one in both factors.** At a controllable
position where `a` and `b` have the same bit, XOR makes the corresponding
result bits equal as well. Choosing `x` so that both result bits are `1`
adds the current power of two to both factors. This strictly increases their
product unless no increase is possible, so omitting that shared bit cannot be
optimal.

**A differing bit belongs to exactly one factor.** Where the input bits differ,
XOR preserves that difference: one result receives the current power of two
and the other does not. The total `first + second` is therefore fixed by the
inputs and by the already forced equal-bit choices. For a fixed nonnegative
sum, the product is largest when the two factors are as close as possible.

Process these optional assignments from the highest controllable bit downward.
Give each differing bit to the currently smaller partial factor. The current
power of two exceeds the sum of every still-undecided lower power, so assigning
it to the larger factor would create a difference that no later decision could
repair as well. The greedy choice minimizes the factors' final absolute
difference, and hence maximizes their product. Only after both maximizing
factors are known is their product reduced modulo $10^9+7$.

## Complexity detail

The algorithm examines exactly the $n$ controllable bit positions, taking
$O(n)$ time. It stores a mask, two partial factors, and the current bit, so its
auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Exhaust every value of x:** Trying all $2^n$ permitted choices is direct and correct but requires $O(2^n)$ time.
- **Dynamic programming over factor differences:** Bitwise states can represent partial assignments, but the dominance of higher bits makes that machinery unnecessary.
- **Process bits from least significant to most significant:** A locally balanced low prefix can be overturned by a later high bit, so the greedy proof requires descending bit order.
- **No controllable bits:** When `n == 0`, only `x = 0` is legal and the answer is `a * b` modulo $10^9+7$.
- **Equal controllable bits:** Set both resulting bits to `1`, including when both original bits are already `1` by choosing the corresponding bit of `x` as `0`.
- **Modulo timing:** Compare and balance the full factors; reducing partial values modulo $10^9+7$ would destroy their ordering and can change the maximizing choice.

