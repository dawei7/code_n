## General

**View the operations through binary representation**

The allowed operations interact directly with binary digits:

- an even number ends in bit `0`, and dividing by two removes that trailing zero with a right shift;
- an odd number ends in bit `1`, and adding or subtracting one makes it even.

The goal is therefore to create trailing zero bits efficiently, because each trailing zero can then be removed by one forced division. The exact greedy solution repeatedly inspects the lowest one or two bits of `n` and chooses the operation that exposes the shortest path toward fewer significant bits.

**Even numbers have no choice**

If `(n & 1) == 0`, the least significant bit is zero, so `n` is even. The only legal operation is division by two. The implementation uses `n >>= 1`, which shifts every bit right once and is exactly integer division by two for positive integers.

There is no optimization decision in this branch. Delaying or replacing the division is impossible under the rules.

**Odd numbers offer two neighboring even choices**

For odd `n`, both `n - 1` and `n + 1` are even. The important question is which result contains more trailing zeros. More trailing zeros mean more immediate right shifts before another odd choice is required.

Every odd binary number ends in either:

- `01`, meaning `n % 4 == 1`;
- `11`, meaning `n % 4 == 3`.

The expression `n & 3` keeps only the lowest two bits because decimal three is binary `11`. Thus `(n & 3) == 3` tests whether `n` ends in `11`.

**When the suffix is `01`, subtract one**

If an odd number ends in `01`, subtracting one changes that suffix to `00`. The result is divisible by four, so at least two divisions by two become available.

Adding one changes `01` to `10`. That result has only one trailing zero; after one division it is odd again and needs another plus-or-minus decision.

For example, `13` is binary `1101`:

```text
13 - 1 = 12 = 1100₂   (two trailing zeros)
13 + 1 = 14 = 1110₂   (one trailing zero)
```

The exact code reaches the final `else` and decrements in this case.

**When the suffix is `11`, usually add one**

If an odd number ends in `11`, subtracting one produces a suffix `10`, with only one trailing zero. Adding one carries through the run of trailing one bits and converts them to zeros.

For example, `7` is `111` in binary:

```text
7 - 1 = 6 = 110₂
7 + 1 = 8 = 1000₂
```

Incrementing reaches a power of two, which can be halved repeatedly: `7 -> 8 -> 4 -> 2 -> 1`.

For a longer pattern such as `...01111`, adding one produces `...10000`, removing an entire block of trailing ones through one increment followed by several shifts. The test `n != 3 and (n & 3) == 3` chooses this increment branch.

**Why `3` is the exception**

The number three also ends in `11`, but incrementing is worse:

```text
3 -> 4 -> 2 -> 1   (three operations)
3 -> 2 -> 1        (two operations)
```

For larger numbers ending in `11`, the carry produced by incrementing clears a useful trailing run without making the overall route longer. At `3`, the higher prefix is empty; incrementing creates a new significant bit (`100`) rather than efficiently simplifying an existing higher prefix. The explicit `n != 3` check forces the optimal decrement.

The number one never reaches this choice because it is the loop’s termination state.

**A local bit-block argument**

For an odd number ending in `01`, the decrement route turns the two-bit suffix into `00`; the increment route turns it into `10`. Both spend one operation to become even, but the decrement route can discard two low bits with shifts before another decision, while the increment route can discard only one. Choosing decrement cannot leave more unresolved low-order work.

For an odd number greater than three ending in `11`, there are at least two trailing one bits. Incrementing carries across the entire trailing-one block and replaces it with zeros. Decrementing changes only the final bit, leaving the remaining one bits to cause further odd decisions. Except for the isolated value three, clearing the maximal one block is never worse than processing it piecemeal.

This greedy rule can also be seen from the standard recurrence. For odd $n$, either choice costs one operation and is followed by a forced division:

$$
f(n)
=
2+min\left(
f\left(\frac{n-1}{2}\right),
f\left(\frac{n+1}{2}\right)
\right).
$$

The low two bits tell which quotient is even and therefore immediately reducible again. The algorithm chooses that branch, with the `3` base-pattern correction.

**Tracing `n = 7`**

1. `7` is odd, not three, and `7 & 3 == 3`; increment to `8`.
2. `8` is even; shift to `4`.
3. `4` is even; shift to `2`.
4. `2` is even; shift to `1`.

The counter `ans` becomes four, matching the minimum.

For `n = 8`, every value is even until one: `8 -> 4 -> 2 -> 1`, so the answer is three.

**Why the operation counter is exact**

Every loop iteration performs exactly one legal replacement and then increments `ans` once. The loop stops only when the current value is one. Therefore `ans` is the length of the greedy operation sequence.

The binary greedy rule selects an optimal neighbor at every odd state, and even states are forced. Consequently the constructed sequence has minimum possible length, so the returned counter is the requested optimum.

## Complexity detail

Let $b=\lfloor\log_2 n\rfloor+1$ be the number of binary digits.

Every even operation removes one bit position through a right shift. An odd increment or decrement is followed by an even state, and the chosen operation commonly creates several trailing zeros. Thus only a constant number of operations is spent per bit before the significant length decreases. Total time is $O(\log n)$.

The method stores only `n` and `ans`, so auxiliary space is $O(1)$. It uses no recursion, memoization table, queue, or binary string.

Python integers can safely represent `n + 1` when the input is $2^{31}-1$. In a signed 32-bit implementation, that increment would overflow; using a 64-bit integer for the working value is necessary even though the input itself fits in 32 bits.

## Alternatives and edge cases

- **Memoized recursion:** Evaluate both `n - 1` and `n + 1` branches for odd values and cache results. This is straightforward and optimal but uses $O(\log n)$ recursion/cache space. The bit rule removes the branching.

- **Breadth-first search:** Treat integers as graph states and search for one. It guarantees a shortest path but can store many unnecessary states and ignores the arithmetic structure.

- **Always decrement odd values:** This fails on values such as `7` and `15`, where incrementing reaches a power of two far faster.

- **Always increment values ending in `11`:** This is correct for such values except `3`; omitting that exception adds one unnecessary operation.

- **`n = 1`:** The loop is skipped and zero operations are returned.

- **`n = 2`:** One forced right shift reaches one, so the answer is one.

- **`n = 3`:** The explicit exception chooses `3 -> 2 -> 1`.

- **Power of two:** Every step is a right shift, and the answer is exactly the exponent.

- **One below a power of two:** A suffix of ones triggers increment, reaching the power of two in one operation and then shifting down.

- **Odd value ending in `01`:** Decrement creates at least two trailing zeros and is selected by the final branch.

- **Maximum input:** $2^{31}-1$ is a long run of one bits. Incrementing produces $2^{31}$, after which shifts finish efficiently; the working type must allow that temporary value.

- **Bitwise-test meaning:** `n & 1` reads the lowest bit, while `n & 3` reads the lowest two. These tests avoid converting to a binary string and remain constant time in the standard word model.
