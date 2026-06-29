# Chef Solves Word Break

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TXBCN01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [TXBCN01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/TXBCN01) |

---

## Problem Statement

Chef has a string of lowercase English letters $inputString$ and a list of dictionary words $dictionaryWords$. \
Chef wants to determine if it is possible to segment the entire string into a sequence of one or more words from the dictionary. The same dictionary word can be used multiple times in the segmentation. Help Chef decide whether such a segmentation exists.

## Function Declaration

### Function Name
$canSegmentString$ - This function determines whether the given text string can be segmented into a sequence of one or more dictionary words.

### Parameters
- $inputString$ : The text string to be segmented. It consists of lowercase English letters.
- $dictionaryWords$ : A reference to a array containing the list of valid dictionary words. Each word consists of lowercase English letters.

### Return Value
- Returns a boolean indicating if the segmentation is possible.
- $true$ means the string can be segmented into dictionary words; $false$ means it cannot.

## Constraints
- $1 \leq T \leq 10$
- $1 \leq |inputString| \leq 300$
- $1 \leq |\text{dictionaryWords}| \leq 1000$
- $1 \leq |\text{dictionaryWords}[i]| \leq 20$ for each valid $i$
- All characters in `inputString` and `dictionaryWords[i]` are lowercase English letters.
- All strings in `dictionaryWords` are unique.

**The input and output formats given below are only if you want to test using custom inputs.**

---

## Input Format

- The first line contains an integer $T$, the number of test cases.
- For each test case:
  - The second line contains the string $inputString$ that Chef wants to segment.
  - The next line contains all the dictionary words.

---

## Output Format

For each test case, print a single line containing 1 if Chef can segment the string into dictionary words, or 0 otherwise. Help Chef by providing the correct answer for each test case.

---

## Examples

**Example 1**

**Input**

```text
2
catsdo
["cats", "dog", "sand", "and"]
pineapplepen
["apple", "pen", "pineapple"]
```

**Output**

```text
0
1
```

**Explanation**

- T1: "catsdo" cannot be segmented into any combination of "cats", "dog", "sand", or "and".
- T2: "pineapplepen" can be segmented as "pineapple" + "pen".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
catsdo
["cats", "dog", "sand", "and"]
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
pineapplepen
["apple", "pen", "pineapple"]
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## 1. Problem Breakdown

You are given a text string `inputString` consisting of lowercase English letters and a list of valid dictionary words `dictionaryWords`.

Your task is to determine whether `inputString` can be segmented into a sequence of **one or more dictionary words**, where:

* Each segment must exactly match a word from `dictionaryWords`
* A dictionary word may be used **multiple times**
* The entire string must be covered (no leftover characters)

If such a segmentation exists, return `true`; otherwise, return `false`.

For example:

* `inputString = "applepie"`
* `dictionaryWords = ["apple", "pie"]`

The string can be segmented as `"apple" + "pie"`, so the answer is `true`.

---

## 2. Approach 1 — Brute Force (Recursive)

### Idea

Try all possible ways to split the string and check whether every resulting substring belongs to the dictionary.

At every position in the string:

* Try all possible prefixes starting at that position
* If a prefix is in the dictionary, recursively attempt to segment the remaining suffix
* If you reach the end of the string successfully, return `true`

If no valid split exists, return `false`.

---

### Step-by-Step Reasoning

1. Start from index `0`
2. Try all substrings `inputString[0:1]`, `inputString[0:2]`, ..., up to the full string
3. If a substring exists in `dictionaryWords`, recursively check the remaining part
4. If the recursion reaches the end of the string, segmentation is possible
5. If all possibilities fail, return `false`

---

### Dry Run Example

`inputString = "catsand"`
`dictionaryWords = ["cat", "cats", "and", "sand"]`

* Start at index `0`

  * `"c"` → not in dictionary
  * `"ca"` → not in dictionary
  * `"cat"` → valid

    * Remaining string `"sand"`

      * `"sand"` → valid

        * End reached → return `true`

---

### Limitations

* Exponential number of recursive calls
* Same substrings are recomputed multiple times
* Not feasible for large inputs

---

## 3. Approach 2 — Optimized Brute Force (Top-Down DP / Memoization)

### Optimization Idea

Store the result of subproblems to avoid recomputation.

Instead of checking the same suffix multiple times, cache whether a substring starting at a given index can be segmented.

---

### How It Works

* Use a recursive function `solve(startIndex)`
* If `startIndex == inputString.length`, return `true`
* If the result for `startIndex` is already cached, return it
* Try all dictionary word matches starting at `startIndex`
* Cache and return the result (`true` or `false`)

---

### Complexity Analysis

Let `n = length of inputString`

* **Time Complexity:**
  `O(n²)` when dictionary lookup is optimized (hash set or word-length bound)

* **Space Complexity:**
  `O(n)` for memoization + recursion stack

---

### Important Note on `substr()`

In C++, `substr()` creates a new string and copies characters.

* Each call costs `O(k)` time and space, where `k` is substring length
* This **does not change the asymptotic auxiliary space** (`O(n)`),
  but it **increases constant factors and real memory usage**

To avoid this, comparisons should be done using:

* `string::compare`
* word-length bounds
* or a Trie

---

## Summary

| Approach               | Time Complexity | Space Complexity | Remarks                 |
| ---------------------- | --------------- | ---------------- | ----------------------- |
| Brute Force            | Exponential     | O(n)             | Too slow                |
| Memoization (Top-Down) | O(n²)           | O(n)             | Avoids recomputation    |

</details>
