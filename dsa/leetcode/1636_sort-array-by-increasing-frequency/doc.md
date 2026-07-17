# Sort Array by Increasing Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1636 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-array-by-increasing-frequency/) |

## Problem Description
### Goal
Given an integer array `nums`, reorder all of its elements according to the frequency of their values. A value that occurs fewer times must appear before every value that occurs more often. When two distinct values have the same frequency, the larger value must appear first.

Return the completely reordered array. Equal values remain together because every copy receives the same frequency and value-based ordering keys.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 100$ and $-100 \le \texttt{nums[i]} \le 100$.

**Return value**

Return an array containing exactly the input elements, ordered first by increasing frequency and then, for equal frequencies, by decreasing numeric value.

### Examples
**Example 1**

- Input: `nums = [1,1,2,2,2,3]`
- Output: `[3,1,1,2,2,2]`

The values 3, 1, and 2 occur one, two, and three times respectively.

**Example 2**

- Input: `nums = [2,3,1,3,2]`
- Output: `[1,3,3,2,2]`

Values 2 and 3 both occur twice, so the larger value 3 precedes 2.

**Example 3**

- Input: `nums = [-1,1,-6,4,5,-6,1,4,1]`
- Output: `[5,-1,4,4,-6,-6,1,1,1]`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate counting from ordering.** Scan `nums` once and store the number of occurrences of every distinct value in a frequency map. After this pass, the complete ordering rule for an element `value` is represented by the pair `(frequency[value], -value)`: the first component puts rarer values first, and the negative second component reverses the usual numeric order whenever frequencies tie.

**Apply one lexicographic sort.** Sort every element using that pair as its key. All copies of one value receive identical keys and therefore form one block. Between different blocks, a smaller frequency wins the first comparison; only equal frequencies reach the second comparison, where the larger original value has the smaller negated key and comes first.

These two comparisons exactly match the requested priority rules. The result preserves every input occurrence because sorting only permutes the array, and every pair of distinct value blocks is placed in the required relative order.

#### Complexity detail

Counting takes $O(n)$ time, and comparison sorting $n$ elements takes $O(n\log n)$ time. The frequency map, key storage, and returned ordering use $O(n)$ space in the worst case when all values are distinct.

#### Alternatives and edge cases

- **Sort distinct values, then expand:** Sort at most $n$ frequency-map keys by the same pair and append each key the recorded number of times. This has the same worst-case bounds and can avoid comparing repeated elements.
- **Fixed-range buckets:** Because values are restricted to $[-100,100]$, counts can be stored in a 201-slot array and emitted by frequency groups in $O(n+201)$ time, but that optimization depends on this small numeric domain.
- **Repeated minimum selection:** Repeatedly searching for the next block produces the right order but can require quadratic time.
- A one-element array is already correctly ordered.
- If all values are distinct, every frequency is one, so the result is the input values in strictly decreasing order.
- If all elements are equal, sorting leaves the array unchanged.
- Negative values use ordinary numeric comparison: for example, $-1$ precedes $-6$ when their frequencies tie because $-1$ is larger.

</details>
