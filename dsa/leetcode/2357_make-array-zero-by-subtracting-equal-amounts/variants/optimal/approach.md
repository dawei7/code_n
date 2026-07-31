## General

**Track value levels, not array states.** Consider the distinct positive
values in sorted order:

$$
0 < v_1 < v_2 < \cdots < v_d.
$$

Choosing `x = v_1` removes the smallest level. Every larger positive value is
reduced by the same amount, so the remaining distinct positive levels become
$v_2-v_1,\ldots,v_d-v_1$: there are exactly $d-1$ of them. Repeating this
choice removes one level per operation, proving that $d$ operations are
sufficient.

**Why fewer operations cannot work.** During one operation, two unequal
positive entries both lose the same `x`, so their difference is unchanged
while both stay positive. Consequently, one subtraction cannot make two
different positive levels reach zero simultaneously: only entries at the
current smallest level can become zero. Each of the original $d$ positive
levels therefore requires a separate operation, giving a matching lower bound.

The minimum operation count is thus exactly the number of distinct positive
values. Build a set from `nums`, ignore zero, and return its remaining size;
the physical subtraction process never needs to be simulated.

## Complexity detail

Scanning $n$ elements and inserting them into a hash set takes $O(n)$ expected
time. The set may contain $n$ distinct values, so it uses $O(n)$ auxiliary
space. Because the legal values lie between 0 and 100, a fixed boolean array
can alternatively make the auxiliary space $O(1)$ with respect to $n$.

## Alternatives and edge cases

- **Repeated subtraction simulation:** Always choosing the current smallest
  positive value is correct, but rescanning and rewriting the array for every
  distinct level can take $O(n^2)$ time over the legal domain.
- **Sort and count changes:** Sorting the positive values and counting adjacent
  changes also works, but costs $O(n\log n)$ time.
- **Fixed presence array:** Marking values 1 through 100 avoids hashing and
  uses constant domain-sized storage.
- **Zeros:** Zero is never a selectable positive level and contributes nothing
  to the answer.
- **Duplicates:** All occurrences of one positive value reach zero in the same
  operation, so multiplicity does not increase the count.
- **Input order:** Only the set of positive magnitudes matters; their positions
  are irrelevant.
