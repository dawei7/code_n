## General

The Range I upper bound permits direct enumeration of every value in `[num1,num2]`. For each number, convert its decimal representation to a sequence of digits and inspect only indices from the second digit through the penultimate digit.

At an inspected index, add one exactly when the middle digit is greater than both neighbors or less than both neighbors. These conditions are mutually exclusive and reproduce the source definitions directly. Equality with even one neighbor satisfies neither condition.

Summing those local contributions gives one number's waviness. Adding that value for every integer in the inclusive range counts every eligible digit exactly once and therefore produces the requested total.

## Complexity detail

Let $R=\texttt{num2}-\texttt{num1}+1$ and let $D$ be the maximum decimal digit count in the range. Converting and scanning every number takes $O(RD)$ time. The current number's digit representation uses $O(D)$ auxiliary space. Under the Range I constraint, $R\le10^5$ and $D\le6$.

## Alternatives and edge cases

- **Digit dynamic programming:** Counting contributions for every value up to each endpoint avoids enumerating a very large range, but is unnecessary for the Range I limit and is the natural tool for the larger-range version.
- **Arithmetic digit extraction:** Division and remainder can expose the digits without string conversion, but the digits arrive in reverse order unless stored or processed with additional place-value logic.
- **Fewer than three digits:** There is no interior position, so the waviness is `0`.
- **Equal neighboring digit:** Peaks and valleys are strict; equality with either neighbor prevents a contribution.
- **Multiple turns:** A digit may be followed immediately by another counted digit, as the peak and valley in `4848` demonstrate.
- **Single-value range:** When `num1 == num2`, return exactly that one number's waviness.
- **Inclusive upper endpoint:** The scan must include `num2`; Example 1 relies on counting `130`.
