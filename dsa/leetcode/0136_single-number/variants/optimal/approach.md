## General

**Use the frequency guarantee, not a frequency table**

The array has a very strong structure: exactly one value occurs once, and every other value occurs exactly twice. The required constant extra space rules out storing counts or a set proportional to the input.

Bitwise exclusive OR, written XOR, is designed for this cancellation pattern. For one bit, its result is one exactly when the two input bits differ:

| First bit | Second bit | XOR |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Applying that operation independently to every bit gives several useful integer identities:

$$
x \mathbin{\oplus} x = 0
$$

$$
x \mathbin{\oplus} 0 = x
$$

XOR is also associative and commutative. Associativity allows parentheses to move, and commutativity allows operands to be reordered. Therefore, equal values can be brought together conceptually even when their occurrences are far apart in the array.

**What `reduce(xor, nums)` computes**

`reduce` takes the first two elements, combines them with `xor`, combines that result with the third element, and continues until one accumulator remains. For `[4, 1, 2, 1, 2]`, the effective expression is:

$$
4 \mathbin{\oplus} 1 \mathbin{\oplus} 2
\mathbin{\oplus} 1 \mathbin{\oplus} 2.
$$

By reordering and regrouping for reasoning, this equals:

$$
4 \mathbin{\oplus}
(1 \mathbin{\oplus} 1)
\mathbin{\oplus}
(2 \mathbin{\oplus} 2).
$$

Each pair becomes zero, leaving:

$$
4 \mathbin{\oplus} 0 \mathbin{\oplus} 0 = 4.
$$

The actual implementation does not sort or rearrange the array. Those algebraic properties merely prove that the left-to-right reduction has the same result as the pair-grouped expression.

**Why the remaining value is exactly the answer**

Let the unique value be $u$, and let the repeated values be $p_1,p_2,\ldots,p_k$. The reduction contains:

$$
u
\mathbin{\oplus}
p_1 \mathbin{\oplus} p_1
\mathbin{\oplus}\cdots\mathbin{\oplus}
p_k \mathbin{\oplus} p_k.
$$

Every repeated pair contributes zero. XORing any number of zeros with $u$ leaves $u$. Thus the returned accumulator is the value that appears once.

This is not merely detecting oddness of the array length. The result follows from the exact multiplicity guarantee. If another value occurred three times, two copies would cancel and one would remain in the XOR too, so the method would no longer identify a uniquely specified element.

**Why negative integers still work**

The allowed values include negatives. Python defines bitwise operations on negative integers consistently with an unbounded two’s-complement representation. A negative integer XORed with itself is still zero, and XOR with zero still returns that integer. Cancellation depends on identical bit patterns, so sign does not invalidate the method.

In fixed-width languages, the same reasoning holds within the integer width: two identical negative bit patterns cancel bit for bit.

**Why no initial value is supplied**

The call uses `reduce(xor, nums)` without a third initializer argument. For a nonempty sequence, `reduce` takes `nums[0]` as the initial accumulator and processes the remaining values. A one-element input therefore returns that element directly, which is exactly right.

For an empty sequence, the same call would raise `TypeError`. The Reference explicitly guarantees at least one element, so the absence of an initializer is valid. Writing `reduce(xor, nums, 0)` would also work and would define an empty-input result, but it is not necessary for this contract.

The input list is only read; no value or ordering is changed.

## Complexity detail

Let $n$ be the length of `nums`.

The reduction applies XOR $n-1$ times, so time is $O(n)$. With the problem’s bounded integer values, each XOR is constant time.

The reduction keeps one accumulator and a constant amount of iteration state. It creates no set, dictionary, sorted copy, or frequency array, so auxiliary space is $O(1)$.

In Python’s general arbitrary-precision integer model, bitwise-operation cost depends on the number of machine words in the operands. Here values are bounded between $-3\cdot10^4$ and $3\cdot10^4$, making that width bounded and the stated $O(n)$ model exact for the problem domain.

## Alternatives and edge cases

- **Hash set toggling:** Add an unseen value and remove a seen value. The final set contains the answer, but it requires $O(n)$ extra space.
- **Frequency dictionary:** Count occurrences and return the key with count one. It is linear expected time but violates the constant-space requirement.
- **Sort then scan pairs:** Equal values become adjacent, making the singleton easy to find. It costs $O(n\log n)$ time and may use extra sorting memory or mutate the input.
- **Arithmetic with a set:** Compute twice the sum of distinct values minus the full sum. It uses $O(n)$ set space and can overflow in fixed-width languages.
- **One element:** `reduce` returns that element without calling `xor`.
- **Unique value is zero:** All duplicate pairs cancel to zero, and the remaining zero is correctly returned.
- **Negative values:** Identical negative integers cancel exactly under bitwise XOR.
- **Arbitrary ordering:** Pair occurrences need not be adjacent because XOR is associative and commutative.
- **Malformed multiplicities:** The proof depends on every non-answer appearing exactly twice; the function does not validate that promise.
- **Runtime dependencies:** The selected source uses `List`, `reduce`, and `xor` without imports. Standalone Python needs `from typing import List`, `from functools import reduce`, and `from operator import xor`.
