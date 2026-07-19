# Intersection of Three Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1213 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-three-sorted-arrays/) |

## Problem Description

### Goal

You are given three integer arrays `arr1`, `arr2`, and `arr3`. Every array is sorted in strictly increasing order, so a value occurs at most once within any one array and later positions always contain larger values.

Return a sorted array containing only the integers that appear in all three inputs. A value present in only one or two arrays is excluded, and if the three arrays have no common value, return an empty array.

### Function Contract

**Inputs**

- `arr1`, `arr2`, and `arr3`: Strictly increasing integer arrays.
- Their lengths $n_1$, $n_2$, and $n_3$ each lie between 1 and 1000.
- Every array value lies between 1 and 2000.

**Return value**

- All values present in every input array, in increasing order.

### Examples

**Example 1**

- Input: `arr1 = [1,2,3,4,5]`, `arr2 = [1,2,5,7,9]`, `arr3 = [1,3,4,5,8]`
- Output: `[1,5]`

**Example 2**

- Input: `arr1 = [197,418,523,876,1356]`, `arr2 = [501,880,1593,1710,1870]`, `arr3 = [521,682,1337,1395,1764]`
- Output: `[]`

**Example 3**

- Input: `arr1 = [2,4,6]`, `arr2 = [1,2,3,4,5,6]`, `arr3 = [2,6,8]`
- Output: `[2,6]`
