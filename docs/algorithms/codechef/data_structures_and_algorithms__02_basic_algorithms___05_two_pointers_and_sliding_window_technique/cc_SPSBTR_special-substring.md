# Special Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPSBTR |
| Difficulty Rating | 1400 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [SPSBTR](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SPSBTR) |

---

## Problem Statement

Chef gave you a string $S$ of size $N$ which contains only lowercase English letters  and asked you to find the length of the longest substring of the string which satisfies the following condition:

- Each character $\beta$ should appear at most $f(\beta)$ times.

Here $f(\beta)$ denotes the index of the character $\beta$ in the alphabet series. For example $f('a')$ = $1$, $f('b')$ = $2$ and so on.

**Note:** A substring of a string is a contiguous subsequence of that string.

## Function Declaration

### Function Name

$longestValidSubstring$ – This function finds the length of the longest substring such that each character appears at most a limited number of times based on its alphabetical position.

### Parameters

* $s$ : A reference to a string containing only lowercase English letters.
  Represents the input string from which the substring is selected.

### Return Value

* Returns an integer representing the **maximum length** of a valid substring where:

  * Each character `β` appears **at most `f(β)` times**
  * `f(β)` is the **1-based alphabetical index** of the character
    (e.g., `a → 1`, `b → 2`, ..., `z → 26`)

## Constraints

- $1 \leq T \leq 2500$
- $1 \leq N \leq 10^5, \sum N \leq 5\cdot10^5$
- The string contains only lowercase english letters

---

## Input Format

- First-line will contain $T$ - the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the size of the string.
- The second line of every test case contains a string $S$ of size $N$.

---

## Output Format

For each testcase, output in a single line - the answer to the $i$-th test case.

---

## Examples

**Example 1**

**Input**

```text
2
6
jyjerm
4
abbb
```

**Output**

```text
6
3
```

**Explanation**

- **Test Case $1$**: Every character appears less than its index in the English alphabet so we can consider the entire string.

- **Test Case $2$**: We can consider 'b' at most 2 times, therefore, the answer is $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
jyjerm
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
4
abbb
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Overview

You are given a string consisting of lowercase English letters. For any substring to be considered **valid**, each character `β` in that substring must appear **at most `f(β)` times**, where `f(β)` is the 1-based position of the character in the English alphabet (`a → 1`, `b → 2`, …, `z → 26`).

Your task is to determine the **maximum possible length** of such a valid substring.

---

### Key Observations

* The constraint on each character is **fixed and independent** of the substring length.
* We are dealing with **contiguous substrings**, which naturally suggests a two-pointer or sliding window approach.
* If a substring becomes invalid due to excess frequency of a character, shrinking it from the left is the only way to restore validity.

---

### Approach: Sliding Window (Two Pointers)

We maintain a window `[left, right]` that always represents a valid substring.

#### Data Tracked

* A frequency counter for characters currently in the window.
* Two pointers:

  * `left`: start of the window
  * `right`: end of the window
* A variable to track the maximum valid window size seen so far.

---

### Step-by-Step Logic

1. **Expand the window**

   * Move `right` forward one character at a time.
   * Increase the frequency of the newly included character.

2. **Validate the constraint**

   * For the character just added, check if its frequency exceeds its allowed limit (`alphabet index`).
   * If it does, the window is no longer valid.

3. **Shrink the window**

   * Move `left` forward while decreasing frequencies.
   * Continue shrinking until the constraint is satisfied again.

4. **Update the answer**

   * After restoring validity, update the maximum window length using:

     ```
     right - left + 1
     ```

5. **Repeat**

   * Continue until the end of the string is reached.

---

### Why This Works

* Each character is added to the window once and removed once.
* The window always maintains validity before updating the answer.
* No redundant reprocessing occurs, making the method efficient.

---

### Time Complexity

* **O(N)** per test case
  Each character is processed at most twice (once by `right`, once by `left`).

### Space Complexity

* **O(1)**
  Only a fixed-size character frequency structure is needed (at most 26 lowercase letters).

---

### Example Walkthrough

For the string `"abbb"`:

* `'a'` can appear at most `1` time
* `'b'` can appear at most `2` times

Sliding window progression identifies `"abb"` as the longest valid substring, with length `3`.

---

### Final Notes

This problem is a classic example of:

* Fixed frequency constraints
* Longest valid contiguous segment
* Efficient window maintenance using two pointers

The sliding window technique ensures optimal performance while maintaining clarity and correctness.

</details>
