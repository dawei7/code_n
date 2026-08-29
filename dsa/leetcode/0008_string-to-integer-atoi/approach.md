## General

**Parsing rules are ordered phases, not independent character filters**

`myAtoi` does not search the whole string for characters that look useful. It reads a prefix from left to right under a strict order:

1. skip only leading space characters;
2. consume at most one optional sign;
3. consume one consecutive run of decimal digits;
4. stop permanently at the first non-digit after that point;
5. clamp the numerical result to the signed 32-bit range.

Once a phase ends, it never restarts. A space after digits is not skipped, a sign after a digit is not reconsidered, and digits after a letter are ignored. This is why `"1337c0d3"` becomes `1337` rather than `133703`, and `"0-1"` becomes `0` rather than `-1`.

**Handle empty input before indexing**

The method begins with

```python
if not s:
    return 0
```

An empty string has no digits, so zero is correct. More importantly, this guard makes the later access to `s[i]` safe.

The following check

```python
n = len(s)
if n == 0:
    return 0
```

is redundant because `not s` already covered exactly that case. It does not alter behavior; it simply repeats the same protection.

**Skip leading spaces without running past the end**

The loop

```python
while s[i] == ' ':
    i += 1
    if i == n:
        return 0
```

advances over ordinary space characters at the beginning. The bounds check occurs immediately after incrementing. If the string consists entirely of spaces, the method returns before the next loop condition can evaluate `s[n]`, which would be out of range.

The Reference names the exact leading whitespace character as `" "`, and the input alphabet contains no tabs or newlines, so comparing with `' '` matches the contract. A parser intended for broader text would need to decide deliberately whether other Unicode or ASCII whitespace should count.

Once the first non-space character is reached, later spaces are no longer skippable. They are non-digits that terminate conversion.

**Read one optional sign**

The code determines the sign from the current character:

```python
sign = -1 if s[i] == '-' else 1
```

Only `'-'` makes the result negative. A `'+'` or a digit leaves `sign = 1`. It then consumes exactly one sign character when present:

```python
if s[i] in ['-', '+']:
    i += 1
```

If the sign is the final character, the digit loop has no iterations and `sign * 0` returns zero. If another sign follows, such as in `"-+12"`, the second sign is not a digit, so conversion stops before reading any digit and also returns zero. This enforces the “at most one sign immediately after leading spaces” rule naturally.

**Build the magnitude one digit at a time**

The variable `res` stores a nonnegative magnitude. For a digit `c`, appending it in base ten is

```python
res = res * 10 + c
```

For the characters `"042"`, the values are `0`, `4`, and `42`. Leading zeros require no separate skip loop because multiplying zero by ten and adding zero leaves the value unchanged.

The digit scan is

```python
while i < n:
    if not s[i].isdigit():
        break
    ...
```

The index check comes first, so end-of-string termination is safe. The first non-digit breaks the loop, and nothing after it is examined. Under the Reference's input alphabet, every character accepted by `isdigit()` is one of `'0'` through `'9'`, so `int(s[i])` produces the intended decimal value. With unrestricted Unicode input, `isdigit()` can accept characters beyond ASCII and would require a more carefully specified conversion rule.

**Detect clamping before the dangerous decimal push**

The positive 32-bit maximum is

$$
M = 2^{31}-1 = 2147483647.
$$

The code stores

```python
flag = (2**31 - 1) // 10
```

so `flag = 214748364`. Before evaluating `res * 10 + c`, there are three cases:

- If `res < flag`, appending any digit `0` through `9` remains within the positive limit.
- If `res > flag`, appending even zero exceeds the limit.
- If `res == flag`, only a final digit at most `7` fits the positive limit.

That becomes

```python
if res > flag or (res == flag and c > 7):
```

The check happens before multiplication, so the method does not need an integer wider than the target range to discover overflow.

For a positive number, an unsafe push returns `2147483647`. For a negative sign, it returns `-2147483648`:

