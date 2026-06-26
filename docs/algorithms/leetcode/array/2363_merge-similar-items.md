# Merge Similar Items

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2363 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting, Ordered Set |
| Official Link | [merge-similar-items](https://leetcode.com/problems/merge-similar-items/) |

## Problem Description & Examples
### Goal
Given two 2D integer arrays, `items1` and `items2`, representing items where each element is of the form `[value, weight]`, merge the two arrays. 

The merge rules are as follows:
1. If a `value` appears in both arrays, its weights should be summed together.
2. If a `value` appears in only one array, it should be kept with its original weight.

Return the merged list of `[value, weight]` pairs sorted in ascending order by their `value`.

### Function Contract
**Inputs**

- `items1`: `List[List[int]]` - A list of `[value, weight]` pairs, where each `value` is unique within `items1`.
- `items2`: `List[List[int]]` - A list of `[value, weight]` pairs, where each `value` is unique within `items2`.

**Return value**

- `List[List[int]]` - The merged list of `[value, weight]` pairs, sorted in ascending order by `value`.

### Examples
**Example 1**

- Input: `items1 = [[1,1],[4,5],[3,8]]`, `items2 = [[3,1],[1,5]]`
- Output: `[[1,6],[3,9],[4,5]]`

**Example 2**

- Input: `items1 = [[1,1],[3,2],[2,3]]`, `items2 = [[2,1],[3,2],[1,3]]`
- Output: `[[1,4],[2,4],[3,4]]`

**Example 3**

- Input: `items1 = [[1,3],[2,2]]`, `items2 = [[7,1],[2,2],[1,4]]`
- Output: `[[1,7],[2,4],[7,1]]`

---

## Underlying Base Algorithm(s)
The problem requires aggregating weights associated with unique values and returning the result sorted by those values. Two primary approaches can be used:

1. **Hash Map (Dictionary) + Sorting**:
   - We iterate through both lists and accumulate the weights for each value in a hash map.
   - After processing all items, we extract the key-value pairs from the hash map, sort them by key (value), and return the result.

2. **Bucket Array (Counting Sort approach)**:
   - Since the values are bounded (e.g., $1 \le \text{value} \le 1000$), we can use a fixed-size array where the index represents the item's `value` and the value at that index represents the accumulated `weight`.
   - We populate this array by iterating through both lists, then traverse the array to collect non-zero weights, which naturally yields a sorted result.

The Hash Map approach is more generalizable to arbitrary or sparse values, while the Bucket Array approach is highly efficient for small, bounded value ranges.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}((N + M) \log(N + M))$ where $N$ is the length of `items1` and $M$ is the length of `items2`. Populating the hash map takes $\mathcal{O}(N + M)$ time, and sorting the unique keys takes $\mathcal{O}(U \log U)$ time, where $U \le N + M$ is the number of unique values.
- **Space Complexity**: $\mathcal{O}(N + M)$ auxiliary space to store the aggregated weights in the hash map.
