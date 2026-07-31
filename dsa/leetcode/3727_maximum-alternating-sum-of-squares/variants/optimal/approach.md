## General

**Separate positions by their coefficient**

Squaring removes each input value's original sign. Therefore, only the squared magnitudes and the signs assigned by their final indices matter. For $n$ elements, exactly $\lfloor n/2 \rfloor$ squares receive a negative coefficient and the remaining $\lceil n/2 \rceil$ receive a positive coefficient.

**Why the smallest squares belong to negative positions**

Suppose a positive position contains a square $a$ while a negative position contains a larger square $b$. Their current contribution is $a-b$. Swapping the two contributions changes it to $b-a$, an increase of $2(b-a) > 0$. Any arrangement with such an inverted pair is therefore not maximal.

It follows that every square assigned a negative coefficient must be no larger than every square assigned a positive coefficient. Sort all squares in non-decreasing order, subtract the first $\lfloor n/2 \rfloor$, and add the rest. The particular order within either group is irrelevant, so the maximizing permutation itself does not need to be constructed.

## Complexity detail

Let $n$ be the length of `nums`. Forming the squares takes $O(n)$ time, sorting them takes $O(n \log n)$ time, and summing the two groups takes $O(n)$ time. The total time is therefore $O(n \log n)$. The list of squares uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Sort by absolute value:** Sorting the original elements by magnitude produces the same grouping, but the score must still be accumulated from squared values.
- **Two heaps:** Keeping the smallest $\lfloor n/2 \rfloor$ squares in one heap can also identify the negative group in $O(n \log n)$ time, with more bookkeeping than a direct sort.
- **Magnitude frequencies:** Because $\lvert\texttt{nums}[i]\rvert \leq 40000$, a frequency array can scan magnitudes in $O(n + M)$ time and $O(M)$ space for $M=40001$; that optimization depends on the fixed value bound.
- **Negative inputs:** An input value and its negation have the same square, so their original signs are immaterial.
- **Equal magnitudes:** Tied squares may be placed on either kind of position without changing the maximum.
- **One element:** There is no subtracted position, so the result is simply that element's square.
- **All zeros:** Every permutation has score zero.
