## General

**Translate distinct powers into ternary digits**

Every nonnegative integer has a unique base-three representation:

$$
n=d_0 3^0+d_1 3^1+d_2 3^2+\cdots,
$$

where each digit $d_i$ is zero, one, or two.

Representing `n` as a sum of distinct powers of three means each power may be selected zero times or one time. Therefore the representation is possible exactly when every ternary digit is zero or one. A digit two would require using that power twice.

The exact solution extracts ternary digits from least significant to most significant and rejects the first digit greater than one.

**Extract one digit with remainder**

`n % 3` is the least significant base-three digit. The source checks:

`if n % 3 > 1`.

Because a remainder modulo three can only be zero, one, or two, “greater than one” means exactly digit two. In that case no sum of distinct powers can equal the original number, so the method returns false immediately.

If the digit is zero, the current power is omitted. If it is one, the current power is included once. Neither case violates distinctness.

**Move to the next power**

After accepting the current digit, `n //= 3` discards it. Integer division shifts the ternary representation right by one place, making the next digit the new remainder.

For example, decimal 12 has ternary representation 110:

- `12 % 3 = 0`, so $3^0$ is not used; division gives four.
- `4 % 3 = 1`, so $3^1$ is used; division gives one.
- `1 % 3 = 1`, so $3^2$ is used; division gives zero.

No digit two appears, and $12=3+9$.

**Why a digit two cannot be repaired by carrying**

One might wonder whether a ternary two could be replaced by a higher power and adjustments elsewhere. Positional representation is unique. Two copies of $3^i$ equal $2\cdot3^i$, which cannot be formed by distinct lower powers because:

$$
1+3+\cdots+3^{i-1}
=
\frac{3^i-1}{2}
<
3^i.
$$

Nor can a higher power be used and canceled because all selected powers are positive. Thus digit two is a definitive impossibility.

**Trace the false example**

Decimal 21 divides as follows:

- `21 % 3 = 0`, then `n` becomes seven.
- `7 % 3 = 1`, then `n` becomes two.
- `2 % 3 = 2`.

The final remainder requires two copies of $3^2$, so the source returns false.

**Why reaching zero proves success**

Each accepted remainder records a legal choice of zero or one copy of the corresponding power. Repeated division eventually removes every ternary digit.

If the loop ends without seeing two, all digits belong to `{0,1}`. Selecting precisely the powers at digit-one positions reconstructs the original number, and the powers are distinct by position.

**Loop invariant**

After processing $k$ iterations, the already inspected digits for $3^0$ through $3^{k-1}$ are all zero or one, and current `n` is the integer represented by the unprocessed higher digits.

Modulo and division examine the next digit while preserving this statement. A two disproves representability; zero ends the scan with every digit valid. This establishes correctness.

## Complexity detail

For a generalized positive input `n`, each iteration divides it by three, so the loop runs $\lfloor\log_3 n\rfloor+1$ times. Exact time is $O(\log n)$ and auxiliary space is $O(1)$.

The manifest states $O(1)$ time. Under the fixed official constraint `n <= 10^7`, there are at most 15 ternary digits, a constant upper bound, so that constraint-specific classification is defensible. The implementation's growth behavior without the frozen bound is logarithmic.

The source mutates only its local integer parameter binding; it allocates no digit string or collection.

## Alternatives and edge cases

- **Convert to a ternary string:** It makes digits visible but allocates $O(\log n)$ space.
- **Backtracking over powers:** Include or exclude every power, producing exponentially more search than direct unique representation.
- **Greedy subtract largest power:** It can work with careful checks, but ternary digits state the condition more directly.
- **n equal to a power of three:** Its representation has one digit one and otherwise zeros, so it passes.
- **n equal to two:** The first remainder is two and it fails.
- **n equal to one:** The single remainder is one and it passes as $3^0$.
- **Several selected powers:** Multiple digit-one positions are allowed because exponents are distinct.
- **Ternary zero digit:** It simply means skip that power.
- **Ternary two digit:** It means the same power would be needed twice and causes immediate failure.
- **Positive-input guarantee:** The official input excludes zero, though the loop would return true for zero as the empty sum.
- **Uniqueness of representation:** It prevents alternative carry arrangements from avoiding a digit two.
- **Early exit:** The method stops at the first impossible digit.
- **Local mutation:** Dividing `n` does not alter an external object.
- **Fixed bound:** It explains the manifest's constant-time label while the general algorithm is logarithmic.
- **Loop progress:** Integer division by three removes the ternary digit just inspected, so positive `n` strictly decreases and the scan must terminate.
