## General

**Shrink a set of possible answers**

Start with a set containing every value from the first inner array. For each
later array, intersect the current set with that row. After processing any
prefix of rows, the set contains exactly the values present in every row of
that prefix: this is true initially, and intersection removes precisely the
values missing from the next row.

Consequently, after the last row the set is exactly the requested multi-array
intersection. Convert it to a list and sort it in ascending order to satisfy
the output contract. The promise that values within a row are distinct is not
needed by set intersection, but confirms that ordinary occurrence and
membership have the same meaning here.

## Complexity detail

Let

$$
T=\sum_{\texttt{row}\in\texttt{nums}}\lvert\texttt{row}\rvert
$$

be the total number of input elements, and let $r$ be the number of returned
values. Expected hash-set construction and intersections take $O(T)$ time,
and sorting the result takes $O(r\log r)$ time. Temporary sets and the
surviving intersection use at most $O(T)$ space.

## Alternatives and edge cases

- **Test each first-row value in every list:** This is correct, but linear list membership can make the work quadratic in the total input size.
- **Count occurrences globally:** Because each row has distinct values, a value with count equal to the number of rows is common to all; this is also linear before output ordering.
- **Sort every row and merge:** Multiway pointer scans work, but sorting all input rows performs more ordering work than sorting only the answer.
- **One inner array:** Every value in that row belongs to the intersection; return the row sorted.
- **Disjoint rows:** The maintained set becomes empty and the result is `[]`.
- **Different row orders:** Membership is independent of position, and only the final result must be ascending.
- **Early empty intersection:** Further intersections remain empty, though continuing is still correct.
