# Snakes and transition from Capitalism to Socialism

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNSOCIAL |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [SNSOCIAL](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/SNSOCIAL) |

---

## Problem Statement

After a long duration of the painful, torturous and tumultuous periods of capitalism in Snakeland, now the snakes have decided to adopt socialism. The houses in Snakeland are arranged in a rectangular fashion of dimension **n * m**. The wealth of the snake in the house at cell (i, j) is given by **a**[i][j] rupees.

A bill has been passed for making a smooth transition from capitalism to socialism. At the end of each hour, the wealth of a snake will grow and will become equal to the highest wealth that its neighbor had (at the start of the hour). That is, consider the maximum wealth among its neighbors at the start of the hour, and this snake's wealth will become equal to that at the end of the hour. Note that this increase in wealth will happen simultaneously for each snake. Two houses are said to be neighbors of each other if they share a side or corner with each other. Find out the minimum number of hours required for this transition.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two space separated integers: **n, m**.

Each of the next **n** lines contains **m** space separated integers. The j-th integer in the i-th row denotes **a**[i][j].

### Output

For each test case output a single integer corresponding to the minimum number of hours required for the transition.

### Constraints

- 1 ≤ **T** ≤ 4

- 1 ≤ **n, m** ≤ 500

- 1 ≤ **a**[i][j] ≤ 106

---

## Examples

**Example 1**

**Input**

```text
3
2 2
1 1
1 1
2 2
1 1
1 2
3 4
1 2 1 2
1 1 1 2
1 1 2 2
```

**Output**

```text
0
1
2
```

**Explanation**

**Example 1**. The wealth of all the snakes is already equal. So, no time is required for the transition.

**Example 2**. At the end of the first hour, the wealth of snakes at cells (1, 1), (2,1) and (1, 2) will change from 1 to 2. Then, the wealth of all the snakes becomes equal, and hence it required a total of 1 hour.

**Example 3**. At the end of the first hour, the distribution of wealth of Snakeland will be as given below:

`
2 2 2 2
2 2 2 2
1 2 2 2
`

After the end of the second hour, the wealth of all the snakes will be equal. So, the answer is 2.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SNGRAPH)

[Contest](https://www.codechef.com/SNCKPB17/problems/SNGRAPH)

**Author:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Sidhant Bansal](https://www.codechef.com/users/sidhant007)

**DIFFICULTY** -

Easy - Medium

**PREREQUISITES** -

BFS

**PROBLEM** -

Given a grid of n * m dimension, where the value of cell (i, j) is a[i][j].

Determine the minimum no. of moves after which all the values of array a[][] will be equal given that in every move for every cell (i, j) its value a[i][j] becomes the maximum of the 8 adjacent values to that cell, only if this maximum value is greater than current a[i][j].

**EXPLANATION** -

Firstly, we can easily see that this process will end when all the values in the a[][] array have attained the maximum element of the a[][] array.

Now if we find the maximum element in the a[][] array and mark all its occurrences as **SPECIAL**.

The problem is reduced to this -

For each cell (i, j) we need to determine the shortest distance from cell (i, j) to any cell which is marked as **SPECIAL**, and the maximum of all these shortest distances is our answer. This can be done using a multi - source BFS.

This works because the shortest distance for cell (i, j) is equal to the no. of moves taken for the max value to reach cell (i, j).

**Graph Theory Equivalent** -

The graph theory equivalent to the above problem is this -

Given a graph with X nodes and Y edges where all the edges are bidirectional and have weight 1. Also where Z of its nodes are marked **SPECIAL**. Find the shortest distance of each node from any of the **SPECIAL** node, meaning that you have to minimise the shortest distance given that one end point is fixed as the current node and the other end point can be any **SPECIAL** node.

The naive method to do the above problem is to do a BFS from each **SPECIAL** node and then for each node determine which **SPECIAL** node is optimal for it depending on which **SPECIAL** node is nearest to it. But this solution is of the order O((X + Y) * Z), which will TLE in our case.

The faster method is to assume a fictional node W and assume that it is connected all the Z **SPECIAL** nodes with weight 1. Now a single BFS considering the source as W will give the answer with an extra 1 added. So subtract 1 from the shortest distances since the edge from W to the **SPECIAL** nodes is irrelevant. This method is commonly known as multi - source BFS as it enables us to have multiple sources. Same method can be extended to Dijkstra algorithm. This solution is fast enough and is of the order O(X + Y).

Below is a C++ implementation for better understanding -

``#include "bits/stdc++.h"
using namespace std;

const int N = 505;

int a[N][N];
int dx[] = {1, 1, 1, -1, -1, -1, 0, 0}, dy[] = {1, 0, -1, 1, 0, -1, 1, -1};

bool visited[N][N];
queue<pair<pair<int, int>, int> > Q;

int n, m;

bool valid(int x, int y){
	if(x < 1 or x > n or y < 1 or y > m)	return false;
	else return true;
}

void solve(){
	int maxm = 0;

	cin>>n>>m;
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= m; j++){
			cin>>a[i][j];

			maxm = max(maxm, a[i][j]);
			visited[i][j] = 0;
		}
	}

	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= m; j++){
			if(a[i][j] == maxm){
				Q.push({{i, j}, 0});
				visited[i][j] = 1;
			}
		}
	}

	int ans = 0;

	while(!Q.empty()){
		int x = Q.front().first.first, y = Q.front().first.second, d = Q.front().second;
		ans = max(ans, d);
		Q.pop();

		for(int i = 0; i < 8; i++){
			if(valid(x + dx[i], y + dy[i]) == 1 and visited[x + dx[i]][y + dy[i]] == 0){
				Q.push({{x + dx[i], y + dy[i]}, d + 1});
				visited[x + dx[i]][y + dy[i]] = 1;
			}
		}
	}
	cout<<ans<<endl;
}

int main(){
	int t;
	scanf("%d", &t);
	while(t--)	solve();
}
``

**Complexity** -

The time complexity of a single BFS is O(no. of vertices + no. of edges in the graph) = O(n * m)

### AUTHOR’S AND TESTER’S SOLUTIONS:

**AUTHOR’s solution**:  [Here] [444](http://www.codechef.com/download/Solutions/SNCKPB17/Setter/SNGRAPH.cpp)

**TESTER’s solution**: [Here] [555](http://www.codechef.com/download/Solutions/SNCKPB17/Tester/SNGRAPH.cpp)

</details>
