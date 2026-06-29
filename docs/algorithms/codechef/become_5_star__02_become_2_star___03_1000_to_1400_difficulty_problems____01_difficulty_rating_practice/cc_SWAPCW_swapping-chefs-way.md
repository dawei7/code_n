# Swapping Chefs Way

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SWAPCW |
| Difficulty Rating | 1238 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SWAPCW](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SWAPCW) |

---

## Problem Statement

Chef is working on his swap-based sorting algorithm for strings.

Given a string $S$ of length $N$, he wants to know whether he can sort the string using his algorithm.

According to the algorithm, one can perform the following operation on string $S$ any number of times:
- Choose some index $i$ $(1 \leq i \leq N)$ and swap the $i^{th}$ character from the front and the $i^{th}$ character from the back.
More formally, choose an index $i$ and swap $S_i$ and $S_{(N+1-i)}$.

For example, $\underline{\texttt{d}} \texttt{cb} \underline{\texttt{a}}$ can be converted to $\underline{\texttt{a}} \texttt{cb} \underline{\texttt{d}}$ using one operation where $i = 1$.

Help Chef find if it is possible to sort the string using **any** (possibly zero) number of operations.

---

## Input Format

- The first line of the input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains $N$, the length of the string.
- The second line contains a string $S$ of length $N$ consisting of lowercase letters of the Latin alphabet.

---

## Output Format

For each test case, print $\texttt{YES}$ if it is possible to sort the string by performing **any** number of operations. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^3$
- Sum of $N$ over all test cases does not exceed $2\cdot10^3$.
- $S$ consists of lowercase Latin alphabets only.

---

## Examples

**Example 1**

**Input**

```text
3
4
dbca
3
ccc
3
bza
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test case $1$:** Chef can sort the string using $1$ operation.
- Choose $i = 1$ and swap $S_1 = \texttt{d}$ and $S_4 = \texttt{a}$.
This way, the string becomes $\texttt{abcd}$.

Hence, the string is sorted.

**Test case $2$:** Chef needs $0$ operations to sort this string as it is already sorted.

**Test case $3$:** It can be proven that the given string **cannot** be sorted using any number of operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
dbca
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3
ccc
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
3
bza
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Swapping Chefs Way Practice Problem in 1000 to 1400 difficulty problems](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SWAPCW)

### [](#problem-statement-1)Problem Statement:

Given a string `S` of length `N`, he wants to know whether he can sort the string using his algorithm. According to the algorithm, one can perform the following operation on string `S` any number of times:

Choose some index `i` `(1≤i≤N)` and swap the `i-th` character from the front and the `i-th` character from the back. More formally, choose an index `i` and swap `S(i)` and `S(N+1−i)`. Help Chef find if it is possible to sort the string using any (possibly zero) number of operations.

### [](#approach-2)Approach:

**Steps:**

- Make copy of input string (to compare with the sorted version).

- Iterate over the first half of the string and swap characters in pairs of symmetric positions (i.e., for `i` from `0` to `N/2 - 1`, swap `S[i]` and `S[N-i-1]` if `S[i] > S[N-i-1]`).

- Finally, check if the modified string is equal to the sorted string.

- If yes, print `"YES"`, otherwise print `"NO"`.

### [](#complexity-3)Complexity:

- **Time Complexity:** Sorting the string takes `O(N log N)`. The loop for swapping characters runs in `O(N/2)`, which is effectively `O(N)`. Hence, the time complexity for each test case is `O(N log N)`,

- **Space Complexity:** `O(N)` as we are storing the input string in another string.

</details>
