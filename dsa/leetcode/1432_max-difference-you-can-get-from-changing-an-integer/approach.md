## General

**Maximize one independent result and minimize the other**

The two replacement operations are applied independently to the original number. Therefore, maximizing $a-b$ separates into:

- Make `a` as large as any legal single all-occurrences replacement can make it.
- Make `b` as small as any legal replacement can make it without a leading zero or a zero result.

The code stores two independent decimal strings:

```python
a, b = str(num), str(num)
```

Changing `a` never changes `b`, which matches the problem's independent operations.

**Why the earliest changed digit dominates**

Decimal place values decrease from left to right. Improving the first position where two candidate numbers differ has more effect than every possible change to later positions combined.

For example, increasing the thousands digit by one adds 1000, while all three later digits together can change by at most 999. Thus both the maximum and minimum strategies should make the best legal replacement involving the earliest digit that can improve the number.

Because one chosen digit must be replaced at all its occurrences, the algorithm selects which original digit to change based on its first relevant appearance, then uses `replace` globally.

**Construct the largest possible result**

The loop scans `a` from most significant digit to least:

```python
for c in a:
    if c != "9":
        a = a.replace(c, "9")
        break
```

A digit already equal to 9 cannot be increased. The first digit that is not 9 is the earliest improvable position. Replacing its digit value with 9 gives the largest possible value at that decisive position. Every later occurrence of the same digit must also be replaced under the operation rule, and changing it to 9 can only further increase the result.

Choosing a later original digit would leave this earlier non-9 position unchanged and produce a smaller number. Choosing a replacement below 9 would also be smaller at the first changed position.

If every digit is already 9, no replacement can increase the number. The loop performs no change, which is legal because the selected replacement digits may be equal.

**Minimize when the leading digit is not one**

If `b[0] != "1"`, the leading digit is between 2 and 9 because the original positive integer has no leading zero. The smallest legal leading digit is 1:

```python
b = b.replace(b[0], "1")
```

Replacing it with zero would create a forbidden leading zero. Replacing it with any digit above one would be larger. The global replacement also changes later occurrences of that original leading digit to one, which cannot make the result worse than using a larger replacement.

This is optimal because the most significant digit is decreased as far as legality permits. No operation that leaves it unchanged can compensate through later positions.

**Minimize when the leading digit is already one**

When `b[0] == "1"`, replacing digit 1 with zero is illegal because it changes the leading one. Replacing it with another nonzero digit cannot reduce it below one. Therefore, all occurrences of digit 1 must effectively be left alone in an optimal reduction.

The code scans the remaining suffix for:

```python
if c not in "01":
```

Zeros are already the smallest digit and cannot be reduced. Ones cannot be replaced with zero because the same replacement would affect the leading one. The first digit that is neither zero nor one is therefore the earliest legally reducible digit.

Replacing all its occurrences with zero makes that decisive position as small as possible:

```python
b = b.replace(c, "0")
```

If the suffix consists only of zeroes and ones, no legal operation can reduce `b`, so it remains unchanged.

**Trace `num = 9288`**

For the maximum, the first non-9 digit is 2. Replacing every 2 with 9 gives `a = 9988`.

For the minimum, the leading digit 9 is not one. Replacing every 9 with 1 gives `b = 1288`. The difference is 8700.

Changing digit 2 or 8 for the minimum would leave the leading 9 and therefore could not beat a number beginning with 1.

**Trace a leading-one case**

For `num = 110105`, the maximum replaces the first non-9 digit, which is 1, with 9, giving `990905`.

For the minimum, the leading one cannot be changed to zero. The suffix scan skips another 1, zero, and another 1; the first reducible digit is 5. Replacing all 5s with zero gives `110100`.

**Why the difference is globally maximal**

The maximum construction chooses the best possible first changed position and replacement digit for `a`. The minimum construction handles the only leading-zero restriction and chooses the earliest legally reducible digit for `b`, with the smallest legal replacement.

Because the two operations do not constrain each other, combining the independently largest `a` and smallest `b` maximizes `a-b`. Converting the strings back to integers and subtracting returns that value.

## Complexity detail

Let $d$ be the number of decimal digits. Each scan visits at most $d$ characters. Python's `str.replace` also scans and creates a length-$d$ string, and integer conversion is linear in the digit count. Total time is $O(d)$.

The two decimal strings and replacement results use $O(d)$ space, matching the manifest. Since `num <= 10^8`, $d$ is small in this problem, but the analysis treats it as variable.

## Alternatives and edge cases

- **Enumerate all digit replacements:** Try every original and replacement digit pair, reject leading-zero results, and retain maximum and minimum. It is correct but obscures the place-value greedy insight.
- **Arithmetic digit manipulation:** Compute place values without strings. It avoids string methods but makes replacing every equal digit more verbose.
- **All nines:** The maximum result is unchanged because no digit can increase.
- **Single digit nine:** Maximum is 9, minimum is 1, and the difference is 8.
- **Leading digit already one:** It cannot be changed to zero, so minimization searches the suffix.
- **Suffix contains only zero and one:** No legal replacement can reduce the number further.
- **Repeated chosen digit:** Every occurrence must change; `replace` enforces this rule exactly.
- **Replacement digit equals original:** This permits leaving an already optimal maximum or minimum unchanged.
- **No leading zero:** The minimum uses 1 for a changed leading digit and never replaces a leading one with zero.
- **Independent operations:** The digit choice used for `a` has no effect on which digit may be chosen for `b`.
