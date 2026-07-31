## General

**The sign determines the digit order**

For a negative input, minimizing the signed value means maximizing its positive
magnitude. Arrange every magnitude digit in non-increasing order, then restore
the minus sign. This order cannot begin with zero unless all digits are zero,
which is impossible for a negative input.

For a positive input, the magnitude should be lexicographically smallest.
Sorting digits in non-decreasing order achieves that except when zeros appear
first. Find the smallest nonzero digit and swap it with the first zero. The
result now has the least possible leading digit; placing all zeros immediately
after it and leaving the remaining digits ascending minimizes every subsequent
position.

Handle `num = 0` directly. In all other cases the construction uses the same
digit multiset, preserves the sign, avoids a leading zero, and is optimal at the
first position where any competing arrangement could differ.

## Complexity detail

Let $d$ be the number of decimal digits. Sorting takes $O(d\log d)$ time and
$O(d)$ space in the generalized problem. Under the actual contract,
$\lvert\texttt{num}\rvert\le 10^{15}$, so $d\le16$ and both bounds are $O(1)$.
The bounded-domain certificate records that fixed maximum instead of claiming
a runtime scaling trend over only a handful of digit lengths.

## Alternatives and edge cases

- **Digit-frequency counting:** Count occurrences in ten slots, then emit
  digits in the required order. This avoids comparison sorting and is an
  independent $O(d)$ generalized solution, but sorting at most 16 digits is
  simpler.
- **Enumerate permutations:** Trying every distinct digit order is correct as
  a small-input oracle, but grows factorially and repeats equivalent orders
  when digits are duplicated.
- `num = 0` must return `0`; there is no nonzero digit to move forward.
- Positive inputs with zeros require the smallest nonzero digit first, followed
  by every zero.
- Negative inputs sort magnitude digits descending because a larger magnitude
  produces a smaller signed value.
- Repeated digits must retain their exact multiplicities.
- The legal endpoints $\pm10^{15}$ contain 16 digits.
