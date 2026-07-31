## General

**Enumerate the normalized minute field**

After padding, an entry represents a pair `(minutes, seconds)` with both values
between $0$ and $99$. For any chosen `minutes`, the only possible matching
second field is

$$
\textit{seconds}=\texttt{targetSeconds}-60\cdot\textit{minutes}.
$$

Inspect all 100 minute values and retain a pair exactly when its derived
`seconds` lies from $0$ through $99$. This enumerates every valid
representation of the target, including forms such as 9 minutes and 60
seconds.

**Evaluate the digits that actually need pressing**

Format a retained pair as four digits and remove its leading zeros. Pressing
those zeros can never help: deleting a leading zero removes a positive press
cost and cannot add a movement that the longer entry avoided. Because the
target is positive, at least one digit remains.

Walk through the remaining digits from `startAt`. Each digit adds `pushCost`;
when it differs from the finger's current digit, first add `moveCost` and
update the finger position. The minimum cost over all retained pairs is the
answer. Every feasible entry has been considered in its cheapest
leading-zero-free form, so choosing the least evaluated cost is optimal.

## Complexity detail

The source contract fixes the minute field to 100 possible values and every
entry to at most four digits. The enumeration and cost evaluation therefore
take $O(1)$ time and $O(1)$ auxiliary space. The bounded-domain certificate
records this fixed workload explicitly instead of presenting a misleading
runtime-scaling measurement.

## Alternatives and edge cases

- **Check the quotient and one borrowed minute:** Starting from
  `targetSeconds // 60`, only that minute value and its predecessor can produce
  a second field at most 99. This is shorter but less directly mirrors the
  complete field domain.
- **Enumerate all digit strings:** Trying all entries from `1` through `9999`
  is a valid independent oracle, but repeats parsing work for thousands of
  irrelevant entries.
- A second field may exceed 59; `0960`, for example, is a legal normalized
  entry.
- Leading zeros are never pressed in an optimal entry, even though padding
  still determines which digits belong to the minute and second fields.
- Repeated equal digits incur a press cost each time but no movement between
  those presses.
- `targetSeconds = 6039` has the single normalized representation `9999`.
