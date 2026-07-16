# The k Strongest Values in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1471 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/the-k-strongest-values-in-an-array/) |

## Problem Description
### Goal

For an integer array `arr`, define its median as the element at index $\lfloor (n-1)/2 \rfloor$ after the array has been sorted in ascending order, where $n$ is the array length. This is the ordinary middle element when $n$ is odd and the lower of the two middle elements when $n$ is even.

Let that median be $m$. A value $a$ is stronger than a value $b$ when $\lvert a-m\rvert > \lvert b-m\rvert$. If the two distances are equal, the larger value is stronger. Return the $k$ strongest occurrences from `arr` in any order. Repeated values remain distinct occurrences, so the result may contain duplicates.

### Function Contract
**Inputs**

- `arr`: an integer array with length $n$, where $1 \le n \le 10^5$.
- Every value satisfies $-10^5 \le \texttt{arr[i]} \le 10^5$.
- `k`: the number of occurrences to return, where $1 \le k \le n$.

**Return value**

Return an array containing exactly the $k$ strongest occurrences under the ordering induced by the pair

$$
(\lvert a-m\rvert,a).
$$

The result order is arbitrary, but its multiplicities must match those of the selected occurrences.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5], k = 2`
- Output: `[5,1]`
- Explanation: The median is $3$. Values $5$ and $1$ both have distance $2$, and $5$ ranks ahead of $1$ because it is larger.

**Example 2**

- Input: `arr = [1,1,3,5,5], k = 2`
- Output: `[5,5]`
- Explanation: The median is $3$, and both occurrences of $5$ outrank both occurrences of $1$ on the equal-distance tie.

**Example 3**

- Input: `arr = [6,7,11,7,6,8], k = 5`
- Output: `[11,8,6,6,7]`
- Explanation: The median is $7$. The two copies of $6$ are separate selected occurrences, while either copy of $7$ may be the final occurrence.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turning the strength definition into an ordered geometry problem**

The median cannot be determined from the original positions, so first sort a copy of `arr` in ascending order and read

$$
m=\texttt{ordered}\!\left[\left\lfloor\frac{n-1}{2}\right\rfloor\right].
$$

After sorting, values smaller than or equal to $m$ become farther from the median as their indices move left, while values greater than or equal to $m$ become farther as their indices move right. Thus, among any still-unselected contiguous interval of the sorted array, a strongest remaining value must be at one of its two endpoints. No interior value can be farther from $m$ than both extremes.

**Comparing the two possible strongest values**

Maintain pointers `left` and `right` at the current interval endpoints. Compare the endpoint strengths by their distances from $m$.

- If $\lvert\texttt{ordered[left]}-m\rvert$ is larger, select the left value and advance `left`.
- If the right distance is larger, select the right value and decrement `right`.
- If the distances tie, select the right value. Because the array is sorted, the right endpoint is at least as large as the left endpoint, exactly implementing the larger-value tie-breaker.

Append the selected endpoint and repeat until $k$ occurrences have been collected. The returned order happens to run from strongest to weakest, although the contract permits any permutation of the selected multiset.

**Why endpoint removal remains correct**

Initially, every array occurrence lies in the interval `[left, right]`, and the preceding geometric observation proves that the strongest one is an endpoint. The comparison chooses the stronger endpoint under both parts of the definition, so the first removal is correct.

After one endpoint is removed, all remaining occurrences still form a contiguous sorted interval around the same fixed median. The same argument therefore applies again. By induction, each iteration removes the strongest occurrence not chosen earlier. After $k$ iterations, the result contains exactly the top $k$ occurrences. Moving a pointer by one also preserves duplicate multiplicities: equal values at different indices are considered and removed independently.

#### Complexity detail

Sorting the $n$ values costs $O(n\log n)$ time. The two-pointer selection performs exactly $k$ constant-time comparisons and removals, adding $O(k)$ time; because $k \le n$, the total remains $O(n\log n)$.

The app-local implementation sorts a copy so that callers retain their input, requiring $O(n)$ storage. The returned list holds $k$ values and is also bounded by $O(n)$. If input mutation is allowed, an in-place sort can reduce auxiliary storage apart from the output to the sorting implementation's own stack or workspace.

#### Alternatives and edge cases

- **Sort directly by strength:** Compute the median, then sort all values by `(abs(value - median), value)` in descending order. This is correct and has the same asymptotic bounds, but it performs another full sort and repeatedly evaluates the ranking key instead of exploiting the already sorted order.
- **Heap selection:** After finding the median, maintain a min-heap of the best $k$ strength pairs. This takes $O(n\log k)$ selection time after median discovery and $O(k)$ heap space; obtaining the median by sorting still dominates unless a linear-time selection algorithm is also used.
- **Linear-time selection:** The median can be found with selection, and the $k$th strength threshold can be selected similarly. This can achieve expected or worst-case linear time with careful tie and multiplicity handling, but it is substantially more intricate than the required sorting solution.
- **Repeated maximum search:** Scanning every remaining value to choose one strongest occurrence at a time is correct, yet selecting $\Theta(n)$ values takes $O(n^2)$ time.
- **Even-length arrays:** The median is the lower middle value at index $\lfloor(n-1)/2\rfloor$, not the average of the middle pair and not the upper middle value.
- **Equal distances:** When endpoints are equally far from the median, the numerically larger right endpoint must be chosen first.
- **Duplicates:** Equal array entries are separate occurrences. Selecting one does not remove or represent all copies.
- **All values requested:** When `k == n`, every occurrence is returned; the arbitrary-order rule still applies.
- **Single-element input:** The lone value is the median and necessarily the single strongest result.

</details>
