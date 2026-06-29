# Single number in multiple numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SINGLENUM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SINGLENUM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/SINGLENUM) |

---

## Problem Statement

You are given a **non-empty** array of integers $nums$.
In this array, every number occurs **exactly twice** except for one number that occurs only once.
Your task is to find and return that unique number.

The solution must run in **O(n)** time complexity and use **O(1)** space complexity.

##  **Function Declaration**

### **Function Name**

$singleNumber$ – Finds the one number in the array that appears exactly once while all other numbers appear twice.

### **Parameters**

* $nums$ : A list/array of integers where every value appears exactly twice except one.

### **Return Value**

* Returns an **integer** — \
  the unique number that appears only once.

## Constraints:

- $1 \leq nums.length \leq 3 * 10^4$
- $-3 * 10^4 \leq nums[i] \leq 3 * 10^4$
- Exactly one element in the array appears once, and all others appear twice.

---

## Input Format

* $N$ → number of elements in the array
* Next line → **N integers** representing $nums$

---

## Output Format

* Print the single number that appears exactly once.

---

## Examples

**Example 1**

**Input**

```text
3
1
10
5
9 1 9 2 1
5
7 3 5 3 7
```

**Output**

```text
10
2
5
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
10
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
5
9 1 9 2 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
7 3 5 3 7
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

You are given an array of integers where **every element appears exactly twice except for one element** that appears **once**. The task is to find the unique element.

**Constraints:**

* Linear runtime is required (`O(n)`).
* Constant extra space (`O(1)`).

---

## Key Observations

1. **Duplicates cancel out**
   Any element appearing **twice** can cancel itself in certain operations that are **associative and commutative**, such as XOR.

2. **XOR properties** (core idea for the optimal solution):

   * `x ^ x = 0` → XOR of a number with itself is 0
   * `x ^ 0 = x` → XOR of a number with 0 is the number itself
   * XOR is **commutative and associative**, so the order of operations does not matter

These properties imply that if you XOR **all elements of the array**, the duplicates will cancel out, leaving the unique element.

---

## Approach

1. Initialize a variable `result` to 0.
2. Iterate through the array:

   * For each element `num`, update `result = result XOR num`.
3. After processing the entire array, `result` will contain the single number.

**Why it works:**

* Every element that appears twice will XOR to 0.
* The element that appears once will remain because `0 XOR unique = unique`.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each element is visited once.
* **Space Complexity:** `O(1)`

  * Only a single variable is used for XOR accumulation.

---

## Examples

1. **Input:** `[2, 2, 1]`
   **XOR computation:** `0 ^ 2 ^ 2 ^ 1 = 1` → **Output:** `1`

2. **Input:** `[4, 1, 2, 1, 2]`
   **XOR computation:** `0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4` → **Output:** `4`

3. **Input:** `[1]`
   **XOR computation:** `0 ^ 1 = 1` → **Output:** `1`

---

## Notes / Edge Cases

* The array will always have **exactly one unique element**, otherwise the XOR trick gives the XOR of all single occurrences.
* Works for **negative numbers** as well because XOR operates at the bit level.
* Optimal for **large arrays** (up to `10^4`–`3*10^4`) due to its linear runtime and constant space.

---

## Conclusion

* The XOR method is elegant, concise, and optimal for this problem.
* It leverages the **mathematical properties of XOR** rather than using extra memory structures like hash maps or sets.

</details>
