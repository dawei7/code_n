# Linear Search using Recursion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR09 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR09](https://www.codechef.com/learn/course/recursion/LRECUR02/problems/RECUR09) |

---

## Problem Statement

You are given an array $Arr$ and an integer $X$. You have to search the array $Arr$ and check if $X$ exists in $Arr$ or not, if yes print the first position of $X$ else print $-1$.

---

## Input Format

- The first line contains two integers $N$ and $X$ - denoting the number of elements in $Arr$ and the number to search in the array.
- The second line contains $N$ integers.

---

## Output Format

Output the first index of $X$ in $Arr$ if it exists, else output $-1$.

---

## Constraints

- $1 \leq N \leq 10^5$.
- $1 \leq A_i \leq 10^5$.
- $1 \leq X\leq 10^5$.

---

## Examples

**Example 1**

**Input**

```text
5 9
1 4 9 2 8
```

**Output**

```text
2
```

**Example 2**

**Input**

```text
3 1
2 3 4
```

**Output**

```text
-1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Linear Search using Recursion in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR02/problems/RECUR09)

### [](#problem-statement-1)Problem Statement:

You are given an array Arr and an integer X. You have to search the array Arr and check if X exists in Arr or not, if yes print the first position of X else print −1.

### [](#approach-2)Approach

- **Base Case**: If `index` is greater than or equal to `n` (the size of the array), it means we have checked all elements without finding X. Therefore, we return `-1` to indicate that the target value is not present in the array.

- **Check Current Element**: If the current element at `arr[index]` matches X Return `index` because we have found the target value.

- **Recursive Call**: If the current element does not match X, make a recursive call to function with the next index (`index + 1`). This means we will check the next element in the array.

- **Start the Search**: In the `main()` function, we initialize the search by calling the function with `index` set to `0` (the first element of the array).

### [](#complexity-3)Complexity:

-

**Time Complexity:** `O(N)` We might need to check every element in the array once if X is either the last element or not present at all.

-

**Space Complexity:** `O(N)` if the array length is N and X is not found, we will have N recursive calls stacked on the call stack.

</details>
