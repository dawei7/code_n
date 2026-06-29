# Flipping subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS277 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [DSCPPAS277](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/DSCPPAS277) |

---

## Problem Statement

- You are given a binary array $arr$ whose elements are only $0$ and $1$. Your task is to find the length of the longest subarray that contains only $1s$ after flipping exactly one contiguous subarray from $0$ to $1$.

- You must perform the flip operation at least once.

---

## Input Format

- The first line contains one integer $n$, the size of the array.                                                                                                               - Next line contains $n$ integers $arr[0],arr[1]...arr[n]$, representing the elements of the array.

---

## Output Format

- Find length of longest subarray with $1$ after flipping one contiguous subarray.

---

## Constraints

- $1 \leq n \leq 10^5$
- $0 \leq arr[i] \leq 1$

---

## Examples

**Example 1**

**Input**

```text
3
0 1 0
```

**Output**

```text
2
```

**Explanation**

Flip the first contiguous 0 to make it 1, the arr would look like 1,1,0. it contains 2 ones that are maximum from all possible cases.

**Example 2**

**Input**

```text
3
0 0 0
```

**Output**

```text
3
```

**Explanation**

FLip all the elements as it is contiguous , then the arr would look like 1,1,1 and it has a maximum number of ones that is 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

Given a binary array `arr` (containing only 0s and 1s), you need to find the length of the longest subarray that contains only `1`s after flipping exactly one contiguous subarray of `0`s to `1`s.

#### [](#approach-2)Approach:

To solve this problem efficiently, we can break it down into a series of steps. The key idea is to first identify and group contiguous segments of `0`s and `1`s. By analyzing these segments, we can determine the best place to flip a segment of `0`s to maximize the length of `1`s.

### [](#step-by-step-explanation-3)Step-by-Step Explanation:

-

**Identify Contiguous Segments:**

- Traverse the array and group contiguous segments of `0`s and `1`s.

- Store the lengths of these segments in a list called `freq`.

-

**Calculate Maximum Possible Length After Flip:**

- Iterate through the `freq` list and evaluate the maximum possible length of `1`s that can be obtained by flipping one segment of `0`s.

- Specifically, focus on segments of `0`s surrounded by `1`s (e.g., `[1s] 0 [1s]`):

- The effective length of `1`s after flipping a segment of `0`s is the sum of the lengths of the surrounding `1`s plus the length of the `0` segment.

- Also, consider edge cases where the array contains only one segment of `1`s or where the flip results in a continuous segment of `1`s.

-

**Edge Case Handling:**

- If the array has only two segments and the first is all `0`s, flipping all the `0`s results in a segment of length `n-1` (if `n` is the length of the array), as flipping an empty array would trivially not yield any `1`s.

### [](#example-4)Example:

For an array like `[1, 0, 0, 1, 1, 0, 1]`:

- Segments are: `[1]`, `[2]`, `[2]`, `[1]`.

- Possible flips:

- Flip the first segment of `0`s: results in `[3]`.

- Flip the second segment of `0`s: results in `[4]`.

- The maximum possible length of `1`s is `4`.

### [](#complexity-5)Complexity:

-

**Time Complexity:** The solution runs in `O(N)` time, where `N` is the length of the array. This is because we make a single pass through the array to build the `freq` list and then another pass to calculate the maximum possible length of `1`s.

-

**Space Complexity:** The space complexity is `O(N)` due to the storage used by the `freq` list.

</details>
