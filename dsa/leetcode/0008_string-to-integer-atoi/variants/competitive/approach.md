## General

**Advance one reader through a fixed parsing grammar**

The selected method treats the valid integer prefix as

```text
leading whitespace*  optional sign  decimal digit*
```

and stops at the first character that no longer fits the current phase. It does not remove arbitrary whitespace, search for a sign later in the string, or resume digit reading after a delimiter.

The variable named `str` is the input string. It shadows Python's built-in `str` type inside this method, which is a naming drawback but does not change the parsing behavior because the method never needs to call that built-in directly.

**Return zero for missing content**

The initial state is

```python
result = 0
```

An empty input returns it immediately. After whitespace is skipped, the method also checks whether the reader reached the end. Thus `""`, `" "`, and `"    "` all return zero without an out-of-range access.

**Skip the permitted leading whitespace**

The loop

```python
while i < len(str) and str[i].isspace():
    i += 1
```

checks the bound before indexing and advances only at the beginning. `isspace()` recognizes more kinds of whitespace than the literal ordinary space named by the Reference. The supplied input alphabet contains only `' '` among whitespace characters, so its behavior is equivalent for every legal test.

Once this loop ends, whitespace is no longer accepted. A space encountered during digit scanning terminates the number.

**Consume at most one sign**

The parser starts with `sign = 1`. A plus sign advances the index without changing it; a minus sign sets `sign = -1` and advances:

```python
if str[i] == "+":
    i += 1
elif str[i] == "-":
    sign = -1
    i += 1
```

Because this is one `if`/`elif` decision rather than a loop, only one sign can be consumed. A second sign is not a digit and stops the following loop. If no digits follow the sign, the untouched `result = 0` is returned, and either sign applied to zero still gives zero.

**Accept only ASCII decimal digits**

The loop condition

```python
'0' <= str[i] <= '9'
```

is an explicit ASCII range test. It exactly matches the Reference's digits `0-9` and avoids the broader Unicode behavior of `isdigit()`.

Each accepted character is converted with `int(str[i])`, and the magnitude is extended by

```python
result = result * 10 + digit
```

Leading zeros need no special code. They leave the magnitude unchanged until a nonzero digit arrives. The loop ends at the first letter, sign, period, space, or end of string, so only the maximal consecutive digit prefix is used.

**Derive the pre-push overflow inequality**

Let `digit = int(str[i])`. A new positive magnitude would be

$$
10 \cdot \texttt{result} + \texttt{digit}.
$$

It fits the positive maximum `INT_MAX` exactly when

$$
10 \cdot \texttt{result} + \texttt{digit} \le \texttt{INT\_MAX}.
$$

Rearranging before performing the multiplication gives

$$
\texttt{result} \le \frac{\texttt{INT\_MAX} - \texttt{digit}}{10}.
$$

The implementation tests the negation:

```python
if result > (INT_MAX - int(str[i])) / 10:
```

If true, appending the digit would exceed the magnitude boundary, so the method immediately returns `INT_MAX` for a positive sign or `INT_MIN` for a negative sign. No overflowing integer multiplication occurs first.

In Python 3, `/` produces a floating-point value. The numbers involved are around $2.1 \times 10^8$, far below the range where an IEEE-754 double loses unit precision, so these particular comparisons are exact enough for every digit and 32-bit boundary. Integer division with an explicit equality/digit check would be more portable across languages and avoids introducing floating point into integer parsing.

**Why one magnitude threshold handles the asymmetric signed range**

The positive maximum is `2147483647`, while the negative minimum permits magnitude `2147483648`. The check is based on `INT_MAX`, so it treats a next digit `8` after prefix `214748364` as out of positive range.

For a negative sign, returning `INT_MIN` at that moment is correct both when the exact mathematical value is `-2147483648` and when further digits would make it even smaller. The parser is allowed to clamp as soon as the boundary outcome is determined; it does not need to construct the exact oversized magnitude.

**Trace `"   -042rest"`**

1. `i` advances over three whitespace characters.
2. The minus sign sets `sign = -1` and advances `i` once.
3. Digit `0` leaves `result = 0`.
4. Digit `4` makes `result = 4`.
5. Digit `2` makes `result = 42`.
6. Character `r` fails the ASCII digit condition, so scanning stops.
7. `sign * result` returns `-42`; `"rest"` is ignored.

At every successful digit iteration, `result` equals the value of exactly the consumed digit prefix. The overflow inequality proves the next update is safe before it occurs. On normal termination, applying `sign` gives the specified signed value. On an unsafe update, the immediate signed clamp is exactly the required outcome.

## Complexity detail

Let $n$ be the input length.

- **Time complexity: $O(n)$.** The whitespace phase and digit phase share one monotonically increasing index. No character is revisited, and sign processing is constant work. Early termination can scan less, while an all-digit string scans all $n$ characters.
- **Space complexity: $O(1)$.** The method stores fixed integer limits, an index, sign, result, and transient digit conversions. It allocates no prefix substring, list, regex match collection, or recursion stack.

The overflow branch may return before consuming the rest of a long digit run. Once clamping is inevitable, later digits cannot change which signed boundary must be returned.

## Alternatives and edge cases

- **Integer threshold with quotient and remainder:** Compare `result` with `INT_MAX // 10`, then compare the next digit with `7` on equality. This avoids floating point and is the conventional portable pre-push check.
- **Explicit DFA:** Represent start, sign, digit, and dead states. It scales well when a number grammar has more transitions, but direct phases are easier to read for this small contract.
- **Regular-expression prefix extraction:** This can identify the prefix concisely but still needs overflow-safe conversion and introduces an unnecessary parsing dependency.
- **Wider integer then clamp:** Simple in Python but does not honor a strict no-wider-integer assumption. This method determines overflow before the push.
- **Empty input:** Returns the initialized zero immediately.
- **All whitespace:** The bounded skip reaches the end and returns zero.
- **Only a sign:** The digit loop is skipped and signed zero is returned.
- **Multiple signs:** Only the first can be consumed; the next is a non-digit terminator, yielding zero if no digit preceded it.
- **Leading zeros:** They are accumulated mathematically and disappear from the integer representation.
- **Letter before any digit:** The digit loop never starts, so the result is zero.
- **Letter, period, sign, or space after digits:** It terminates conversion, and all later characters are ignored.
- **Positive overflow:** Returns `2147483647` before the unsafe decimal append.
- **Exact negative minimum:** The same magnitude threshold triggers and returns `-2147483648`, which is the exact legal result.
- **Negative underflow:** It also returns `-2147483648`, now as a clamp.
- **Whitespace definition:** `isspace()` is broader than required, but the legal alphabet supplies only ordinary spaces. If arbitrary input were allowed, this would be an intentional grammar choice to revisit.
- **Built-in shadowing:** Naming the parameter `str` does not break this code, but a clearer name such as `s` would preserve access to the built-in type and improve readability.
