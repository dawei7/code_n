## General

**Format before concatenating**

For each row, emit `+` for a positive factor and `-` for a negative one, then
append `ABS(factor)`. A `CASE` expression supplies the power-dependent tail:
an empty string for power zero, `X` for power one, and `X^power` for every
higher power.

Sort these complete term fragments by `power DESC` before aggregation.
Concatenating that ordered relation with an empty separator creates the entire
left-hand side, including the mandatory sign on its first term. Finally append
`=0` and expose the value as `equation`.

Every table row produces exactly one fragment with the specified sign,
magnitude, and power syntax. The ordered input to the aggregate places every
fragment in the required descending-power position, so their concatenation is
exactly the requested left-hand side. Appending the fixed suffix supplies the
right-hand side.

## Complexity detail

Formatting visits each of the $N$ rows once. Ordering by the unique power takes
$O(N\log N)$ time, and concatenation is linear in the output size. The ordered
rows and constructed equation require $O(N)$ space under the bounded term
widths.

## Alternatives and edge cases

- **Correlated rank per term:** Count how many rows have a greater power and
  order by that derived rank. It is correct but repeatedly scans `Terms`,
  taking $O(N^2)$ time.
- **Recursive concatenation:** Build the string one power at a time in a
  recursive CTE. This is more complex and repeatedly copies an expanding
  string.
- Power zero emits only the signed factor.
- Power one emits `X` but no exponent.
- Missing powers create no zero-factor placeholders.
- Positive leading terms still begin with `+`.
- `ABS(factor)` prevents a duplicated minus sign for negative factors.
