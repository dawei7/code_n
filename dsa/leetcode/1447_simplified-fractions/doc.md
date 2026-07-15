# Simplified Fractions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1447 |
| Difficulty | Medium |
| Topics | Math, String, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/simplified-fractions/) |

## Problem Description
### Goal

Given an integer `n`, list every simplified fraction strictly between $0$ and
$1$ whose denominator is at most `n`. A fraction is simplified when its
positive numerator and denominator share no common divisor greater than one;
equivalent representations such as `"1/2"` and `"2/4"` must therefore not
both appear.

Represent each retained fraction as a string in the form
`"numerator/denominator"`. Return every qualifying value exactly once. The
list may be arranged in any order.

### Function Contract
**Inputs**

- `n`: an integer satisfying $1 \le n \le 100$.

**Return value**

Return a list of strings `"a/b"` containing exactly the fractions for which
$1 \le a < b \le n$ and $\gcd(a,b)=1$. The order of the strings is not part of
the result contract.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `["1/2"]`

**Example 2**

- Input: `n = 3`
- Output: `["1/2", "1/3", "2/3"]`

**Example 3**

- Input: `n = 4`
- Output: `["1/2", "1/3", "1/4", "2/3", "3/4"]`
- Explanation: `"2/4"` is excluded because reducing it produces the already
  represented fraction `"1/2"`.

**Example 4**

- Input: `n = 1`
- Output: `[]`
- Explanation: No denominator at most one admits a positive numerator that is
  smaller than it.

### Required Complexity
- **Time:** $O(n^2\log n)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Enumerate exactly the fractions inside the open interval**

For each denominator $b$ from $2$ through $n$, the only integer numerators
that place $a/b$ strictly between $0$ and $1$ are $a=1,2,\ldots,b-1$.
Enumerating precisely those pairs automatically excludes zero, one, negative
fractions, and denominators beyond the limit. There are fewer than
$n(n-1)/2$ candidate pairs, so direct enumeration is practical for the given
bound.

**Coprimality is exactly the simplification test**

For each candidate $(a,b)$, compute $\gcd(a,b)$ with Euclid's algorithm. If
the result is one, no integer greater than one divides both values, so the
fraction is already in lowest terms and `f"{a}/{b}"` belongs in the answer.
If the GCD is greater than one, dividing both parts by that common factor
produces another representation of the same rational value, so the candidate
must be omitted.

Euclid's algorithm repeatedly replaces the larger pair by a remainder pair;
`gcd(a, b)` reaches the same common divisor after logarithmically many
steps. It avoids trying every possible divisor separately.

**Why the enumeration is complete and duplicate-free**

Every requested fraction has some denominator $b \le n$ and, because it lies
strictly between zero and one, some numerator $a$ with $1 \le a < b$. The
nested loops therefore inspect its pair. Its simplified status gives
$\gcd(a,b)=1$, so the method includes it.

Conversely, every emitted pair satisfies the interval, denominator, and
coprimality conditions by construction. Two different emitted coprime pairs
cannot represent the same rational number: the reduced numerator and
denominator of a positive fraction are unique. Thus nothing valid is missing
and no value is duplicated. Iterating denominators and then numerators gives a
stable order, although correctness does not rely on that order.

#### Complexity detail

There are $\sum_{b=2}^{n}(b-1)=O(n^2)$ candidate pairs. A Euclidean GCD on
values at most $n$ costs $O(\log n)$ time, giving an $O(n^2\log n)$ upper
bound including candidate testing. Formatting the retained strings is bounded
by the same asymptotic time because each representation has $O(\log n)$
characters.

The returned list can contain $\Theta(n^2)$ fractions, so its storage is
$O(n^2)$ when each bounded-size string is treated as one output item. Apart
from the required output, the loops and GCD computation use $O(1)$ auxiliary
space. Counting individual characters more explicitly makes the output
$O(n^2\log n)$ characters; the stated space convention counts result items,
as is customary for this contract.

#### Alternatives and edge cases

- **Trial division for every pair:** Test all possible common divisors up to
  $\min(a,b)$. This is correct but can spend $O(n)$ work per candidate and
  $O(n^3)$ overall, compared with Euclid's logarithmic GCD.
- **Generate a Farey sequence:** Neighbor recurrences can enumerate reduced
  fractions in sorted order without checking every pair. That is elegant and
  output-sensitive, but it is more delicate to derive and the contract does
  not require sorted output.
- **Store rational numeric values in a set:** Floating-point keys can merge
  or distinguish values incorrectly, while normalized integer pairs merely
  reproduce the GCD work with extra storage.
- **`n = 1`:** The denominator loop is empty, so return an empty list.
- **Exclusive endpoints:** Never emit `"0/b"` or `"b/b"`; the requested
  interval excludes both $0$ and $1$.
- **Reducible candidates:** Values such as `"2/4"` and `"3/6"` are omitted,
  not reduced and inserted a second time.
- **Output ordering:** Any permutation of the complete set is valid, so a
  checker must compare the returned strings without imposing list order.

</details>
