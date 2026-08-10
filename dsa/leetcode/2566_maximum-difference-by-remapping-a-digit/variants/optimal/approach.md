## General

**A remapping changes every occurrence**

Choosing source digit $a$ and destination digit $b$ replaces all occurrences of $a$ in the decimal numeral, not just one position. The remapping used for the maximum may differ from the one used for the minimum, so the two extremes can be optimized independently.

The solution converts `num` to string `s`. String replacement naturally applies a mapping to every occurrence of one digit. Because leading zeros are allowed, the resulting string may begin with zero; converting it with `int` correctly interprets those zeros as having no numeric value.

**Construct the smallest possible value**

The most significant digit `s[0]` is nonzero because `num` is a normal positive integer. Replacing that digit with `'0'` creates the largest possible decrease at the earliest decimal position. The code computes

`mi = int(s.replace(s[0], '0'))`.

Why is this globally minimal? Suppose a different source digit first appears at position $p>0$. Any decrease produced by changing it begins at a less significant position, while the original leading digit remains unchanged. Replacing the leading digit with zero lowers the number at the very first position, which dominates every possible combination of changes in later positions.

Among mappings of the leading digit, zero is the smallest destination. Replacing all later occurrences of that same digit with zero can only decrease the value further. Therefore this one replacement gives the minimum.

For `num = 11891`, replacing all ones with zero produces string `"00890"`, interpreted as $890$.

**Construct the largest possible value**

To maximize the number, scan from left to right for the first digit that is not nine. Call it $c$. Replacing every occurrence of $c$ with nine makes the earliest improvable position as large as possible:

`s.replace(c, '9')`.

All earlier digits are already nine and cannot be increased. Any remapping whose first changed position comes later leaves digit $c$ smaller than nine at this earliest point, so its result is smaller regardless of later digits. Once $c$ is chosen, nine is the greatest destination digit, and replacing every later occurrence of $c$ with nine can only help.

The function returns immediately when it finds this first non-nine digit, calculating the maximum value minus `mi`.

For `11891`, the first non-nine digit is `'1'`. Replacing every one by nine gives `99899`. Subtracting $890$ yields $99009$.

**Why the all-nine case is different**

If every character in `s` is `'9'`, no digit can be increased. The rules still require exactly one remapping, but remapping nine to itself is explicitly permitted. Therefore the maximum remains `num`.

The loop finishes without an early return, and the final statement `return num - mi` handles precisely this case.

The minimum still replaces the leading nine, which means every nine, with zero. For `99`, `mi` is zero and the maximum is $99$, so the difference is $99$.

**Why optimizing each endpoint separately is valid**

The requested result is

$$
\max(\text{obtainable value})-\min(\text{obtainable value}).
$$

The problem explicitly allows different remappings for those two values. Making the maximum as large as possible and the minimum as small as possible independently therefore maximizes their difference. There is no requirement that a single digit mapping produce both endpoints.

**Place-value proof**

Decimal numbers are compared lexicographically when they have the same digit length, including leading zeros as padded positions. At the first position where two candidate strings differ, the one with the larger digit has the larger numeric value; later positions cannot compensate for a one-unit difference at that place because all later digits together are worth less than one unit of the earlier place.

The minimum rule changes the earliest possible position to the smallest digit. The maximum rule changes the earliest position that can improve to the largest digit. This first-difference property is the core greedy proof.

Remapping a digit to itself satisfies the “exactly one” rule when no beneficial change is needed. The code relies on this for an all-nine maximum; the minimum always has a beneficial leading-digit-to-zero mapping because the original leading digit is nonzero.

## Complexity detail

Let $d$ be the number of decimal digits in `num`. Converting to a string takes $O(d)$ time and space. Replacing the leading digit scans the string once. Finding the first non-nine digit scans at most $d$ positions, and the maximum replacement performs another $O(d)$ scan. Integer parsing is also $O(d)$.

These sequential passes give $O(d)$ total time and $O(d)$ auxiliary space for the strings, matching the manifest. Since `num <= 10^8`, $d$ is at most nine, but the symbolic bound describes the method clearly.

## Alternatives and edge cases

- **Try every source and destination digit:** Testing all 100 mappings for each endpoint is still constant in digit-alphabet size, but it repeats full scans and hides the simple place-value greedy rule.
- **Arithmetic digit rebuilding:** Digits can be extracted and reconstructed numerically, but string replacement expresses “all occurrences” more directly.
- **All digits are nine:** The maximum cannot increase; remapping nine to itself keeps `num` valid under the exactly-one-remapping rule.
- **Leading zeros in the minimum:** They are explicitly allowed, and `int` discards them naturally when computing the numeric value.
- **Repeated leading digit:** Every occurrence is replaced, so later copies become zero in the minimum as required.
- **First digit already nine for maximum:** The scan skips it and improves the first later non-nine digit.
- **Single-digit number:** A digit below nine can become nine for the maximum and zero for the minimum; digit nine keeps nine as its maximum.
- **Digit absent from the number:** Remapping an absent digit changes nothing and is allowed conceptually, but it cannot beat the greedy maximum or minimum.
- **Different mappings:** The maximum and minimum constructions intentionally choose source digits independently.
