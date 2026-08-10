## General

**The candidate domain is tiny**

The displayed time contributes at most four distinct digits. Digits may be reused without limit, so every candidate display is a four-character choice from that set.

There are at most:

`4 * 4 * 4 * 4 = 256`

digit strings. Exhaustively generating them is simpler and safer than trying to greedily change one clock position without considering hour and minute validity.

**Collect allowed digits**

`s = {c for c in time if c != ":"}` removes the colon and deduplicates the display digits.

Using a set means DFS iteration order is unspecified, but the algorithm compares every valid candidate numerically and retains the closest, so generation order does not affect the result.

**Generate four positions recursively**

`dfs(curr)` appends every allowed digit until `curr` has length four. Reuse happens naturally because each recursive level iterates over the full set `s` again.

The four generated positions represent:

- hour tens;
- hour units;
- minute tens;
- minute units.

Leading zero characters remain in `curr`, so displays such as `"01:05"` are preserved correctly when formatting the answer.

**Reject invalid clock displays**

At length four, `check(curr)` parses:

- `curr[:2]` as hours;
- `curr[2:]` as minutes.

A candidate is valid only when hours are from zero through 23 and minutes from zero through 59.

This validation is necessary because allowed digits can form strings such as `"29:99"` that are not real 24-hour times.

**Compare candidates in minutes**

The input time is converted to minutes after midnight:

`t = hours * 60 + minutes`.

Each valid candidate becomes `p` in the same way. The exact search considers candidates satisfying `p > t`, meaning later on the same day.

`d` stores the smallest positive same-day difference found. The condition:

`t < p < t + d`

means that `p` is later than the input and closer than the current best. On improvement, update `d = p - t` and build `ans` by inserting a colon into `curr`.

The original display itself has `p == t` and is deliberately ignored; “next” requires positive elapsed time.

**Why same-day candidates can be considered first**

Any valid candidate later on the same day occurs before every candidate after midnight on the following day. Therefore, if at least one `p > t` exists, the smallest such `p` is globally the next time and wraparound candidates cannot beat it.

This justifies choosing among same-day times without applying modulo during DFS.

**Handle midnight wraparound**

If no later same-day candidate exists, `ans` remains `None`. The next valid time must occur on the following day.

Among all displays made from the allowed digits, the numerically earliest valid time is obtained by repeating the smallest allowed digit in all four positions:

`mimi:mimi`.

Why is it valid? Every valid input hour has a first digit at most two, so the minimum allowed digit is at most two. Repeating zero, one, or two forms hour `00`, `11`, or `22`, all valid; the repeated minute is also at most 22 and valid.

It is the earliest because every other allowed four-digit string has some first differing position containing a digit no smaller than this minimum.

For `"23:59"`, the minimum available digit is two, so fallback gives `"22:22"` on the next day.

**A same-day example**

For `"19:34"`, allowed digits are one, nine, three, and four. DFS generates all arrangements and filters invalid ones.

`"19:39"` is valid and five minutes later. A display such as `"19:33"` is numerically earlier, so it belongs to the next day's cycle and is much farther away. The best same-day comparison correctly selects `"19:39"`.

**Why the method is correct**

DFS enumerates every four-digit display constructible from the input digits because each position independently tries every allowed choice. `check` retains exactly valid 24-hour times.

If any valid time is later on the same day, minimizing `p - t` finds the earliest forward occurrence. If none exists, every constructible valid display occurs only after wraparound; the smallest numeric display is then the first reached after midnight, and the repeated minimum produces it.

Thus the returned display is always the closest strictly future occurrence.

## Complexity detail

Let `A` be the number of distinct allowed digits. The search generates `A^4` leaves and a bounded number of internal recursion nodes. Since `A <= 4` and the display always has four digits, this is at most 256 candidates and is `O(1)` under the fixed clock domain.

The allowed set has at most four entries, recursion depth is four, and only scalar candidate data is stored. Auxiliary space is `O(1)`.

If generalized to arbitrary display length `L`, enumeration would be exponential `O(A^L)`, but neither `A` nor `L` grows in this problem.

## Alternatives and edge cases

- **Minute-by-minute simulation:** Advance from the input one minute at a time modulo 1440 and return the first display using only allowed digits. At most 1440 checks still give `O(1)` time.

- **Cartesian product utility:** Generate the four positions with a standard product iterator rather than recursion. The candidate set and proof are identical.

- **Greedily increment the last digit:** Clock validity and carry behavior can require changing earlier positions, making a direct greedy implementation error-prone.

- **All four input digits identical:** No different same-day display exists. Fallback returns the same display, representing its occurrence 24 hours later.

- **Time near midnight:** If no valid later minute exists, fallback correctly wraps to the next day.

- **Leading zero:** Candidate strings retain character positions, so `00` through `09` hours format correctly.

- **Invalid generated hour:** `check` rejects values 24 or above even if all digits are allowed.

- **Invalid generated minute:** Values 60 or above are likewise rejected.

- **Repeated digit use:** Every recursion level iterates the same set, so a digit may appear more times than in the input, as allowed.

- **Current time candidate:** Strict `p > t` excludes zero elapsed time.

- **Unordered digit set:** Best-distance comparison makes traversal order irrelevant.

- **Fallback validity:** The smallest allowed digit is guaranteed at most two by the valid input's hour tens digit, so repeating it always forms a legal time.

- **Same-day versus next-day candidate:** Any later same-day time is closer than any wrapped time; the two-phase logic relies on this clock ordering.
