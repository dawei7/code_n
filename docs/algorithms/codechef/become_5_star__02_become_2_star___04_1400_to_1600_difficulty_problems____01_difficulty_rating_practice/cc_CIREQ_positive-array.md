# Positive array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CIREQ |
| Difficulty Rating | 1620 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [CIREQ](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/CIREQ) |

---

## Problem Statement

​A `1`-indexed array is called *positive* if every element of the array is greater than or equal to the index on which it lies. Formally, an array $B$ of size $M$ is called positive if $B_i \ge i$ for each $1\le i \le M$.

For example, the arrays $[1], [2, 2], [3, 2, 4, 4]$ are positive while the arrays $[2, 1], [3, 1, 2]$ are not positive.

You are given an array $A$ containing $N$ integers. You want to distribute all elements of the array into some positive arrays. The elements of a positive array might not occur in the order they appear in the array $A$.

Find the **minimum** number of positive arrays that the elements of the array $A$ can be divided into.

Please see the sample cases below for more clarity.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the number of elements in the array $A$.
    - The next line contains $N$ space-separated integers $A_1, A_2,\ldots, A_N$ — the elements of array $A$.

---

## Output Format

For each test case, output on a new line the minimum number of positive arrays that the elements of the array $A$ can be divided into.
​

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
5
3
2 3 3
4
3 1 1 2
3
1 1 1
5
1 2 2 4 5
6
3 2 1 2 2 1
```

**Output**

```text
1
2
3
2
3
```

**Explanation**

**Test case $1$:** The given array is already positive. So the optimal division is $[2,3,3]$.

**Test case $2$:** One possible division is $[1, 2], [1, 3]$.

**Test case $3$:** The only possible division is $[1],[1],[1]$.

**Test case $4$:** One possible division is $[1, 2, 5], [2, 4]$.

**Test case $5$:** One possible division is $[1, 2, 3], [1], [2,2]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 3 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
3 1 1 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
1 1 1
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
5
1 2 2 4 5
```

**Output for this case**

```text
2
```



#### Test case 5

**Input for this case**

```text
6
3 2 1 2 2 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START48A/problems/CIREQ)

[Contest Division 2](https://www.codechef.com/START48B/problems/CIREQ)

[Contest Division 3](https://www.codechef.com/START48C/problems/CIREQ)

[Contest Division 4](https://www.codechef.com/START48D/problems/CIREQ)

Setter: [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

Tester: [Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

1620

#
[](#prerequisites-3)PREREQUISITES:

[Heaps]

#
[](#problem-4)PROBLEM:

?A `1`-indexed array is called *positive* if every element of the array is greater than or equal to the index on which it lies. Formally, an array B of size M is called positive if B_i \ge i for each 1\le i \le M.

For example, the arrays [1], [2, 2], [3, 2, 4, 4] are positive while the arrays [2, 1], [3, 1, 2] are not positive.

You are given an array A containing N integers. You want to distribute all elements of the array into some positive arrays. The elements of a positive array might not occur in the order they appear in the array A.

Find the **minimum** number of positive arrays that the elements of the array A can be divided into.

?

Please see the sample cases below for more clarity.

#
[](#explanation-5)EXPLANATION:

Hint

It is always better to keep smaller elements before larger ones while forming a positive array because this will surely reduce the number of positive arrays required to distribute all the elements in A.

Hence, sorting will surely help!

Solution

From the hint it is clear that we should form positive arrays which have elements in an ascending order. If there are K elements in an existing positive array then the next element should be  \geq K + 1.

We can greedily assign each element of A (in the ascending order) to some already existing positive array if it can accommodate the current element (if A[i] \geq number of elements in the positive array + 1) or in the other case we need to create another positive array.

We can maintain the information about all the existing positive arrays by storing the minimum required element for each of them.

If the current element (A[i]) can be part of any of the existing positive arrays i.e. it is \geq the least among all the minimum required elements for the positive arrays then we can just update the minimum required element and there is no need to create another positive array. The least among all the minimum required elements can be easily obtained if we store all the minimum required elements in a priority queue and updating also becomes easy.

On the other hand, if the current element (A[i]) cannot become a part of any of the existing positive arrays then we create a new positive array with the current element (A[i]) being the first element in it i.e. add a new value (minimum requirement of 2) into the priority queue.

At the end of the iteration over A the size of the priority queue denotes the minimum number of positive arrays required i.e. our answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(NlogN) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``using namespace std;

int main() {
	ios_base :: sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		vector<int> a(n + 1);
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			a[x]++;
		}
		int sum = 0, ans = 0;
		for (int i = 1; i <= n; i++) {
			sum += a[i];
			ans = max(ans, (sum + i - 1) / i);
		}
		cout << ans << '\n';
	}
	return 0;
}
``

Editorialist's Solution
``using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--){
	    int n;
	    cin >> n;
	    vector<int>v(n);
	    for(int i=0;i<n;i++)cin >> v[i];
	    sort(v.begin(),v.end());
	    priority_queue<int,vector<int>,greater<int>>pq;
	    pq.push(1);
	    for(int i=0;i<n;i++){
	        if(v[i]>=pq.top()){
	            pq.push(pq.top()+1);
	            pq.pop();
	        }
	        else{
	            pq.push(2);
	        }
	    }
	    cout << pq.size() << endl;
	}
	return 0;
}
``

</details>
