## General

Partition the numbers by whether they are less than $10$. Let $S$ be the sum of all single-digit values and $D$ the sum of all double-digit values.

Alice has exactly two choices. Choosing the single-digit group wins precisely when $S>D$; choosing the double-digit group wins precisely when $D>S$. Therefore at least one choice wins if and only if $S\ne D$.

A single running balance can represent $S-D$: add each single-digit value and subtract each double-digit value. The final balance is nonzero exactly when one group has a strictly larger sum. This examines every input once and does not need to store either group.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The scan takes $O(n)$ time and uses $O(1)$ auxiliary space.

The contract caps $n$ at $100$. That legal range is too narrow for a reliable scaling verdict, so complexity is verified by the package's bounded-domain certificate and property regression rather than a runtime benchmark.

## Alternatives and edge cases

- **Build two filtered lists:** Summing explicit groups is correct but uses $O(n)$ avoidable auxiliary space.
- **Sort by digit length:** Sorting does not help the two-group sum comparison and costs $O(n\log n)$ time.
- Equal group sums return `False` because Alice must win strictly.
- If only one digit-length group is present, Alice chooses that nonempty group and wins.
- Values `1` and `9` are single-digit; values `10` and `99` are double-digit.
- Duplicate values contribute once per occurrence.
- The order of `nums` is irrelevant to both sums.
