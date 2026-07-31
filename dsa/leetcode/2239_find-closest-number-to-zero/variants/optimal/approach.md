## General

**Order candidates by distance and value**

Initialize the answer with the first array element. For each later value,
replace the current answer when the new absolute value is smaller. If the
absolute values are equal, replace it only when the new numeric value is
larger. These are exactly the problem's primary and secondary comparison keys.

After processing any prefix, the retained value is closest to zero within that
prefix, with the largest value retained among distance ties. The next
comparison preserves this property whether the new element is better, tied, or
worse. Once the complete array has been processed, the retained value is
therefore the required global choice.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm examines every element once,
using $O(n)$ time. It retains one current value and uses $O(1)$ auxiliary
space.

## Alternatives and edge cases

- **Sort by comparison key:** Sorting by absolute value and then by descending numeric value is correct but costs $O(n\log n)$ time and may allocate additional storage.
- **Repeated candidate verification:** Checking every candidate against every other value is correct but takes $O(n^2)$ time.
- **Opposite values:** If both $-x$ and $x$ attain the minimum distance, return the positive value $x$.
- **Zero present:** Zero has distance zero and is necessarily the answer.
- **All negative:** Choose the negative value with the smallest magnitude, which is also the numerically largest among an equal-magnitude tie.
- **Duplicates:** Repeated copies do not change the selected value.
- **One element:** The sole array value is returned.
