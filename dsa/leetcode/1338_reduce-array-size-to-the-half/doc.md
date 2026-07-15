# Reduce Array Size to The Half

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1338 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/) |

## Problem Description
### Goal
Given an even-length integer array `arr`, choose a set of integer values. For every chosen value, remove all of its occurrences from the array.

Return the minimum possible size of the chosen set such that at least half of the original array elements are removed. Only distinct selected values count toward that size, regardless of how many occurrences each one removes. The values themselves do not need to be returned.

### Function Contract
**Inputs**

- `arr`: an even-length integer array of length $n$, where $2\le n\le10^5$ and $1\le\texttt{arr[i]}\le10^5$.

**Return value**

The smallest number of distinct values whose complete removal deletes at least $n/2$ elements.

### Examples
**Example 1**

- Input: `arr = [3,3,3,3,5,5,5,2,2,7]`
- Output: `2`
- Explanation: Removing all copies of 3 and any suitable additional value removes at least five elements.

**Example 2**

- Input: `arr = [7,7,7,7,7,7]`
- Output: `1`

**Example 3**

- Input: `arr = [1,2,3,4]`
- Output: `2`
- Explanation: Every selected value removes only one element.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Convert value choices into frequency choices**

Count the occurrences of every distinct value. Choosing a value removes exactly its frequency, so the identities of values no longer matter; only these counts affect how quickly the target of $n/2$ removed elements is reached.

Sort the frequencies descending and accumulate them until their sum is at least $n/2$. The number of consumed frequencies is the answer.

For any fixed number $q$ of selected values, the $q$ largest frequencies remove at least as many elements as any other $q$ frequencies: replacing a selected smaller frequency by an unselected larger one cannot reduce the total. Therefore, if the greedy prefix of length $q$ has not reached half, no set of $q$ values can succeed. The first greedy prefix that reaches the target is consequently minimal.

#### Complexity detail

Hash counting takes expected $O(n)$ time. There are at most $n$ distinct frequencies to sort, costing $O(n\log n)$ time in the worst case. The counter and frequency list use $O(n)$ space.

#### Alternatives and edge cases

- **Maximum heap:** Push all frequencies into a heap and repeatedly remove the largest; this can avoid fully sorting when the answer is small, while retaining $O(n\log n)$ worst-case time.
- **Counting frequencies of frequencies:** Because no frequency exceeds $n$, a bucket array can process counts descending in $O(n)$ time and $O(n)$ space.
- **Linear-search frequency table:** Avoiding a hash map by scanning prior distinct values for every element can take $O(n^2)$ time.
- **One distinct value:** Selecting it removes the complete array, so the answer is 1.
- **All values distinct:** Each choice removes one element, making the answer exactly $n/2$.
- **Tied frequencies:** Their order is irrelevant because they remove equal numbers of elements.
- **Overshooting half:** Removing more than $n/2$ elements is allowed.

</details>
