# Consecutive Adding

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONSADD |
| Difficulty Rating | 2038 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CONSADD](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CONSADD) |

---

## Problem Statement

You are given two matrices $A$ and $B$, each with $R$ rows (numbered $1$ through $R$) and $C$ columns (numbered $1$ through $C$). Let's denote an element of $A$ or $B$ in row $i$ and column $j$ by $A_{i,j}$ or $B_{i,j}$ respectively.

You are also given an integer $X$. You may perform the following operation on $A$ any number of times:
- Choose an integer $v$.
- Choose $X$ consecutive elements of $A$, either in the same row or in the same column.
- Add $v$ to each of the chosen elements of $A$.

Determine whether it is possible to change $A$ to $B$ in a finite number of operations.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $R$, $C$ and $X$.
- $R$ lines follow. For each valid $i$, the $i$-th of these lines contains $C$ space-separated integers $A_{i,1}, A_{i,2}, \ldots, A_{i,C}$.
- $R$ more lines follow. For each valid $i$, the $i$-th of these lines contains $C$ space-separated integers $B_{i,1}, B_{i,2}, \ldots, B_{i,C}$.

### Output
For each test case, print a single line containing the string `"Yes"` if there is a sequence of operations that changes the matrix $A$ to $B$, or `"No"` if such a sequence of operations does not exist.

### Constraints
- $1 \leq T \leq 10^3$
- $2 \leq R,C \leq 10^3$
- $2 \leq X \leq \min(R,C)$
- $|A_{i,j}|, |B_{i,j}| \leq 10^9$ for each valid $i,j$
- the sum of $R$ over all test cases does not exceed $10^3$
- the sum of $C$ over all test cases does not exceed $10^3$

### Subtasks
**Subtask #1 (5 points):** $X=2$

**Subtask #2 (10 points):** $X=3$

**Subtask #3 (85 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2 2 2
1 2
0 1
0 0
0 0
2 2 2
1 2
0 1
0 0
-1 0
3 2 2
1 1
2 2
3 3
1 0
2 0
3 0
```

**Output**

```text
Yes
No
No
```

**Explanation**

**Example case 1:** We can add $-1$ to both elements in row $1$ and add $-1$ to both elements in column $2$.

**Example case 2:** After any operation, the sum of elements of $A$ remains even. However, the sum of elements of $B$ is odd, so $A$ cannot be changed to $B$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/CONSADD)

[Div-3 Contest](https://www.codechef.com/MARCH21C/problems/CONSADD)

[Div-2 Contest](https://www.codechef.com/MARCH21B/problems/CONSADD)

[Div-1 Contest](https://www.codechef.com/MARCH21A/problems/CONSADD)

***Author:*** [Divyam Singal](https://www.codechef.com/users/div5252)

***Tester:*** [Felipe Mota](https://www.codechef.com/users/fmota)

***Editorialist:*** [Divyam Singal](https://www.codechef.com/users/div5252)

# DIFFICULTY:

Easy-Medium

# PREREQUISITES:

Math, Colorings

# PROBLEM:

You are given two matrices A and B, each of size R \times C. You are also given an integer X. You may perform the following operation on A any number of times:

- Choose an integer v.

- Choose X consecutive elements of A, either in the same row or in the same column.

- Add v to each of the chosen elements of A.

Determine whether it is possible to change A to B in a finite number of operations.

# QUICK EXPLANATION:

We will first convert the matrix B=0, and so A = A-B. We can change the set of our available operations to:

- Add v on 1 \times X or X \times 1 which is in the top-left square X \times X.

- Do +v and -v in two cells in the same row/column on distance exactly X.

Now we can create an X \times X matrix A', where A'_{i,j} contains the sum of all cells having row number i remainder modulo X and having column number j remainder modulo X. Now the problem is converted into modified problem where R=C=X.

We will build a bipartite graph where left part is rows and right part is columns and the edge between two vertices is a cell on intersection of that row and column. We are given numbers on edges and we have to put numbers on vertices such that for each edge, the number on the edge is equal to sum of numbers in its ends.

Let us suppose there is a solution. For any number v we can do +v to all vertices in the left part, and -v to all vertices in the right part and get another valid solution. So we can choose any vertex and make it 0. Now we know all the numbers in the other part and, eventually, all the numbers.

# EXPLANATION:

We will first convert the matrix B=0, and so A = A-B, as absolute values in the matrix A and B doesn’t matter, only difference matters.

We will first consider the case where R=C=X.

We will think of this problem as a bipartite graph. The left vertices will represent the rows and the right vertices will represent the columns. The edge between the left and right vertices is a cell on the intersection of that row and column. Now the problem converts to:

We are given some numbers on edges and we have to put numbers on vertices such that for each edge, the number on the edge is equal to sum of numbers on its ends i.e the two vertices.

Now let us suppose there is a solution to this problem.  For any number v we can do +v to all vertices in the left part, and -v to all vertices in the right part and get another valid solution. This is due to the fact that the sum of vertices in the left and right part still remains the same, as +v-v=0. This gives us the freedom to choose any vertex and make it 0. This will help us find all the numbers on the other part of the vertex and eventually we can find all the numbers.

Now let us move onto the general case. We will try to convert it into the case where R=C=X.

We can change the set of our available operations to:

- Add v on 1 \times X or X \times 1 which is in the top-left square X \times X.

- Do +v and -v in two cells in the same row/column on distance exactly X.

As to why we can do so, we can add +v to X consecutive rows/columns and then add -v to X consecutive rows/columns, shifted by one cell. This will effectively make a change of +v and -v in two cells in the same row/column separated by a distance of X. This is the second operation.

And to make changes in the cells with (i,j), where i \leq R and j \leq C, we need the first operation.

By doing such a modification we can convert A to another matrix A' of size X \times X. Here A'_{i,j} contains the sum of all cells having index of row =i remainder modulo X and having index of column =j remainder modulo X.

Now we can proceed to solve the this reduced problem as above approach for R=C=X.

Time complexity is O(RC).

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ll long long
#define vll vector<ll>
#define ld long double
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define oset tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
#define osetll tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>
#define ook order_of_key
#define fbo find_by_order
const int MOD=1000000007; //998244353
long long int inverse(long long int i){
    if(i==1) return 1;
    return (MOD - ((MOD/i)*inverse(MOD%i))%MOD+MOD)%MOD;
}
ll POW(ll a,ll b)
{
    if(b==0) return 1;
    if(b==1) return a%MOD;
    ll temp=POW(a,b/2);
    if(b%2==0) return (temp*temp)%MOD;
    else return (((temp*temp)%MOD)*a)%MOD;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        ll r,c,x;
        cin>>r>>c>>x;
        ll a[r][c],b[r][c];
        ll a1[x][x];
        for(int i=0;i<x;i++)
        {
            for(int j=0;j<x;j++)
            {
                a1[i][j]=0;
            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cin>>a[i][j];
            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                cin>>b[i][j];
            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                a1[i%x][j%x]+=a[i][j];
                a1[i%x][j%x]-=b[i][j];
            }
        }
        ll flag=0;
        for(int i=1;i<x;i++)
        {
            ll temp=a1[i][0]-a1[0][0];
            for(int j=1;j<x;j++)
            {
                if(temp!=a1[i][j]-a1[0][j])
                {
                    flag=1;
                }
            }
        }
        if(flag==0) cout<<"Yes";
        else cout<<"No";
        cout<<"\n";
    }
}
``

Tester's Solution

</details>
