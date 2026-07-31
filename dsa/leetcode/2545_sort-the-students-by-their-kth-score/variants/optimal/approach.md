## General

Each student must remain represented by one intact row, so the only choice is the order of those rows. The ranking value for a row is available directly as `row[k]`. Sort the rows with that value as the key and request descending order.

Because every integer in `score` is distinct, the selected column also contains distinct values. No tie-breaking rule is needed: comparing two selected scores determines exactly which student must appear first. A comparison sort places every larger key before every smaller key, which is precisely the required ranking while leaving every row's other exam scores attached to the same student.

The returned matrix may have a new outer list, but its elements are the original complete rows; copying the individual cells is unnecessary.

## Complexity detail

Let $m$ be the number of students. Comparison sorting takes $O(m \log m)$ time, and reading `row[k]` for a comparison is constant time. Python's `sorted` creates an output list of $m$ row references and may use linear temporary storage, so the auxiliary space is $O(m)$; the existing $m \times n$ matrix is input storage.

## Alternatives and edge cases

- **Repeated maximum selection:** Finding the best remaining row for every output position is correct but performs $O(m^2)$ comparisons.
- **Heap ordering:** Building a heap and removing every row also takes $O(m \log m)$ time, but it is more machinery than sorting when the entire order is required.
- **Copy and decorate rows:** Attaching a separate key to every row is unnecessary because `row[k]` is directly accessible; it also adds avoidable storage and reconstruction work.
- **Single student:** With $m = 1$, sorting returns the only row unchanged.
- **Single exam:** With $n = 1$, each row still moves as a complete one-element student record.
- **Target column boundaries:** Both `k = 0` and `k = n - 1` use the same key rule.
- **Distinct scores:** The global distinctness guarantee means selected-column ties cannot occur, so sort stability does not affect the result.
