# Cherry and Bits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CENS20A |
| Difficulty Rating | 2179 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CENS20A](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CENS20A) |

---

## Problem Statement

Cherry has a binary matrix $A$ consisting of $N$ rows and $M$ columns. The rows are numbered from $1$ to $N$, columns are numbered from $1$ to $M$. Element at row $i$ ($1$ ≤ $i$ ≤ $N$) and column $j$ ($1$ ≤ $j$ ≤ $M$) is denoted as $A_{ij}$. All elements of $A$ are either $0$ or $1$.

He performs $Q$ queries on matrix. Each query is provided by four integers $x_{1}$, $y_{1}$, $x_{2}$, $y_{2}$ which define the rectangle, where ($x_{1}$, $y_{1}$) stands for the coordinates of the top left cell of the rectangle, while ($x_{2}$, $y_{2}$) stands for the coordinates of the bottom right cell. You need to flip all the bits i.e. ($0$ to $1$, $1$ to $0$) that are located fully inside the query rectangle.

Finally, print the matrix after performing all the queries.

Note: $x_{1}$ represents the row number while $y_{1}$ represents the column number.

###Input:

- The first line of the input contains two integers $N$ and $M$ — the number of rows and the number of columns in the matrix.
- Each of the next $N$ lines contains a string of length $M$, where the $j^{th}$ character of $i^{th}$ line denotes the value of $A_{i,j}$.
- Next line contains an integer $Q$ — the number of queries.
- Then follow $Q$ lines with queries descriptions. Each of them contains four space-seperated integers $x_{1}$, $y_{1}$, $x_{2}$, $y_{2}$ — coordinates of the up left and bottom right cells of the query rectangle.

###Output:

Print the matrix, in the form of $N$ strings, after performing all the queries.

###Constraints
- $1 \leq N,M \leq 1000$
- $0 \leq  A_{ij}  \leq 1$
- $1 \leq Q \leq 10^6$
- $1 \leq x_{1} \leq x_{2} \leq N$
- $1 \leq y_{1} \leq y_{2} \leq M$

---

## Examples

**Example 1**

**Input**

```text
2 2
00
00
3
1 1 1 1
2 2 2 2
1 1 2 2
```

**Output**

```text
01
10
```

**Explanation**

**Example case 1:**

After processing the 1st query **1 1 1 1**, matrix becomes:
$$\begin{bmatrix} 10 \\ 00  \end{bmatrix}$$
After processing the 2nd query **2 2 2 2**, the matrix becomes:
$$\begin{bmatrix} 10 \\ 01  \end{bmatrix}$$
After processing the 3rd query **1 1 2 2**, matrix becomes:
$$\begin{bmatrix} 01 \\ 10  \end{bmatrix}$$
We need to output the matrix after processing all queries.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CENS20A)

