# Count max Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS262 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [DSCPPAS262](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/DSCPPAS262) |

---

## Problem Statement

Given an array $arr[]$ of $N$ integers and an integer $K$. The task is to find the number of subarray with a maximum value equal to $K$.

---

## Input Format

- The first line contains two integers $N$ , $K$ - the size of `arr` and the maximum value that should be in the
  subarray.
- The second line contains $n$ integers $arr[1],arr[2],…,arr[n]$ — the elements of $arr$.

---

## Output Format

Print the number of subarrays having $K$ as the maximum value.

---

## Constraints

- $ 1 \leq N,K \leq 10000 $
- $ 0 \leq arr[i] \leq 10000 $

---

## Examples

**Example 1**

**Input**

```text
4 3
2 1 3 4
```

**Output**

```text
3
```

**Explanation**

There are 3 subarrays in which the maximum element is 3, they are [2,1,3], [1,3], [3].

**Example 2**

**Input**

```text
3 1
1 2 1
```

**Output**

```text
2
```

**Explanation**

There are 2 subarrays in which the maximum element is 1, they are [1], [1].

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

The problem at hand is to determine the number of subarrays in a given array where the maximum element is exactly `K`. This problem, though seemingly simple, requires careful consideration of edge cases and efficient handling of the array to avoid unnecessary computations.

### [](#problem-breakdown-1)Problem Breakdown

We are given an array of integers, and our task is to count the subarrays where the maximum element is exactly `K`. To solve this problem, we can break it down into two key steps:

- **Counting subarrays where the maximum element is less than or equal to `K`.**

- **Counting subarrays where the maximum element is less than or equal to `K-1`.**

The difference between the two counts will give us the number of subarrays where the maximum element is exactly `K`.

### [](#key-idea-and-approach-2)Key Idea and Approach

To achieve this, we use a helper function `totalSubarrays` that counts all subarrays where the maximum element is not greater than a given value `K`. This function works as follows:

- **Iterating through the array:** We traverse the array and identify sequences of consecutive elements that are all less than or equal to `K`.

- **Counting valid subarrays:** For each such sequence, we calculate the number of subarrays that can be formed. If a sequence has `count` elements, the number of subarrays is given by the formula `count * (count + 1) / 2`. This formula derives from the fact that a sequence of `n` elements can form `1 + 2 + ... + n = n * (n + 1) / 2` subarrays.

Using this function, we calculate two values:

- `count1`: The total number of subarrays where the maximum element is less than or equal to `K-1`.

- `count2`: The total number of subarrays where the maximum element is less than or equal to `K`.

Finally, the difference `count2 - count1` gives us the number of subarrays where the maximum element is exactly `K`.

### [](#efficiency-consideration-3)Efficiency Consideration

The approach used in this solution is efficient with a time complexity of `O(N)`, where `N` is the length of the array. This is because each element in the array is processed at most twice—once when counting valid subarrays and once when moving past elements greater than `K`. This makes the solution scalable for large arrays.

### [](#edge-cases-4)Edge Cases

- **All elements greater than `K`:** The function handles this by skipping over such elements, resulting in zero valid subarrays.

- **All elements less than or equal to `K-1`:** Here, `count2` would be equal to `count1`, and thus the final count would correctly be zero, indicating no subarrays with a maximum element of exactly `K`.

### [](#bonus-5)Bonus

This problem can be also solved using the monotonic stack.  This approach efficiently counts the number of subarrays where the maximum element is exactly `K` by utilizing the concepts of “Next Greater Element” (NGE) and “Previous Greater Element” (PGE). By first identifying the indices of the next and previous greater elements for each element in the array using stacks, we can determine the number of valid subarrays where each occurrence of `K` is the maximum. The total count is calculated by multiplying the number of elements between `K` and its nearest greater elements on both sides. This method runs in (O(N)) time and requires (O(N)) space, making it well-suited for handling large arrays efficiently.

</details>
