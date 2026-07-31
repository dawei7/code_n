## General

Let the array sum be $S$ and its length be $n$. The smallest integer strictly greater than the average $S/n$ is

$$
\left\lfloor\frac{S}{n}\right\rfloor+1.
$$

Because the answer must be positive, use 1 instead whenever that expression is smaller than 1. Integer floor division computes this starting point exactly, including when $S$ is negative, and avoids floating-point rounding near an integer boundary.

Every smaller positive integer fails the strict-average condition, so none needs to be tested for absence. Put all array values into a hash set, begin at the derived lower bound, and increment while the candidate is present. The first missing candidate is strictly above the average by construction, is positive, and is the smallest value satisfying both requirements.

## Complexity detail

Building the set and computing the sum take $O(n)$ expected time. Each successful membership check skips a distinct value present in the array, so at most $n$ increments occur; expected total time remains $O(n)$. The set uses $O(n)$ space. Hash-table bounds assume expected constant-time insertion and lookup.

The complete legal input contains at most 100 elements, which is too small for stable timing to distinguish hash membership from repeated list membership. The package therefore uses a reviewed `bounded_domain` certificate instead of runtime tiers. Its bounded-work proof limits both the initial scan and candidate skips, while deterministic property tests compare the reference with an exact rational oracle across exhaustive small arrays, every legal length, and extrema.

## Alternatives and edge cases

- **Floating-point average:** It is unnecessary and can obscure strict comparisons; floor division derives the first eligible integer exactly.
- **Linear membership checks:** Searching the list for every successive candidate is correct but can take $O(n^2)$ time on consecutive inputs.
- **Negative average:** The average-derived lower bound may be nonpositive, so the candidate must be clamped to 1.
- **Integer average:** Strictly greater means starting one above the average, not at the average itself.
- **Fractional average:** Flooring and adding one gives the mathematical ceiling and therefore the first greater integer.
- **Duplicate values:** Duplicates affect the average but do not require repeated membership storage.
- **Consecutive present values:** Continue until the first gap; a present initial candidate is not an answer.
- **Maximum input values:** The valid answer may be 101 even though each array element is at most 100.
