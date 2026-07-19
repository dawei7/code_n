## General
**Normalize January and February.** Zeller's congruence treats March as the first month of its arithmetic year. When the input month is January or February, add `12` to the month and subtract `1` from the year. Thus those months become months `13` and `14` of the preceding year, placing the leap-day adjustment at the end of the transformed year.

**Separate century and year components.** Let $c=\lfloor y/100\rfloor$ be the century and let $r=y\bmod100$ be the year within that century after normalization. For normalized month $m$ and day $d$, compute

$$
w=\left(\left\lfloor\frac{c}{4}\right\rfloor-2c+r+
\left\lfloor\frac{r}{4}\right\rfloor+
\left\lfloor\frac{13(m+1)}{5}\right\rfloor+d-1\right)\bmod7.
$$

The century and quarter-year terms account for ordinary and leap years, while the month term accounts for the varying month lengths. The residue $w$ uses `0` for Sunday through `6` for Saturday, so it directly indexes the required weekday-name list. Python's nonnegative modulo result also removes any concern about a negative intermediate sum.

## Complexity detail
The calculation uses a fixed number of integer divisions, additions, multiplications, and one seven-element lookup, regardless of the date. It therefore takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Count forward from January 1, 1971:** Advancing one valid date at a time is easy to verify against the given Friday anchor, but its work grows with the number of elapsed days.
- **Standard-library calendar type:** A date library is concise, but the arithmetic method is portable to environments where such a type or formatter is unavailable.
- **Leap-year February:** Years divisible by `400` are leap years; years divisible by `100` but not `400` are not, which distinguishes `2000` from `2100`.
- **January and February:** They must be reassigned to months `13` and `14` of the previous year before applying the congruence.
- **Boundary years:** Both `1971` and `2100` are included in the valid range.
- **Negative intermediate value:** Apply modulo after the entire congruence so the final weekday residue is normalized into $0$ through $6$.
