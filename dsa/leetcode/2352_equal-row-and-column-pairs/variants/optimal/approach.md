## General

Convert each row to a tuple and count how many times every row sequence occurs.
Then construct each column as a tuple. The number of rows equal to that column
is exactly the column tuple's frequency in the row map, so add that frequency
to the answer.

**Why frequencies preserve multiplicity**

Suppose a sequence occurs in $a$ rows and $b$ columns. Each of those rows can
pair with each of those columns, contributing $ab$ ordered pairs. Processing
the $b$ columns one at a time adds the stored row frequency $a$ each time and
therefore produces the same product. Summing this contribution over every
column counts every valid index pair exactly once.

Tuples preserve both value and order, so equality of tuple keys is precisely
the contract's row-column equality test. No hash key is based only on a sum or
another lossy summary.

## Complexity detail

Let $n$ be the grid dimension. Creating and hashing all row and column tuples
processes $n^2$ values, giving expected $O(n^2)$ time. At most $n$ distinct row
tuples of length $n$ are stored, so the auxiliary space is $O(n^2)$. Python's
dictionary operations use expected constant-time bucket access after the
$O(n)$ tuple hash is computed.

## Alternatives and edge cases

- **Direct row-column comparison:** Comparing every one of the $n^2$ pairs
  element by element is straightforward but takes $O(n^3)$ time.
- **Count both rows and columns:** Multiplying matching frequencies is also
  correct, but storing both maps is unnecessary because columns can be counted
  against the row map as they are built.
- **Duplicate sequences:** Repeated rows and columns must contribute all
  combinations, not merely one match per distinct tuple.
- **Single cell:** The sole row and sole column are identical, so the answer is
  1.
- **No equal sequence:** Every column lookup returns zero and the result is 0.
