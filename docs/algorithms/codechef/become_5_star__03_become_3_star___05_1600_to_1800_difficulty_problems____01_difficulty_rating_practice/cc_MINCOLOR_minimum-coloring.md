# Minimum Coloring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINCOLOR |
| Difficulty Rating | 1713 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MINCOLOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MINCOLOR) |

---

## Problem Statement

There is a matrix of size $N \times M$. Two **distinct** cells of the matrix $(x_1, y_1)$ and $(x_2, y_2)$ are painted with colors $\text{1}$ and $\text{2}$ respectively.

You have to paint the **remaining** cells of the matrix such that:
- No two adjacent cells are painted in same color.
- Each color is an integer from $1$ to $10^9$ (both inclusive).
- The number of **distinct** colors used is **minimum** (including $\text{1}$ and $\text{2}$).

**Note**:
1. You cannot repaint the cells $(x_1, y_1)$ and $(x_2, y_2)$.
2. Two cells are adjacent if they share a common edge. Thus, for a cell $(x,y)$ there are $4$ adjacent cells. The adjacent cells are $(x, y+1), (x, y-1), (x+1,y),$ and $(x-1,y)$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow. Each test case consists of $3$ lines.
- The first line contains two space seperated integers $N$ and $M$ denoting the dimensions of the matrix.
- The second line contains two integers $x_1$ and $y_1$, denoting the coordinates of cell which is painted $\text{1}$.
- The third line contains two integers $x_2$ and $y_2$, denoting the coordinates of cell which is painted $\text{2}$.

---

## Output Format

For each test case, output $N$ lines, each consisting of $M$ space separated integers where $j^{th}$ integer in $i^{th}$ line denotes the color of cell in $i^{th}$ row and $j^{th}$ column of the matrix and must be in $[1, 10^9]$ inclusive.

In case of multiple possible answers, output any.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N, M \leq 10^5$
- $1 \leq x_1, x_2 \leq N$
- $1 \leq y_1, y_2 \leq M$
- $(x_1, y_1) \neq (x_2, y_2)$
- Sum of $N \cdot M$ over all test cases does not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2 2
1 1
2 2
2 3
1 1
1 2
```

**Output**

```text
1 4
4 2
1 2 1
2 1 2
```

**Explanation**

**Test Case $1$:**
![](https://s3.amazonaws.com/codechef_shared/download/Images/START30/Sample1.png)
The initially painted cells are $(1,1)$ and $(2,2)$. One possible way is to paint the remaining cells with color $4$. This way, no two adjacent cells have the same color.
Note that, instead of color $4$, we can use any other color in the range $[1, 10^9]$ except colors $1$ and $2$.
The number of distinct colors used in this case is $3$. It can be shown that the minimum number of distinct colors cannot be less than $3$.

**Test Case $2$:**
![](https://s3.amazonaws.com/codechef_shared/download/Images/START30/Sample2.png)
The initially painted cells are $(1,1)$ and $(1,2)$. One possible way is to paint the remaining cells as shown in the figure. This way, no two adjacent cells have the same color.
The number of distinct colors used in this case is $2$. It can be shown that the minimum number of distinct colors cannot be less than $2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START30A/problems/MINCOLOR)

[Contest Division 2](https://www.codechef.com/START30B/problems/MINCOLOR)

[Contest Division 3](https://www.codechef.com/START30C/problems/MINCOLOR)

[Contest Division 4](https://www.codechef.com/START30D/problems/MINCOLOR)

Setter: [Kushagra Goel](https://www.codechef.com/users/kugo)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There is a matrix of size N \times M. Two **distinct** cells of the matrix (x_1, y_1) and (x_2, y_2) are painted with colors \text{1} and \text{2} respectively.

You have to paint the **remaining** cells of the matrix such that:

- No two adjacent cells are painted in same color.

- Each color is an integer from 1 to 10^9 (both inclusive).

- The number of **distinct** colors used is **minimum** (including \text{1} and \text{2}).

**Note**:

- You cannot repaint the cells (x_1, y_1) and (x_2, y_2).

- Two cells are adjacent if they share a common edge. Thus, for a cell (x,y) there are 4 adjacent cells. The adjacent cells are (x, y+1), (x, y-1), (x+1,y), and (x-1,y).

#
[](#explanation-5)EXPLANATION:

Let us define the parity of a cell (x,y) as the parity of x+y. So, (5 , 1) is an even cell, whereas (4 , 1) is an odd cell. Consider a cell (x,y). Observe that if (x,y) is an even cell, then all the cells adjacent to (x,y) will be odd cells. Similarly, if (x,y) is an odd cell, then all the cells adjacent to (x,y) will be even cells. This property is useful while solving many grid related problems.

Consider the problem when none of the cells were already painted. In that case, we could have painted all the even cells by 1 and all the odd cells by 2. Note that the above coloring satisfies all the required properties.

Now if one of the cell (x, y) was already painted as 1, we could have assigned that color to all the cells having same parity as that of (x, y), and color 2 to the remaining opposite parity cells.

In the above problem, we are given two cells: (x_1, y_1) with color 1, and (x_2, y_2) with color 2. If the parity of both these cells are same, we can assign either color 1 or 2 to all the cells having same parity as these cells, and color 3 to all the remaining cells. We have used 3 distinct colors in this case.

If the parity of both these cells are different, we can assign color 1 to all the cells having same parity as that of (x_1, y_1), and color 2 to all the remaining cells (having same parity as that of (x_2, y_2)). We have used 2 distinct colors in this case.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N \cdot M) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#define ll long long
#define fo(i , n) for(ll i = 0 ; i < n ; i++)
#include<bits/stdc++.h>
using namespace std ;

void solve()
{
    ll n , m ;
    cin >> n >> m ;

    ll x1 , y1 , x2 , y2 ;
    cin >> x1 >> y1 >> x2 >> y2 ;

    x1-- ; y1-- ; x2-- ; y2-- ; // making the indices 0-based

    ll col[2] ; // col[0]: color on even-sum cells. col[1]: color on odd-sum cells.

    ll p1 = (x1 + y1)%2 ; // parity of first cell
    ll p2 = (x2 + y2)%2 ; // parity of second cell

    if(p1 == 0 && p2 == 0)
    {
        col[0] = 1 ; // can use either 1 or 2.
        col[1] = 3 ; // can't use 2 as it is used on an even-sum cell.
    }

    if(p1 == 0 && p2 == 1)
    {
        col[0] = 1 ;
        col[1] = 2 ; // the given colors can be used directly.
    }

    if(p1 == 1 && p2 == 0)
    {
        col[0] = 2 ;
        col[1] = 1 ; // the given colors can be used directly.
    }

    if(p1 == 1 && p2 == 1)
    {
        col[0] = 3 ; // can't use 1 or 2 as they are used on an odd-sum cell.
        col[1] = 1 ; // can use either 1 or 2.
    }

    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < m ; j++)
        {
            if(i == x1 && j == y1)
            {
                cout << 1 << ' ';
                continue ;
            }

            if(i == x2 && j == y2)
            {
                cout << 2 << ' ';
                continue ;
            }

            cout << col[(i+j)%2] << ' ' ;
        }
        cout << '\n' ;
    }
    return ;
}

int main()
{

    ll t = 1 ;
    cin >> t ;
    while(t--)
    {
        solve() ;
    }

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";

    return 0;
}
``

</details>