[Contest](https://www.codechef.com/CENS2020/problems/CENS20A)

**Author:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

**Tester:** [Jatin Nagpal](https://www.codechef.com/users/nagpaljatin141)

**Editorialist:** [Sarthak Shukla](https://www.codechef.com/users/sarthak_eddy)

# DIFFICULTY:

SIMPLE - EASY

# PREREQUISITES:

Difference array

# PROBLEM:

Given a binary matrix of N rows and M columns. For Q queries, given x_1, y_1, x_2, y_2. Flip all bits lying inside the rectangle formed by (x_1,y_1) as top left corner and (x_2,y_2) as bottom right corner. At last, print the final binary matrix after processing queries.

# QUICK EXPLANATION:

- Create a 2 D sum array initialized to zero.

- Perform 2 D range update on a given submatrix in each query and calculate difference array after processing queries.

- If sum at particular index is odd then bit at that index is flipped else it’s the same.

# EXPLANATION:

We have to flip all the bits lying inside the rectangle given in each query.

It’s quite obvious that we can’t loop through the given rectangle in each query to flip the bits.

So, instead of flipping the bits in each query, we can keep track of the number of times bit at any index is flipped.

Now, how can we do this?

Answer

We can perform range updates for each query and find the final 2 D matrix after performing updates. We can use another 2 D array preSum of size N*M, initialized to zero, for this operation where each element denotes the number of times bit at that position is flipped.

Now the question is reduced to..

This problem is now reduced to a problem where we are given a grid A of size N*M, and we are asked to increment all the elements lying inside the sub-matrix, formed by (x_1,y_1) as the top left corner and (x_2,y_2) as a bottom right corner, by 1. And, finally, print the final matrix after updates.

The rectangle given in each query is (x_1,y_1), (x_1,y_2), (x_2,y_1) and (x_2,y_2).

Now comes the part to perform updates in each query.

We can use O(1) range update technique of 1 D array as [here](https://www.geeksforgeeks.org/constant-time-range-add-operation-array/). Since our rectangle is a group of 1 D arrays, we can perform this operation for every row/column.

But wait, the number of queries is very high, it will result in TLE.

Now, what?

Can we extend this O(1) range update for 1 D array to 2 D array as well? If you don’t know this, think about it before moving onto the implementation.

2 D range update

We can increment preSum[x_1][y_1] and preSum[x_2+1][y_2+1] by 1. And, decrement preSum[x_1][y_2+1] and preSum[x_2+1][y_1] by 1. Make sure to check if these indices are in range or not.

The proof for this update is simple and similar to that of 1 D array. Try figuring it out.

Proof

It is recommended that you first get comfortable working with 1D difference arrays.

Lets try maintaining a 1D difference array for each row. Initially it would look like this.

\begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}

Now suppose we update the range (2, 2) to (4, 3). The matrix changes to

 \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 1 & 0 & -1 \\ 0 & 1 & 0 & -1 \end{bmatrix}

Notice that this is the same as a range update on column. So we take a new matrix and do updates based on column. Which would look like this

 \begin{bmatrix} 0 & 1 & 0 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}

We would have to perform updates at most 4 different points in this matrix. After performing all the queries, we iterate column wise over this matrix to find all the 1D difference arrays of the rows. And then iterate row wise to find all the actual values of the elements.

Now, the only remaining thing is to find the final matrix. This calculation is also similar to that in 1 D technique. In 1 D technique, we calculate the difference array of the array to get the final array. Here, find the difference array for both rows and columns.

Now, how is the difference array related to our flipping of bits?

Answer

Each element of our difference array denotes the number of times bit is flipped at that position. If the sum at any index is even, then it means a bit at that position is flipped even number of times and will remain the same as previously. But, if sum at any index is odd then the bit at that index is flipped.

# TIME COMPLEXITY:

**Time**: O(N*M + Q)

**Space**: O(N*M)

# SOLUTIONS:

C++ Code
``#include<bits/stdc++.h>
using namespace std;
#define ll int
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int main() {
	fast
	ll n,m;
	cin>>n>>m;
	ll a[n][m],i,j,pre[n][m];
	string s[n];
	for(i=0;i<n;i++)
		cin>>s[i];

	for(i=0;i<n;i++) {
		for(j=0;j<m;j++) {
			a[i][j] = s[i][j]-'0';
			pre[i][j]=0;
		}
	}

	ll q;
	cin>>q;
	ll x1,y1,x2,y2;
	while(q--) {
		cin>>x1>>y1>>x2>>y2;
		x1--;
		y1--;
		y2--;
		x2--;
		pre[x1][y1]++;
		if(x2+1<n && y2+1<m)
			pre[x2+1][y2+1]++;
		if(x2+1<n)
			pre[x2+1][y1]--;
		if(y2+1<m)
			pre[x1][y2+1]--;
	}

	for(i=0;i<m;i++) {
		for(j=1;j<n;j++) {
			pre[j][i] += pre[j-1][i];
		}
	}

	for(i=0;i<n;i++) {
		for(j=1;j<m;j++) {
			pre[i][j] += pre[i][j-1];
		}
	}

	for(i=0;i<n;i++) {
		for(j=0;j<m;j++) {
			if(pre[i][j]%2) {
				if(a[i][j] == 1)
					cout<<0;
				else
					cout<<1;
			}
			else
				cout<<a[i][j];
		}
		cout<<"\n";
	}
}
``

Python Code
``import sys

n, m = map(int, sys.stdin.readline().strip().split())

arr = []
for i in range(n):
	s = input() + "0"
	temp = []
	for x in s:
		temp += [int(x)]
	arr += [temp]

arr += [[0]*(m+1)]

add = [[0 for i in range(m+1)] for j in range(n+1)]
pref1 = [[0 for i in range(m+1)] for j in range(n+1)]
pref2 = [[0 for i in range(m+1)] for j in range(n+1)]

q = int(sys.stdin.readline().strip())
for _ in range(q):
	x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
	x1 -= 1
	y1 -= 1
	x2 -= 1
	y2 -= 1
	pref2[x1][y1] += 1
	pref2[x2+1][y1] -= 1
	pref2[x1][y2+1] += -1
	pref2[x2+1][y2+1] -= -1

for i in range(m):
	for j in range(n):
		if j == 0:
			pref1[j][i] = pref2[j][i]
		else:
			pref1[j][i] = pref1[j-1][i] + pref2[j][i]

for i in range(n):
	for j in range(m):
		if j == 0:
			add[i][j] += pref1[i][j]
		else:
			add[i][j] = add[i][j-1] + pref1[i][j]

for i in range(n):
	for j in range(m):
		arr[i][j] += add[i][j]
		arr[i][j] %= 2

for i in range(n):
	for j in range(m):
		print(arr[i][j], end='')
	print('')
``

</details>
