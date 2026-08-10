## General

A positional base-seven number uses digits zero through six. If its digits from most significant to least significant are `d_k, d_{k-1}, ..., d_0`, its value is

$$
d_k7^k+d_{k-1}7^{k-1}+\cdots+d_1 7+d_0.
$$

Repeated division by seven discovers these digits from the opposite direction: the remainder gives the least significant digit, and the quotient contains every more significant digit still to be found.

**Handle zero before the extraction loop.** If `num == 0`, the correct representation is `"0"`. The later loop runs only while `num` is nonzero, so without this special return it would collect no digits and incorrectly produce an empty string.

**Separate the sign from the magnitude.** A leading minus sign is not a base-seven digit. For a negative input, the code returns

`'-' + self.convertToBase7(-num)`.

Negating the input produces its positive magnitude, which the same conversion logic can process. The recursive call is only one sign-handling level deep: its argument is positive, so it does not recurse again for the sign. Prefixing `'-'` afterward preserves the standard textual representation.

For `num = -7`, the recursive positive conversion returns `"10"`, and the outer call returns `"-10"`.

**Extract one digit with quotient and remainder.** For positive `num`, the loop computes `num % 7`. Euclidean division guarantees

$$
\textit{num}=7\left\lfloor\frac{\textit{num}}7\right\rfloor+(\textit{num}\bmod 7),
$$

where the remainder is an integer from zero through six. That remainder is exactly the current least significant base-seven digit.

The code converts it to text and appends it to `ans`, then applies `num //= 7`. Integer division discards the digit just extracted and shifts the remaining base-seven representation one place to the right.

For decimal `100`:

- `100 % 7 = 2` and `100 // 7 = 14`;
- `14 % 7 = 0` and `14 // 7 = 2`;
- `2 % 7 = 2` and `2 // 7 = 0`.

The extracted list is therefore `['2', '0', '2']`. This example happens to read the same in either direction, so consider decimal `15` as well: remainders are one and then two, producing `['1', '2']` during extraction, while the correct representation is `"21"`.

**Reverse because remainders arrive least significant first.** Each append records the digit for successively larger powers `7^0, 7^1, 7^2, ...`. Human-readable positional notation writes the largest power first. `ans[::-1]` reverses the digit list, and `''.join(...)` concatenates it without separators.

The loop terminates because positive integer division by seven strictly decreases every positive `num` until it reaches zero. At termination, every quotient digit has been extracted.

Reconstruction verifies why the remainder sequence is enough. If the extracted low-to-high digits are `r0, r1, ..., rk`, repeatedly expanding the quotient equations gives

$$
N=r_0+7r_1+7^2r_2+\cdots+7^kr_k.
$$

After reversal, the string writes `rk` first and `r0` last, exactly matching positional notation. For decimal forty-nine, extraction yields remainders zero, zero, and one. Reversal produces `"100"`, whose value is `1 * 7^2 + 0 * 7 + 0 = 49`. Interior and trailing zero digits are therefore preserved naturally; only leading zeros are absent.

Correctness can be proved by a loop invariant. After `t` iterations, the collected remainders are exactly the lowest `t` base-seven digits of the original magnitude, in low-to-high order, and current `num` is the original magnitude with those `t` digits removed. Quotient-and-remainder division establishes the next digit and preserves the invariant. When `num` becomes zero, no higher digits remain. Reversing yields the unique valid base-seven representation.

The constraint magnitude is modest, but the method does not depend on a fixed digit table or language conversion helper. It derives the representation directly and works for any integer magnitude supported by Python.

## Complexity detail

Let $N = |\textit{num}|$. For $N > 0$, each loop iteration divides the remaining magnitude by seven, so the number of iterations is $\lfloor\log_7 N\rfloor+1$. Digit extraction, reversal, and joining therefore take $O(\log N)$ time.

The digit list and returned string contain $O(\log N)$ characters, giving $O(\log N)$ space. The negative-input recursive call adds only one constant-depth frame. For zero, both time and output size are constant; the logarithmic bound is understood for positive magnitude.

## Alternatives and edge cases

- **Built-in base conversion:** Some languages provide formatting for arbitrary bases, but manual repeated division demonstrates the required representation and is portable.
- **Recursive digit extraction:** Recurse on `num // 7` and append the remainder while unwinding. It naturally produces high-to-low order but uses $O(\log N)$ call-stack depth.
- **Prepend every digit to a string:** This avoids a final reversal but repeatedly copying an immutable growing string can make the implementation quadratic in the number of digits.
- **Zero:** It must return `"0"` explicitly because the positive extraction loop would execute zero times.
- **Negative input:** Convert only the magnitude and add one leading minus sign; Python's negative remainder behavior should not be used as digit logic here.
- **Exact multiple of seven:** A zero remainder is a real interior or final digit and must be appended, as shown by decimal seven becoming `"10"`.
- **Single base-seven digit:** Values zero through six return their ordinary one-character decimal digit strings.
- **No leading zeros:** The final extracted quotient is from one through six for positive input, so reversal automatically places a nonzero leading digit.
