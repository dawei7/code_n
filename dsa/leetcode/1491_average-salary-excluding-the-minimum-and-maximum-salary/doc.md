# Average Salary Excluding the Minimum and Maximum Salary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1491 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/) |

## Problem Description
### Goal

An array `salary` contains the distinct integer salaries of a group of employees. Remove exactly two entries from consideration: the unique minimum salary and the unique maximum salary.

Return the arithmetic mean of all remaining salaries. The array always contains at least three values, so at least one salary remains after the two extremes are excluded. A floating-point result within absolute error $10^{-5}$ of the exact average is accepted.

### Function Contract
**Inputs**

Let $N$ be the length of `salary`.

- `salary`: a list of unique integers with $3 \le N \le 100$.
- Every salary satisfies $1000 \le \texttt{salary[i]} \le 10^6$.
- Input order has no semantic meaning; the minimum and maximum may occur at any positions.

**Return value**

Return the sum of the $N-2$ non-extreme salaries divided by $N-2$. The result is a floating-point number, and an absolute error of at most $10^{-5}$ is accepted.

### Examples
**Example 1**

- Input: `salary = [4000,3000,1000,2000]`
- Output: `2500.0`
- Explanation: Removing `1000` and `4000` leaves `2000` and `3000`, whose average is `2500`.

**Example 2**

- Input: `salary = [1000,2000,3000]`
- Output: `2000.0`
- Explanation: With three employees, only the middle salary remains after both extremes are excluded.

**Example 3**

- Input: `salary = [1000,2000,3001,9000]`
- Output: `2500.5`
- Explanation: The two retained salaries sum to `5001`, so the requested average need not be an integer.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Replace explicit removal with an aggregate identity**

Only the smallest and largest values are excluded. If `total` is the sum of all salaries, `minimum` is the least salary, and `maximum` is the greatest, then the retained sum is computed directly as `total - minimum - maximum`. No element has to be deleted, and the remaining count is exactly `N - 2`.

The uniqueness guarantee means there is exactly one occurrence of each extreme. Without uniqueness, the phrase "exclude the minimum and maximum salary" would need an occurrence rule; here subtracting each extreme once matches the contract unambiguously.

**Accumulate all three statistics in one scan**

Initialize `total` to zero and both extremes from the first salary. For each value, add it to `total`, lower `minimum` when necessary, and raise `maximum` when necessary. After the scan, divide `total - minimum - maximum` by `N - 2`.

The input length is guaranteed to be at least three, so the denominator is positive. Keeping the accumulation integral until the final division avoids repeated floating-point rounding.

**Why the computed numerator contains exactly the desired values**

Every array entry contributes once to `total`. Because all salaries are distinct, exactly one entry equals `minimum` and exactly one different entry equals `maximum`. Subtracting those two values removes precisely their two contributions while leaving every other contribution unchanged.

The divisor counts those unchanged contributions: $N$ original entries minus two excluded entries. Therefore the final quotient is the arithmetic mean of exactly the employees required by the problem.

**Why input order cannot affect the result**

Sum, minimum, and maximum are all independent of permutation. The scan may encounter an extreme early or late, but each update retains the best extreme seen so far. After processing any prefix, `total`, `minimum`, and `maximum` describe that prefix; extending the prefix preserves this statement. At the full array, they describe the complete input.

#### Complexity detail

The algorithm performs constant work for each of the $N$ salaries, so its time complexity is $O(N)$. It stores only the running sum, two extremes, and loop state, giving $O(1)$ auxiliary space.

The legal source domain has $N \le 100$, which is too small for stable runtime scaling to distinguish this linear scan from optimized built-in sorting. The package therefore uses a strictly validated `bounded_domain` complexity certificate with independent boundary/property regression evidence instead of claiming a measured scaling verdict.

#### Alternatives and edge cases

- **Sort then slice:** sort the salaries and average `salary[1:-1]`. This is straightforward but takes $O(N \log N)$ time and may mutate the input if sorted in place.
- **Three library passes:** compute `sum(salary)`, `min(salary)`, and `max(salary)` separately. It is still $O(N)$ time and $O(1)$ auxiliary space, but reads the array three times instead of once.
- **Remove by index or value:** explicitly deleting both extremes is correct when done carefully, but it mutates or copies the collection without simplifying the result.
- **Average first, then adjust:** subtracting extremes from an already divided average uses the wrong denominator and does not produce the requested mean.
- **Three salaries:** the answer is the sole value that is neither the minimum nor maximum.
- **Fractional result:** perform true division; integer division would truncate a valid non-integral average.
- **Extremes at interior positions:** do not assume the first or last array entry is an extreme.
- **Descending or arbitrary order:** no sorting precondition exists.
- **Large salaries:** integer accumulation safely preserves the exact numerator before the final conversion to floating point.
- **Unique values:** subtract one minimum and one maximum; no duplicate-extreme ambiguity exists.
- **Input preservation:** a scan leaves the caller's array unchanged.

</details>
