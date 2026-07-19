# Number of Different Subsequences GCDs

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/) |
| Frontend ID | 1819 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Counting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The greatest common divisor (GCD) of a non-empty sequence is the greatest positive integer that divides every value in that sequence. A subsequence of `nums` is formed by deleting any number of elements while preserving the relative order of those retained; equal values at different positions remain independently selectable.

Consider every non-empty subsequence of the positive-integer array `nums`. Many subsequences may share a GCD, and the task concerns the distinct GCD values rather than the number of subsequences producing them. Return how many different positive integers occur as the GCD of at least one such subsequence.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers with $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 2\cdot10^5$.
- Let $M = \max(\texttt{nums})$.

**Return value**

- Return the number of distinct GCD values among all non-empty subsequences of `nums`.

### Examples

**Example 1**

- Input: `nums = [6,10,3]`
- Output: `5`

The attainable values are 6, 10, and 3 from single-element subsequences, 2 from `[6,10]`, and 1 from a subsequence containing 3 with either even value.

**Example 2**

- Input: `nums = [5,15,40,5,6]`
- Output: `7`

Repeated occurrences may form different subsequences, but they do not make an already attainable GCD count twice.

### Required Complexity

- **Time:** $O(n + M\log M)$
- **Space:** $O(M)$

<details>
<summary>Approach</summary>

#### General

**Characterize which subsequences could have a candidate GCD**

If a subsequence has GCD $g$, every selected value must be divisible by $g$. Conversely, take all values present in `nums` that are multiples of $g$. If their collective GCD is exactly $g$, those values themselves form a valid subsequence with GCD $g$. If their collective GCD is larger than $g$, every subset of them also has GCD divisible by that larger common divisor, so $g$ is unattainable.

**Enumerate candidates through their multiples**

Record value presence in a Boolean array through $M$. For each candidate $g$ from 1 through $M$, visit `g`, `2*g`, `3*g`, and so on. Fold only the present multiples into a running GCD. As soon as it becomes $g$, count the candidate and stop: adding more multiples cannot make the GCD cease to divide $g$, and it cannot fall below $g$ because every visited value is a multiple of $g$.

**Why the test is both necessary and sufficient**

Any subsequence producing $g$ is contained within the present multiples of $g$. The GCD of the complete set of those multiples divides the GCD of every subset, including that subsequence, while it is itself divisible by $g$; hence it must equal $g$. In the other direction, when the complete set's GCD is $g$, selecting one occurrence of each participating value is a legal non-empty subsequence whose GCD is $g$. The multiple scan therefore counts exactly the attainable values.

#### Complexity detail

Building presence takes $O(n)$ time. Candidate $g$ visits at most $\lfloor M/g\rfloor$ multiples, so the total number of visits is

$$
\sum_{g=1}^{M}\left\lfloor\frac{M}{g}\right\rfloor = O(M\log M).
$$

Early exits can reduce this work but are not required for the bound. The Boolean presence table uses $O(M)$ space; scalar GCD state adds $O(1)$.

#### Alternatives and edge cases

- **Enumerate all subsequences:** It directly follows the definition but considers $2^n-1$ choices and is infeasible.
- **Incrementally store every seen subsequence GCD:** Combining each new number with all previously attainable GCDs is correct, but the set can contain $\Theta(M)$ values and lead to $O(nM)$ work.
- **Duplicate input values:** Presence is sufficient because repeated equal values cannot create a new GCD value.
- **Value 1 present:** GCD 1 is immediately attainable, although other values must still be tested.
- **Single element:** Exactly that element is attainable, so the answer is one.
- **Candidate absent from `nums`:** It may still be attainable as the GCD of several larger multiples.
- **No present multiple:** The running GCD stays zero, so the candidate is not counted.
- **Maximum value:** Its only possible present multiple within the domain is itself; it is attainable exactly when present.

</details>
