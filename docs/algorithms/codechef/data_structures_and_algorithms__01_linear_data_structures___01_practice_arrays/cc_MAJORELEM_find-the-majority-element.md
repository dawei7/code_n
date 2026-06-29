# Find the majority element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAJORELEM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MAJORELEM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MAJORELEM) |

---

## Problem Statement

You are given an array $arr$ containing $n$ integers. Your task is to return the **majority element**.

A majority element is defined as the element that occurs **more than $⌊n / 2⌋$ times**.
It is guaranteed that such an element always exists.

$⌊n / 2⌋$ => The floor value means if 5 divided by 2 equals 2.5, we’ll choose 2 as the output because of the floor function.

### Follow-up:

Can you solve this problem in **O(n)** time complexity while using only **O(1) extra space**?

## **Function Declaration**

### **Function Name**

$majorityElement$ – Finds the element that appears more than $⌊n / 2⌋$ times in the array.

### **Parameters**

* $arr$ : A list/array of integers of size $n$.

### **Return Value**

* Returns an **integer** — the majority element that appears more than half the time in the array.

## Constraints:

* $n == arr.length$
* $1 \leq n \leq 50,000$
* $-10^9 \leq arr[i] \leq 10^9$

---

## Input Format

* $T$ → number of test cases
* For each test case:

  * Line 1 → $n$ (array size)
  * Line 2 → **n integers** representing the array

---

## Output Format

One value per test case.

---

## Examples

**Example 1**

**Input**

```text
2
6
7 1 7 7 3 7
3
5 5 2
```

**Output**

```text
7
5
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
7 1 7 7 3 7
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
3
5 5 2
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## 🔹 Problem Restatement

You are given an array of integers of size `n`. The **majority element** is the element that appears **more than ⌊n/2⌋ times**. It is guaranteed that a majority element always exists.
The task is to find and return this element.

---

## 🔹 Key Observations

1. Since the majority element occurs more than half the time, **it cannot be outnumbered by all other elements combined**.
2. This guarantees **uniqueness** — there can only be one majority element.
3. Several approaches can be used, but we want to optimize for **time complexity** and **space complexity**.

---

## 🔹 Approaches

### 1. Frequency Counting (Hash Map / Dictionary)

* Count the frequency of each element.
* The element with frequency > ⌊n/2⌋ is the answer.
  **Complexity:**
* Time: `O(n)`
* Space: `O(n)`

✅ Simple but not optimal in space.

---

### 2. Sorting

* Sort the array.
* The majority element will always occupy the middle position (`n/2`).
  **Complexity:**
* Time: `O(n log n)`
* Space: `O(1)` or `O(log n)` depending on sorting implementation.

✅ Works, but slower than linear solutions.

---

### 3. Boyer–Moore Voting Algorithm (Optimal)

* Maintain a **candidate** and a **counter**.
* Traverse the array:

  * If the counter is 0, pick the current element as the candidate.
  * If the current element equals the candidate, increment counter.
  * Otherwise, decrement counter.
* At the end, the candidate is guaranteed to be the majority element.

**Intuition:**
The majority element will "cancel out" all other elements and still remain because it appears more than half the time.

**Complexity:**

* Time: `O(n)`
* Space: `O(1)`

✅ Best solution for this problem.

---

## 🔹 Example Walkthrough

Input: `[7, 1, 7, 7, 3, 7]`

* Start with candidate = 7, count = 1
* Next element = 1 → different → count = 0
* Next element = 7 → candidate = 7, count = 1
* Next element = 7 → same → count = 2
* Next element = 3 → different → count = 1
* Next element = 7 → same → count = 2

End result: candidate = **7**, which is the majority element.

---

## 🔹 Edge Cases to Consider

* Single element array → that element is the majority.
* All elements same → that element is the majority.
* Majority appears just slightly more than half.
* Arrays with negative numbers.
* Arrays with very large integers.

---

## 🔹 Final Notes

* The **Boyer–Moore Voting Algorithm** is the optimal solution:

  * Linear time (`O(n)`)
  * Constant space (`O(1)`)
* Other methods (sorting, hash map) work but are less efficient in either time or space.

</details>
