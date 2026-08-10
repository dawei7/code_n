## General

Three consecutive integers are fully determined by their middle value. If the middle integer is $x$, the sorted triple must be

$$
x-1,\quad x,\quad x+1.
$$

Their sum simplifies immediately:

$$
(x-1)+x+(x+1)=3x.
$$

The two offsets cancel. Therefore the requested triple exists exactly when `num` is divisible by three, and its middle value must be `num / 3`.

**Compute quotient and remainder together**

The exact source calls `divmod(num, 3)`. Python returns two integers:

- `x` is the floor quotient;
- `mod` is the remainder.

They satisfy

$$
\texttt{num}=3x+\texttt{mod},
$$

with `mod` equal to zero, one, or two because `num` is non-negative.

Using `divmod` communicates that both parts of the same division matter. The quotient is the candidate middle value, while the remainder decides whether that candidate is exact.

**Reject a nonzero remainder**

If `mod` is nonzero, `num` is not divisible by three. The conditional expression returns an empty list.

This is not merely a convenient test; it is necessary. The sum of any three consecutive integers is three times the middle integer, so it is always divisible by three. A number with remainder one or two cannot equal such a sum, regardless of which starting integer is tried.

For `num = 4`, division gives quotient one and remainder one. The nearby triple `[0, 1, 2]` sums to three, while `[1, 2, 3]` sums to six. There is no integer middle value between one and two that could make the sum four, so the empty result is correct.

**Build the only possible triple when divisible**

If `mod` is zero, then `num = 3x` exactly. The method returns `[x - 1, x, x + 1]`.

The three values differ by one from left to right, so they are consecutive. They are already sorted in ascending order. Their sum is `3 * x`, which equals `num` because the remainder was zero.

For `num = 33`, `divmod` returns `x = 11` and `mod = 0`. The resulting list `[10, 11, 12]` consists of consecutive integers and sums to 33.

**Why the answer is unique**

Suppose a valid sorted triple starts at integer $a$. It must be $a,a+1,a+2$, whose sum is $3a+3=3(a+1)$. Its middle value is therefore `num / 3`.

Division by three has only one quotient when the remainder is zero, so there cannot be two different middle integers producing the same sum. Once the middle is fixed, its predecessor and successor are fixed too. The returned triple is not just one possible answer; it is the unique triple of three consecutive integers with that sum.

**Why no search is needed**

A brute-force approach could try possible starting values and compare sums. The algebra removes that entire search space. The input directly determines the middle value, and one divisibility test decides existence.

This is a useful general pattern: for an odd number of consecutive integers, symmetric offsets cancel around the middle, so the sum equals the count times the middle value. Here the count is three.

**Handle zero and negative members correctly**

The input constraint allows `num = 0`. Division gives `x = 0` and zero remainder, so the method returns `[-1, 0, 1]`. These are valid integers, are consecutive and sorted, and sum to zero.

The problem asks for integers, not positive integers. Therefore the negative first member in this boundary case is allowed. Rejecting it would add a restriction that the contract does not contain.

Although the input itself is non-negative, the same formula also works mathematically for negative multiples of three under Python's `divmod` rules: the quotient remains the exact middle when the remainder is zero. That extension is not needed for the given domain.

**Why the conditional expression matches both cases**

The return statement has exactly two branches: `[] if mod else [x - 1, x, x + 1]`. In Python, zero is falsy and a positive remainder is truthy.

Thus “if `mod`” selects the empty list when division is inexact, while the `else` branch constructs the triple when `mod == 0`. No separate loops, state, or mutation are needed.

## Complexity detail

The method performs one division with remainder, one constant-time conditional decision, and at most three constant-count arithmetic expressions. Under the standard fixed-width integer model, time is $O(1)$.

It stores two scalar results and returns either an empty list or a three-element list. Auxiliary space is $O(1)$, and output space is also $O(1)$ because the output length never exceeds three.

Strict bit-complexity analysis would charge arithmetic according to the number of bits in `num`, but the problem's complexity model and bounded input treat integer arithmetic as constant time. The manifest's $O(1)$ time and space match the exact implementation.

## Alternatives and edge cases

- **Use remainder then integer division:** Check `num % 3` and compute `num // 3` separately. This is equally clear but performs two explicit operations instead of obtaining both results together.
- **Solve from the first value:** From `a + (a + 1) + (a + 2) = num`, derive `a = num / 3 - 1`. It reaches the same list but centering at the middle makes the cancellation more obvious.
- **Brute-force search:** Trying possible triples is unnecessary and becomes slow for values up to $10^{15}$.
- **Remainder zero:** The quotient is an integer middle, so the constructed triple is always valid.
- **Remainder one or two:** No triple exists because every sum of three consecutive integers is a multiple of three.
- **`num = 0`:** Return `[-1, 0, 1]`; negative members are allowed because the members need only be integers.
- **`num = 1` or `num = 2`:** Neither is divisible by three, so both return empty lists.
- **`num = 3`:** The result is `[0, 1, 2]`, showing that zero may appear in a valid triple.
- **Large divisible input:** Direct arithmetic handles it without iteration; Python integers also avoid overflow.
- **Sorted order:** `x - 1 < x < x + 1` guarantees the required ordering automatically.
- **Consecutiveness:** Adjacent differences are exactly one, not merely positive.
- **Uniqueness:** A fixed sum determines a unique middle value, so no tie-breaking is necessary.
- **No input mutation:** `num` is an immutable integer and the method creates a fresh result list.
- **Output length:** Success always returns exactly three values; failure always returns zero values.
