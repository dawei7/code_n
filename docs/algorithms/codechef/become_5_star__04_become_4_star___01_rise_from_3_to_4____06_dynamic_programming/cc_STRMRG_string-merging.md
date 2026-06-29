# String Merging

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRMRG |
| Difficulty Rating | 1965 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [STRMRG](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/STRMRG) |

---

## Problem Statement

For a string **S**, let's define a function **F**(**S**) as the minimum number of blocks consisting of consecutive identical characters in **S**. In other words, **F**(**S**) is equal to 1 plus the number of valid indices **i** such that **Si** ≠ **Si+1**.

You are given two strings **A** and **B** with lengths **N** and **M** respectively. You should merge these two strings into one string **C** with length **N+M**. Specifically, each character of **C** should come either from **A** or **B**; all characters from **A** should be in the same relative order in **C** as in **A** and all characters from **B** should be in the same relative order in **C** as in **B**.

Compute the minimum possible value of **F**(**C**).

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **M**.

- The second line contains a single string **A** with length **N**.

- The third line contains a single string **B** with length **M**.

### Output

For each test case, print a single line containing one integer — the minimum possible value of **F**(**C**).

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **N**, **M** ≤ 5,000

- 1 ≤ sum of **N** in all test cases ≤ 5,000

- 1 ≤ sum of **M** in all test cases ≤ 5,000

- strings **A**, **B** consist only of lowercase English letters

### Subtasks

**Subtask 1 (10 points):** 1 ≤ **T**, **N**, **M** ≤ 10

**Subtask 2 (20 points):** the characters of **A** and **B** are sorted in non-decreasing order

**Subtask 3 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
4 4
abab
baba
```

**Output**

```text
5
```

**Explanation**

**Example case 1:** One possible way to choose the string **C** to get the desired answer is "abbaabba".

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/STRMRG)

[Contest](http://www.codechef.com/JAN18/problems/STRMRG)

**Author:** [Hasan Jaddouh](http://www.codechef.com/users/kingofnumbers)

**Tester:** [Alexey Zayakin](http://www.codechef.com/users/alex_2oo8)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

### DIFFICULTY:

EASY

### PREREQUISITES:

Dynamic programming

### PROBLEM:

You’re given two strings A and B. You have to merge those strings into string C in such a way that amount of valid indices i such that C_i \neq C_{i+1} is minimized.

### QUICK EXPLANATION

Use 2 \cdot n \cdot m dynamic programming to mark length of merged prefixes and string from which you took last letter.

### EXPLANATION:

This problem is straightforward if you use dynamic programming of following form:

DP[pos1][pos2][lastchar]=\text{answer if you merged prefixes $A_{pos_1}$ and $B_{pos_2}$ and last character was from string $lastchar$}

You can implement it in the following manner:

``int sz[2];
cin >> sz[0] >> sz[1];
string a[2];
cin >> a[0] >> a[1];
int dp[sz[0] + 1][sz[1] + 1][2];
memset(dp, 0x3F, sizeof(dp));
dp[1][0][0] = dp[0][1][1] = 1;
int idx[2];
for(idx[0] = 0; idx[0] <= sz[0]; idx[0]++) {
    for(idx[1] = 0; idx[1] <= sz[1]; idx[1]++) {
        for(int pz = 0; pz <= 1; pz++) {
            for(int nz = 0; nz <= 1; nz++) {
                if(idx[nz] < sz[nz] && idx[pz] > 0) {
                    int ndx[2] = {idx[0] + !nz, idx[1] + nz};
                    dp[ndx[0]][ndx[1]][nz] = min(dp[ndx[0]][ndx[1]][nz],
                        dp[idx[0]][idx[1]][pz] + (a[nz][idx[nz]] != a[pz][idx[pz] - 1]));
                }
            }
        }
    }
}
cout << min(dp[sz[0]][sz[1]][0], dp[sz[0]][sz[1]][1]) << endl;
``

Note that it should be 2 \cdot 2 \cdot n \cdot m and not 26 \cdot n \cdot m since the last one will not fit into TL.

In the code above we consider that we already merged prefixed A_{idx_1} and B_{idx_2}. Variable pz indicates if we had character from A (in case pz=0) or from B (in case pz=1) on the top before adding new character and nz indicates from which string we added new character (same way as pz). After that new character we can assume that we merged prefixed A_{ndx_1} and B_{ndx_2}. Answer for DP[ndx_1][ndx_2][nz] can be relaxed by answer for DP[idx_1][idx_2][pz] plus one if old top character and new top character do not match.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN18/Setter/STRMRG.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN18/Tester/STRMRG.cpp).

### RELATED PROBLEMS:

</details>
