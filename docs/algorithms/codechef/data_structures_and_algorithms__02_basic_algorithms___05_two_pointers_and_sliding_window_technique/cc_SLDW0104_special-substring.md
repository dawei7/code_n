# Special Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SLDW0104 |
| Difficulty Rating | 1400 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [SLDW0104](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0104) |

---

## Problem Statement

Chef gave you a string $S$ of size $N$ which contains only lowercase English letters  and asked you to find the length of the longest substring of the string which satisfies the following condition:

- Each character $\beta$ should appear at most $f(\beta)$ times.

Here $f(\beta)$ denotes the index of the character $\beta$ in the alphabet series. For example $f('a')$ = $1$, $f('b')$ = $2$ and so on.

**Note:** A substring of a string is a contiguous subsequence of that string.

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

## Constraints

- $1 \leq T \leq 2500$
- $1 \leq N \leq 10^5, \sum N \leq 5\cdot10^5$
- The string contains only lowercase english letters

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

Problem Link - [Special Substring](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0104)

### [](#problem-statement-1)Problem Statement

Chef gave you a string S of size N which contains only lowercase English letters  and asked you to find the length of the longest substring of the string which satisfies the following condition:

- Each character \beta should appear at most f(\beta) times.

Here f(\beta) denotes the index of the character \beta in the alphabet series. For example f('a') = 1, f('b') = 2 and so on.

**Note:** A substring of a string is a contiguous subsequence of that string.

### [](#approach-2)Approach

The code uses the **sliding window** technique to find the longest valid **substring**. It maintains a frequency map to count occurrences of characters while expanding the right pointer. For each character added, it checks if any character exceeds its allowed frequency based on its position in the alphabet. If so, it adjusts the left pointer to shrink the window until the substring becomes valid again. At each valid state, it updates the **maximum** length found. This efficiently finds the longest substring meeting the character frequency condition.

### [](#time-complexity-3)Time Complexity

O(N) for each test case, where N is the length of the string.

### [](#space-complexity-4)Space Complexity

O(1) since the frequency map can hold at most 26 characters (lowercase letters).

</details>
