## General

**Collapse matching pairs with XOR**

The competitive source applies `operator.xor` to the entire array through `functools.reduce`. This is a direct expression of the mathematical observation behind the problem.

For each bit position, XOR returns zero when both input bits match and one when they differ. Consequently, an integer XORed with itself is zero:

$$
x \mathbin{\oplus} x=0.
$$

Zero is the identity:

$$
x \mathbin{\oplus} 0=x.
$$

Finally, XOR is associative and commutative:

$$
(a\mathbin{\oplus}b)\mathbin{\oplus}c
=a\mathbin{\oplus}(b\mathbin{\oplus}c)
$$

and

$$
a\mathbin{\oplus}b=b\mathbin{\oplus}a.
$$

These properties are precisely what the frequency pattern needs. Every duplicate value can cancel with its matching copy even when other values appear between them.

**Follow the reduction step by step**

`reduce(operator.xor, A)` begins with the first array value as its accumulator. It XORs in each later value and returns the final accumulator.

For `[2, 2, 1]`, the steps are:

- start with accumulator `2`;
- XOR the second `2`, producing zero;
- XOR `1`, producing one.

For `[4, 1, 2, 1, 2]`, a literal left fold produces successive intermediate values, but its final result can be understood by regrouping:

$$
4
\mathbin{\oplus}(1\mathbin{\oplus}1)
\mathbin{\oplus}(2\mathbin{\oplus}2)
=4\mathbin{\oplus}0\mathbin{\oplus}0
=4.
$$

Regrouping is part of the proof, not an extra runtime step. The code performs a single pass and never searches for a mate.

**An invariant for beginners**

After reducing the first `k` array entries, the accumulator equals the XOR of exactly those `k` entries.

This is true initially because the accumulator is the first entry. Every reduction step XORs the next entry into the existing result, so the statement remains true.

After all entries, the accumulator equals the XOR of the full array. Associativity and commutativity then let each repeated pair be considered together. Every such pair becomes zero. The one value with no mate remains unchanged, so it is the returned answer.

Another useful interpretation is parity. At each bit position, XOR records whether an odd number of processed values have a one in that position. Two identical integers contribute each of their one-bits twice, an even count, so their contribution disappears. The singleton contributes its full bit pattern once.

**Negative values and the one-element case**

Python’s XOR works for negative integers using behavior equivalent to an unbounded two’s-complement representation. The identities above still hold: `x ^ x` is zero for negative `x`, and `0 ^ x` is `x`.

The call supplies no initializer. Since the contract guarantees a nonempty list, `reduce` always has a first element. If `A` has one value, no XOR call is needed and `reduce` returns that value directly.

The method does not rely on the unique value being positive or nonzero, and it does not mutate `A`.

**Why the problem’s assumptions are essential**

If every ordinary value appeared an even number of times, XOR would cancel all of those copies, so the idea generalizes beyond exactly two copies. However, if two different values both appeared an odd number of times, the result would be their XOR, not either individual value.

The problem guarantees one and only one odd-frequency value—the singleton—so the XOR result has an unambiguous interpretation.

## Complexity detail

Let $n$ be the number of integers.

`reduce` combines the values in one pass and invokes `operator.xor` $n-1$ times. Because the problem bounds each integer’s magnitude, every bitwise operation has bounded cost. Total time is $O(n)$.

Only one accumulated integer and constant iterator state are needed. The imported function objects are module-level constants, not input-sized storage. Auxiliary space is $O(1)$.

The solution meets both explicit requirements: linear runtime and constant extra space. It also leaves the input untouched.

For arbitrary-precision integers outside the problem bounds, a bitwise operation technically costs time proportional to operand bit length. The given numerical range keeps that detail from changing the stated complexity.

## Alternatives and edge cases

- **Explicit XOR loop:** Initialize an accumulator to zero and apply `accumulator ^= value` for every item. It has identical bounds and can be easier to debug than `reduce`.
- **Frequency map:** Counting values is straightforward and linear expected time, but it needs $O(n)$ extra storage.
- **Toggle a set:** Insert on first occurrence and remove on second. The singleton remains, at the cost of linear space.
- **Sort and pair:** After sorting, compare adjacent positions. This costs $O(n\log n)$ time and may alter the input.
- **Distinct-sum formula:** `2 * sum(set(A)) - sum(A)` returns the singleton under the exact twice-plus-once rule but allocates a set and risks overflow in fixed-width arithmetic.
- **One value:** The non-initialized reduction returns it directly.
- **Singleton zero:** Duplicate contributions cancel, leaving zero as the correct result.
- **Negative integers:** Equality-based bit cancellation remains valid for signed values.
- **Separated duplicate occurrences:** Adjacency is irrelevant; algebraic regrouping handles any order.
- **Empty list outside the contract:** `reduce` without an initializer raises `TypeError`, so the nonempty guarantee is operationally important.
- **Invalid frequency data:** The implementation deliberately trusts the contract and cannot report which assumption was violated.
