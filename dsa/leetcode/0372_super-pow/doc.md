# Super Pow

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 372 |
| Difficulty | Medium |
| Topics | Math, Divide and Conquer |
| Official Link | [LeetCode](https://leetcode.com/problems/super-pow/) |

## Problem Description
### Goal
Given a positive integer base `a` and a nonempty list of decimal digits `b`, let `B` be the positive exponent represented by those digits from most significant to least significant. The representation contains no leading zeroes, and `B` may be far too large for an ordinary integer type.

Return $a ^{B} \bmod 1337$. Process the exponent representation without constructing its full numerical value, reducing intermediate powers modulo `1337` to control size. Preserve ordinary modular behavior for bases larger than or divisible by the modulus, and return only the modular value rather than the enormous full power.

### Function Contract
**Inputs**

- `a`: an integer base
- `b`: a non-empty list of decimal digits representing the exponent from most significant to least significant

**Return value**

- $a ^{B} \bmod 1337$, where `B` is the integer represented by `b`.

### Examples
**Example 1**

- Input: `a = 2, b = [3]`
- Output: `8`

**Example 2**

- Input: `a = 2, b = [1,0]`
- Output: `1024`

**Example 3**

- Input: `a = 1, b = [4,3,3,8,5,2]`
- Output: `1`

### Required Complexity

- **Time:** $O(d)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Extend the exponent one decimal digit at a time**

Suppose the processed prefix represents exponent `E` and the next digit is `x`. Appending that digit produces exponent $10E + x$. The corresponding power decomposes as

$a^{(10E + x)} = (a^{E})^{10} \cdot a^{x}$.

Maintain `result = a ** E % 1337`. For each digit, replace it with `result ** 10 * a ^ digit % 1337`. Both exponents used in this update are at most ten, so each digit costs constant work.

**Reduce after every multiplication**

Modular multiplication and exponentiation may reduce their operands at any step without changing the final remainder. Taking modulo `1337` after both small powers and their product keeps every intermediate bounded even though the represented decimal exponent may contain hundreds of digits.

**Why the invariant reaches the full exponent**

Before reading digits, the empty prefix has exponent zero and `result = 1 = a ** 0`. If the invariant holds for prefix `E`, the decimal identity above proves that the update yields the correct modular power for prefix $10E + x$. Induction over all digits therefore leaves the exact remainder for the complete exponent.

**Trace exponent ten**

Starting from one with base two, processing digit `1` gives `2`. Appending digit `0` raises that partial result to the tenth power and multiplies by $2^{0}$, producing $1024 \bmod 1337$.

#### Complexity detail

Let `d` be the number of exponent digits. Each digit performs modular powers with fixed exponents ten and at most nine, so total time is $O(d)$. Only the running remainder, base remainder, and current digit are stored, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Right-to-left digit processing:** can maintain successive powers $a^{10^i}$ and is also $O(d)$.
- **Recompute every decimal prefix from the beginning:** remains correct but repeats work and costs $O(d^2)$.
- **Materialize the full exponent:** requires arbitrary-precision storage and defeats the digit-streaming contract, even if modular exponentiation follows.
- Exponent zero returns one, including when the base is divisible by 1337.
- A base divisible by 1337 returns zero for every positive exponent.
- The base may be reduced modulo 1337 before processing any digit.
- Internal zero digits still multiply the prior exponent by ten and cannot simply be skipped.

</details>
