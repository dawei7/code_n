## General
**Parse one strict prefix grammar**

The valid portion is not an arbitrary integer hidden somewhere in the string. It has this ordered form:

```text
leading spaces -> optional single sign -> consecutive decimal digits
```

Use one index and move through those phases exactly once. First skip only leading space characters allowed by the contract. Then consume at most one `+` or `-`. Finally consume ASCII digits until the first nondigit. Characters after that stopping point are irrelevant.

The ordering explains several easily confused cases:

- `"   -42abc"` parses as `-42`.
- `"words 42"` returns `0`; parsing cannot search ahead after an invalid first non-space character.
- `"+-12"` returns `0`; after consuming `+`, the `-` is not a digit.
- `"  00017-5"` parses as `17`; the later sign terminates the digit phase.

If no digit follows the optional sign, the accumulated magnitude remains zero, which is the required result.

**Accumulate the magnitude without building a substring**

For each digit `digit`, appending it to the current magnitude `value` would calculate:

```text
value * 10 + digit
```

Leading zeroes require no special case: appending them to zero leaves the magnitude unchanged. Stopping as soon as a nondigit appears ensures `value` always represents exactly the consecutive digit prefix, never later digits elsewhere in the string.

**Clamp safely before multiplication**

Choose a sign-specific magnitude limit. A positive result may be at most $2^{31} - 1$, while a negative result may have magnitude $2^{31}$. Before appending a digit, test:

```text
value > (limit - digit) // 10
```

If true, `value * 10 + digit` would exceed the selected limit. The exact remaining digits no longer matter: additional decimal digits cannot reduce a nonnegative magnitude. Return $2^{31} - 1$ for a positive sign or $-2^{31}$ for a negative sign immediately.

Performing this comparison first is important in fixed-width languages, where calculating an overflowing intermediate and clamping it afterward is not reliable.

**Trace the phases on a representative input**

For `"   -042x"`, the index first skips three spaces. The sign phase records `-1`. The digit phase consumes `0`, `4`, and `2`, producing magnitudes `0`, `4`, and `42`. The `x` ends parsing, and applying the stored sign returns `-42`.

Notice that parsing does not need to consume the rest of the string after `x`; the contract is determined entirely by the valid initial prefix.

**Why the consumed prefix is exactly the parsed integer**

After skipping leading spaces and consuming at most one sign, the index is either at the first decimal digit or at a character proving that the valid numeric prefix is empty. During the digit phase, `value` is exactly the magnitude denoted by the consumed consecutive digits; multiplying by ten and adding the next digit preserves that meaning.

The first nondigit ends the only grammar phase in which digits are legal, so ignoring the remaining suffix matches the contract rather than losing valid input. Before every append, the sign-specific inequality proves either that the new magnitude remains representable or that the mathematical value has crossed the required clamp boundary. Consequently the normal exit returns precisely the accepted prefix with its sign, while the early exit returns exactly the mandated 32-bit limit.

## Complexity detail
The index advances monotonically and examines each relevant character at most once, so the worst-case time is $O(n)$. Parsing stops early when a nondigit or guaranteed overflow is found. Only the index, sign, magnitude, limit, and current digit are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- A built-in integer parser often rejects trailing text, accepts a different whitespace or sign grammar, or throws on overflow, so it does not directly implement this contract.
- A regular expression can extract the prefix, but it adds machinery, may allocate a matched substring, and still needs explicit clamping.
- Building a digit substring before conversion uses $O(n)$ additional space; direct accumulation does not.
- Empty strings, strings containing only spaces, a sign without digits, or a prefix beginning with an invalid character all return `0`.
- Leading zeroes do not change the value. Parsing stops at decimal points, letters, embedded spaces, and second signs rather than rounding or resuming later.
- The negative magnitude limit is one larger than the positive limit because the signed 32-bit interval is asymmetric.
