# Repeated String Match

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRINGMATCH |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [STRINGMATCH](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/STRINGMATCH) |

---

## Problem Statement

You are given two strings **$A$** and **$B$**, consisting of lowercase English letters.

In one operation, you may repeat string **$A$** any number of times and concatenate the results.

Your task is to find the **minimum number of repetitions** required so that **$B$** appears as a **substring** of the repeated string.

If no such number of repetitions exists, return **$-1$**.

---

### Function Declaration

* **Function Name:**

  * **$repeatedStringMatch$**

* **Parameters:**

  * **$A$** (`string`)
    The base string that can be repeated any number of times.
  * **$B$** (`string`)
    The target string that must appear as a substring.

* **Return Value:**

  * Returns an `int` representing the **minimum number of repetitions** of **$A$** needed so that **$B$** is a substring.
  * Returns **$-1$** if it is impossible.
---

---

## Input Format

The first line contains a single integer **$T$** — the number of test cases.

For each test case:

* The first line contains the string **$A$**.
* The second line contains the string **$B$**.
---

---

## Output Format

For each test case, print a single integer — the **minimum number of repetitions** of **$A$** needed so that **$B$** is a substring, or **$-1$** if it is impossible.

---

## Constraints

* $1 \le T \le 100$
* $1 \le |A|, |B| \le 10^4$
* **$A$** and **$B$** consist of only lowercase English letters.

---

## Examples

**Example 1**

**Input**

```text
2
abcd
cdabcdab
a
aa
```

**Output**

```text
3
2
```

**Explanation**

* **Test Case 1 :**
  Repeating **`"abcd"`** three times gives **`"abcdabcdabcd"`**, which contains **`"cdabcdab"`** as a substring.
  Hence, the minimum number of repetitions required is **`3`**.

* **Test Case 2 :**
  Repeating **`"a"`** two times gives **`"aa"`**, which contains **`"aa"`** as a substring.
  Hence, the minimum number of repetitions required is **`2`**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcd
cdabcdab
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
a
aa
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Statement

You are given two lowercase strings `A` and `B`.\
Your task is to find the **minimum number of times** `A` must be **repeated** so that `B` becomes a **substring** of the repeated string.\
If `B` can’t be a substring of any repetition of `A`, print `-1`.

---

# Intuition

The problem revolves around **repeating A** until it becomes long enough to potentially contain **B** as a substring.

Let’s analyze:

- If `B` is shorter than `A`, it might fit inside one or two concatenations of `A`.

- If `B` is longer, we’ll need to repeat `A` multiple times — at least until the **length of the repeated A ≥ length of B**.

But there's a twist:\
👉 Sometimes `B` overlaps between repetitions of `A`.
That’s why, even after the repeated string’s length exceeds `B`, we must **check one extra repetition**.

---

# Complexity Analysis

| Type      | Complexity |
| --------- | ---------- |
| **Time**  | O(n × m)   |
| **Space** | O(n + m)   |

---

### **Optimal Approach (Knuth-Morris-Pratt / Rabin-Karp)**

#### **Idea**

Instead of physically building a massive string, we can treat the repeated $A$ as an "infinite" stream of characters. We map any index  in this infinite stream to `A[i % A.length]`. We can then use an efficient pattern matching algorithm like **KMP (Knuth-Morris-Pratt)** to search for $B$ within this virtual stream.

#### **Steps**

  1. **LPS Array:** Compute the **Longest Prefix Suffix (LPS)** array for the pattern string $B$ . This array helps us skip unnecessary comparisons when a mismatch occurs.
  2. **Search with Modulo:** Iterate through the "virtual" repeated string $A$. The character at index  is `A[i % A.length]`.
  3. **KMP Matching:** Use the standard KMP logic. If characters match, advance both pointers. If they mismatch, use the LPS array to backtrack the pattern pointer without moving the text pointer back.
  4. **Found:** If the pattern pointer reaches the end of $B$, we have found a match. The number of repetitions is calculated based on the index we reached in the virtual stream.
  5. **Not Found:** If we traverse more than `2 * A.length + B.length` characters without a match, it is mathematically impossible. Return -1.

#### **Explanation**

The "virtual indexing" trick allows us to perform the search without allocating massive memory. The KMP algorithm guarantees that we only traverse the "text" (repeated A) essentially once, making it very fast. The termination limit is proven because if $B$ exists, it must start within the first repetition of $A$ or overlap effectively within the next few.

#### **Example**

**A = "abcd", B = "cdabcdab"**

1. **Length check:**  is length 4.  is length 8. We need at least  repeats.
2. **Virtual Stream:** `a b c d a b c d a b c d ...`
3. **Search:**
  * Match "cd" (indices 2, 3 of A).
  * Match "abcd" (indices 0, 1, 2, 3 of A).
  * Match "ab" (indices 0, 1 of A).
  * Total characters traversed: 10.

4. **Count:** We spanned indices 2 to 9. The max index 9 corresponds to the 3rd repetition (indices 0-3, 4-7, 8-11). So, answer is **3**.

#### **Complexity Analysis**

* **Time Complexity: $O(N + M)$**
  *  $O(M)$ to build the LPS array for $B$.
  *  $O(N + M)$ to search since we traverse a limited length proportional to $A$ and $B$.

* **Space Complexity: $O(M)$**
  * To store the LPS array for $B$.

</details>