```python
return 2**31 - 1 if sign > 0 else -(2**31)
```

The negative range allows magnitude `2147483648`, one more than the positive maximum. The shared `c > 7` check intentionally treats that boundary digit `8` as a clamping event. Returning `INT_MIN` immediately is still the correct numerical result for exactly `"-2147483648"`, and it is also correct for every more-negative magnitude. Thus no separate “digit at most 8” construction branch is needed.

**Trace spaces, sign, zero, and digits together**

For `s = "   -042xyz"`:

| Phase | Reader position/content | State change |
|---|---|---|
| Leading spaces | skip three `' '` characters | `i` reaches `3` |
| Sign | read `'-'` | `sign = -1`, `i = 4` |
| First digit | read `'0'` | `res = 0` |
| Second digit | read `'4'` | `res = 4` |
| Third digit | read `'2'` | `res = 42` |
| Terminator | encounter `'x'` | break; ignore `"xyz"` |
| Return | apply sign | `-42` |

The parser never needs to materialize `"042"` as a substring. It maintains only the index, sign, and numerical prefix.

**Why the returned value follows every rule**

Before the digit loop, `i` points immediately after the only permitted leading spaces and optional sign. During the loop, `res` equals the base-10 value of exactly the digit prefix already consumed, with leading zeros naturally having no effect. The pre-push check either proves the next magnitude still fits or returns the required signed clamp.

The loop stops only at the string end or the first non-digit. Therefore it consumes the maximal allowed digit run and no later characters. Applying `sign` to an in-range magnitude produces the specified signed result; if no digit was consumed, that magnitude remains zero.

## Complexity detail

Let $n$ be `len(s)`.

- **Time complexity: $O(n)$.** The whitespace loop and digit loop advance the same index and never move it backward. Each character is inspected at most once, and every inspection performs constant-time work. The method may return early on all-space input or overflow, but the worst case scans the complete string.
- **Space complexity: $O(1)$.** The parser stores the length, index, sign, magnitude, threshold, and current digit. It creates no substring, character array, recursion chain, or input-sized state machine.

Since the Reference limits $n$ to `200`, the work is also absolutely bounded, but linear notation captures the parser's scaling behavior.

## Alternatives and edge cases

- **Deterministic finite automaton:** Model “start,” “sign seen,” “reading digits,” and “dead” as explicit states. This makes transition rules reusable and formal, but the small fixed sequence here is clearer with direct control flow.
- **Regular expression plus integer conversion:** A pattern can extract the allowed prefix, but it adds a parsing engine, still requires careful clamping, and may build a large intermediate integer unless overflow is checked separately.
- **Use a wider integer then clamp:** Easy in Python, but it does not honor a no-wider-integer environment. The pre-push threshold handles the limit portably.
- **Empty string:** The first guard returns zero before any indexing.
- **Only spaces:** The whitespace loop reaches `n` and returns zero without reading `s[n]`.
- **Only a sign:** The sign is consumed, no digit is read, and zero is returned.
- **Two signs:** The first is consumed as the optional sign; the second terminates the digit scan, so the result is zero.
- **Leading zeros:** They are processed normally and do not change `res`; `"-00042"` becomes `-42`.
- **Non-digit first character:** No whitespace or sign phase consumes it, the digit loop stops immediately, and zero is returned.
- **Non-digit after digits:** Conversion returns the completed prefix and ignores everything from that character onward.
- **Space after digits:** It is a terminator, not skippable whitespace, because only the initial phase ignores spaces.
- **Positive overflow:** The function returns `2147483647` before performing the unsafe push.
- **Negative boundary or underflow:** Both `"-2147483648"` and any smaller mathematical value return `-2147483648`; the former is an exact boundary, while the latter is clamped.
- **Plus sign:** It is consumed but leaves `sign = 1`.
- **Decimal point:** `'.'` is not a digit, so `"3.14"` parses as `3`; the function does not parse floating-point syntax.
