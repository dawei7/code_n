# Sum of Beauty of All Substrings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSTRINGSUM |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [SUBSTRINGSUM](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/SUBSTRINGSUM) |

---

## Problem Statement

You are given a string **$S$** consisting of lowercase English letters.

The **beauty** of a substring is defined as the difference between the frequency of the **most frequent character** and the frequency of the **least frequent character** in that substring, considering **only characters that appear at least once**.

Your task is to calculate the **sum of beauty** of all possible substrings of the given string **$S$**.

---

### Function Declaration

* **Function Name:**

  * **$beautySum$**

* **Parameters:**

  * **$s$** (`string`)
    A string consisting of lowercase English letters.

* **Return Value:**

  * Returns an `int` representing the **sum of beauty of all substrings** of the string.

---

---

## Input Format

The first line contains an integer **$T$** — the number of test cases.

Each test case contains a single line with the string **$S$**.

---

---

## Output Format

For each test case, print a single integer — the **sum of beauty of all substrings** of **$S$**.

---

---

## Constraints

* $1 \le T \le 100$
* $1 \le |S| \le 500$
* **$S$** consists of only lowercase English letters.

---

## Examples

**Example 1**

**Input**

```text
2
abcab
zzxyzz
```

**Output**

```text
3
12
```

**Explanation**

For **`abcab`**, substrings contributing non-zero beauty are `bcab`, `abca`, and `abcab`, giving a total beauty of **3**.

For **`zzxyzz`**, the total beauty across all substrings is **12**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abcab
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
zzxyzz
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

Chef is given a string **S** consisting of lowercase English letters.\
The **beauty** of a substring is defined as the **difference between** the frequency of the most frequent character and the frequency of the least frequent character in that substring (considering only characters that appear at least once).

Your task is to calculate the **sum of beauty of all possible substrings** of the given string **S**

---

# Intuition

To find the **beauty sum** of all substrings, we must analyze **every substring** of **S**.

For each substring:

- Count the **frequency** of each character.
- Find the **maximum frequency** (`maxFreq`) and **minimum frequency** (`minFreq`) among characters that appear at least once.

- The **beauty** of this substring = `maxFreq - minFreq`.

We sum up the beauty for **all substrings**.

To do this efficiently, instead of recomputing frequencies from scratch for every substring, we **expand the substring gradually and update frequencies dynamically**.

---

# Algorithm

Initialize `total = 0`.

For each starting index `i` in the string S:
- Create an array `freq[26]` to store character frequencies (all initialized to 0).

For each ending index `j` from `i` to `n - 1`:
- Increment the frequency of `S[j]`.
- Find the **maximum and minimum** frequencies among characters with frequency > 0.
- Add (`maxFreq - minFreq`) to `total`.

After iterating through all substrings, **return** `total`.

---

# Complexity Analysis

| Type                 | Explanation                                                                                                                      | Complexity |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **Time Complexity**  | Two nested loops over the string (`O(N²)`), and in each inner loop, we scan 26 letters (`O(26)`), giving **O(26 × N²) ≈ O(N²)**. | **O(N²)**  |
| **Space Complexity** | We use a fixed-size frequency array of length 26.                                                                                | **O(1)**   |

</details>
