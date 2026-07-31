## General

**Compare each line with the required set**

Construct the set $\{1,2,\ldots,n\}$. For every index $i$, collect the values
in row $i$ and in column $i$. Both observed sets must equal the required set;
otherwise return false. If all $2n$ comparisons pass, return true.

Each line contains exactly $n$ values, and the contract restricts every value
to the interval from $1$ through $n$. Therefore a line's set equals the target
exactly when no value is duplicated. Checking every row and column proves the
condition in both directions.

## Complexity detail

The $n$ rows and $n$ columns contain $O(n^2)$ entries in total, so the time
complexity is $O(n^2)$. The target and one observed set contain at most $n$
values, requiring $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Search for every required number:** Testing membership by rescanning each
  row and column takes $O(n^3)$ time.
- **Boolean marker array:** Reuse an array of $n+1$ flags for each line. This
  has the same $O(n^2)$ time and $O(n)$ space.
- **Bit mask:** With the small value bound, each line can be represented as a
  bit mask, though arbitrary-width integers still encode $n$ bits.
- Rows being valid does not imply columns are valid, or vice versa.
- The single matrix `[[1]]` is valid.
