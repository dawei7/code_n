## General

A valid number must satisfy two conditions at the same time:

1. digit $x$ occurs somewhere in the decimal representation; and
2. the first, most significant digit is not $x$.

The source processes the number arithmetically from right to left. It checks every digit except the leading digit for an occurrence of $x$, then leaves the leading digit in `n` and tests it separately.

This separation matches the logic especially well: any useful occurrence must be outside the first position, because an occurrence only at the first position simultaneously violates the second condition.

**Removing digits from the right**

For a nonnegative integer $n$ with at least two digits:

$$
n\bmod10
$$

is its rightmost decimal digit, and

$$
\left\lfloor\frac n{10}\right\rfloor
$$

is the remaining prefix after removing that digit.

The loop runs while `n > 9`. Therefore, it keeps extracting rightmost digits only while more than one decimal digit remains. Each iteration:

- compares `n % 10` with `x`; and
- performs `n //= 10` to discard the inspected digit.

When the loop stops, `n` is between 0 and 9 and is exactly the original leading digit.

**What \(has_x\) records**

The Boolean `has_x` begins false. The update

```text
has_x = has_x or n % 10 == x
```

makes it true as soon as any extracted non-leading digit equals $x$. Once true, the logical `or` keeps it true for all remaining iterations.

At loop termination:

$$
\texttt{has\_x}
\iff
x\text{ appeared in at least one non-leading position}.
$$

The source does not need the number or locations of occurrences. The requirement asks only whether at least one exists.

**Why the leading digit is deliberately excluded from \(has_x\)**

Suppose the leading digit equals $x$. The number is invalid regardless of whether $x$ appears again later. Recording the leading occurrence as satisfying the containment rule would not be enough; the start restriction still has to reject it.

By stopping before the last digit and returning

```text
has_x and n != x
```

the source states the exact two facts needed:

- a non-leading occurrence exists; and
- the remaining leading digit differs from $x$.

This is equivalent to the original wording. If the number contains $x$ and does not start with $x$, at least one occurrence must necessarily be non-leading. Conversely, a non-leading occurrence together with a different leading digit satisfies both conditions.

**A trace**

For `n = 101` and `x = 0`:

1. Rightmost digit 1 does not match; division leaves 10.
2. Rightmost digit 0 matches, so `has_x` becomes true; division leaves 1.
3. The loop stops because 1 is a single digit.
4. The leading digit 1 differs from 0.

Both final conditions are true, so the method returns true.

For `n = 232` and `x = 2`:

1. The trailing 2 makes `has_x` true.
2. The middle 3 is inspected.
3. The remaining leading digit is 2.

The final `n != x` condition is false, so the method returns false even though there was another occurrence.

For `n = 5` and `x = 1`, the loop never runs. `has_x` remains false, correctly showing that no non-leading occurrence exists.

**The special representation of zero**

The decimal representation of zero is the one-character string `"0"`. When `n = 0`, the loop does not run.

- If $x=0$, `has_x` is false and the number also starts with 0; the answer is false.
- If $x\ne0$, the number contains no $x$; the answer is also false.

Thus no separate zero branch is required.

**Why the final Boolean is exact**

Every original digit except the leading digit is exposed exactly once by remainder and division. Hence `has_x` neither misses nor invents a qualifying internal occurrence. The one unprocessed digit is exactly the leading digit, so `n != x` evaluates the start rule.

Their conjunction accepts every number satisfying both rules and rejects a number as soon as either required fact is absent.

## Complexity detail

Let $D$ be the number of decimal digits of the original `n`. The loop runs $D-1$ times for a multi-digit number and zero times for a single-digit number. Each iteration performs constant arithmetic and Boolean work.

The time complexity is

$$
O(D)=O(\log_{10}(N+1)).
$$

The $N+1$ form handles $N=0$ without taking a logarithm of zero.

The source stores only `has_x` and the progressively shortened local integer `n`. Its auxiliary-space complexity is

$$
O(1).
$$

Reassigning the integer parameter does not mutate any caller-owned object because Python integers are immutable.

## Alternatives and edge cases

- **String conversion:** `sx = str(x); s = str(n); return sx in s and s[0] != sx` is direct and also linear in the digit count, but allocates a decimal string.
- **Track the original leading digit separately:** One can first find the highest power of ten, but the source obtains the leading digit naturally by repeated division.
- **Single-digit number equal to \(x\):** It contains $x$ but starts with $x$, so it is invalid; `has_x` remains false.
- **Single-digit number different from \(x\):** It does not contain $x$ and is invalid.
- **Zero with \(x=0\):** Its sole occurrence is leading, so it fails.
- **Several internal occurrences:** The first match makes `has_x` true; later matches do not change the result.
- **Leading and internal occurrences:** The leading equality still rejects the number, as required.
- **Occurrence only at the end:** The first loop iteration detects it.
- **Occurrence only immediately after the leading digit:** The final loop iteration before termination detects it.
- **Digit \(x=0\):** Arithmetic extraction handles internal zeros, while ordinary decimal representation has no leading zeros to consider.
- **Nonnegative-input requirement:** The remainder/division loop is designed for $n\ge0$; negative representations would introduce a sign and different floor-division behavior.
