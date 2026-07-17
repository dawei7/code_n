# Count Good Meals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1711 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-meals/) |

## Problem Description
### Goal

A good meal consists of exactly two different food items whose deliciousness values add to a power of two. Items are distinguished by their indices, so two equal values at different positions may form a pair, while one item cannot be paired with itself.

Given the deliciousness value of every item, count the index pairs that form good meals. Count each unordered pair once and return the result modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `deliciousness`: a list of $n$ non-negative integers
- $1 \le n \le 10^5$
- $0 \le \texttt{deliciousness[i]} \le 2^{20}$

Let $B = 22$, the number of powers $2^0$ through $2^{21}$ that can equal a legal pair sum.

**Return value**

The number of pairs $(i,j)$ with $i<j$ whose values sum to a power of two, reduced modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `deliciousness = [1, 3, 5, 7, 9]`
- Output: `4`

The qualifying value pairs are `(1, 3)`, `(1, 7)`, `(3, 5)`, and `(7, 9)`.

**Example 2**

- Input: `deliciousness = [1, 1, 1, 3, 3, 3, 7]`
- Output: `15`

There are three pairs of ones, nine pairs combining a one and a three, and three pairs combining a one and a seven.

**Example 3**

- Input: `deliciousness = [0, 0, 1, 1]`
- Output: `5`

Each zero can pair with either one to make $1$, and the two ones form one pair summing to $2$.

### Required Complexity

- **Time:** $O(nB)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count only partners that appeared earlier**

Scan the array from left to right and maintain a frequency map of values already seen. For the current value `x`, a previous value `y` forms a good meal exactly when `y = power - x` for some legal power of two. Add the stored frequency of each such complement, then insert `x` into the map.

Because insertion happens after the queries, every counted partner has a smaller index. Thus no item pairs with itself and every unordered index pair is counted at the moment its later item is processed, exactly once.

**Bound the target powers**

Every value is at most $2^{20}$, so a pair sum lies from $0$ through $2^{21}$. Zero is not a power of two. Checking $2^0,2^1,\ldots,2^{21}$ therefore covers every possible good sum without testing irrelevant larger targets.

Repeated values are handled by frequencies rather than by distinct-value membership. If a complement has appeared `c` times, the current index creates `c` different meals. Reduce the final count modulo $10^9+7$.

#### Complexity detail

For each of the $n$ items, exactly $B=22$ powers are tested with expected $O(1)$ hash-map lookup, for $O(nB)$ expected time. The map contains at most $n$ distinct values and uses $O(n)$ space.

#### Alternatives and edge cases

- **Check every index pair:** direct nested loops are correct but take $O(n^2)$ time.
- **Sort and use two pointers per power:** repeating a two-pointer scan for all powers takes $O(n\log n+nB)$ time and complicates duplicate counting.
- **Frequency combinations after a full count:** iterating distinct complements can work, but requires careful division or ordering to avoid double-counting equal and unequal values.
- **Duplicate values:** different indices remain different items; use the full previous frequency, not a Boolean membership test.
- **Zero values:** two zeros sum to zero and do not qualify, but zero can pair with a positive power of two.
- **Two equal powers:** values such as two ones may pair because their sum is the next power of two.
- **Maximum values:** two values equal to $2^{20}$ produce the legal target $2^{21}$, so the highest target must be included.
- **Single item:** no pair exists, so the answer is zero.
- **Large pair counts:** apply the required modulus because the raw number can exceed 32-bit range.

</details>
