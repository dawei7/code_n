# Find the repeating and missing number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MISSNDREPEAT |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MISSNDREPEAT](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MISSNDREPEAT) |

---

## Problem Statement

You are given multiple test cases. Each test case consists of an integer array $arr$ of size $n$, containing numbers in the range $[1, n]$.
In each test case:

* Exactly **one number appears twice** (the repeating number).
* Exactly **one number is missing** from the range $[1, n]$.

Your task is to return the result for each test case as an array of size 2:

* The first element is the **repeating number**.
* The second element is the **missing number**.

👉 **Important**: You are **NOT allowed to modify the original array**.

## Function Declaration

### Function Name

$findRepeatingAndMissing$ – This function finds the repeating and missing numbers in the given array without modifying it.

### Parameters

* $arr$ : An integer array of size $n$ containing numbers in the range $[1, n]$.

### Return Value

* Returns an array of size `2`:

  * The **first element** is the repeating number.
  * The **second element** is the missing number.

## Constraints

* $1 ≤ T ≤ 10$
* $2 ≤ n ≤ 10^5$
* $n == arr.length$
* $1 ≤ arr[i] ≤ n$
* Exactly one number appears twice.
* Exactly one number is missing.
* The original array must **not** be modified.

---

## Input Format

* The first line contains a single integer `T` — the number of test cases.
* For each test case:

  * The first line contains a single integer `n` — the size of the array.
  * The second line contains `n` space-separated integers representing the array `arr`.

---

## Output Format

* For each test case, print two space-separated integers:

  * The repeating number
  * The missing number

---

## Constraints

* n == arr.length
* 2 <= n <= 10^5
* All numbers in `arr` are in the range `[1, n]`.
* Exactly **one element appears twice**, and exactly **one element is missing**.

---

## Examples

**Example 1**

**Input**

```text
2
5
4 1 2 2 5
7
7 1 3 4 5 6 7
```

**Output**

```text
2 3
7 2
```

**Explanation**

* In the first test case:
The array is `[4, 1, 2, 2, 5]`.
Repeating: `2`
Missing: `3`
* In the second test case:
The array is `[7, 1, 3, 4, 5, 6, 7]`.
Repeating: `7`
Missing: `2`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
4 1 2 2 5
```

**Output for this case**

```text
2 3
```



#### Test case 2

**Input for this case**

```text
7
7 1 3 4 5 6 7
```

**Output for this case**

```text
7 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### **Problem Restatement**

You are given an array of size `n` where numbers are in the range `[1, n]`.

* Exactly **one number appears twice** (the repeating number).
* Exactly **one number from the range `[1, n]` is missing**.

Your goal is to find:

* The **repeating number**.
* The **missing number**.

Return them as an array of size 2: `[repeating, missing]`.

---

#### **Example**

* Input: `[4, 1, 2, 2, 5]`
  Output: `[2, 3]`
  Explanation:

  * The number `2` appears twice.
  * The number `3` is missing.

---

#### **Approach 1: Frequency Counting (Hash Map or Array)**

The simplest and most intuitive way is to:

1. Use a frequency map or frequency array of size `n + 1` (1-based index).
2. Iterate over the input array and count the occurrences of each number.
3. After counting:

   * The number that appears **twice** is the **repeating number**.
   * The number that appears **zero times** is the **missing number**.

This approach has:

* **Time Complexity**: O(n)
* **Space Complexity**: O(n)

---

#### **Approach 2: Mathematical Formula (Sum and Sum of Squares)**

Let the expected sum of numbers from `1` to `n` be:

* `expected_sum = n * (n + 1) / 2`
* `expected_square_sum = n * (n + 1) * (2n + 1) / 6`

Let:

* `actual_sum = sum of all elements in the array`
* `actual_square_sum = sum of squares of all elements in the array`

Then:

* `(repeating - missing) = actual_sum - expected_sum`
* `(repeating^2 - missing^2) = actual_square_sum - expected_square_sum`

Let:

```
diff = repeating - missing
sum_diff = repeating^2 - missing^2 = diff * (repeating + missing)
```

From these two equations, you can solve for the two numbers.

Advantages:

* No extra space needed (O(1) space).
* Time Complexity: O(n)

---

#### **Approach 3: XOR-Based Trick**

1. XOR all array elements and XOR numbers from 1 to n:

   ```
   xor_all = (1 ^ 2 ^ 3 ^ ... ^ n) ^ (arr[0] ^ arr[1] ^ ... ^ arr[n-1])
   ```

   The result will be `repeating ^ missing`.

2. Find a set bit in `xor_all` (to partition into two groups).

3. Split numbers into two groups based on the set bit and XOR separately.

4. At the end, you get the two numbers:

   * One is repeating.
   * The other is missing.

Finally, determine which is which by scanning the array.

Advantages:

* Time Complexity: O(n)
* Space Complexity: O(1)

---

#### **Why Frequency Approach Is Used in This Solution**

* Easy to implement and understand.
* Direct and straightforward for competitive programming.
* Avoids tricky math or bit manipulation, especially when dealing with large numbers (avoiding overflow).
* Suitable when constraints allow O(n) extra space.

---

#### **Time & Space Complexity**

| Approach             | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| Frequency Counting   | O(n)            | O(n)             |
| Mathematical Formula | O(n)            | O(1)             |
| XOR Trick            | O(n)            | O(1)             |

---

#### **Conclusion**

* For most practical cases, frequency counting is fine and safe.
* For large-scale constraints where extra space matters, prefer XOR or Mathematical formula approaches.

</details>
