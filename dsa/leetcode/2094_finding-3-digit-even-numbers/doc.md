# Finding 3-Digit Even Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2094 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Recursion, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/finding-3-digit-even-numbers/) |

## Problem Description

### Goal

You are given an array `digits` whose elements are decimal digits and may repeat. Choose three distinct array positions and concatenate their digits in any order to form an integer. A valid result must have exactly three digits, so its hundreds digit cannot be zero, and its ones digit must make the number even.

Return every distinct valid integer in increasing order. A digit value may be used repeatedly only when at least that many copies occur in `digits`; different choices of equal-valued positions do not create duplicate output numbers.

### Function Contract

**Input**

- `digits`: an array of $n$ values, where $3 \le n \le 100$.
- Every element is an integer from $0$ through $9$.

**Return value**

Return the sorted list of unique three-digit even integers constructible from the available digit multiplicities.

### Examples

**Example 1**

- Input: `digits = [2, 1, 3, 0]`
- Output: `[102,120,130,132,210,230,302,310,312,320]`

**Example 2**

- Input: `digits = [2, 2, 8, 8, 2]`
- Output: `[222,228,282,288,822,828,882]`
- Explanation: A value may be reused up to its number of copies in the input.

**Example 3**

- Input: `digits = [3, 7, 5]`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Using the fixed three-digit universe**

There are only $450$ even integers from `100` through `998`. Count the available copies of each digit from `0` through `9`, then inspect those candidate numbers in increasing order. This avoids choosing among as many as $100$ input positions.

**Testing one candidate by multiplicity**

Split a candidate into its hundreds, tens, and ones digits and count how many copies of each value it requires. The candidate is constructible exactly when every required count is no greater than the corresponding available count. Starting enumeration at `100` excludes leading zeroes, and stepping by two guarantees an even ones digit.

**Why the output is unique and sorted**

Each three-digit even integer is visited exactly once, so equal input positions cannot duplicate it. Any valid constructible number belongs to the enumerated range and passes its exact multiplicity test, while every accepted candidate can be assigned to that many distinct occurrences in the input. Ascending enumeration directly produces the required order.

#### Complexity detail

Counting the $n$ input digits takes $O(n)$ time. Checking the fixed set of $450$ candidates performs constant work independent of $n$, so the total remains $O(n)$. Ten counters and constant-size candidate data use $O(1)$ auxiliary space; the output is also bounded by $450$ integers.

#### Alternatives and edge cases

- **Three index loops:** Enumerating ordered triples of distinct positions and deduplicating their numbers is correct but takes $O(n^3)$ time.
- **Backtracking over digit counts:** Choosing hundreds, tens, and even ones values directly is also constant after the $O(n)$ count pass, but needs explicit restoration and duplicate handling.
- **Permutation library:** Materializing all length-three permutations repeats equal-valued arrangements and still scales cubically with input length.
- Zero may appear in the tens or ones position but never in the hundreds position.
- Forming a number such as `222` requires three separate copies of digit `2`.
- If no even digit is available for the ones position, the result is empty.

</details>
