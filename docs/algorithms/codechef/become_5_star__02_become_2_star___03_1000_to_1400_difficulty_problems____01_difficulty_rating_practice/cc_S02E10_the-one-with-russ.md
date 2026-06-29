# The One with Russ

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | S02E10 |
| Difficulty Rating | 1230 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [S02E10](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/S02E10) |

---

## Problem Statement

*Rachel has a date and tells everyone she is not mad at Ross but doesn't have any feelings for him anymore either. Seeing her date for the first time, everyone notices that he looks exactly like Ross. However, Rachel refuses to believe so.*

Rachel makes a list of $N$ characteristics and assigns a score to both Ross and Russ for each of the characteristics. Ross' $i^{th}$ characteristic has a score equal to $A_i$ and Russ' $i^{th}$ characteristic has a score equal to $B_i$. Rachel decides that Russ looks exactly like Ross if the following condition is satisfied for at least $X$ distinct values of $j$, $1 \leq j \leq N$ :

- $|A_j - B_j| \leq K$.

Help Rachel in finding if both are alike.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line for each test case contains three integers $N$, $X$ and $K$, denoting the number of characteristics, the minimum number of characteristics  and maximum possible score difference.
- Second line for each test case contains $N$ integers denoting array $A$.
- Third line for each test case contains $N$ integers denoting array $B$.

---

## Output Format

For each test case print "YES" if they are alike, else print "NO".

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^3$
- $1 \leq A_i, B_i \leq 10^3$
- $1 \leq X \leq n$
- $0 \leq K \leq 10^3$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 2
1 7 7 5
1 8 1 2
5 1 3
9 8 7 2 5
5 4 1 8 9
3 3 0
2 3 4
2 3 4
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case 1**: The values of absolute difference between scores of Ross' and Russ' characteristics $1$ and $2$ are $0$ and $1$ respectively, both these values are less than $K = 2$. Thus, Ross and Russ are alike.

**Test case 2**: The values of absolute difference between the scores of *ALL* of the Ross' and Russ' characteristics are greater than $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 2
1 7 7 5
1 8 1 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5 1 3
9 8 7 2 5
5 4 1 8 9
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
3 3 0
2 3 4
2 3 4
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 3](https://www.codechef.com/FOUR21C/problems/S02E10)

**Setter:** [ Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [ Nishant Shah](https://www.codechef.com/users/nishant403)

**Editorialist:** [ Shivam Thakur](https://www.codechef.com/users/thakur_01)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

Basic-implementation skills

#
[](#problem-4)PROBLEM

Given two arrays A and B of length N, along with 2 integers X and K. You need to find if the number of indices for which abs(A[i] - B[i]) <= K exceeds X or not.

#
[](#explanation-5)EXPLANATION

This problem uses a simple implementation of comparing values.

You can use a for loop to count the number of indices for which abs(A[i] - B[i]) <= K. Then compare the count with X. If the count is greater than or equal to X, print “Yes”, else print “No”.

#
[](#time-complexity-6)TIME COMPLEXITY

O(N)                                                where N is the size of arrays

#
[](#solutions-7)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while(t--){
        int n, x, k;
        cin >> n >> x >> k;
        int a[n], b[n];
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        for(int i = 0; i < n; i++){
            cin >> b[i];
        }
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(abs(a[i] - b[i]) <= k){
                cnt++;
            }
        }
        if(cnt >= x){
            cout << "YES\n";
        }else{
            cout << "NO\n";
        }
    }

    return 0;
}
``

</details>
