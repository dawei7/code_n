## General

**Put the smallest digits in the expensive positions**

Any solution using a three-digit number has a hundreds-place contribution,
while the four digits can always form two two-digit numbers. Moving that
hundreds-place digit into an available tens or ones place cannot increase the
sum, so an optimum can be represented by two two-digit numbers, with leading
zeros permitted.

Sort the digits as $a \le b \le c \le d$. Across two two-digit numbers, the
tens positions carry weight ten and the ones positions carry weight one.
Therefore the two smallest digits, $a$ and $b$, must occupy the tens positions;
otherwise swapping a smaller ones digit with a larger tens digit reduces the
sum.

The remaining digits $c$ and $d$ occupy the ones positions in either order.
The minimum sum is consequently

$$
10(a+b)+c+d.
$$

This construction uses every digit exactly once and the exchange argument
shows that no other placement can have a smaller positional contribution.

## Complexity detail

The contract always supplies exactly four digits. Extracting and sorting this
fixed collection takes $O(1)$ time and $O(1)$ auxiliary space. If generalized
to $d$ digits, comparison sorting would take $O(d\log d)$ time, but the legal
domain fixes $d=4$.

## Alternatives and edge cases

- **Enumerate permutations and splits:** Trying every digit order and each
  nonempty split is correct and useful as an independent oracle, but performs
  unnecessary repeated work.
- **Digit-frequency counting:** A ten-slot frequency array can recover the
  digits in sorted order without comparison sorting, though it is more verbose
  for four positions.
- Leading zeros are valid and should take the highest available place values.
- Repeated digits are distinct occurrences and must all be used.
- The input itself cannot contain a leading zero because it is a four-digit
  integer, but either constructed number may have one.
