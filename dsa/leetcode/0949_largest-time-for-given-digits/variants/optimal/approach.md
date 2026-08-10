## General

**Search times in the order the answer wants**

There are only 24 possible hours and 60 possible minutes, for 1,440 valid 24-hour times. This domain size is fixed, independent of input values.

Instead of generating arrangements and later comparing them, the solution enumerates valid times from latest to earliest:

- hours from `23` down to `0`;
- for each hour, minutes from `59` down to `0`.

The first time whose four digits exactly match the supplied multiset is necessarily the latest constructible time.

**Represent duplicate digits correctly**

The input may contain repeated digits, so a set is insufficient. For example, `[1, 1, 2, 3]` must distinguish two copies of one from one copy.

Array `cnt` has ten positions. For each input digit `v`, `cnt[v]` increases. It is a frequency signature of the four available digits.

For each candidate time, a new ten-entry array `t` counts:

- `h // 10`, the hour tens digit;
- `h % 10`, the hour ones digit;
- `m // 10`, the minute tens digit;
- `m % 10`, the minute ones digit.

The condition `cnt == t` means every digit occurs exactly the same number of times in the candidate and input. This simultaneously proves that every input digit is used and no digit is reused too many times.

**Why integer division preserves leading zeros**

For hour five, `h // 10` is zero and `h % 10` is five, so the candidate contributes digits zero and five. Similarly, minute seven contributes zero and seven.

Thus `05:07` is treated as the four digits `0, 5, 0, 7` even though the numeric variables are merely five and seven. Leading zeros are not lost from the frequency check.

**Why the first match is optimal**

The nested loop order is chronological descending order. Every time examined before candidate `h:m` is later:

- a greater hour is later regardless of minute;
- within the same hour, a greater minute is later.

Therefore, once a candidate matches `cnt`, no unexamined candidate can be later. The function can return immediately.

There is also no need to compare formatted strings. The loop structure already establishes the order numerically.

**Formatting the answer**

The expression `f'{h:02}:{m:02}'` prints both numbers with at least two digits, inserting a leading zero when needed.

This produces exactly `HH:MM`:

- hour five becomes `05`;
- minute seven becomes `07`;
- the colon is inserted between them.

The frequency test and output formatting agree about leading zeros.

**Trace with a valid answer**

For digits `[1, 2, 3, 4]`, the search rejects every time from `23:59` downward until `23:41`. Its digit count contains one each of one, two, three, and four, so it matches and is returned.

Although other valid arrangements such as `21:43` exist, they occur later in the descending search and are chronologically earlier.

For `[5, 5, 5, 5]`, no valid hour can use two fives because hours stop at 23. Every candidate count differs, both loops finish, and the function returns an empty string.

**Why the method is correct**

Every returned candidate is a valid time because the loops enumerate only hours 0 through 23 and minutes 0 through 59. Frequency equality proves that it uses the input digits exactly once.

Because candidates are visited from latest to earliest, the returned first match is at least as late as every other constructible time. If no match is found among all 1,440 valid times, no valid time can be made from the digits, so the empty string is correct.

## Complexity detail

The loops always examine at most `24 * 60 = 1440` candidates. Each candidate performs a constant number of digit operations and compares two fixed ten-entry arrays. Since the input always contains exactly four digits and the search domain never grows, time is `O(1)`.

The two frequency arrays each have length ten, so auxiliary space is `O(1)`.

The constant 1,440 is meaningful in practice but does not become a variable asymptotic factor.

## Alternatives and edge cases

- **Enumerate the 24 digit permutations:** Four positions have at most `4! = 24` arrangements. Validate each and keep the latest. This is also constant time, but duplicate permutations require care.
- **Backtracking with a used array:** It handles repeated positions explicitly but is more machinery than enumerating the small valid-time domain.
- **Greedily choose each digit:** A locally largest hour digit can make the remaining hour or minute invalid. Complete enumeration is safer.
- **Repeated digits:** Frequency arrays enforce exact multiplicity and avoid set-related mistakes.
- **Midnight:** Digits `0, 0, 0, 0` produce `00:00`, a valid answer rather than an empty string.
- **Leading-zero hour or minute:** Division and modulo count the zero, and two-digit formatting restores it visibly.
- **No valid arrangement:** Exhausting every valid time proves impossibility.
- **Several valid times:** Descending enumeration returns the latest without a separate maximum variable.
- **Exactly 24:00:** It is not a valid 24-hour representation under the contract; the hour loop correctly stops at 23.
- **Input order:** Only digit multiplicities matter, so the original array order has no effect.
