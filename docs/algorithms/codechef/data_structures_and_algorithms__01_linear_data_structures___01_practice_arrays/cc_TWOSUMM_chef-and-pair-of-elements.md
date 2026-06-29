# Chef and Pair of Elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWOSUMM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [TWOSUMM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/TWOSUMM) |

---

## Problem Statement

Chef has an array of integers $nums$.\
He wants to invite two of his friends such that the **sum of their lucky numbers equals a given target** $X$.

Your task is to help Chef find the **indices of the two numbers** in the array whose sum is exactly $X$.
- Each input will have **exactly one valid pair**.
- You cannot use the **same element twice**.
- The index of the element that appears first in the array must be printed before the index of the element that appears later.

## **Function Declaration**

### **Function Name**

$findPair$ – Finds two indices of numbers in the array whose sum equals the target value.

### **Parameters**

* $nums$ : A list/array of integers.
* $target$ : An integer representing the required sum $X$.

### **Return Value**

* Returns the **two indices** of the numbers whose sum equals $target$. Answers are accepted on 0-based indexing.

## Constraints:
* $2 \leq nums.length \leq 10^4$
* $-10^9 \leq nums[i] \leq 10^9$
* $-10^9 \leq target \leq 10^9$
Only one valid answer exists.

---

## Input Format

* $N$ → size of array
* Next line → **N integers** (the array)
* Third line → **target sum X**

---

## Output Format

Print the two indices (0-based or 1-based depending on implementation; your samples use **0-based**).

---

## Examples

**Example 1**

**Input**

```text
4
3 5 2 6
7
```

**Output**

```text
1 2
```

**Explanation**

1 index = 5 \
2 index = 2 \
5+2=7

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Chef has an array of integers `nums`.\
He wants to invite two of his friends such that the sum of their lucky numbers equals a given target `X`.

Your task is to **find the indices of the two numbers** in the array whose sum is exactly `X`.

- Each input has exactly one valid pair.
- You cannot use the same element twice.
- The answer can be returned in any order.

**Follow-up**: Can you solve this problem in **O(N)** time instead of the naive **O(N²)**?

---

## Key Observations

- For each number `nums[i]`, the other number needed to reach the target is `X - nums[i]`.
- If we can quickly check whether this complement exists among the numbers seen so far, we can find the pair in **O(N)**.
- Using a **hash map** (**or dictionary**) allows us to store numbers and their indices for fast lookup.

---

## Approach

- Initialize an empty map `mp` that maps a number to its index.
- Traverse the array `nums` with index `i`:
   - Compute `complement = target - nums[i]`.
   - If `complement` exists in `mp`, we have found the solution: return `[mp[complement], i]`.
   - Otherwise, store the current number and its index in the map: mp[nums[i]] = i.
- Since the problem guarantees **exactly one solution**, the pair will always be found.

**Example walkthrough**:
- nums = [1, 4, 6, 8, 2], target = 10
1. i = 0 → 1 → complement = 9 → not in map → store 1:0
2. i = 1 → 4 → complement = 6 → not in map → store 4:1
3. i = 2 → 6 → complement = 4 → found in map → return [1,2]

---

## Complexity Analysis
**Time Complexity**:\
We traverse the array once and perform O(1) map operations, so the complexity is **O(N)**.

**Space Complexity**:\
We store numbers and their indices in a map, so the space complexity is **O(N)**.

</details>
